---
tags:
  - consulting
---
{
  "nodes": [
    {
      "parameters": {
        "operation": "download",
        "fileId": {
          "__rl": true,
          "value": "={{ $json.id }}",
          "mode": "id"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleDrive",
      "typeVersion": 3,
      "position": [
        624,
        160
      ],
      "id": "ce153b91-8376-4752-8bc2-b74bee959ec3",
      "name": "Download file",
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "UcfIN5LCO68VG5wm",
          "name": "07/01"
        }
      }
    },
    {
      "parameters": {
        "operation": "sendVideo",
        "chatId": "6228081299",
        "binaryData": true,
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        864,
        176
      ],
      "id": "6750e655-9ad5-4cef-8c8a-499b4441eb8e",
      "name": "Send a video",
      "webhookId": "db7c89a5-6fb5-4c3f-a9af-7f66bf55e7cc",
      "credentials": {}
    },
    {
      "parameters": {
        "chatId": "6228081299",
        "text": "=🚀 **NEW CONTENT SCHEDULED** 📢\n--------------------------------------\n🪝 **Hook:** {{ $json.Hook }}\n📅 **Date:** {{ $json.Posts }}\n⏰ **Time:** {{ $json.Time }}\n📂 **Type:** {{ $json.Type }}\n🎬 **Format:** {{ $json.Format }}\n\n🛠️ **Triggered:** {{ $now.setZone('Asia/Jakarta').toFormat('HH:mm / dd LLL') }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        1504,
        176
      ],
      "id": "750f283a-a4a9-43fc-841a-33346fa59761",
      "name": "Send a text message",
      "webhookId": "43fdc020-6f85-49c6-bc37-f4d602c38d35",
      "credentials": {}
    },
    {
      "parameters": {
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        },
        "triggerOn": "specificFolder",
        "folderToWatch": {
          "__rl": true,
          "value": "11_sHEKrGFUp2eZOQwpWKgwVEbd_skuuX",
          "mode": "list",
          "cachedResultName": "Calendar Fadli",
          "cachedResultUrl": "https://drive.google.com/drive/folders/11_sHEKrGFUp2eZOQwpWKgwVEbd_skuuX"
        },
        "event": "fileCreated",
        "options": {}
      },
      "type": "n8n-nodes-base.googleDriveTrigger",
      "typeVersion": 1,
      "position": [
        400,
        160
      ],
      "id": "247733a7-ef36-4a80-bca3-6491cf656646",
      "name": "Google Drive Trigger",
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "UcfIN5LCO68VG5wm",
          "name": "07/01"
        }
      }
    },
    {
      "parameters": {
        "documentId": {
          "__rl": true,
          "value": "1dqixXShSeLEow4M14mxJ5YlD84yw41vj025ZOxvdj_8",
          "mode": "list",
          "cachedResultName": "Content-JOConsult",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1dqixXShSeLEow4M14mxJ5YlD84yw41vj025ZOxvdj_8/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 1269365760,
          "mode": "list",
          "cachedResultName": "CLD-Jordan",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1dqixXShSeLEow4M14mxJ5YlD84yw41vj025ZOxvdj_8/edit#gid=1269365760"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.7,
      "position": [
        1072,
        176
      ],
      "id": "c8f7c8a0-7b58-4b32-84eb-7e686321b8d7",
      "name": "Get row(s) in sheet",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "RCC3FnRYOQz8RdxJ",
          "name": "07/01"
        }
      }
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "aa8b60cc-9824-41fa-beb4-96ab8f91171a",
              "leftValue": "={{ $json.Hook }}",
              "rightValue": "={{ $('Download file').item.json.name }}",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.filter",
      "typeVersion": 2.2,
      "position": [
        1280,
        176
      ],
      "id": "3f1fdde3-2a67-4775-b24e-f1b434eda7bc",
      "name": "Filter"
    },
    {
      "parameters": {
        "operation": "append",
        "documentId": {
          "__rl": true,
          "value": "1l_8MvNXMTsHSr4kcSapLrDOWO5EAt4tOdABMkz6teFU",
          "mode": "list",
          "cachedResultName": "Setter-JOConsult",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1l_8MvNXMTsHSr4kcSapLrDOWO5EAt4tOdABMkz6teFU/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 1561806105,
          "mode": "list",
          "cachedResultName": "Log-Fadli",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1l_8MvNXMTsHSr4kcSapLrDOWO5EAt4tOdABMkz6teFU/edit#gid=1561806105"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Messages": "={{ $json.result.text }}",
            "Leads Age": "={{ $now.setZone('Asia/Jakarta').toFormat('HH:mm/MM-dd') }}\n",
            "Status": "={{ $('Lead Sheet Fetch1').item.json.Status }}"
          },
          "matchingColumns": [],
          "schema": [
            {
              "id": "Leads Age",
              "displayName": "Leads Age",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Messages",
              "displayName": "Messages",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Status",
              "displayName": "Status",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Trigger Date",
              "displayName": "Trigger Date",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
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
        1808,
        304
      ],
      "id": "a28c8269-c4e5-40c2-8ac9-2e7356fef655",
      "name": "AutomationQuota1",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "RCC3FnRYOQz8RdxJ",
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
        2016,
        304
      ],
      "id": "dac6e3af-7ad6-45ef-9f68-16208e1a9640",
      "name": "Jo Monitor",
      "webhookId": "ecc9b6f1-97ec-437d-ba86-0d697dd9fa9c",
      "credentials": {}
    }
  ],
  "connections": {
    "Download file": {
      "main": [
        [
          {
            "node": "Send a video",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send a video": {
      "main": [
        [
          {
            "node": "Get row(s) in sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send a text message": {
      "main": [
        [
          {
            "node": "AutomationQuota1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Drive Trigger": {
      "main": [
        [
          {
            "node": "Download file",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get row(s) in sheet": {
      "main": [
        [
          {
            "node": "Filter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter": {
      "main": [
        [
          {
            "node": "Send a text message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AutomationQuota1": {
      "main": [
        [
          {
            "node": "Jo Monitor",
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