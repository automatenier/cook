---
tags:
  - automation
---
{
  "nodes": [
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "ceeb3e80-717f-4251-8a14-26d62674e030",
              "name": "telegram chat id ",
              "type": "string",
              "value": "6228081299"
            }
          ]
        },
        "options": {}
      },
      "id": "8ebd2e85-74ca-4ffe-8268-38225e0f68b9",
      "name": "Set your Telegram Chat ID",
      "type": "n8n-nodes-base.set",
      "position": [
        -880,
        1584
      ],
      "typeVersion": 3.4
    },
    {
      "parameters": {
        "chatId": "6228081299",
        "text": "=Automation Succeed\n--",
        "additionalFields": {
          "appendAttribution": true
        }
      },
      "id": "5b2d7305-5e0b-49c9-a9f2-f76f134b3df3",
      "name": "Telegram Delivery",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -624,
        1584
      ],
      "webhookId": "7bbbcd0d-b0ca-418a-8c9b-ad4d6870c7d8",
      "typeVersion": 1.2,
      "credentials": {}
    },
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
        -1904,
        1584
      ],
      "id": "23dbd318-89eb-4d39-8099-ed98669f9437",
      "name": "Telegram Trigger",
      "webhookId": "0ac8e9dd-1e3d-4165-ab55-2debfcd1cb2b",
      "credentials": {}
    },
    {
      "parameters": {
        "resource": "file",
        "fileId": "={{ $json.message.photo[3].file_id }}",
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        -1728,
        1584
      ],
      "id": "624e71af-492f-4a89-b471-ce5526163f26",
      "name": "Get a file",
      "webhookId": "3f9dc8b0-801d-4b26-a1a2-34fc5dac6ded",
      "credentials": {}
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
          "value": "https://drive.google.com/drive/folders/1syYFtrQhcxEmeJTqdVCxC5JtxKSsTvEp",
          "mode": "url"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleDrive",
      "typeVersion": 3,
      "position": [
        -1280,
        1584
      ],
      "id": "b0708664-ad81-448e-8264-811faea8b0da",
      "name": "Upload file",
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "D5yBmGClWitY2Sco",
          "name": "2/1"
        }
      }
    }
  ],
  "connections": {
    "Set your Telegram Chat ID": {
      "main": [
        [
          {
            "node": "Telegram Delivery",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Telegram Delivery": {
      "main": [
        []
      ]
    },
    "Telegram Trigger": {
      "main": [
        [
          {
            "node": "Get a file",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get a file": {
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
    "Upload file": {
      "main": [
        [
          {
            "node": "Set your Telegram Chat ID",
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