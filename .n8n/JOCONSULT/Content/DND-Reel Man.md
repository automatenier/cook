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
      "id": "81caeaf0-3468-489d-a290-5e170e271674",
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
      "id": "93749e51-0eb3-44ae-ba39-bfe7bace628b",
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
      "id": "d231e3fd-5e36-4aa4-af57-ad5fa02a0e73",
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
      "id": "d84f3ea2-dfed-449e-8bef-2958db6ef0ec",
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
      "id": "dcf43ee5-f8d4-4f04-937a-715fe3afb5d2",
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
      "id": "cd3e5365-46d6-41bd-9e37-140f819ffb05",
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
      "id": "7847f61a-de13-4288-b3c3-486791155e7e",
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
      "id": "48692b3f-1fc2-4a5f-9a5c-7c0b12e1a7cc",
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
      "id": "d506b431-4872-4a67-9d68-7686e3064ce2",
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
      "id": "500aed95-b8cb-43ae-86bf-ed72a1354616",
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
      "id": "09a95cd6-d037-4765-a43c-64da5f40dfbe",
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
      "id": "43dba83a-8fea-4bd2-ac92-e643027d6c70",
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
      "id": "1ca85cea-1a92-44da-982a-46a141c84385",
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
      "id": "71507fae-210a-4d3d-8b58-751c6505659e",
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
      "id": "832043c4-2892-4809-8469-df087dbb9dd2",
      "name": "INVALID URL",
      "type": "n8n-nodes-base.telegram",
      "position": [
        192,
        1440
      ],
      "webhookId": "cf08190a-9534-40ff-9ead-76ab3bdfe48e",
      "typeVersion": 1.2,
      "credentials": {}
    },
    {
      "parameters": {
        "jsCode": "const url = $input.first().json.message.text; // your input text\n\n// Regex patterns\nconst fbRegex = /https?:\\/\\/([a-zA-Z0-9-]+\\.)?facebook\\.com\\/[^\\s]+/i;\nconst igRegex = /https?:\\/\\/([a-zA-Z0-9-]+\\.)?instagram\\.com\\/[^\\s]+/i;\n\n// Match\nconst fbMatch = url.match(fbRegex);\nconst igMatch = url.match(igRegex);\n\nreturn {\n  json: {\n    isFacebookLink: !!fbMatch,\n    facebookUrl: fbMatch ? fbMatch[0] : null,\n    isInstagramLink: !!igMatch,\n    instagramUrl: igMatch ? igMatch[0] : null\n  }\n};\n"
      },
      "id": "e7099570-8039-4fd1-a5d5-5dd3493ee195",
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
      "id": "a1a780dd-ba61-44d9-8f88-ef114516900b",
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
      "id": "5304fec6-265e-41c5-94d2-2efb61d88d1f",
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
      "id": "02966640-85ee-4288-ad68-8f35f51609b1",
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
      "id": "ba7c93f8-7a81-4d19-a9c0-1a35a197e41b",
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
      "id": "78539627-19cd-4d13-8c9e-7c34c20d3a59",
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
      "id": "54213e68-8945-4a90-ac12-807659320ff0",
      "name": "Telegram Trigger1",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        -1088,
        384
      ],
      "webhookId": "563e04dc-8c54-40d7-89cc-a5aa60950a78",
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
      "id": "68d3ba11-5fcf-423c-abfa-179f0248d8b3",
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
      "id": "770aef8f-045c-4f00-81dc-4fc86cab36af",
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
      "id": "38404d6e-ee82-44ce-bc52-2b60a9d8c301",
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
      "id": "165c521e-9b4b-46fa-b8aa-817e15214196",
      "name": "Append row in sheet",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "e2LG2x8nsg1JdYNX",
          "name": "Google Sheets account"
        }
      },
      "disabled": true
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
      "id": "f96d80bc-ff69-4c00-9984-30a7b651f400",
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
      "id": "e0bb36e3-7650-45eb-9031-e6b099141ce0",
      "name": "Append row in sheet2",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "e2LG2x8nsg1JdYNX",
          "name": "Google Sheets account"
        }
      },
      "disabled": true
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
      "id": "f868109f-5134-42cc-8018-b26737d024ac",
      "name": "Send a text message",
      "webhookId": "17ce22c7-f6c2-422f-b6ff-0d6e1027c628",
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
      "id": "361d207c-8589-432a-99ee-390f72693a13",
      "name": "Send a text message1",
      "webhookId": "17ce22c7-f6c2-422f-b6ff-0d6e1027c628",
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
      "id": "3f0e3cd5-616d-4d12-b7b2-4d7d86e9511b",
      "name": "Send a text message2",
      "webhookId": "17ce22c7-f6c2-422f-b6ff-0d6e1027c628",
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
      "id": "19de6ebb-c00c-4aec-a11a-19ae5aaf63d3",
      "name": "Edit Fields1"
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
          "value": "https://drive.google.com/drive/folders/1cL-rGqWBasCUVfDvPhpQG6I-ExMvSBkG",
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
      "id": "5be994cb-f9d5-4f0d-959a-223ec4251355",
      "name": "Reels Fitness",
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "D5yBmGClWitY2Sco",
          "name": "2/1"
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
          "value": "https://drive.google.com/drive/folders/1cL-rGqWBasCUVfDvPhpQG6I-ExMvSBkG",
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
      "id": "a87d8716-145f-40b3-ad61-6cf7cbf6090f",
      "name": "Reels Fitness1",
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "D5yBmGClWitY2Sco",
          "name": "2/1"
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
          "value": "https://drive.google.com/drive/folders/1cL-rGqWBasCUVfDvPhpQG6I-ExMvSBkG",
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
      "id": "28b93078-6a95-4d3c-a761-b8e34932a00c",
      "name": "Reels Fitness2",
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "D5yBmGClWitY2Sco",
          "name": "2/1"
        }
      }
    },
    {
      "parameters": {
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "typeVersion": 1.4,
      "position": [
        -992,
        96
      ],
      "id": "bc5920eb-4518-4d17-a7a2-f7d29b61d700",
      "name": "When chat message received",
      "webhookId": "49133821-a87c-49af-9ed8-841bdf3635a0"
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
            "node": "Reels Fitness1",
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
            "node": "Reels Fitness2",
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
            "node": "Reels Fitness",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When chat message received": {
      "main": [
        []
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
    ]
  },
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "3039fbd4cadb80067e54b2133333595ff57d847dd0124b88f494b4fc1d62ef2e"
  }
}