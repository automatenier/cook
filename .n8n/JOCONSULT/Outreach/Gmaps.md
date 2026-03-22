---
tags:
  - automation
---
{
  "nodes": [
    {
      "parameters": {
        "content": "## 🔄 STEP 3: Smart Website Scraping\n\nProcesses each website individually to prevent IP blocking:\n\n**Loop Over Items:** Processes websites one by one with built-in delays\n**Scrape Site:** Downloads HTML content from each business website\n**Wait Nodes:** Prevent rate limiting and IP blocking\n**Error Handling:** Continues processing even if some sites fail\n\n**Critical:** The batching and delays are essential for reliable operation at scale",
        "height": 472,
        "width": 380
      },
      "id": "b15bc15d-3e8e-4216-b571-e76f5bc71698",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -592,
        -112
      ],
      "typeVersion": 1,
      "name": "Sticky Note2"
    },
    {
      "parameters": {
        "content": "## 📧 STEP 4: Email Extraction & Export\n\nFinal processing pipeline:\n\n1. **Extract Emails:** JavaScript regex finds all email addresses in website HTML\n2. **Filter Out Empties:** Removes websites with no emails found\n3. **Split Out:** Converts email arrays into individual items\n4. **Remove Duplicates:** Final deduplication across all sources\n5. **Add to Sheet:** Exports clean email list to Google Sheets\n\n**Result:** Organized database of business emails ready for outreach",
        "height": 220,
        "width": 400
      },
      "id": "5bfaa587-44bb-4d2b-b94d-8123b3f84293",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -176,
        64
      ],
      "typeVersion": 1,
      "name": "Sticky Note3"
    },
    {
      "parameters": {},
      "id": "2485ee60-3e72-4ba6-9233-a97a5406a5e7",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -1136,
        416
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "options": {}
      },
      "id": "579806c9-e039-4487-ac58-42789b5c0470",
      "name": "Remove Duplicates",
      "type": "n8n-nodes-base.removeDuplicates",
      "position": [
        -336,
        416
      ],
      "typeVersion": 2
    },
    {
      "parameters": {
        "options": {}
      },
      "id": "0d01f243-f12b-44a1-8d63-4ce0419da3f5",
      "name": "Loop Over Items",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        64,
        416
      ],
      "typeVersion": 3
    },
    {
      "parameters": {
        "amount": 1
      },
      "id": "d7c342d5-f170-4434-a122-31aa2bc3bdc9",
      "name": "Wait",
      "type": "n8n-nodes-base.wait",
      "position": [
        432,
        512
      ],
      "webhookId": "19cc6ed4-4fe7-485b-b879-c679e4b3374d",
      "typeVersion": 1.1
    },
    {
      "parameters": {
        "maxItems": 10
      },
      "id": "f95498db-6ea3-41cc-95c2-ba08e795af0a",
      "name": "Limit",
      "type": "n8n-nodes-base.limit",
      "position": [
        -160,
        416
      ],
      "typeVersion": 1
    },
    {
      "parameters": {},
      "id": "c28ebe26-8fb3-4abd-a62b-7e526b4f57dc",
      "name": "Wait1",
      "type": "n8n-nodes-base.wait",
      "position": [
        256,
        352
      ],
      "webhookId": "0fe34756-6e43-4603-8891-5747a9a6500a",
      "typeVersion": 1.1
    },
    {
      "parameters": {
        "fieldToSplitOut": "emails",
        "options": {}
      },
      "id": "67f5139f-ae31-4480-9b17-45ae741d8df7",
      "name": "Split Out",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        608,
        352
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "jsCode": "const input = $input.first().json.data\nconst regex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.(?!jpeg|jpg|png|gif|webp|svg)[a-zA-Z]{2,}/g\nconst emails = input.match(regex)\nreturn {json: {emails:emails}}"
      },
      "id": "0b599be3-cf33-4438-9f05-085699654b29",
      "name": "Extract Emails",
      "type": "n8n-nodes-base.code",
      "position": [
        608,
        512
      ],
      "typeVersion": 2,
      "alwaysOutputData": true,
      "onError": "continueRegularOutput"
    },
    {
      "parameters": {
        "jsCode": "const input = $input.first().json.data\nconst regex = /https?:\\/\\/[^\\/\\s\"'>]+/g\nconst websites = input.match(regex)\nreturn websites.map(website => ({json:{website}}))"
      },
      "id": "4f7ef1bf-ba86-453b-a688-54311f6da33e",
      "name": "Extract URLs",
      "type": "n8n-nodes-base.code",
      "position": [
        -736,
        416
      ],
      "typeVersion": 2
    },
    {
      "parameters": {
        "url": "https://www.google.com/maps/search/dokter+gigi",
        "options": {
          "allowUnauthorizedCerts": true,
          "response": {
            "response": {
              "fullResponse": true
            }
          }
        }
      },
      "id": "2110e871-27df-4895-8584-d35c8b446866",
      "name": "Scrape Google Maps",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -944,
        416
      ],
      "typeVersion": 4.2
    },
    {
      "parameters": {
        "url": "={{ $json.website }}",
        "options": {
          "redirect": {
            "redirect": {
              "followRedirects": false
            }
          }
        }
      },
      "id": "4d830f29-9c76-4626-a220-13f1d4bcd87e",
      "name": "Scrape Site",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        256,
        512
      ],
      "typeVersion": 4.2,
      "onError": "continueRegularOutput"
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "a6786c58-424a-409a-b87f-8a7592cb7944",
              "operator": {
                "type": "array",
                "operation": "exists",
                "singleValue": true
              },
              "leftValue": "={{ $json.emails }}",
              "rightValue": ""
            }
          ]
        },
        "options": {}
      },
      "id": "365320a5-3dcd-46a1-9eac-86ffeef8381f",
      "name": "Filter Out Empties",
      "type": "n8n-nodes-base.filter",
      "position": [
        432,
        352
      ],
      "typeVersion": 2.2
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "bf0a5053-9660-457c-9581-964793bb6d7d",
              "operator": {
                "type": "string",
                "operation": "notContains"
              },
              "leftValue": "={{ $json.website }}",
              "rightValue": "schema"
            },
            {
              "id": "9110b9e0-12aa-45cc-bde0-9eda8c10970e",
              "operator": {
                "type": "string",
                "operation": "notContains"
              },
              "leftValue": "={{ $json.website }}",
              "rightValue": "google"
            },
            {
              "id": "fb9b6ed6-96a5-4560-ab10-b8a4b9a61a2b",
              "operator": {
                "type": "string",
                "operation": "notContains"
              },
              "leftValue": "={{ $json.website }}",
              "rightValue": "gg"
            },
            {
              "id": "10500c0b-cdbd-4816-aba3-df60d69845dc",
              "operator": {
                "type": "string",
                "operation": "notContains"
              },
              "leftValue": "={{ $json.website }}",
              "rightValue": "gstatic"
            }
          ]
        },
        "options": {}
      },
      "id": "3aab21d0-3c15-41bd-a2b3-7244124e592e",
      "name": "Filter Google URLs",
      "type": "n8n-nodes-base.filter",
      "position": [
        -544,
        416
      ],
      "typeVersion": 2.2
    },
    {
      "parameters": {
        "options": {}
      },
      "id": "0f862f09-9551-44e5-b7e8-6ec939bc915b",
      "name": "Remove Duplicates (2)",
      "type": "n8n-nodes-base.removeDuplicates",
      "position": [
        816,
        352
      ],
      "typeVersion": 2
    },
    {
      "parameters": {
        "operation": "append",
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1fcijyZM1oU73i2xUbXYJ4j6RshmVEduOkCJji2SJP68",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1fcijyZM1oU73i2xUbXYJ4j6RshmVEduOkCJji2SJP68/edit?usp=drivesdk",
          "cachedResultName": "Scrape WITHOUT Paying for APIs"
        },
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1fcijyZM1oU73i2xUbXYJ4j6RshmVEduOkCJji2SJP68/edit#gid=0",
          "cachedResultName": "emails"
        },
        "columns": {
          "value": {
            "emails": "={{ $json.emails }}"
          },
          "schema": [
            {
              "id": "emails",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "emails",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "emails"
          ]
        },
        "options": {
          "useAppend": true
        }
      },
      "id": "a1570e2d-7b37-43e0-a9a3-264cbc5044a2",
      "name": "Add to Sheet (or whatever you want!)",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1008,
        352
      ],
      "typeVersion": 4.5
    }
  ],
  "connections": {
    "When clicking ‘Test workflow’": {
      "main": [
        [
          {
            "node": "Scrape Google Maps",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Remove Duplicates": {
      "main": [
        [
          {
            "node": "Limit",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Loop Over Items": {
      "main": [
        [
          {
            "node": "Wait1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Scrape Site",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wait": {
      "main": [
        [
          {
            "node": "Extract Emails",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Limit": {
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
    "Wait1": {
      "main": [
        [
          {
            "node": "Filter Out Empties",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split Out": {
      "main": [
        [
          {
            "node": "Remove Duplicates (2)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Emails": {
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
    "Extract URLs": {
      "main": [
        [
          {
            "node": "Filter Google URLs",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Scrape Google Maps": {
      "main": [
        [
          {
            "node": "Extract URLs",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Scrape Site": {
      "main": [
        [
          {
            "node": "Wait",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter Out Empties": {
      "main": [
        [
          {
            "node": "Split Out",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter Google URLs": {
      "main": [
        [
          {
            "node": "Remove Duplicates",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Remove Duplicates (2)": {
      "main": [
        [
          {
            "node": "Add to Sheet (or whatever you want!)",
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