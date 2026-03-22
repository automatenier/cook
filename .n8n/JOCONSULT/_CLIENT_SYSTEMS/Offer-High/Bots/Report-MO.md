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
      "id": "00c538bb-0bf9-4254-b00a-98655271379c",
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
      "id": "654b3c4f-2095-4a31-ad6e-470a63c146c2",
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
      "id": "80372642-0b75-4d72-981d-c2ce4d2e91e0",
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
      "id": "eb02a43e-56b1-4171-9457-d7dc72291315",
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
      "id": "f3c4267d-2357-4c74-a5c3-c8b10503a705",
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
      "id": "780f52bd-d67e-49ac-b3d0-a7b0881f632a",
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
      "id": "611539ac-084a-4d8f-8e2c-3c33b6bc4f67",
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
      "id": "145b87ea-5b9b-4f9e-905a-3ce08bacd56e",
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
      "id": "4dc1ee7e-9e5b-4f86-a2eb-99a8dd6574cc",
      "name": "Review PDF",
      "webhookId": "3c9f3267-f22d-4a64-a615-b0fa663996bf",
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
      "id": "c1d5e16c-cc1e-4ed9-9f6d-4d279c7b4881",
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
      "id": "4dd74397-814f-4d3d-9940-68e178d93d3e",
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
      "id": "5f619a69-d516-4379-90ce-7dd3308e7483",
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