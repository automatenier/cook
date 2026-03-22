---
tags:
  - automation
---
{
  "nodes": [
    {
      "parameters": {
        "rule": {
          "interval": [
            {}
          ]
        }
      },
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.2,
      "position": [
        0,
        0
      ],
      "id": "6483691b-45d8-484a-8cfc-5485846bac4e",
      "name": "Schedule Trigger"
    },
    {
      "parameters": {
        "operation": "get"
      },
      "type": "n8n-nodes-base.googleDocs",
      "typeVersion": 2,
      "position": [
        208,
        0
      ],
      "id": "d8b07046-4562-4e98-8c62-2f28616f502f",
      "name": "Get a document"
    },
    {
      "parameters": {
        "operation": "Run actor and get dataset",
        "actorId": {
          "__rl": true,
          "value": "https://console.apify.com/actors/BHzefUZlZRKWxkTck/input",
          "mode": "url"
        }
      },
      "type": "@apify/n8n-nodes-apify.apify",
      "typeVersion": 1,
      "position": [
        416,
        0
      ],
      "id": "5171eaf5-0adb-4c7c-a701-56a62c50f43f",
      "name": "Run an Actor and get dataset",
      "credentials": {
        "apifyApi": {
          "id": "AuMAM42YTZ9Ue9DQ",
          "name": "Apify account"
        }
      }
    },
    {
      "parameters": {
        "options": {}
      },
      "type": "n8n-nodes-base.splitInBatches",
      "typeVersion": 3,
      "position": [
        624,
        0
      ],
      "id": "18997dd3-f749-4fba-b5c2-9d973a062c10",
      "name": "Loop Over Items"
    },
    {
      "parameters": {
        "modelId": {
          "__rl": true,
          "mode": "list",
          "value": ""
        },
        "messages": {
          "values": [
            {}
          ]
        },
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.anthropic",
      "typeVersion": 1,
      "position": [
        1024,
        0
      ],
      "id": "541fe06a-4ba1-40b7-851f-8a0b117b489c",
      "name": "Message a model",
      "credentials": {
        "anthropicApi": {
          "id": "HWNDqTHGofAbXd0Z",
          "name": "n8n3"
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
              "id": "ad3c478f-300f-4865-bb0a-c5da16bdf372",
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
      "typeVersion": 2.2,
      "position": [
        1376,
        0
      ],
      "id": "fb0714d1-1a7f-43b2-a9c5-1205120a3147",
      "name": "Filter"
    },
    {
      "parameters": {
        "modelId": {
          "__rl": true,
          "mode": "list",
          "value": ""
        },
        "messages": {
          "values": [
            {}
          ]
        },
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.anthropic",
      "typeVersion": 1,
      "position": [
        1584,
        0
      ],
      "id": "63fbce86-ced5-40b6-b5bf-e7fc92f92b27",
      "name": "Write Resume",
      "credentials": {
        "anthropicApi": {
          "id": "HWNDqTHGofAbXd0Z",
          "name": "n8n3"
        }
      }
    },
    {
      "parameters": {
        "options": {}
      },
      "type": "n8n-nodes-base.markdown",
      "typeVersion": 1,
      "position": [
        1936,
        0
      ],
      "id": "9a94d4d1-5429-4c6b-b805-2e9eb1a214b4",
      "name": "Markdown"
    },
    {
      "parameters": {},
      "type": "n8n-nodes-base.googleDocs",
      "typeVersion": 2,
      "position": [
        2144,
        0
      ],
      "id": "f06b7917-aab3-4b06-96a3-86b5001c328e",
      "name": "Create a document"
    },
    {
      "parameters": {
        "options": {}
      },
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.3,
      "position": [
        2352,
        0
      ],
      "id": "df1e703f-ec4b-48c9-989f-21373eafa1f4",
      "name": "HTTP Request"
    },
    {
      "parameters": {
        "resource": "drive",
        "operation": "update",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": ""
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleDrive",
      "typeVersion": 3,
      "position": [
        2560,
        0
      ],
      "id": "88f2334b-ff1e-4457-8c36-872f7a542078",
      "name": "make url public"
    },
    {
      "parameters": {
        "operation": "update",
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
        2768,
        0
      ],
      "id": "18de6a50-ba9c-47aa-9f7f-09f5e8710c4d",
      "name": "Add to database"
    }
  ],
  "connections": {
    "Schedule Trigger": {
      "main": [
        [
          {
            "node": "Get a document",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get a document": {
      "main": [
        [
          {
            "node": "Run an Actor and get dataset",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Run an Actor and get dataset": {
      "main": [
        [
          {
            "node": "Loop Over Items",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Loop Over Items": {
      "main": [
        [],
        [
          {
            "node": "Message a model",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Message a model": {
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
            "node": "Write Resume",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Write Resume": {
      "main": [
        [
          {
            "node": "Markdown",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Markdown": {
      "main": [
        [
          {
            "node": "Create a document",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create a document": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request": {
      "main": [
        [
          {
            "node": "make url public",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "make url public": {
      "main": [
        [
          {
            "node": "Add to database",
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