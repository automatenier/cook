---
tags:
  - consulting
---
{
  "nodes": [
    {
      "parameters": {
        "content": "Every week i screenshot the all dashboard and let AI put it into my sheet and prompt it so it give recomendation as a strategy PDF \n"
      },
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        80,
        272
      ],
      "typeVersion": 1,
      "id": "e1fe4e96-da6a-461f-92cc-bd192a36a5d8",
      "name": "Sticky Note"
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
        -112,
        32
      ],
      "id": "7f8d7b11-9f1f-4726-bfa6-72217202327a",
      "name": "Google Drive Trigger",
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "UcfIN5LCO68VG5wm",
          "name": "07/01"
        }
      }
    },
    {
      "parameters": {
        "resource": "image",
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
        720,
        -128
      ],
      "id": "7a6850aa-4135-41ef-bfe8-51657ca49ff5",
      "name": "IG Prompt",
      "credentials": {
        "anthropicApi": {
          "id": "HWNDqTHGofAbXd0Z",
          "name": "n8n3"
        }
      }
    },
    {
      "parameters": {
        "operation": "append",
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
        1024,
        -128
      ],
      "id": "25a16562-eefd-451a-b4ff-20c7a0032f0d",
      "name": "Append row in sheet",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "xNFdBVlbfdG0Muij",
          "name": "HTSReal1"
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
              "id": "0c2c87f9-540b-4679-b36d-396f688a06a4",
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
        976,
        544
      ],
      "id": "63d5c4d8-4db3-497a-8418-fb9b3fc94d41",
      "name": "Tiktok Dash2"
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
              "id": "0c2c87f9-540b-4679-b36d-396f688a06a4",
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
        512,
        192
      ],
      "id": "4e5254ea-34c2-416d-b964-b39aa00d519d",
      "name": "IG-CNT"
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
              "id": "0c2c87f9-540b-4679-b36d-396f688a06a4",
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
        256,
        48
      ],
      "id": "5747f904-3909-4297-8a57-4f82b769cc44",
      "name": "IG-Main"
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
              "id": "0c2c87f9-540b-4679-b36d-396f688a06a4",
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
        752,
        336
      ],
      "id": "204662e3-68f0-400a-acf0-68358b4e68ad",
      "name": "TT-CNT"
    },
    {
      "parameters": {
        "operation": "sendAndWait",
        "responseType": "customForm",
        "formFields": {
          "values": [
            {
              "fieldLabel": "Changes Prompt"
            }
          ]
        },
        "options": {
          "appendAttribution": false
        }
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        1584,
        144
      ],
      "id": "43a36672-d568-4151-b980-3ea0910ff9f5",
      "name": "Review PDF",
      "webhookId": "50b83204-2674-491e-b016-115ac84da7d8",
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
              "id": "57b4067e-f206-4606-a435-08030a280374",
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
        1792,
        144
      ],
      "id": "3ca3e381-b549-4429-9698-1c8c89ab82a0",
      "name": "If"
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
        2096,
        272
      ],
      "id": "f008f9bf-92d9-40fe-a114-f0f05c2abeb9",
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
        "options": {}
      },
      "type": "n8n-nodes-base.executeWorkflow",
      "typeVersion": 1.3,
      "position": [
        2160,
        32
      ],
      "id": "790e7daf-8325-4095-869d-edcf6887a12d",
      "name": "Trigger \"RPT-WKLY"
    }
  ],
  "connections": {
    "Google Drive Trigger": {
      "main": [
        [
          {
            "node": "IG-Main",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IG Prompt": {
      "main": [
        [
          {
            "node": "Append row in sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Append row in sheet": {
      "main": [
        []
      ]
    },
    "IG-CNT": {
      "main": [
        [],
        [
          {
            "node": "TT-CNT",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IG-Main": {
      "main": [
        [
          {
            "node": "IG Prompt",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "IG-CNT",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Review PDF": {
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
            "node": "Trigger \"RPT-WKLY",
            "type": "main",
            "index": 0
          }
        ],
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
            "node": "Review PDF",
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