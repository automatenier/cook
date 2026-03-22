---
tags:
  - automation
---
{
  "nodes": [
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
        96,
        16
      ],
      "id": "7737dbfb-04c4-445e-a8e4-be18acad2671",
      "name": "Telegram Trigger",
      "webhookId": "247a4c17-35b3-4771-ba14-3818b1e7004f",
      "credentials": {},
      "disabled": true
    },
    {
      "parameters": {},
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [
        1584,
        960
      ],
      "id": "a453d7ef-7e7d-4ed1-9b67-52fddd023c08",
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
              "id": "a547615d-ca3e-47e2-945a-49ddc63e86bc",
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
        2016,
        1008
      ],
      "id": "ef7bcdf2-b555-44d7-a7c3-5a9300b8e522",
      "name": "Filter"
    },
    {
      "parameters": {
        "operation": "sendAndWait",
        "options": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        2224,
        1008
      ],
      "id": "936bb59b-30cf-4e5f-89b1-1f80a340a694",
      "name": "Send message and wait for response",
      "webhookId": "eeec17d8-c922-43ca-af50-58bc459fc507",
      "credentials": {}
    },
    {
      "parameters": {
        "resource": "document",
        "modelId": {
          "__rl": true,
          "mode": "list",
          "value": ""
        },
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.anthropic",
      "typeVersion": 1,
      "position": [
        2496,
        1008
      ],
      "id": "f8a8a2f9-02f1-4f78-a78c-9bb1d7737db2",
      "name": "Analyze document",
      "credentials": {
        "anthropicApi": {
          "id": "HWNDqTHGofAbXd0Z",
          "name": "n8n3"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "// Loop over input items and add a new field called 'myNewField' to the JSON of each one\nfor (const item of $input.all()) {\n  item.json.myNewField = 1;\n}\n\nreturn $input.all();"
      },
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        2976,
        1008
      ],
      "id": "cd410ec7-c0c8-48e9-9ae5-96ae192df7f9",
      "name": "Create The PDF"
    },
    {
      "parameters": {
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        2720,
        1008
      ],
      "id": "4703d1e0-52c4-41b8-a618-774f2ee0f8c0",
      "name": "Send a text message",
      "webhookId": "2aadb67d-5379-4bb0-bc3c-a150ec90aedb",
      "credentials": {}
    },
    {
      "parameters": {
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        3248,
        1008
      ],
      "id": "a8758329-23f2-4cb1-9167-34a09f5f53b1",
      "name": "Send a text message1",
      "webhookId": "5f8a94dc-6fa9-450b-abaa-6b1b35429327",
      "credentials": {}
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
              "id": "d8559b6f-8361-410e-828a-8b92690fdcb1",
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
        1248,
        944
      ],
      "id": "7842a0f3-7b29-4248-8ff5-113cffe532fb",
      "name": "/PDF1"
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
              "id": "d8559b6f-8361-410e-828a-8b92690fdcb1",
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
        16
      ],
      "id": "e408384e-4bee-4c06-be14-63cb68c0eaaa",
      "name": "/TO DO"
    },
    {
      "parameters": {
        "operation": "get",
        "dataTableId": {
          "__rl": true,
          "value": "YswaTsroawYdPRcD",
          "mode": "list",
          "cachedResultName": "Strategy PDF",
          "cachedResultUrl": "/projects/C39zp4t8r8MIodf2/datatables/YswaTsroawYdPRcD"
        }
      },
      "type": "n8n-nodes-base.dataTable",
      "typeVersion": 1.1,
      "position": [
        1856,
        1008
      ],
      "id": "647ed33d-3047-4951-8f7e-4781b1827f1e",
      "name": "PDF Data"
    },
    {
      "parameters": {},
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        336,
        96
      ],
      "typeVersion": 1,
      "id": "67e300db-77e6-4c58-a385-9f730fda97ef",
      "name": "Sticky Note"
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
              "id": "d8559b6f-8361-410e-828a-8b92690fdcb1",
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
        912,
        304
      ],
      "id": "77039d74-083b-42f0-af0a-116905513c37",
      "name": "/editors"
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
              "id": "d8559b6f-8361-410e-828a-8b92690fdcb1",
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
        1104,
        608
      ],
      "id": "ced9bacf-3d8f-4216-9680-c0e62bbb039d",
      "name": "/setters"
    }
  ],
  "connections": {
    "Telegram Trigger": {
      "main": [
        [
          {
            "node": "/TO DO",
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
            "node": "PDF Data",
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
            "node": "Send message and wait for response",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send message and wait for response": {
      "main": [
        [
          {
            "node": "Analyze document",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Analyze document": {
      "main": [
        [
          {
            "node": "Send a text message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create The PDF": {
      "main": [
        [
          {
            "node": "Send a text message1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send a text message": {
      "main": [
        [
          {
            "node": "Create The PDF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send a text message1": {
      "main": [
        []
      ]
    },
    "/TO DO": {
      "main": [
        [],
        []
      ]
    },
    "PDF Data": {
      "main": [
        [
          {
            "node": "Filter",
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