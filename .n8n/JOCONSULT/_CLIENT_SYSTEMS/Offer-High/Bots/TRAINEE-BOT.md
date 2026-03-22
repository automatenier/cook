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
      "id": "fafa9392-298d-4dff-ba8c-0f1c9f85f399",
      "name": "Telegram Trigger",
      "webhookId": "3e96d59f-927f-4442-b18f-f5f0b766fed8",
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
      "id": "cefba7ba-f135-440a-9540-b670923e7a34",
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
      "id": "90e924b2-09ad-4910-80ef-7252b3aad91a",
      "name": "Send a text message",
      "webhookId": "2932102c-e365-4d0b-8a3f-a3b2b74969b0",
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
      "id": "4535859a-6b9d-46fb-b0ee-cad4214cf7a2",
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
      "id": "4a05d86a-8cbf-4fa1-ba07-f1265b469e99",
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
      "id": "b804c83b-aee8-4dda-97a6-f9618fe6f23c",
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
      "id": "53ed6edc-121c-457d-94c3-ab222e998f68",
      "name": "Send a text message1",
      "webhookId": "18ceb4c4-4741-4f33-8180-188ec5163afb",
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
      "id": "4db20eaa-d6ce-44e1-a921-4c741a9680d5",
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
      "id": "272ca8d8-04f4-4eef-9c09-519d26b1a74a",
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
      "id": "86de547e-806c-46ca-ab21-2322d9ec9328",
      "name": "Send a text message2",
      "webhookId": "62b34cee-63c2-40b0-a0cd-a7912e310efb",
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
      "id": "bcaa5202-7225-4171-a250-cbc9de8878d8",
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
      "id": "183bc348-657f-4d9b-b97a-2074a64984af",
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