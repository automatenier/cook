---
tags:
  - consulting
---
{
  "nodes": [
    {
      "parameters": {
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        48,
        -16
      ],
      "id": "b4298362-3c10-47fa-81d2-2d2565d27660",
      "name": "Send a text message",
      "webhookId": "6c2d8403-b61c-439e-9884-3604320f4eef",
      "credentials": {}
    },
    {
      "parameters": {
        "operation": "sendPhoto",
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        -160,
        -16
      ],
      "id": "a12bfc23-bfb4-48c9-a497-fed239958357",
      "name": "Send a photo message",
      "webhookId": "d289c9ca-45d3-4404-9005-596e682ea89f",
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
          "mode": "list",
          "value": ""
        }
      },
      "type": "n8n-nodes-base.googleDriveTrigger",
      "typeVersion": 1,
      "position": [
        -384,
        -16
      ],
      "id": "8fcb54ed-22d3-4841-b445-44aeefaf5ff5",
      "name": "Google Drive Trigger"
    },
    {
      "parameters": {
        "content": "Saat gua input image di drive, di trigger untuk fetch gsheet biar kirim tulisan detailnya dan timezonenya dan kirim udah setup youtube, udah buat business suite"
      },
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -336,
        192
      ],
      "typeVersion": 1,
      "id": "bbbe0dab-eff7-4949-b08b-d0340b3e7ec6",
      "name": "Sticky Note"
    }
  ],
  "connections": {
    "Google Drive Trigger": {
      "main": [
        []
      ]
    }
  },
  "pinData": {},
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "3039fbd4cadb80067e54b2133333595ff57d847dd0124b88f494b4fc1d62ef2e"
  }
}