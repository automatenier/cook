---
tags:
  - consulting
---
{
  "nodes": [
    {
      "parameters": {
        "formTitle": "Form Tugas Harian",
        "formFields": {
          "values": [
            {
              "fieldLabel": "Tugas Hari",
              "fieldType": "date"
            },
            {
              "fieldLabel": "Apakah Tugas Sudah Selesai",
              "fieldType": "checkbox",
              "fieldOptions": {
                "values": [
                  {
                    "option": "Sudah Selesai"
                  }
                ]
              },
              "requiredField": true
            },
            {
              "fieldLabel": "Kendala? Ceritakan"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.formTrigger",
      "typeVersion": 2.3,
      "position": [
        0,
        0
      ],
      "id": "f901a5ba-49a0-4c9d-a645-4422334a068c",
      "name": "On form submission",
      "webhookId": "d5ba9ba8-8c9b-4fa8-9468-a25768edc4af"
    },
    {
      "parameters": {
        "operation": "append",
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": ""
        },
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": ""
        }
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.7,
      "position": [
        208,
        0
      ],
      "id": "c57f9a56-4f66-42d1-a1f1-8d681cf01783",
      "name": "Append row in sheet",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "xNFdBVlbfdG0Muij",
          "name": "HTSReal1"
        }
      }
    }
  ],
  "connections": {
    "On form submission": {
      "main": [
        [
          {
            "node": "Append row in sheet",
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