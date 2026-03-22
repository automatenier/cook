---
tags:
  - consulting
---
{
  "nodes": [
    {
      "parameters": {
        "updates": [
          "message"
        ],
        "additionalFields": {
          "download": false,
          "chatIds": ""
        }
      },
      "type": "n8n-nodes-base.telegramTrigger",
      "typeVersion": 1.2,
      "position": [
        -128,
        -16
      ],
      "id": "908a0409-a25c-45ba-8f4c-ac2706190d2b",
      "name": "Telegram Trigger",
      "webhookId": "81733d7d-41a4-459a-bbcc-727ad7414085",
      "credentials": {}
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
              "id": "b8302917-908d-40d2-918f-59ff093de7fc",
              "leftValue": "",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "contains"
              }
            },
            {
              "id": "74d15591-d8bb-41d2-ac74-239079466df8",
              "leftValue": "",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "equals",
                "name": "filter.operator.equals"
              }
            },
            {
              "id": "1c122922-9055-425a-b8b6-26b4f3d517dc",
              "leftValue": "",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "equals",
                "name": "filter.operator.equals"
              }
            }
          ],
          "combinator": "or"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        128,
        -16
      ],
      "id": "e95aa216-4b92-440e-8bb5-a8109ccfbce1",
      "name": "If"
    },
    {
      "parameters": {
        "chatId": "6228081299",
        "text": "🤖 BOT Akuntabilitas Ready\n\nSilakan pilih perintah berikut: \n🔹 /agenda— Cek List Tugas \n🔹 /setup— Update Progress \n🔹 /meeting — Selesaikan Tugas",
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        320,
        128
      ],
      "id": "dbc61f7a-8011-4e03-8468-8fe8d0da48ba",
      "name": "Send a text message",
      "webhookId": "ffae1e12-4960-4aa1-a51f-417798ef1fca",
      "credentials": {}
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
              "id": "b8302917-908d-40d2-918f-59ff093de7fc",
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
      "typeVersion": 2.2,
      "position": [
        480,
        -32
      ],
      "id": "1d3c95f8-cd33-44f3-a0d7-eef247b0c6bf",
      "name": "Agenda"
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
              "id": "b8302917-908d-40d2-918f-59ff093de7fc",
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
      "typeVersion": 2.2,
      "position": [
        1312,
        -16
      ],
      "id": "afefe11f-fe0d-4a45-a6b4-18bf396bdd3e",
      "name": "Agenda1"
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
        720,
        -224
      ],
      "id": "a2f52a47-da23-47c1-87a9-181426c52290",
      "name": "Get row(s) in sheet",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "xNFdBVlbfdG0Muij",
          "name": "HTSReal1"
        }
      }
    },
    {
      "parameters": {
        "chatId": "6228081299",
        "text": "🤖 BOT Akuntabilitas Ready\n\nSilakan pilih perintah berikut: \n🔹 /agenda— Cek List Tugas \n🔹 /setup— Update Progress \n🔹 /meeting — Selesaikan Tugas",
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        1136,
        -224
      ],
      "id": "a47e49e8-2153-4784-9a5f-06714ef3e9a0",
      "name": "Send a text message1",
      "webhookId": "ffae1e12-4960-4aa1-a51f-417798ef1fca",
      "credentials": {}
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
              "id": "24fb0b35-b549-417f-9a46-0709fad211ff",
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
        944,
        -224
      ],
      "id": "7db98454-cad8-453f-a965-f5dcb2521d2a",
      "name": "Filter"
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
        1488,
        -224
      ],
      "id": "0939a9b5-7691-4880-9b57-0caf2d14af03",
      "name": "Get row(s) in sheet1",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "xNFdBVlbfdG0Muij",
          "name": "HTSReal1"
        }
      }
    },
    {
      "parameters": {
        "chatId": "6228081299",
        "text": "🤖 BOT Akuntabilitas Ready\n\nSilakan pilih perintah berikut: \n🔹 /agenda— Cek List Tugas \n🔹 /setup— Update Progress \n🔹 /meeting — Selesaikan Tugas",
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        1904,
        -224
      ],
      "id": "74cd5d74-0516-4321-8ea0-4f2856314169",
      "name": "Send a text message2",
      "webhookId": "ffae1e12-4960-4aa1-a51f-417798ef1fca",
      "credentials": {}
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
              "id": "24fb0b35-b549-417f-9a46-0709fad211ff",
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
        1712,
        -224
      ],
      "id": "b1f4eabe-1f38-4708-a455-7ebcbaaf6097",
      "name": "Filter1"
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
              "id": "b8302917-908d-40d2-918f-59ff093de7fc",
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
      "typeVersion": 2.2,
      "position": [
        2128,
        -32
      ],
      "id": "26ac10af-dd54-465f-a612-86fa0cd27d67",
      "name": "Agenda2"
    }
  ],
  "connections": {
    "Telegram Trigger": {
      "main": [
        [
          {
            "node": "If",
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
            "node": "Agenda",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    },
    "Agenda": {
      "main": [
        [
          {
            "node": "Get row(s) in sheet",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Agenda1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Agenda1": {
      "main": [
        [
          {
            "node": "Get row(s) in sheet1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get row(s) in sheet": {
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
            "node": "Send a text message1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get row(s) in sheet1": {
      "main": [
        [
          {
            "node": "Filter1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter1": {
      "main": [
        [
          {
            "node": "Send a text message2",
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