---
tags:
  - automation
---
{
  "nodes": [
    {
      "parameters": {
        "url": "={{ $json.text }}",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "User-Agent",
              "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124"
            }
          ]
        },
        "options": {
          "response": {
            "response": {
              "fullResponse": true,
              "responseFormat": "text"
            }
          }
        }
      },
      "id": "f71d2661-3262-46dc-9367-b20b839c1b37",
      "name": "Get TikTok Video Page Data",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        224,
        0
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "jsCode": "const html = $input.first().json.data;\nconst headers = $input.first().json.headers || {};\nconst cookies = headers['set-cookie'] || [];\n\nif (!html) {\n  throw new Error(\"Unable to load TikTok page. Please try again!\");\n}\n\n// Find JSON data from script tag\nconst regex = /<script id=\"__UNIVERSAL_DATA_FOR_REHYDRATION__\" type=\"application\\/json\">([\\s\\S]*?)<\\/script>/;\nconst match = html.match(regex);\n\nif (!match) {\n  throw new Error(\"Video data not found. The link may be deleted or private.\");\n}\n\nconst jsonStr = match[1];\nlet data;\n\ntry {\n  data = JSON.parse(jsonStr);\n} catch (e) {\n  throw new Error(\"Unable to parse video data. Please try again!\");\n}\n\n// Get video URL from multiple possible paths\nconst itemInfo = data?.__DEFAULT_SCOPE__?.[\"webapp.video-detail\"]?.itemInfo?.itemStruct;\nconst videoUrl = itemInfo?.video?.playAddr || itemInfo?.video?.downloadAddr;\n\nif (!videoUrl) {\n  throw new Error(\"Video URL not found. The video may be restricted from downloading.\");\n}\n\nconst videoInfo = {\n  videoUrl: videoUrl,\n  cookies: cookies.join('; '),\n  description: itemInfo?.desc || 'TikTok Video',\n  author: itemInfo?.author?.uniqueId || 'unknown',\n  stats: {\n    plays: itemInfo?.stats?.playCount || 0,\n    likes: itemInfo?.stats?.diggCount || 0,\n    comments: itemInfo?.stats?.commentCount || 0\n  }\n};\n\nreturn [{ json: videoInfo }];"
      },
      "id": "1bf3338f-b381-4374-b799-889a687933e3",
      "name": "Scrape raw video URL",
      "type": "n8n-nodes-base.code",
      "position": [
        400,
        0
      ],
      "typeVersion": 2
    },
    {
      "parameters": {
        "url": "={{ $json.videoUrl }}",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "User-Agent",
              "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            },
            {
              "name": "Referer",
              "value": "https://www.tiktok.com/"
            },
            {
              "name": "Accept",
              "value": "video/mp4,video/webm,video/*;q=0.9,application/octet-stream;q=0.8"
            },
            {
              "name": "Accept-Language",
              "value": "en-US,en;q=0.5"
            },
            {
              "name": "Connection",
              "value": "keep-alive"
            },
            {
              "name": "Cookie",
              "value": "={{ $json.cookies }}"
            }
          ]
        },
        "options": {
          "allowUnauthorizedCerts": true,
          "response": {
            "response": {
              "responseFormat": "file"
            }
          }
        }
      },
      "id": "9e7ac53e-b32e-43e7-8b7e-1e60c7552925",
      "name": "Output video file without watermark",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        560,
        0
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "4e93a67c-1057-45a0-9321-1fa6cd9fab42",
              "name": "chatinput",
              "value": "={{ $json.chatInput }}",
              "type": "string"
            },
            {
              "id": "77462b88-f6e1-4216-b323-0247ef27b382",
              "name": "text",
              "value": "={{ $json.message.text }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        -48,
        0
      ],
      "id": "8fcbf444-bd2b-4fbb-b003-e7c60e7e46a6",
      "name": "Edit Fields"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "bf1ec381-c09a-4e4d-b299-414d197e0c1e",
              "name": "data",
              "type": "string",
              "value": "={{ $json.data }}"
            }
          ]
        },
        "options": {}
      },
      "id": "5d24394d-a3a1-4585-97b7-8f44700fef9b",
      "name": "video scraping",
      "type": "n8n-nodes-base.set",
      "position": [
        480,
        992
      ],
      "typeVersion": 3.4
    },
    {
      "parameters": {
        "jsCode": "const html = $json[\"data\"]; // replace 'data' with your actual field name\nconst match = html.match(/https:\\/\\/dl\\.snapcdn\\.app\\/download\\?token=[^\"]+/);\n\nreturn {\n  json: {\n    downloadUrl: match ? match[0] : null\n  }\n};\n"
      },
      "id": "5990f499-841c-420a-91bb-e9997193434c",
      "name": "Genrate download link",
      "type": "n8n-nodes-base.code",
      "position": [
        704,
        992
      ],
      "typeVersion": 2
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "62b26b58-bd15-4eb8-90e7-235eabe34cc7",
              "operator": {
                "type": "boolean",
                "operation": "true",
                "singleValue": true
              },
              "leftValue": "={{ $json.isFacebookLink }}",
              "rightValue": "true"
            }
          ]
        },
        "options": {}
      },
      "id": "5a3d57fe-034f-46a3-8ba8-d5be95e16119",
      "name": "Link checking",
      "type": "n8n-nodes-base.if",
      "position": [
        -128,
        960
      ],
      "typeVersion": 2.2
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "9f62fc1b-5b1a-41ae-9b44-429bde6795ae",
              "operator": {
                "type": "boolean",
                "operation": "true",
                "singleValue": true
              },
              "leftValue": "={{ $json.isInstagramLink }}",
              "rightValue": ""
            }
          ]
        },
        "options": {}
      },
      "id": "71dde35b-2057-4bdd-aabd-f34534eb5695",
      "name": "If",
      "type": "n8n-nodes-base.if",
      "position": [
        -336,
        496
      ],
      "typeVersion": 2.2
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://fbdownloader.to/api/ajaxSearch",
        "sendBody": true,
        "contentType": "multipart-form-data",
        "bodyParameters": {
          "parameters": [
            {
              "name": "q",
              "value": "={{ $('Telegram Trigger1').item.json.message.text }}"
            }
          ]
        },
        "options": {}
      },
      "id": "1889a1bb-af7e-44c2-935c-fe8fdad7d155",
      "name": "FB API FETCHING",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        256,
        992
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "url": "=https://snapdownloader.com/tools/instagram-downloader/download?url={{ $json.instagramUrl }}",
        "options": {}
      },
      "id": "1b3b3086-9363-41e2-ba6d-f53e3161b701",
      "name": "INSTA API FETCHING",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        192,
        656
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "jsCode": "// n8n Function node\n// Input: HTTP Request node output (with HTML inside `data` field)\n// Output: Only the video file URL\n\nconst results = [];\n\nfor (const item of items) {\n  const html = item.json.data || \"\";\n  \n  // Regex to capture video .mp4 links\n  const regex = /(https?:\\/\\/[^\\s\"']+\\.mp4[^\\s\"']*)/gi;\n  const matches = html.match(regex);\n\n  if (matches && matches.length > 0) {\n    results.push({ json: { videoUrl: matches[0] } }); // take first video link\n  } else {\n    results.push({ json: { videoUrl: null } });\n  }\n}\n\nreturn results;\n"
      },
      "id": "bdc8e39b-3de1-43ab-b1b7-14d813199b4a",
      "name": "URL FINDER",
      "type": "n8n-nodes-base.code",
      "position": [
        432,
        656
      ],
      "typeVersion": 2
    },
    {
      "parameters": {
        "jsCode": "// Function node\n// Input: items[i].json.videoUrl\n// Output: items[i].json.videoUrlClean\nreturn items.map(item => {\n  const url = (item.json.videoUrl || '').split('&amp;').join('&');\n  return { json: { ...item.json, videoUrlClean: url } };\n});\n"
      },
      "id": "eb569d0b-48bf-4946-bea4-ddde6258938c",
      "name": "URL DECODER",
      "type": "n8n-nodes-base.code",
      "position": [
        640,
        656
      ],
      "typeVersion": 2
    },
    {
      "parameters": {
        "url": "={{ $json.videoUrlClean }}",
        "options": {}
      },
      "id": "f4bbe15c-42eb-4e53-b80f-445d9def982f",
      "name": "DOWNLOAD INSTA VID",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        880,
        656
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "url": "={{ $json.downloadUrl }}",
        "options": {}
      },
      "id": "b4cf4640-bf6a-4aa0-87d8-c5a7376b0d33",
      "name": "DOWNLOAD FB VID",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        928,
        992
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "chatId": "={{ $('Telegram Trigger1').item.json.message.chat.id }}",
        "text": "Please paste only facebook/Instagram link ⚠️",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "id": "2785011d-81bd-4aa3-9a7d-a35288f8ea57",
      "name": "INVALID URL",
      "type": "n8n-nodes-base.telegram",
      "position": [
        192,
        1440
      ],
      "webhookId": "069b70f6-449e-4567-b0d2-9b80c1aac821",
      "typeVersion": 1.2,
      "credentials": {}
    },
    {
      "parameters": {
        "jsCode": "const url = $input.first().json.message.text; // your input text\n\n// Regex patterns\nconst fbRegex = /https?:\\/\\/([a-zA-Z0-9-]+\\.)?facebook\\.com\\/[^\\s]+/i;\nconst igRegex = /https?:\\/\\/([a-zA-Z0-9-]+\\.)?instagram\\.com\\/[^\\s]+/i;\n\n// Match\nconst fbMatch = url.match(fbRegex);\nconst igMatch = url.match(igRegex);\n\nreturn {\n  json: {\n    isFacebookLink: !!fbMatch,\n    facebookUrl: fbMatch ? fbMatch[0] : null,\n    isInstagramLink: !!igMatch,\n    instagramUrl: igMatch ? igMatch[0] : null\n  }\n};\n"
      },
      "id": "cb443fd9-028a-45ac-a008-d22ad1491297",
      "name": "FB IG LINK REGEX",
      "type": "n8n-nodes-base.code",
      "position": [
        -544,
        496
      ],
      "typeVersion": 2
    },
    {
      "parameters": {
        "content": "## Checking IG or not",
        "height": 176,
        "width": 352,
        "color": 5
      },
      "id": "133362f7-de9b-43c8-b8d1-a9099929bd19",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -560,
        448
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "## FACEBOOK NODE",
        "height": 400,
        "width": 1360,
        "color": 4
      },
      "id": "fe9414d7-65f9-4f52-b75b-45ca96766c01",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        192,
        928
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "## INSTAGRAM NODE",
        "height": 400,
        "width": 1344,
        "color": 6
      },
      "id": "60dcb7f5-6041-476c-92c3-193c79adc731",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        112,
        432
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "## CHECKING Tiktok Or Not",
        "height": 304,
        "width": 448,
        "color": 7
      },
      "id": "5ade13df-872e-4d28-8934-65e6d4de066a",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1104,
        272
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "## SENDING ERROR MSG IF INVALID LINK",
        "height": 208,
        "width": 416,
        "color": 2
      },
      "id": "537590b8-7061-4d08-8f6e-202f97772254",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        176,
        1360
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "updates": [
          "message"
        ],
        "additionalFields": {}
      },
      "id": "31a29bdd-10e2-42f8-acb0-cb9aae2a4265",
      "name": "Telegram Trigger1",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        -1056,
        384
      ],
      "webhookId": "70d965f1-4d42-4b68-9122-751279046934",
      "typeVersion": 1.2,
      "credentials": {}
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "conditions": [
            {
              "id": "62b26b58-bd15-4eb8-90e7-235eabe34cc7",
              "operator": {
                "type": "string",
                "operation": "contains"
              },
              "leftValue": "={{ $('Telegram Trigger1').item.json.message.text }} {{ $('Telegram Trigger1').item.json.message.link_preview_options.url }}",
              "rightValue": "tiktok"
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "id": "35f092b9-8566-4daa-a192-d04c05db6350",
      "name": "Link checking1",
      "type": "n8n-nodes-base.if",
      "position": [
        -848,
        384
      ],
      "typeVersion": 2.2
    },
    {
      "parameters": {
        "content": "## Checking FB or not",
        "height": 176,
        "width": 352,
        "color": 5
      },
      "id": "38af22b3-78eb-42d6-a577-65b69a4f66bd",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -272,
        928
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "resource": "video",
        "operation": "analyze",
        "modelId": {
          "__rl": true,
          "value": "models/gemini-2.5-flash",
          "mode": "list",
          "cachedResultName": "models/gemini-2.5-flash"
        },
        "text": "1.Transcript the Script of this video \n2.  analyze this script and give deep analysiss every sentences\n3. and then add indonesian translated version\n",
        "inputType": "binary",
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.googleGemini",
      "typeVersion": 1,
      "position": [
        1200,
        448
      ],
      "id": "47268a45-2d66-4a8d-b231-a7de0394a73d",
      "name": "Analyze video",
      "credentials": {
        "googlePalmApi": {
          "id": "RNEx3c1Xh5UDcnH6",
          "name": "MYAPI"
        }
      },
      "disabled": true
    },
    {
      "parameters": {
        "operation": "append",
        "documentId": {
          "__rl": true,
          "value": "1Y7CVtPEjR15Po3zCRFO6tAdMsTwrxsEESN64tcgZwNg",
          "mode": "list",
          "cachedResultName": "Copywriting Trends",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1Y7CVtPEjR15Po3zCRFO6tAdMsTwrxsEESN64tcgZwNg/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 1932542407,
          "mode": "list",
          "cachedResultName": "Transcript",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1Y7CVtPEjR15Po3zCRFO6tAdMsTwrxsEESN64tcgZwNg/edit#gid=1932542407"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Transcript": "={{ $json.content.parts[0].text }}"
          },
          "matchingColumns": [],
          "schema": [
            {
              "id": "Transcript",
              "displayName": "Transcript",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Repurpose AI",
              "displayName": "Repurpose AI",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 2",
              "displayName": "Column 2",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 4",
              "displayName": "Column 4",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 5",
              "displayName": "Column 5",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 6",
              "displayName": "Column 6",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 7",
              "displayName": "Column 7",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 8",
              "displayName": "Column 8",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 9",
              "displayName": "Column 9",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 10",
              "displayName": "Column 10",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 11",
              "displayName": "Column 11",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 12",
              "displayName": "Column 12",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 13",
              "displayName": "Column 13",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 14",
              "displayName": "Column 14",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 15",
              "displayName": "Column 15",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.7,
      "position": [
        1392,
        448
      ],
      "id": "3f276f2f-0474-4b59-89c8-38466fab9891",
      "name": "Append row in sheet",
      "disabled": true
    },
    {
      "parameters": {
        "name": "Transcript.mp4",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "folderId": {
          "__rl": true,
          "value": "https://drive.google.com/drive/folders/13GTMhShXDwz_j_TZkoKZVBVDuSHA4Ngj",
          "mode": "url"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleDrive",
      "typeVersion": 3,
      "position": [
        1408,
        624
      ],
      "id": "74f4081c-ca49-4db4-be68-fad0e57dfb40",
      "name": "Upload file",
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "UcfIN5LCO68VG5wm",
          "name": "07/01"
        }
      }
    },
    {
      "parameters": {
        "resource": "video",
        "operation": "analyze",
        "modelId": {
          "__rl": true,
          "value": "models/gemini-2.5-flash",
          "mode": "list",
          "cachedResultName": "models/gemini-2.5-flash"
        },
        "text": "1.Transcript the Script of this video \n2.  analyze this script and give deep analysiss every sentences\n3. and then add indonesian translated version\n",
        "inputType": "binary",
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.googleGemini",
      "typeVersion": 1,
      "position": [
        1328,
        -112
      ],
      "id": "ceabb1e2-f9df-4b3c-b006-d449ff036c8d",
      "name": "Analyze video1",
      "credentials": {
        "googlePalmApi": {
          "id": "RNEx3c1Xh5UDcnH6",
          "name": "MYAPI"
        }
      },
      "disabled": true
    },
    {
      "parameters": {
        "operation": "append",
        "documentId": {
          "__rl": true,
          "value": "1Y7CVtPEjR15Po3zCRFO6tAdMsTwrxsEESN64tcgZwNg",
          "mode": "list",
          "cachedResultName": "Copywriting Trends",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1Y7CVtPEjR15Po3zCRFO6tAdMsTwrxsEESN64tcgZwNg/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 1932542407,
          "mode": "list",
          "cachedResultName": "Transcript",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1Y7CVtPEjR15Po3zCRFO6tAdMsTwrxsEESN64tcgZwNg/edit#gid=1932542407"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Transcript": "={{ $json.content.parts[0].text }}"
          },
          "matchingColumns": [],
          "schema": [
            {
              "id": "Transcript",
              "displayName": "Transcript",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Repurpose AI",
              "displayName": "Repurpose AI",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 2",
              "displayName": "Column 2",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 4",
              "displayName": "Column 4",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 5",
              "displayName": "Column 5",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 6",
              "displayName": "Column 6",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 7",
              "displayName": "Column 7",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 8",
              "displayName": "Column 8",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 9",
              "displayName": "Column 9",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 10",
              "displayName": "Column 10",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 11",
              "displayName": "Column 11",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 12",
              "displayName": "Column 12",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 13",
              "displayName": "Column 13",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 14",
              "displayName": "Column 14",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 15",
              "displayName": "Column 15",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.7,
      "position": [
        1520,
        -112
      ],
      "id": "4477b221-7921-4a38-8c73-e54dcd62d324",
      "name": "Append row in sheet1",
      "disabled": true
    },
    {
      "parameters": {
        "name": "Transcript.mp4",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "folderId": {
          "__rl": true,
          "value": "https://drive.google.com/drive/folders/13GTMhShXDwz_j_TZkoKZVBVDuSHA4Ngj",
          "mode": "url"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleDrive",
      "typeVersion": 3,
      "position": [
        1536,
        64
      ],
      "id": "d1e0255d-975e-4692-b862-aef6b79d23c2",
      "name": "Upload file1",
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "UcfIN5LCO68VG5wm",
          "name": "07/01"
        }
      }
    },
    {
      "parameters": {
        "resource": "video",
        "operation": "analyze",
        "modelId": {
          "__rl": true,
          "value": "models/gemini-2.5-flash",
          "mode": "list",
          "cachedResultName": "models/gemini-2.5-flash"
        },
        "text": "1.Transcript the Script of this video \n2.  analyze this script and give deep analysiss every sentences\n3. and then add indonesian translated version\n",
        "inputType": "binary",
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.googleGemini",
      "typeVersion": 1,
      "position": [
        1264,
        976
      ],
      "id": "701ce09e-34c5-49f3-a624-9cd9844ddb0d",
      "name": "Analyze video2",
      "credentials": {
        "googlePalmApi": {
          "id": "RNEx3c1Xh5UDcnH6",
          "name": "MYAPI"
        }
      },
      "disabled": true
    },
    {
      "parameters": {
        "operation": "append",
        "documentId": {
          "__rl": true,
          "value": "1Y7CVtPEjR15Po3zCRFO6tAdMsTwrxsEESN64tcgZwNg",
          "mode": "list",
          "cachedResultName": "Copywriting Trends",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1Y7CVtPEjR15Po3zCRFO6tAdMsTwrxsEESN64tcgZwNg/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 1932542407,
          "mode": "list",
          "cachedResultName": "Transcript",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1Y7CVtPEjR15Po3zCRFO6tAdMsTwrxsEESN64tcgZwNg/edit#gid=1932542407"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Transcript": "={{ $json.content.parts[0].text }}"
          },
          "matchingColumns": [],
          "schema": [
            {
              "id": "Transcript",
              "displayName": "Transcript",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Repurpose AI",
              "displayName": "Repurpose AI",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 2",
              "displayName": "Column 2",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 4",
              "displayName": "Column 4",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 5",
              "displayName": "Column 5",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 6",
              "displayName": "Column 6",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 7",
              "displayName": "Column 7",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 8",
              "displayName": "Column 8",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 9",
              "displayName": "Column 9",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 10",
              "displayName": "Column 10",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 11",
              "displayName": "Column 11",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 12",
              "displayName": "Column 12",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 13",
              "displayName": "Column 13",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 14",
              "displayName": "Column 14",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Column 15",
              "displayName": "Column 15",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.7,
      "position": [
        1456,
        976
      ],
      "id": "9efcb4c6-8ab4-4bd3-834d-78cd0716e973",
      "name": "Append row in sheet2",
      "disabled": true
    },
    {
      "parameters": {
        "name": "Transcript.mp4",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "folderId": {
          "__rl": true,
          "value": "https://drive.google.com/drive/folders/13GTMhShXDwz_j_TZkoKZVBVDuSHA4Ngj",
          "mode": "url"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleDrive",
      "typeVersion": 3,
      "position": [
        1264,
        1152
      ],
      "id": "7b7c8555-5e3e-4475-8dd3-08093ed3a63a",
      "name": "Upload file2",
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "UcfIN5LCO68VG5wm",
          "name": "07/01"
        }
      }
    },
    {
      "parameters": {
        "chatId": "6228081299",
        "text": "video saved",
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        1328,
        208
      ],
      "id": "0e143ead-5b70-439c-9374-ce15f85b2172",
      "name": "Send a text message",
      "webhookId": "b9ffd582-8f89-449e-9fee-afca1feb4937",
      "credentials": {}
    },
    {
      "parameters": {
        "chatId": "6228081299",
        "text": "video saved",
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        1408,
        768
      ],
      "id": "e6262f47-3542-4eb9-8b5f-27e627139c14",
      "name": "Send a text message1",
      "webhookId": "f4772a9b-bbbe-4bf8-893e-5da851d91f2d",
      "credentials": {}
    },
    {
      "parameters": {
        "chatId": "6228081299",
        "text": "video saved",
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        1264,
        1296
      ],
      "id": "c83fdf6b-aac4-4caf-8721-669c7a8b1abd",
      "name": "Send a text message2",
      "webhookId": "7710106b-c1b2-4d82-bd6f-15bf5c143716",
      "credentials": {}
    },
    {
      "parameters": {
        "options": {}
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        768,
        0
      ],
      "id": "64375efc-9e1f-4608-8068-d94b28f437f2",
      "name": "Edit Fields1"
    },
    {
      "parameters": {
        "options": {}
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        976,
        0
      ],
      "id": "34327e8b-1f47-4160-8e4d-796e612fc97a",
      "name": "Edit Fields2"
    },
    {
      "parameters": {
        "updates": [
          "message"
        ],
        "additionalFields": {}
      },
      "id": "f493a8dd-56cf-4cdb-aa12-fcf1badd13d8",
      "name": "Telegram Trigger",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        -1200,
        -48
      ],
      "webhookId": "70d965f1-4d42-4b68-9122-751279046934",
      "typeVersion": 1.2,
      "credentials": {
        "telegramApi": {
          "id": "5BjZgtWlAghx9Zit",
          "name": "Reel Analyzer"
        }
      }
    },
    {
      "parameters": {
        "name": "Transcript.mp4",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "folderId": {
          "__rl": true,
          "value": "https://drive.google.com/drive/folders/13GTMhShXDwz_j_TZkoKZVBVDuSHA4Ngj",
          "mode": "url"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleDrive",
      "typeVersion": 3,
      "position": [
        224,
        528
      ],
      "id": "72a8a7ce-19d3-4de2-88eb-b522d18a9b05",
      "name": "Upload file3",
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "UcfIN5LCO68VG5wm",
          "name": "07/01"
        }
      }
    },
    {
      "parameters": {
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        -992,
        -48
      ],
      "id": "3e8cd136-edc5-4f83-9375-70e3dee270cc",
      "name": "Send a text message3",
      "webhookId": "206c5156-7032-4363-b969-5a2f87d18de1",
      "credentials": {
        "telegramApi": {
          "id": "5BjZgtWlAghx9Zit",
          "name": "Reel Analyzer"
        }
      }
    }
  ],
  "connections": {
    "Get TikTok Video Page Data": {
      "main": [
        [
          {
            "node": "Scrape raw video URL",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Scrape raw video URL": {
      "main": [
        [
          {
            "node": "Output video file without watermark",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Output video file without watermark": {
      "main": [
        [
          {
            "node": "Analyze video1",
            "type": "main",
            "index": 0
          },
          {
            "node": "Send a text message",
            "type": "main",
            "index": 0
          },
          {
            "node": "Edit Fields1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Edit Fields": {
      "main": [
        [
          {
            "node": "Get TikTok Video Page Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "video scraping": {
      "main": [
        [
          {
            "node": "Genrate download link",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Genrate download link": {
      "main": [
        [
          {
            "node": "DOWNLOAD FB VID",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Link checking": {
      "main": [
        [
          {
            "node": "FB API FETCHING",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "INVALID URL",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If": {
      "main": [
        [
          {
            "node": "INSTA API FETCHING",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Link checking",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "FB API FETCHING": {
      "main": [
        [
          {
            "node": "video scraping",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "INSTA API FETCHING": {
      "main": [
        [
          {
            "node": "URL FINDER",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "URL FINDER": {
      "main": [
        [
          {
            "node": "URL DECODER",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "URL DECODER": {
      "main": [
        [
          {
            "node": "DOWNLOAD INSTA VID",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "DOWNLOAD INSTA VID": {
      "main": [
        [
          {
            "node": "Send a text message1",
            "type": "main",
            "index": 0
          },
          {
            "node": "Upload file",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "DOWNLOAD FB VID": {
      "main": [
        [
          {
            "node": "Analyze video2",
            "type": "main",
            "index": 0
          },
          {
            "node": "Upload file2",
            "type": "main",
            "index": 0
          },
          {
            "node": "Send a text message2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "FB IG LINK REGEX": {
      "main": [
        [
          {
            "node": "If",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Telegram Trigger1": {
      "main": [
        [
          {
            "node": "Link checking1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Link checking1": {
      "main": [
        [
          {
            "node": "Edit Fields",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "FB IG LINK REGEX",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Analyze video": {
      "main": [
        [
          {
            "node": "Append row in sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Append row in sheet": {
      "main": [
        []
      ]
    },
    "Analyze video1": {
      "main": [
        [
          {
            "node": "Append row in sheet1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Analyze video2": {
      "main": [
        [
          {
            "node": "Append row in sheet2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send a text message1": {
      "main": [
        []
      ]
    },
    "Edit Fields1": {
      "main": [
        [
          {
            "node": "Edit Fields2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Edit Fields2": {
      "main": [
        [
          {
            "node": "Upload file1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Telegram Trigger": {
      "main": [
        [
          {
            "node": "Send a text message3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {
    "Telegram Trigger1": [
      {
        "update_id": 888547672,
        "message": {
          "message_id": 2134,
          "from": {
            "id": 6228081299,
            "is_bot": false,
            "first_name": "Mathew",
            "last_name": "Jordan",
            "username": "jordanengg",
            "language_code": "en"
          },
          "chat": {
            "id": 6228081299,
            "first_name": "Mathew",
            "last_name": "Jordan",
            "username": "jordanengg",
            "type": "private"
          },
          "date": 1767344145,
          "text": "https://www.instagram.com/reel/DS2da-4D7_z/?igsh=OTZkYjg1bzNnZzZy",
          "entities": [
            {
              "offset": 0,
              "length": 65,
              "type": "url"
            }
          ],
          "link_preview_options": {
            "url": "https://www.instagram.com/reel/DS2da-4D7_z/?igsh=OTZkYjg1bzNnZzZy"
          }
        }
      }
    ],
    "Telegram Trigger": [
      {
        "update_id": 888547672,
        "message": {
          "message_id": 2134,
          "from": {
            "id": 6228081299,
            "is_bot": false,
            "first_name": "Mathew",
            "last_name": "Jordan",
            "username": "jordanengg",
            "language_code": "en"
          },
          "chat": {
            "id": 6228081299,
            "first_name": "Mathew",
            "last_name": "Jordan",
            "username": "jordanengg",
            "type": "private"
          },
          "date": 1767344145,
          "text": "https://www.instagram.com/reel/DS2da-4D7_z/?igsh=OTZkYjg1bzNnZzZy",
          "entities": [
            {
              "offset": 0,
              "length": 65,
              "type": "url"
            }
          ],
          "link_preview_options": {
            "url": "https://www.instagram.com/reel/DS2da-4D7_z/?igsh=OTZkYjg1bzNnZzZy"
          }
        }
      }
    ]
  },
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "3039fbd4cadb80067e54b2133333595ff57d847dd0124b88f494b4fc1d62ef2e"
  }
}