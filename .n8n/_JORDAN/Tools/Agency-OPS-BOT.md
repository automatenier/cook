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
      "id": "9ad260be-55c6-4905-9555-e535ac70235a",
      "name": "Telegram Trigger",
      "webhookId": "72d01622-93a1-45d3-9085-e1df96558716",
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
      "id": "3013f6e8-ba75-4416-b4b9-73208c26c8ab",
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
      "id": "1c9afb70-82b5-4a04-8ba0-3fe1522b3785",
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
      "id": "ad8b709c-6572-4cac-90ef-6f852d5accf0",
      "name": "Send message and wait for response",
      "webhookId": "d2754b4f-e9ed-4c02-a818-54c37a3fc504",
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
      "id": "be4ed85b-aaef-44a5-a064-c6d735a0e6b3",
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
      "id": "85ef86c8-806d-41de-9dfb-65f5088afb95",
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
      "id": "66ec5d77-c8e5-428c-b866-12ac4ca8bda0",
      "name": "Send a text message",
      "webhookId": "11e01ec4-d9d2-463f-8c93-6df48db65b77",
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
      "id": "34f34ecf-fc7f-4696-a9db-0c35f363230e",
      "name": "Send a text message1",
      "webhookId": "11e01ec4-d9d2-463f-8c93-6df48db65b77",
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
      "id": "1a69af4b-1d76-4f23-86bc-bd36153eef12",
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
      "id": "91d55181-427d-4c2c-b2ef-e2f1c569086b",
      "name": "/TO DO"
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
      "id": "e88fa877-99b7-4096-bc46-c9b58292cf04",
      "name": "/Coach TO DO"
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
      "id": "a3a4058d-1b82-40bb-8224-21ce61fad8ba",
      "name": "/Client TO DO"
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
      "id": "35fce087-f2fa-4b13-8e41-d80b28c75187",
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
      "id": "446a5451-6d62-4c29-8616-310c0e3b2f08",
      "name": "Sticky Note"
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