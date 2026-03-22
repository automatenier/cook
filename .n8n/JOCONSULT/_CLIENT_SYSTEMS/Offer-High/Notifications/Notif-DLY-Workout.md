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
              "triggerAtHour": 18
            }
          ]
        }
      },
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.3,
      "position": [
        32,
        -48
      ],
      "id": "ba056d43-47e6-4e48-a608-98b5b42187b0",
      "name": "Schedule Trigger"
    },
    {
      "parameters": {
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
        192,
        -48
      ],
      "id": "507a6108-69d1-459f-af00-0abe00da8a73",
      "name": "Get Workout",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "xNFdBVlbfdG0Muij",
          "name": "HTSReal1"
        }
      },
      "disabled": true
    },
    {
      "parameters": {},
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [
        208,
        -240
      ],
      "id": "fe5ce231-952e-419b-a31a-2dcb653e4425",
      "name": "When clicking ‘Execute workflow’"
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 3
          },
          "conditions": [
            {
              "id": "fb475056-97fd-4383-8aff-559e2ec9032c",
              "leftValue": "",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "equals",
                "name": "filter.operator.equals"
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.3,
      "position": [
        640,
        -224
      ],
      "id": "3dd46e56-bdc3-4f42-be15-348ef5f46fe8",
      "name": "If"
    },
    {
      "parameters": {
        "unit": "hours"
      },
      "type": "n8n-nodes-base.wait",
      "typeVersion": 1.1,
      "position": [
        864,
        -272
      ],
      "id": "30a1604c-0115-4a52-9d12-6496bb0c6c2a",
      "name": "Wait",
      "webhookId": "37c9d945-cd7b-43a7-9cfd-dccec40db6d7"
    },
    {
      "parameters": {
        "unit": "hours"
      },
      "type": "n8n-nodes-base.wait",
      "typeVersion": 1.1,
      "position": [
        1216,
        -80
      ],
      "id": "31bcf3aa-b48c-4d27-afe0-e26bd27bea78",
      "name": "Wait1",
      "webhookId": "37c9d945-cd7b-43a7-9cfd-dccec40db6d7"
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 3
          },
          "conditions": [
            {
              "id": "f1333c33-5c5d-44af-99a0-baff287578ec",
              "leftValue": "",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "equals",
                "name": "filter.operator.equals"
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.filter",
      "typeVersion": 2.3,
      "position": [
        336,
        -48
      ],
      "id": "9cc64141-7d52-4c02-841b-517fe2049f8f",
      "name": "Filter"
    },
    {
      "parameters": {
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        1136,
        -272
      ],
      "id": "901ab8ae-d348-401a-bc75-cd251a5e6949",
      "name": "Workout Message",
      "webhookId": "2d374a47-a1ad-44b9-b618-80703f13090a",
      "credentials": {}
    },
    {
      "parameters": {
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        1440,
        -80
      ],
      "id": "6fd00b37-30f0-4ae2-ae32-7b5716f1a942",
      "name": "Workout Message1",
      "webhookId": "2d374a47-a1ad-44b9-b618-80703f13090a",
      "credentials": {}
    },
    {
      "parameters": {
        "operation": "sendAndWait",
        "options": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        928,
        -80
      ],
      "id": "ca129ed0-02b4-4818-96ff-d86be2610060",
      "name": "Kirim Perubahan",
      "webhookId": "316b4675-1ad0-4671-8fc2-e1cfa959a67b",
      "credentials": {}
    },
    {
      "parameters": {
        "operation": "sendAndWait",
        "chatId": "6228081299",
        "message": "Workout {date} for {client}\n\n",
        "approvalOptions": {
          "values": {
            "approvalType": "double",
            "approveLabel": "✅ Setuju",
            "disapproveLabel": "❌ Buat Perubahan"
          }
        },
        "options": {
          "appendAttribution": false
        }
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        432,
        -224
      ],
      "id": "8b5e97e9-c29b-4acd-b8c5-071ca83915cb",
      "name": "Konfirmasi Workout",
      "webhookId": "1281d5a1-37e3-4e4d-94d5-812392968426",
      "credentials": {}
    }
  ],
  "connections": {
    "Schedule Trigger": {
      "main": [
        [
          {
            "node": "Get Workout",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Workout": {
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
    "When clicking ‘Execute workflow’": {
      "main": [
        [
          {
            "node": "Konfirmasi Workout",
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
            "node": "Wait",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Kirim Perubahan",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wait": {
      "main": [
        [
          {
            "node": "Workout Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wait1": {
      "main": [
        [
          {
            "node": "Workout Message1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Kirim Perubahan": {
      "main": [
        [
          {
            "node": "Wait1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Konfirmasi Workout": {
      "main": [
        [
          {
            "node": "If",
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