---
tags:
  - consulting
---
{
  "nodes": [
    {
      "parameters": {
        "updates": [
          "message"
        ],
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegramTrigger",
      "typeVersion": 1.2,
      "position": [
        368,
        -80
      ],
      "id": "4db1c44b-17ab-4ed8-b48e-bf0281b7aed1",
      "name": "Telegram Trigger",
      "webhookId": "a6e473a4-8ef5-459f-a0ad-3997c69182df",
      "credentials": {
        "telegramApi": {
          "id": "5BjZgtWlAghx9Zit",
          "name": "Reel Analyzer"
        }
      }
    },
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
      "id": "247bf3ad-eb55-4c56-bdf2-9feca4b5451c",
      "name": "Get TikTok Video Page Data",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1648,
        -480
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "jsCode": "const html = $input.first().json.data;\nconst headers = $input.first().json.headers || {};\nconst cookies = headers['set-cookie'] || [];\n\nif (!html) {\n  throw new Error(\"Unable to load TikTok page. Please try again!\");\n}\n\n// Find JSON data from script tag\nconst regex = /<script id=\"__UNIVERSAL_DATA_FOR_REHYDRATION__\" type=\"application\\/json\">([\\s\\S]*?)<\\/script>/;\nconst match = html.match(regex);\n\nif (!match) {\n  throw new Error(\"Video data not found. The link may be deleted or private.\");\n}\n\nconst jsonStr = match[1];\nlet data;\n\ntry {\n  data = JSON.parse(jsonStr);\n} catch (e) {\n  throw new Error(\"Unable to parse video data. Please try again!\");\n}\n\n// Get video URL from multiple possible paths\nconst itemInfo = data?.__DEFAULT_SCOPE__?.[\"webapp.video-detail\"]?.itemInfo?.itemStruct;\nconst videoUrl = itemInfo?.video?.playAddr || itemInfo?.video?.downloadAddr;\n\nif (!videoUrl) {\n  throw new Error(\"Video URL not found. The video may be restricted from downloading.\");\n}\n\nconst videoInfo = {\n  videoUrl: videoUrl,\n  cookies: cookies.join('; '),\n  description: itemInfo?.desc || 'TikTok Video',\n  author: itemInfo?.author?.uniqueId || 'unknown',\n  stats: {\n    plays: itemInfo?.stats?.playCount || 0,\n    likes: itemInfo?.stats?.diggCount || 0,\n    comments: itemInfo?.stats?.commentCount || 0\n  }\n};\n\nreturn [{ json: videoInfo }];"
      },
      "id": "148dbfc2-bde5-4afb-a567-434d835b5cb6",
      "name": "Scrape raw video URL",
      "type": "n8n-nodes-base.code",
      "position": [
        1824,
        -480
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
      "id": "c691d135-82da-4ff4-a7ee-05bd72c236c9",
      "name": "Output video file without watermark",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1984,
        -480
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
        1376,
        -480
      ],
      "id": "bcd21170-b732-4815-abd3-6e83c1205f6f",
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
      "id": "d6857524-eeb5-4971-9c3f-4afee2085597",
      "name": "video scraping",
      "type": "n8n-nodes-base.set",
      "position": [
        1904,
        512
      ],
      "typeVersion": 3.4
    },
    {
      "parameters": {
        "jsCode": "const html = $json[\"data\"]; // replace 'data' with your actual field name\nconst match = html.match(/https:\\/\\/dl\\.snapcdn\\.app\\/download\\?token=[^\"]+/);\n\nreturn {\n  json: {\n    downloadUrl: match ? match[0] : null\n  }\n};\n"
      },
      "id": "a7abe3d5-eb5b-4988-8298-0d5cf0e19724",
      "name": "Genrate download link",
      "type": "n8n-nodes-base.code",
      "position": [
        2128,
        512
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
      "id": "6ac949bb-cc0b-43b7-a690-8eed32081bda",
      "name": "Link checking",
      "type": "n8n-nodes-base.if",
      "position": [
        1296,
        480
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
      "id": "9a8c5218-8988-4970-9309-688a13877fc7",
      "name": "If",
      "type": "n8n-nodes-base.if",
      "position": [
        1088,
        16
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
      "id": "fae4158b-12db-418f-8c13-20fca00bca7b",
      "name": "FB API FETCHING",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1680,
        512
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "url": "=https://snapdownloader.com/tools/instagram-downloader/download?url={{ $json.instagramUrl }}",
        "options": {}
      },
      "id": "dc3c879f-0714-4598-ada6-a85eba5457a5",
      "name": "INSTA API FETCHING",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1616,
        176
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "jsCode": "// n8n Function node\n// Input: HTTP Request node output (with HTML inside `data` field)\n// Output: Only the video file URL\n\nconst results = [];\n\nfor (const item of items) {\n  const html = item.json.data || \"\";\n  \n  // Regex to capture video .mp4 links\n  const regex = /(https?:\\/\\/[^\\s\"']+\\.mp4[^\\s\"']*)/gi;\n  const matches = html.match(regex);\n\n  if (matches && matches.length > 0) {\n    results.push({ json: { videoUrl: matches[0] } }); // take first video link\n  } else {\n    results.push({ json: { videoUrl: null } });\n  }\n}\n\nreturn results;\n"
      },
      "id": "07e2086e-0ffe-4433-8b52-eedee5cddd73",
      "name": "URL FINDER",
      "type": "n8n-nodes-base.code",
      "position": [
        1856,
        176
      ],
      "typeVersion": 2
    },
    {
      "parameters": {
        "jsCode": "// Function node\n// Input: items[i].json.videoUrl\n// Output: items[i].json.videoUrlClean\nreturn items.map(item => {\n  const url = (item.json.videoUrl || '').split('&amp;').join('&');\n  return { json: { ...item.json, videoUrlClean: url } };\n});\n"
      },
      "id": "f0b88b23-ae3c-4551-8ecb-39f6926ee968",
      "name": "URL DECODER",
      "type": "n8n-nodes-base.code",
      "position": [
        2064,
        176
      ],
      "typeVersion": 2
    },
    {
      "parameters": {
        "url": "={{ $json.videoUrlClean }}",
        "options": {}
      },
      "id": "bf5b946c-cb0d-400d-980f-15be992792fd",
      "name": "DOWNLOAD INSTA VID",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        2304,
        176
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "url": "={{ $json.downloadUrl }}",
        "options": {}
      },
      "id": "e8eef00d-b5a0-4586-80a7-f14a5575f084",
      "name": "DOWNLOAD FB VID",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        2352,
        512
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
      "id": "b1174976-c376-4a12-83cb-815972dffc38",
      "name": "INVALID URL",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1616,
        960
      ],
      "webhookId": "069b70f6-449e-4567-b0d2-9b80c1aac821",
      "typeVersion": 1.2
    },
    {
      "parameters": {
        "jsCode": "const url = $input.first().json.message.text; // your input text\n\n// Regex patterns\nconst fbRegex = /https?:\\/\\/([a-zA-Z0-9-]+\\.)?facebook\\.com\\/[^\\s]+/i;\nconst igRegex = /https?:\\/\\/([a-zA-Z0-9-]+\\.)?instagram\\.com\\/[^\\s]+/i;\n\n// Match\nconst fbMatch = url.match(fbRegex);\nconst igMatch = url.match(igRegex);\n\nreturn {\n  json: {\n    isFacebookLink: !!fbMatch,\n    facebookUrl: fbMatch ? fbMatch[0] : null,\n    isInstagramLink: !!igMatch,\n    instagramUrl: igMatch ? igMatch[0] : null\n  }\n};\n"
      },
      "id": "887b192d-b159-4ebd-af43-3c17b723cb1b",
      "name": "FB IG LINK REGEX",
      "type": "n8n-nodes-base.code",
      "position": [
        880,
        16
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
      "id": "7892b9f6-dc4f-441d-9b4b-636814af8ba2",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        864,
        -32
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
      "id": "7706a5fb-4b73-40b1-b977-4cb6cf68a8bb",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1616,
        448
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
      "id": "0a47a3eb-97b5-4d76-9cd7-07e259e90daa",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1536,
        -48
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
      "id": "a19e162f-0403-42ff-a9af-307e1ca9ee35",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        320,
        -208
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
      "id": "3168560e-9e13-47bf-b651-f66efd58bca9",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1600,
        880
      ],
      "typeVersion": 1
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
                "operation": "equals"
              },
              "leftValue": "={{ $json.message.text }}",
              "rightValue": "tiktok"
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "id": "f11f7b65-5ccc-4326-a6f1-cef61c645b21",
      "name": "Link checking1",
      "type": "n8n-nodes-base.if",
      "position": [
        576,
        -96
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
      "id": "34bf858a-04b5-4151-a670-3bd10fc84cb8",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1152,
        448
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
        2624,
        -32
      ],
      "id": "58556a4e-c9d0-487c-ba54-f9ff562d9442",
      "name": "Analyze video",
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
        2816,
        -32
      ],
      "id": "2fc4173a-7a3b-4690-958f-69cacba5203b",
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
        2736,
        192
      ],
      "id": "d46a39af-ce67-4586-80e2-3290b1b8699d",
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
        2752,
        -592
      ],
      "id": "ff141cd0-98bf-4509-8231-a2b6dab4afd4",
      "name": "Analyze video1",
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
        2944,
        -592
      ],
      "id": "3b3895ac-040b-4bc6-b322-72381173b5be",
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
        2960,
        -416
      ],
      "id": "d6d921cd-7857-441c-91f4-345573e5241e",
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
        2688,
        496
      ],
      "id": "4aa50a37-c48a-4bb7-863b-652c469dae9c",
      "name": "Analyze video2",
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
        2880,
        496
      ],
      "id": "bcf9c541-2dc9-46d5-add7-b2a88ee76cf1",
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
        2688,
        672
      ],
      "id": "0137f3ef-657b-42bf-8144-ab6c92dfad78",
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
        2752,
        -272
      ],
      "id": "d746dd7e-fe43-42d1-a3be-3ab681b4a746",
      "name": "Send a text message",
      "webhookId": "b9ffd582-8f89-449e-9fee-afca1feb4937"
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
        2960,
        304
      ],
      "id": "6ce227e0-6112-4873-933a-85ef5797e7a2",
      "name": "Send a text message1",
      "webhookId": "f4772a9b-bbbe-4bf8-893e-5da851d91f2d"
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
        2688,
        816
      ],
      "id": "e2f7c000-b4cc-4c89-a54c-5eedea718bd2",
      "name": "Send a text message2",
      "webhookId": "7710106b-c1b2-4d82-bd6f-15bf5c143716"
    },
    {
      "parameters": {
        "options": {}
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        2192,
        -480
      ],
      "id": "d4f97c6a-f416-4467-b387-253427d815ad",
      "name": "Edit Fields1"
    },
    {
      "parameters": {
        "options": {}
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        2400,
        -480
      ],
      "id": "0bda89da-3632-4a0f-bed4-7415e574f602",
      "name": "Edit Fields2"
    }
  ],
  "connections": {
    "Telegram Trigger": {
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
        []
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
    }
  },
  "pinData": {},
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "3039fbd4cadb80067e54b2133333595ff57d847dd0124b88f494b4fc1d62ef2e"
  }
}