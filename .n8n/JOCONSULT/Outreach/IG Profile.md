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
        -240,
        -48
      ],
      "id": "16a3e62d-64e5-4e90-b758-1f5b698d7c99",
      "name": "Schedule Trigger"
    },
    {
      "parameters": {
        "operation": "get"
      },
      "type": "n8n-nodes-base.googleDocs",
      "typeVersion": 2,
      "position": [
        -32,
        -48
      ],
      "id": "2fcd176f-7558-4f86-812d-73c44dffc427",
      "name": "Get a document"
    },
    {
      "parameters": {
        "options": {}
      },
      "type": "n8n-nodes-base.splitInBatches",
      "typeVersion": 3,
      "position": [
        384,
        -48
      ],
      "id": "265a8a09-2e7e-48ec-9a0a-acff861e40f6",
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
        672,
        -48
      ],
      "id": "c79ae4d9-f7bb-4c1e-a44c-f0ca07086163",
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
        1024,
        -48
      ],
      "id": "9b588c6f-98bb-46a8-84de-d4fef9c55b25",
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
        1232,
        -48
      ],
      "id": "f8050ce2-8726-4092-a06e-c360e3de9062",
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
        1584,
        -48
      ],
      "id": "b448937f-e146-4020-8d6c-58604e20f6ee",
      "name": "Markdown"
    },
    {
      "parameters": {},
      "type": "n8n-nodes-base.googleDocs",
      "typeVersion": 2,
      "position": [
        1792,
        -48
      ],
      "id": "a5d05719-fa37-497b-8a9b-a83c51df8915",
      "name": "Create a document"
    },
    {
      "parameters": {
        "options": {}
      },
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.3,
      "position": [
        2000,
        -48
      ],
      "id": "95dbfd31-36dc-4db9-ad96-4b7aa4d0bc7e",
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
        2224,
        -48
      ],
      "id": "69be9ebf-7c53-4892-aa1b-499ced146af3",
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
        2432,
        -48
      ],
      "id": "a4ee3bd7-7857-4cc3-8a37-f9501ffb1b58",
      "name": "Add to database"
    },
    {
      "parameters": {
        "operation": "Run actor and get dataset",
        "actorId": {
          "__rl": true,
          "value": "https://console.apify.com/actors/dSCLg0C3YEZ83HzYX/input",
          "mode": "url"
        }
      },
      "type": "@apify/n8n-nodes-apify.apify",
      "typeVersion": 1,
      "position": [
        176,
        -48
      ],
      "id": "a1b0b9a7-6f1d-42a8-9612-26141437488a",
      "name": "IG Profile",
      "credentials": {
        "apifyApi": {
          "id": "AuMAM42YTZ9Ue9DQ",
          "name": "Apify account"
        }
      }
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
            "node": "IG Profile",
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
    },
    "IG Profile": {
      "main": [
        [
          {
            "node": "Loop Over Items",
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