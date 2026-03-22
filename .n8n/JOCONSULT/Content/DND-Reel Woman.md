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
      "id": "9003700d-c95f-4acd-841c-152222741f8a",
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
      "id": "e2700c3c-0792-4509-adc9-fe08b393edb9",
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
      "id": "ca9992aa-8753-4aeb-925b-e6e72a2d18df",
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
      "id": "62ce245d-e1cc-4aeb-b956-d9bf884c6fd1",
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
      "id": "66e48974-8e80-421c-b5e8-d396870cba32",
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
      "id": "8a0a60d7-c5d5-44dc-b35e-51ad6cc328e2",
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
      "id": "cdc7a176-d83f-4459-8aa2-2e9ed48e802d",
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
      "id": "2c6d0aa6-cc64-4577-9e9b-38ee1e0755e7",
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
              "value": "={{ $('ReelSaveFitWoman').item.json.message.text }}"
            }
          ]
        },
        "options": {}
      },
      "id": "44da0b66-bf9d-4f52-aa16-9e53ff806a39",
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
      "id": "760fe932-c92b-436f-bb69-275ac83348a1",
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
      "id": "c49f849e-d0eb-4efa-b920-c891069e3b8f",
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
      "id": "9b44c0eb-7b5d-4f53-9a76-c5519dd76320",
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
      "id": "1dd12c1c-b341-46e5-b2d4-c961eafc43af",
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
      "id": "2f2fa55e-f217-4e51-903b-b9ecea45785a",
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
        "chatId": "={{ $('ReelSaveFitWoman').item.json.message.chat.id }}",
        "text": "Please paste only facebook/Instagram link ⚠️",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "id": "d1fdb1fd-482b-4713-9b18-8048bdab5263",
      "name": "INVALID URL",
      "type": "n8n-nodes-base.telegram",
      "position": [
        192,
        1440
      ],
      "webhookId": "ebe5c941-482d-4fcb-a8ba-bafaeb5087cd",
      "typeVersion": 1.2,
      "credentials": {}
    },
    {
      "parameters": {
        "jsCode": "const url = $input.first().json.message.text; // your input text\n\n// Regex patterns\nconst fbRegex = /https?:\\/\\/([a-zA-Z0-9-]+\\.)?facebook\\.com\\/[^\\s]+/i;\nconst igRegex = /https?:\\/\\/([a-zA-Z0-9-]+\\.)?instagram\\.com\\/[^\\s]+/i;\n\n// Match\nconst fbMatch = url.match(fbRegex);\nconst igMatch = url.match(igRegex);\n\nreturn {\n  json: {\n    isFacebookLink: !!fbMatch,\n    facebookUrl: fbMatch ? fbMatch[0] : null,\n    isInstagramLink: !!igMatch,\n    instagramUrl: igMatch ? igMatch[0] : null\n  }\n};\n"
      },
      "id": "3e520518-0e20-4fd9-a63c-17d3d6332a11",
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
      "id": "b557974d-dda2-4c73-8236-e793f0501d57",
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
      "id": "12846fa8-2142-43ed-9242-ea5bf5ccb362",
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
      "id": "f5518bea-bf31-409b-9630-e7ed6002ee8e",
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
      "id": "09c3c25c-0b04-4554-9682-52b80ced27f5",
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
      "id": "492508cb-5fe5-4251-bcab-d5b16c6b8291",
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
              "leftValue": "={{ $('ReelSaveFitWoman').item.json.message.text }} {{ $('ReelSaveFitWoman').item.json.message.link_preview_options.url }}",
              "rightValue": "tiktok"
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "id": "799608eb-368d-4e7a-9f79-c2c254ccd18b",
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
      "id": "7eb334b9-71b6-4964-8a98-4018ee16311e",
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
      "id": "29226020-40d7-4a65-a319-bfc512af2979",
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
      "id": "60bdcaf4-9f86-456d-9803-a67975a61d16",
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
        1328,
        -112
      ],
      "id": "71426c29-5244-40d8-b830-b4bcd2986223",
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
      "id": "4e6f33e6-aa44-41e5-bcbe-3e679e342fa5",
      "name": "Append row in sheet1",
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
      "id": "a37ffbff-e435-4ca8-808b-397bac451877",
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
      "id": "17297828-7dce-4852-9948-fa8a7c471b5e",
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
      "id": "853cbb41-a38a-4abc-8f28-8a47a5bece77",
      "name": "Send a text message",
      "webhookId": "e541e374-dcbb-4656-a6f6-6f63f3f802ba",
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
      "id": "ab2b3fed-c96b-4463-9fe4-dc12b84a6965",
      "name": "Send a text message1",
      "webhookId": "19fd95bf-a26c-457b-acd3-58dfc106a2a4",
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
      "id": "f655e198-2e87-4211-aa2f-4fa627b9ecdd",
      "name": "Send a text message2",
      "webhookId": "7e887413-eac4-45a8-bf20-c130be7d07c8",
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
      "id": "82f48034-4f1a-4acf-a7da-9730f06459b7",
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
      "id": "6aabf454-1ad8-4097-8147-262cdc41f3ac",
      "name": "Edit Fields2"
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
          "value": "https://drive.google.com/drive/folders/1SKr3mr8aOHlSHZJcJIetM43V-Q0Wziso",
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
      "id": "7ec3cf87-8de1-490d-8e30-e9e3bcb8f416",
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
          "value": "https://drive.google.com/drive/folders/1SKr3mr8aOHlSHZJcJIetM43V-Q0Wziso",
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
      "id": "abc88721-6bd4-4f9d-ba5c-c0359f57e563",
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
          "value": "https://drive.google.com/drive/folders/1SKr3mr8aOHlSHZJcJIetM43V-Q0Wziso",
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
      "id": "31955963-b347-485d-8abc-96df8c53ee74",
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
        "updates": [
          "message"
        ],
        "additionalFields": {}
      },
      "id": "358c6817-a945-4acb-b0a1-469b2bb18031",
      "name": "ReelSaveFitWoman",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        -1056,
        384
      ],
      "webhookId": "7f31f00a-66e6-497b-877b-af986de37cb2",
      "typeVersion": 1.2,
      "credentials": {}
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
            "node": "Reels Fitness",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "ReelSaveFitWoman": {
      "main": [
        [
          {
            "node": "Link checking1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {
    "ReelSaveFitWoman": [
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