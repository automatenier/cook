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
      "id": "e452ee5e-38bd-4d71-a28c-ea21396cbb7e",
      "name": "Telegram Trigger",
      "webhookId": "0051de7d-6463-4f8c-8508-b6bcaaa43e9b",
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
      "id": "10ddcb94-4184-47a3-b645-0b6c28c9e74b",
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
      "id": "6faa7099-a756-4410-b3df-b505f538c78c",
      "name": "Send a text message",
      "webhookId": "45c31085-ec58-4339-82ea-f7407afdf31d",
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
      "id": "66287df0-03c5-439e-b5b0-9d8bb20223d9",
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
      "id": "a79de0f6-d6d0-4da7-8ebd-28f214401d9d",
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
      "id": "52bcc450-644d-4cae-ba7a-7b18fa2c9cbc",
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
      "id": "f6696de9-80c0-4d72-947a-ff0f0da530af",
      "name": "Send a text message1",
      "webhookId": "6fc693af-30a6-4c7c-9b10-772fba0866d6",
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
      "id": "206ca542-7ebe-457b-be84-fad56d1b346e",
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
      "id": "5cb8008a-6ab9-42a0-b294-123291959a6c",
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
      "id": "41ad51dc-c09c-48b0-ad46-e73cbb6eda80",
      "name": "Send a text message2",
      "webhookId": "9828306e-85ae-46de-a663-468615cefc62",
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
      "id": "15efec65-44cd-4067-ad46-8f7aefe68b6d",
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
      "id": "ee734f8c-e457-4e51-82fa-f4bbf0124799",
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