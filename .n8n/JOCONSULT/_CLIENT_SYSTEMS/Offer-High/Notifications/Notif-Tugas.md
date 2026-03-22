---
tags:
  - consulting
---
{
  "nodes": [
    {
      "parameters": {
        "rule": {
          "interval": [
            {
              "triggerAtHour": 8
            }
          ]
        }
      },
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.3,
      "position": [
        -32,
        -16
      ],
      "id": "8692d39a-c844-4415-9071-a57941988cd2",
      "name": "Schedule Trigger"
    },
    {
      "parameters": {
        "documentId": {
          "__rl": true,
          "value": "1eeoNSSQloJBc1Itvm-YCahw_M2RiV8lMemtVerktqrg",
          "mode": "list",
          "cachedResultName": "Fadli-JOConsult",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1eeoNSSQloJBc1Itvm-YCahw_M2RiV8lMemtVerktqrg/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 833770569,
          "mode": "list",
          "cachedResultName": "90 Hari Setup",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1eeoNSSQloJBc1Itvm-YCahw_M2RiV8lMemtVerktqrg/edit#gid=833770569"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.7,
      "position": [
        208,
        0
      ],
      "id": "fb8e4826-7ac3-45ed-99df-f22d41451ad9",
      "name": "Get row(s) in sheet",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "wAXX1lV81Bmr7FUX",
          "name": "15/01"
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
              "id": "1d1f74fd-9238-46b1-b780-1d93351a83c1",
              "leftValue": "={{ $json.Date }}",
              "rightValue": "={{ $now.setZone('Asia/Jakarta').toFormat('dd/MM') }}",
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
        416,
        0
      ],
      "id": "275265f3-94bd-4b44-ad28-cfd81dd6e228",
      "name": "Filter"
    },
    {
      "parameters": {
        "chatId": "6228081299",
        "text": "=Tugas Hari ini {{ $now.setZone('Asia/Jakarta').toFormat('dd/MM') }}\n\n{{ $json.SOP }}\n\n{{ $json.URL }}\n\nCek Lengkapnya di tabel google sheet\n\n---\n\nJika sudah boleh mengisi form disini sebelum jam 19:00 dan kami akan review\nhttps://n8n.htsagency.id/form-test/d5ba9ba8-8c9b-4fa8-9468-a25768edc4af\n----\nButuh Bantuan?\nChat kami \nhttps://t.me/+U5gyVqJ3z2w4YWJl",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        880,
        0
      ],
      "id": "9348b4c6-608f-4e90-9258-3b5ae802ae32",
      "name": "Send a text message",
      "webhookId": "3329be80-31ca-487f-944b-f17ffc3e66eb",
      "credentials": {}
    },
    {
      "parameters": {
        "fieldsToAggregate": {
          "fieldToAggregate": [
            {
              "fieldToAggregate": "SOP"
            },
            {
              "fieldToAggregate": "URL"
            }
          ]
        },
        "options": {
          "mergeLists": false
        }
      },
      "type": "n8n-nodes-base.aggregate",
      "typeVersion": 1,
      "position": [
        624,
        0
      ],
      "id": "a32671a0-c639-421b-9305-cdb7823fed6e",
      "name": "Aggregate"
    }
  ],
  "connections": {
    "Schedule Trigger": {
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
            "node": "Aggregate",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Aggregate": {
      "main": [
        [
          {
            "node": "Send a text message",
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