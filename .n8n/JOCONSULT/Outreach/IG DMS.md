---
tags:
  - automation
---
{
  "nodes": [
    {
      "parameters": {
        "amount": 2
      },
      "id": "d1dfab6e-c3df-473e-9827-996fb1f95fd9",
      "name": "Wait2",
      "type": "n8n-nodes-base.wait",
      "position": [
        3040,
        1792
      ],
      "webhookId": "1f2864af-8b9b-419f-9098-0260745d0d9f",
      "typeVersion": 1.1
    },
    {
      "parameters": {
        "operation": "appendOrUpdate",
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1ZNX9fypcwyObMT5tXV6U7iQ7lth2xYul-q8diaiohlo",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1ZNX9fypcwyObMT5tXV6U7iQ7lth2xYul-q8diaiohlo/edit?usp=drivesdk",
          "cachedResultName": "next-task"
        },
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": 1434077398,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1ZNX9fypcwyObMT5tXV6U7iQ7lth2xYul-q8diaiohlo/edit#gid=1434077398",
          "cachedResultName": "acc"
        },
        "columns": {
          "value": {
            "Active": "=TRUE",
            "username": "={{ $json.user }}"
          },
          "schema": [
            {
              "id": "username",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "username",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "password",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "password",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "proxy",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "proxy",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Active",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Active",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "username"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "id": "6b0e9ce1-0997-448f-a283-a8abc3b22934",
      "name": "Append or update row in sheet1",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        2816,
        1792
      ],
      "typeVersion": 4.7
    },
    {
      "parameters": {
        "options": {}
      },
      "id": "1c067212-a774-4767-9e6f-4ed58f9b8e1f",
      "name": "Loop Over Items2",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        2144,
        1888
      ],
      "typeVersion": 3
    },
    {
      "parameters": {
        "method": "POST",
        "url": "http://host.docker.internal:3001/login",
        "sendBody": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "username",
              "value": "={{ $json.username }}"
            },
            {
              "name": "password",
              "value": "={{ $json.password }}"
            },
            {
              "name": "proxy",
              "value": "={{ $json.proxy }}"
            }
          ]
        },
        "options": {}
      },
      "id": "c03abc9f-9ed2-4fc3-b52a-856f3866b521",
      "name": "HTTP Request1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        2368,
        1888
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1ZNX9fypcwyObMT5tXV6U7iQ7lth2xYul-q8diaiohlo",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1ZNX9fypcwyObMT5tXV6U7iQ7lth2xYul-q8diaiohlo/edit?usp=drivesdk",
          "cachedResultName": "next-task"
        },
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": 1434077398,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1ZNX9fypcwyObMT5tXV6U7iQ7lth2xYul-q8diaiohlo/edit#gid=1434077398",
          "cachedResultName": "acc"
        },
        "options": {}
      },
      "id": "66ac6441-7d35-4a64-bae2-f7b6d02c79d7",
      "name": "Get row(s) in sheet2",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1920,
        1888
      ],
      "typeVersion": 4.7
    },
    {
      "parameters": {
        "options": {}
      },
      "id": "e5737237-5da3-4ffb-8e8f-fa935b3f1aa5",
      "name": "Loop Over Items3",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        1664,
        1104
      ],
      "typeVersion": 3
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
              "id": "1f33fb41-ca94-4dd6-8303-b099d518b915",
              "operator": {
                "type": "string",
                "operation": "empty",
                "singleValue": true
              },
              "leftValue": "={{ $json.Status }}",
              "rightValue": "s"
            }
          ]
        },
        "options": {}
      },
      "id": "68323e76-1c57-467b-b963-c604fb094a27",
      "name": "Filter1",
      "type": "n8n-nodes-base.filter",
      "position": [
        1216,
        1104
      ],
      "typeVersion": 2.2
    },
    {
      "parameters": {
        "maxItems": 100
      },
      "id": "fd420681-4804-42b5-9bee-2296792e91dc",
      "name": "Limit1",
      "type": "n8n-nodes-base.limit",
      "position": [
        1440,
        1104
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1ZNX9fypcwyObMT5tXV6U7iQ7lth2xYul-q8diaiohlo",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1ZNX9fypcwyObMT5tXV6U7iQ7lth2xYul-q8diaiohlo/edit?usp=drivesdk",
          "cachedResultName": "next-task"
        },
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1ZNX9fypcwyObMT5tXV6U7iQ7lth2xYul-q8diaiohlo/edit#gid=0",
          "cachedResultName": "leads"
        },
        "options": {}
      },
      "id": "a1a8d7cd-628c-488c-9bc8-8ef3c6b56027",
      "name": "Get row(s) in sheet3",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        992,
        1104
      ],
      "typeVersion": 4.7
    },
    {
      "parameters": {
        "content": "## Login with an instagram account",
        "height": 384,
        "width": 2528,
        "color": 3
      },
      "id": "72e54690-e964-4a3b-820c-8954f4543937",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1216,
        1728
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "method": "POST",
        "url": "http://host.docker.internal:3001/instagram",
        "sendBody": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "to",
              "value": "={{ $json['username '] }}"
            },
            {
              "name": "message",
              "value": "={{ $json.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "e255e7e5-5445-48f5-a4de-a0a1a2736f8e",
      "name": "HTTP Request5",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1888,
        736
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "method": "POST",
        "url": "http://host.docker.internal:3001/viewstory",
        "sendBody": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "status",
              "value": "start"
            }
          ]
        },
        "options": {}
      },
      "id": "0e7c260a-8fb5-493b-970b-822d8ef69257",
      "name": "start-viewing-storeies",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        2560,
        544
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "jsCode": "// n8n Function Node code\n\n// Generate random delay between min and max seconds\nfunction randomDelaySeconds(minSec = 0.2, maxSec = 0.5) {\n  return Math.floor(Math.random() * (maxSec - minSec + 1) + minSec);\n}\n\n// Example: get current message (from previous node)\nconst messages = items.map(item => item.json.message);\n\n// Output array\nconst output = [];\n\nfor (let i = 0; i < messages.length; i++) {\n  output.push({\n    json: {\n      message: messages[i],\n      delaySeconds: randomDelaySeconds(20, 30), // random 20–25 sec delay\n    }\n  });\n}\n\nreturn output;\n"
      },
      "id": "163eebbe-bbcb-4864-a153-2498eef97cd9",
      "name": "Code in JavaScript3",
      "type": "n8n-nodes-base.code",
      "position": [
        2784,
        544
      ],
      "typeVersion": 2
    },
    {
      "parameters": {
        "amount": "={{ $('Code in JavaScript3').item.json.delaySeconds }}"
      },
      "id": "db21f6c6-c8c9-415f-997a-45026e22c21b",
      "name": "Wait5",
      "type": "n8n-nodes-base.wait",
      "position": [
        3232,
        544
      ],
      "webhookId": "7dc4be61-a5f8-4345-b67f-d1ea9366969f",
      "typeVersion": 1.1
    },
    {
      "parameters": {
        "method": "POST",
        "url": "http://host.docker.internal:3001/viewstory",
        "sendBody": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "status",
              "value": "stop"
            }
          ]
        },
        "options": {}
      },
      "id": "917f4879-3b5c-44dd-8905-cbe261cde5cc",
      "name": "start-viewing-storeies1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        3456,
        544
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "jsCode": "// n8n Function Node code\n\n// Generate random delay between min and max seconds\nfunction randomDelaySeconds(minSec = 0.2, maxSec = 0.5) {\n  return Math.floor(Math.random() * (maxSec - minSec + 1) + minSec);\n}\n\n// Example: get current message (from previous node)\nconst messages = items.map(item => item.json.message);\n\n// Output array\nconst output = [];\n\nfor (let i = 0; i < messages.length; i++) {\n  output.push({\n    json: {\n      message: messages[i],\n      delaySeconds: randomDelaySeconds(10, 20), // random 20–25 sec delay\n    }\n  });\n}\n\nreturn output;\n"
      },
      "id": "3a6f2ca4-03ed-48a0-9c9a-adde57eb32f2",
      "name": "Code in JavaScript4",
      "type": "n8n-nodes-base.code",
      "position": [
        3680,
        544
      ],
      "typeVersion": 2
    },
    {
      "parameters": {
        "amount": "={{ $('Code in JavaScript4').item.json.delaySeconds }}"
      },
      "id": "1fc7e706-e500-409c-8d14-ba19ba28b6ef",
      "name": "Wait6",
      "type": "n8n-nodes-base.wait",
      "position": [
        4128,
        912
      ],
      "webhookId": "7dc4be61-a5f8-4345-b67f-d1ea9366969f",
      "typeVersion": 1.1
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1ZNX9fypcwyObMT5tXV6U7iQ7lth2xYul-q8diaiohlo",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1ZNX9fypcwyObMT5tXV6U7iQ7lth2xYul-q8diaiohlo/edit?usp=drivesdk",
          "cachedResultName": "next-task"
        },
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1ZNX9fypcwyObMT5tXV6U7iQ7lth2xYul-q8diaiohlo/edit#gid=0",
          "cachedResultName": "leads"
        },
        "columns": {
          "value": {
            "Status": "send",
            "username ": "={{ $('Loop Over Items3').item.json['username '] }}",
            "Time Stamp": "= {{ $now.format('hh:mm a') }} / {{ $now.format('yyyy-MM-dd') }}\n"
          },
          "schema": [
            {
              "id": "username ",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "username ",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "message",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "message",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Status",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Status",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Time Stamp",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Time Stamp",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "row_number",
              "type": "number",
              "display": true,
              "removed": true,
              "readOnly": true,
              "required": false,
              "displayName": "row_number",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "username "
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "id": "23e62155-5b82-4735-9e1a-ce6d45332f8c",
      "name": "Update row in sheet6",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        2336,
        544
      ],
      "typeVersion": 4.7
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
              "id": "54987f58-a3ac-499b-b114-27b2364a6c5e",
              "operator": {
                "type": "boolean",
                "operation": "true",
                "singleValue": true
              },
              "leftValue": "={{ $json.success }}",
              "rightValue": ""
            }
          ]
        },
        "options": {}
      },
      "id": "bebd3728-b2bb-4403-aa19-b1e6ef12e200",
      "name": "If3",
      "type": "n8n-nodes-base.if",
      "position": [
        2112,
        736
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
              "id": "ba487652-ef4d-4d00-8423-e826224ba7aa",
              "operator": {
                "type": "boolean",
                "operation": "true",
                "singleValue": true
              },
              "leftValue": "={{ $json.success }}",
              "rightValue": ""
            }
          ]
        },
        "options": {}
      },
      "id": "1c1989b5-0e2c-43c4-84cc-970dce60b18f",
      "name": "If",
      "type": "n8n-nodes-base.if",
      "position": [
        2592,
        1888
      ],
      "typeVersion": 2.2
    },
    {
      "parameters": {
        "errorMessage": "Try again login with the account"
      },
      "id": "e17bce9c-0795-4dea-aea7-30ac3cf1ccba",
      "name": "Stop and Error",
      "type": "n8n-nodes-base.stopAndError",
      "position": [
        2816,
        1984
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "## Sending Messge to the username from google sheet",
        "color": 7
      },
      "id": "d3d239a3-59c9-4127-bc25-99ac3e17584b",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1744,
        592
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "## Getting the leads information",
        "color": 7
      },
      "id": "2f4540a1-a84a-422a-8e3e-9fe5d8758a73",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        944,
        1264
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "## Filtering based onthe send status that is avaliable on google sheet",
        "color": 7
      },
      "id": "bb824f9d-6978-4d17-b75a-3f4de8c28986",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1248,
        912
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "## If message is send then updating it on google sheet",
        "color": 7
      },
      "id": "e6526d4e-326c-47f9-b5a8-fa396f5deaa1",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2272,
        368
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "## Waiting 15 -20 seconds , before running the story views",
        "color": 7
      },
      "id": "6ee5fc42-5bb9-431b-a931-a40dd7feed65",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2720,
        672
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "## Starting the stories views and scroll interactions",
        "color": 7
      },
      "id": "02830eb8-047f-44d6-a245-cd4dbc639a68",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        3344,
        704
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "## Stoping the stories views and scroll interactions",
        "height": 128,
        "color": 7
      },
      "id": "d2af3b9d-fcac-464c-8d4d-141e0cbae17c",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        3824,
        480
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "## Waiting 4.5 to 5.5 minutes for this story views and stuff",
        "color": 7
      },
      "id": "e30da4c4-5b13-46e6-9d02-44d5b15c5b7a",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2896,
        320
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "## Waiting for 2 to 3 minutes  before sending the next message ",
        "color": 7
      },
      "id": "d9107882-fffd-4704-88bc-1e646206d976",
      "name": "Sticky Note9",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        4240,
        816
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "## run the below workflow first ,before running this ",
        "color": 7
      },
      "id": "2d8cb79e-d751-4178-8987-217a2754d66c",
      "name": "Sticky Note10",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        512,
        1120
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
          "combinator": "and",
          "conditions": [
            {
              "id": "54987f58-a3ac-499b-b114-27b2364a6c5e",
              "operator": {
                "type": "boolean",
                "operation": "true",
                "singleValue": true
              },
              "leftValue": "={{ $json.requestExceeded }}",
              "rightValue": ""
            }
          ]
        },
        "options": {}
      },
      "id": "44e50a43-9d9f-4600-8617-311a19e53da3",
      "name": "If4",
      "type": "n8n-nodes-base.if",
      "position": [
        2336,
        832
      ],
      "typeVersion": 2.2
    },
    {
      "parameters": {
        "errorMessage": "={{ $json.error }}"
      },
      "id": "43299226-4ea5-472b-8d39-678ae8dba858",
      "name": "Stop and Error1",
      "type": "n8n-nodes-base.stopAndError",
      "position": [
        2560,
        736
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "## Checking for the rate limit if exceed , it will stop",
        "color": 7
      },
      "id": "33e9c3d0-5a25-4bf2-9644-e138ea1e10c3",
      "name": "Sticky Note11",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2128,
        896
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "path": "3cb5f159-4fc0-426e-8b16-8da1049fa7f1",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "c04415c1-f24a-4db3-ad26-890cb88fe8cb",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        1696,
        1888
      ],
      "webhookId": "3cb5f159-4fc0-426e-8b16-8da1049fa7f1",
      "typeVersion": 2.1
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={\n  \"success\": {{ $('HTTP Request1').item.json.success }} ,\n  \"message\": \"{{ $('HTTP Request1').item.json.message }}\",\n  \"user\": \"{{ $('HTTP Request1').item.json.user }}\"\n} ",
        "options": {}
      },
      "id": "4876c76d-ed7f-4485-846d-5f5f562f5c18",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        3264,
        1792
      ],
      "typeVersion": 1.4
    },
    {
      "parameters": {
        "path": "cdf1fb17-2208-4676-bc41-70e5fa0a2ecc",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "77141971-0452-46db-acde-cdf9b23bf4ec",
      "name": "Webhook1",
      "type": "n8n-nodes-base.webhook",
      "position": [
        768,
        1104
      ],
      "webhookId": "cdf1fb17-2208-4676-bc41-70e5fa0a2ecc",
      "typeVersion": 2.1
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1ZNX9fypcwyObMT5tXV6U7iQ7lth2xYul-q8diaiohlo",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1ZNX9fypcwyObMT5tXV6U7iQ7lth2xYul-q8diaiohlo/edit?usp=drivesdk",
          "cachedResultName": "next-task"
        },
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1ZNX9fypcwyObMT5tXV6U7iQ7lth2xYul-q8diaiohlo/edit#gid=0",
          "cachedResultName": "leads"
        },
        "columns": {
          "value": {
            "Status": "=not-send ( Error :  {{ $json.error }} ) ",
            "username ": "={{ $('Loop Over Items3').item.json['username '] }}",
            "Time Stamp": "= {{ $now.format('hh:mm a') }} / {{ $now.format('yyyy-MM-dd') }}\n"
          },
          "schema": [
            {
              "id": "username ",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "username ",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "message",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "message",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Status",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Status",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Time Stamp",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Time Stamp",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "row_number",
              "type": "number",
              "display": true,
              "removed": true,
              "readOnly": true,
              "required": false,
              "displayName": "row_number",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "username "
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "id": "e3456636-1097-4fa0-b1e3-65b1f81f9d16",
      "name": "Update row in sheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        2560,
        928
      ],
      "typeVersion": 4.7
    },
    {
      "parameters": {
        "method": "POST",
        "url": "http://host.docker.internal:3001/logthis",
        "sendBody": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "message",
              "value": "=🧠 Simulating user actions | Delay {{ $json.delaySeconds }}s\n"
            }
          ]
        },
        "options": {}
      },
      "id": "feef282a-1753-40a9-9b37-5057f1451f0d",
      "name": "HTTP Request2",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        3008,
        544
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "method": "POST",
        "url": "http://host.docker.internal:3001/logthis",
        "sendBody": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "message",
              "value": "=⏳ Waiting {{ $json.delaySeconds }}s before next user\n"
            }
          ]
        },
        "options": {}
      },
      "id": "8ddf1b2b-1950-4157-9728-891da5bff1c2",
      "name": "HTTP Request4",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        3904,
        544
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "{\n  \"myField\": \"done man \"\n}",
        "options": {}
      },
      "id": "25e4506d-d460-438a-94f2-27cfa6fe76d6",
      "name": "Respond to Webhook1",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1888,
        1024
      ],
      "typeVersion": 1.4
    },
    {
      "parameters": {
        "content": "### **🤖 Instagram DM Automation Workflow**\n\n---\n\n## **How It Works**\n\nThis workflow automates **Instagram direct messages and engagement tasks** using a **Puppeteer-powered backend**.\nIt connects with **Google Sheets** to fetch leads (Instagram usernames and custom messages) and sends **personalized DMs** automatically — while also simulating real human actions like scrolling, liking posts, and viewing stories.\n\nThe automation helps marketers and creators **nurture leads**, **maintain engagement**, and **save hours of manual effort** by running safe, human-like interactions on Instagram. It also logs all activity and updates your Google Sheets with the latest DM status for transparent tracking.\n\n---\n\n## **Setup Steps**\n\n1. **Google Sheets:** Connect with OAuth2 and add Sheet IDs for `leads` and `acc` tracking.\n2. **Backend Service:** Host a Puppeteer service (Node.js) handling `/login`, `/instagram`, `/viewstory`, and `/logthis`.\n3. **Webhook:** Use your n8n Webhook URL to trigger the workflow manually or through API calls.\n4. **Timing:** Adjust DM or story-view delays in “Code (JavaScript)” nodes for safety.\n5. **Test Run:** Try with 1–2 leads before deployment to confirm messages, logging, and updates.\n\n🕐 **Setup time:** ~10–15 minutes\n💡 Once connected, just trigger the workflow — it’ll do the rest automatically.\n",
        "height": 1008,
        "width": 1040
      },
      "id": "2e91d925-6c59-472a-b8b4-cbc69803f3c9",
      "name": "Sticky Note12",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        0
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "## This isthe Flow of login with an instagram account ",
        "color": 7
      },
      "id": "0c5624f0-39ef-4379-b7b2-4fc24a0ef901",
      "name": "Sticky Note13",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1104,
        1872
      ],
      "typeVersion": 1
    }
  ],
  "connections": {
    "Wait2": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Append or update row in sheet1": {
      "main": [
        [
          {
            "node": "Wait2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Loop Over Items2": {
      "main": [
        [],
        [
          {
            "node": "HTTP Request1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request1": {
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
    "Get row(s) in sheet2": {
      "main": [
        [
          {
            "node": "Loop Over Items2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Loop Over Items3": {
      "main": [
        [
          {
            "node": "Respond to Webhook1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "HTTP Request5",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter1": {
      "main": [
        [
          {
            "node": "Limit1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Limit1": {
      "main": [
        [
          {
            "node": "Loop Over Items3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get row(s) in sheet3": {
      "main": [
        [
          {
            "node": "Filter1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request5": {
      "main": [
        [
          {
            "node": "If3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "start-viewing-storeies": {
      "main": [
        [
          {
            "node": "Code in JavaScript3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Code in JavaScript3": {
      "main": [
        [
          {
            "node": "HTTP Request2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wait5": {
      "main": [
        [
          {
            "node": "start-viewing-storeies1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "start-viewing-storeies1": {
      "main": [
        [
          {
            "node": "Code in JavaScript4",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Code in JavaScript4": {
      "main": [
        [
          {
            "node": "HTTP Request4",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wait6": {
      "main": [
        [
          {
            "node": "Loop Over Items3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Update row in sheet6": {
      "main": [
        [
          {
            "node": "start-viewing-storeies",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If3": {
      "main": [
        [
          {
            "node": "Update row in sheet6",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "If4",
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
            "node": "Append or update row in sheet1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Stop and Error",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If4": {
      "main": [
        [
          {
            "node": "Stop and Error1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Update row in sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Webhook": {
      "main": [
        [
          {
            "node": "Get row(s) in sheet2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Webhook1": {
      "main": [
        [
          {
            "node": "Get row(s) in sheet3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Update row in sheet": {
      "main": [
        [
          {
            "node": "Loop Over Items3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request2": {
      "main": [
        [
          {
            "node": "Wait5",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request4": {
      "main": [
        [
          {
            "node": "Wait6",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {},
  "meta": {
    "instanceId": "3039fbd4cadb80067e54b2133333595ff57d847dd0124b88f494b4fc1d62ef2e"
  }
}