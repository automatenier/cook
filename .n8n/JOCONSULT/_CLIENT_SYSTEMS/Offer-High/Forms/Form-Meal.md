---
tags:
  - consulting
---
{
  "nodes": [
    {
      "parameters": {
        "dataTableId": {
          "__rl": true,
          "value": "yDRYdqpJzQMF2UqK",
          "mode": "list",
          "cachedResultName": "Cynthia Meal Prep",
          "cachedResultUrl": "/projects/C39zp4t8r8MIodf2/datatables/yDRYdqpJzQMF2UqK"
        },
        "columns": {
          "mappingMode": "autoMapInputData",
          "value": {},
          "matchingColumns": [],
          "schema": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.dataTable",
      "typeVersion": 1,
      "position": [
        336,
        -32
      ],
      "id": "2fcca225-d7f3-49a3-bc4a-b158b4ecc09b",
      "name": "Insert row"
    },
    {
      "parameters": {
        "formTitle": "Meal Prep",
        "formDescription": "Dokumentasi Makanan Kalian",
        "formFields": {
          "values": [
            {
              "fieldLabel": "Breakfast",
              "fieldType": "file",
              "acceptFileTypes": ".jpg, .png",
              "requiredField": true
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.formTrigger",
      "typeVersion": 2.3,
      "position": [
        32,
        -16
      ],
      "id": "ff4bce6e-635e-40d0-9a43-6e831222bbd2",
      "name": "Breakfast Form",
      "webhookId": "1f06e6c7-5142-49e5-9226-a2ba10972ea1"
    },
    {
      "parameters": {
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "folderId": {
          "__rl": true,
          "mode": "list",
          "value": "root",
          "cachedResultName": "/ (Root folder)"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleDrive",
      "typeVersion": 3,
      "position": [
        592,
        -32
      ],
      "id": "6dcd8860-9966-4806-9a0a-65f84c6486e7",
      "name": "Upload file",
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "Ad9DfhVABG29A7DX",
          "name": "web 3"
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
        1264,
        -64
      ],
      "id": "f414cbbc-3575-4682-9e61-7984edf5786a",
      "name": "CoachNotif",
      "webhookId": "3a3b2265-6cd5-47a1-9290-36f1d859fe88",
      "credentials": {},
      "disabled": true
    },
    {
      "parameters": {
        "operation": "sendPhoto",
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        1104,
        -64
      ],
      "id": "ece3ea60-e614-4a53-8a03-8dedda1c180f",
      "name": "Send a photo message",
      "webhookId": "e129cfbe-930e-4748-b494-5af15814e0a2",
      "credentials": {},
      "disabled": true
    },
    {
      "parameters": {
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        1472,
        -64
      ],
      "id": "5219e789-a354-4347-a6da-a65a6bb76256",
      "name": "Upload Success Notif",
      "webhookId": "083884cf-db98-4b8d-bfb0-0a33c00f448f",
      "credentials": {},
      "disabled": true
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
        800,
        -32
      ],
      "id": "80aaf63e-82b5-4d26-8537-bd9cf934fad5",
      "name": "Append row in sheet",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "xNFdBVlbfdG0Muij",
          "name": "HTSReal1"
        }
      },
      "disabled": true
    }
  ],
  "connections": {
    "Insert row": {
      "main": [
        [
          {
            "node": "Upload file",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Breakfast Form": {
      "main": [
        [
          {
            "node": "Insert row",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Upload file": {
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
    "CoachNotif": {
      "main": [
        [
          {
            "node": "Upload Success Notif",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send a photo message": {
      "main": [
        [
          {
            "node": "CoachNotif",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Append row in sheet": {
      "main": [
        [
          {
            "node": "Send a photo message",
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