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
      "id": "427acad3-1567-4ea9-8c81-3d2c58a95ac8",
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
      "id": "9c045474-9f83-42f9-b2f9-cbec9162c016",
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
      "id": "f3691504-3ff3-42a0-a2a4-10c052594d9f",
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
      "id": "e899eb94-b953-4589-a1e6-50ef7e27424b",
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
      "id": "0e0f76b6-c1be-46bf-b117-1f17416ff76f",
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
      "id": "b3472c41-a914-4e17-a47b-fb299622ef7a",
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
      "id": "8decdd45-9f12-4f17-9723-10d36ad8a0a8",
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
      "id": "0747a4d4-3bae-47b9-a438-b068e500cf77",
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
      "id": "f1ec8a54-7f1e-4136-a279-4ad7e4144a99",
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
      "id": "a36cadbb-ba35-459b-bbb8-287a61dcf7f7",
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
      "id": "f427836a-47d5-4534-91fa-b494e5b0f1fe",
      "name": "Add to database"
    },
    {
      "parameters": {
        "operation": "Run actor and get dataset",
        "actorId": {
          "__rl": true,
          "value": "https://console.apify.com/actors/shu8hvrXbJbY3Eb9W/input",
          "mode": "url"
        }
      },
      "type": "@apify/n8n-nodes-apify.apify",
      "typeVersion": 1,
      "position": [
        176,
        -48
      ],
      "id": "90bb0a71-1640-45c7-855f-8aed4c32f0ba",
      "name": "IG Comments",
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
            "node": "IG Comments",
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
    "IG Comments": {
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