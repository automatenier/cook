---
tags:
  - consulting
---

{
  "nodes": [
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
        560,
        480
      ],
      "id": "9ffc434a-d31c-4d78-bf54-b22b96b4ae5c",
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
        "chatId": "6228081299",
        "text": "=Notif-Leads Triggered for (Fadli)\n\n{{ $('Lead Notify1').item.json.result.text }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        768,
        464
      ],
      "id": "9c36d9cc-3c4c-42cd-bf77-ad423fce6570",
      "name": "AI-agency1",
      "webhookId": "277a288b-d4ac-4921-a8de-e9e1c88172af",
      "credentials": {}
    },
    {
      "parameters": {
        "pollTimes": {
          "item": [
            {
              "mode": "everyHour"
            }
          ]
        },
        "documentId": {
          "__rl": true,
          "value": "1l_8MvNXMTsHSr4kcSapLrDOWO5EAt4tOdABMkz6teFU",
          "mode": "list"
        },
        "sheetName": {
          "__rl": true,
          "value": 1269365760,
          "mode": "list",
          "cachedResultName": "CRM-Fadli",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1l_8MvNXMTsHSr4kcSapLrDOWO5EAt4tOdABMkz6teFU/edit#gid=1269365760"
        },
        "event": "rowUpdate",
        "options": {
          "columnsToWatch": [
            "Status"
          ]
        }
      },
      "type": "n8n-nodes-base.googleSheetsTrigger",
      "typeVersion": 1,
      "position": [
        -48,
        496
      ],
      "id": "6f2eb461-ce19-46a9-8377-5046275edf46",
      "name": "Lead Sheet Fetch1",
      "credentials": {
        "googleSheetsTriggerOAuth2Api": {
          "id": "DetgERBLQuOqFSDg",
          "name": "07/01"
        }
      }
    },
    {
      "parameters": {
        "chatId": "6228081299",
        "text": "=New {{ $json.Status }}\n{{ $now.setZone('Asia/Jakarta').toFormat('HH:mm/MM-dd') }}\nUsername:{{ $json.Username }}\nSource:{{ $json.Source }}\nChannels:{{ $json.Channels }}\n",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        304,
        480
      ],
      "id": "a2a7fb02-11f2-424a-a047-a8f74ab4e066",
      "name": "Lead Notify1",
      "webhookId": "bc78dbc6-03c9-41f2-9dc0-b5f9a9e9f596",
      "credentials": {}
    }
  ],
  "connections": {
    "AutomationQuota1": {
      "main": [
        [
          {
            "node": "AI-agency1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI-agency1": {
      "main": [
        []
      ]
    },
    "Lead Sheet Fetch1": {
      "main": [
        [
          {
            "node": "Lead Notify1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Lead Notify1": {
      "main": [
        [
          {
            "node": "AutomationQuota1",
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