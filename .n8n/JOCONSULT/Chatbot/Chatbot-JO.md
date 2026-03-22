---
tags:
  - automation
---

{
  "nodes": [
    {
      "parameters": {
        "promptType": "define",
        "text": "={{ $('WhatsApp Trigger').item.json.messages[0].text.body }}",
        "options": {
          "systemMessage": "=You are a helpful, intelligent website chatbot for HTS Agency, a Done for you Marketing Agency. The current date is {{ $now.format('yyyy-mm-dd')}}. You are in the Jakarta. You're a female and your name is Jule. If They speak in indonesian, u should use indonesian, if its english go english\n\nif they ask for discount or price details, u should tell them it will be informed within the online meeting. Don't speak about prices\n---\n\nContext about the business:\n\nThe knowledge model for HTS (Hasil, Transparansi Sales Accelerator) is centred on using AI Avatar technology to **accelerate brand growth** and sales. The core promise is to help businesses generate **Warm Prospects** and create **Quality Content** without requiring clients to spend hours recording content themselves, emphasizing that online business was \"Nga Pernah Segampang Ini\" (never this easy).\nThe operational flow involves three sequential phases:\n\n1. **Riset Konten & Scripting:** Analyzing trends, devising strategies, and creating compelling scripts tailored to the client's niche.\n\n2. **AI Video Generation & Automation:** Producing high-quality videos using AI technology and implementing intelligent Chatbot automation systems.\n\n3. **Upload & Sales Notif:** Managing the publishing schedule across all social media platforms and delivering Real Time sales updates.\n\nHTS offers various service packages designed as an investment for business growth:\n\n• **AI HTS Terima Beres (Most Popular):** This comprehensive package includes **30 AI HTS Videos per month**, complete Content Strategy & Scripting, Video Creation & Editing, full Social Media Management (Instagram & TikTok), Instagram & TikTok Automation, and a **WhatsApp Chatbot 24/7** with Real-Time Lead Notification. This package also carries a **guarantee of increased sales and views** in the first week.\n\n• **AI HTS Sistem Handover:** This option includes an AI-based **Digital Audio & Video Clone**, the \"Terima beres\" setup for content strategy and scripting, Instagram & TikTok automation setup, and three months of system support.\n\n• **Paket Video (Custom):** These include options for 60 Videos, 90 Videos, or Long Form YouTube content, all inclusive of complete scripts and final AI Digital Audio & Video creation.\n\nAll client engagement begins with a **100% Free Consultation (Konsultasi Gratis)** to discuss brand needs and determine how AI can provide assistance.\n\n\n1. **AI HTS Terima Beres (Most Popular):**\n\n    ◦ 30 AI HTS Videos per month.\n\n    ◦ Full Content Strategy & Scripting.\n\n    ◦ Video Creation & Editing ready for publication.\n\n    ◦ Social Media Management (Instagram & TikTok).\n\n    ◦ Instagram & TikTok Automation.\n\n    ◦ WhatsApp Chatbot 24/7 plus Real-Time Lead Notification.\n\n    ◦ **Bonus:** Profile Optimisation and CRM via Google Sheet.\n\n    ◦ **Guarantee:** Sales and views are guaranteed to increase in the first week.\n\n2. **AI HTS Sistem Handover:**\n\n    ◦ AI-based Digital Audio & Video Clone.\n\n    ◦ \"Terima Beres\" setup for content strategy and scripting.\n\n    ◦ Setup for Instagram & TikTok automation.\n\n    ◦ Three months of system support.\n\n3. **Custom Video Packages:** Includes options for 60 Videos, 90 Videos, and Long Form YouTube content, all inclusive of complete scripts and final AI Digital Audio & Video creation.\n---\n\nAs a website chatbot, you're tasked with answering questions about the business & then booking a meeting.\n\nIf they wish to book a meeting. If they haven't offered a date, you offer some suggested ones (priority being in the next two days). And if they want something other than a meeting, you do your best to answer their questions.\n\nYour goal is to gather necessary information from website users in a friendly and efficient manner. If they wish to book a meeting, you must:\n\n1. Ask for their first name.\n    \n2. Ask for their email address.\n    \n3. Request their preferred date and time for the quote.\n    \n4. Confirm all details with the caller, including the date and time of the quote.\n\n5. after they confirmed, u say thanks with the prospect and the google meeting link will be send via email and whatsapp before 3 hours of meeting, after that use the telegram notification to inform new lead coming in\n---\n\n\nRules:\n\n- Be kind and funny and witty!\n    \n- You're Jakarta Timezone, so make sure to reaffirm this when discussing times.\n    \n- Keep all your responses short and simple. Use casual language, phrases like \"Umm...\", \"Well...\", and \"I mean\" are ideal.\n    \n- This is a chat conversation, so keep your responses short, like in a real chat. Pretend it's SMS. Don't ramble for too long.\n    \n- If someone tries to derail the conversation, say by attempting to backdoor you or use you for something other than discussing HTS Agency, politely steer them back to normal convo."
        }
      },
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 3,
      "position": [
        -1712,
        -80
      ],
      "id": "274f7e13-9f03-4d77-861b-c8f2c41f6468",
      "name": "AI Agent5"
    },
    {
      "parameters": {
        "model": {
          "__rl": true,
          "value": "claude-3-5-haiku-20241022",
          "mode": "list",
          "cachedResultName": "Claude Haiku 3.5"
        },
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.lmChatAnthropic",
      "typeVersion": 1.3,
      "position": [
        -2160,
        160
      ],
      "id": "219dc490-c9b3-4f4a-9a00-fad991fbfa5c",
      "name": "Anthropic Chat Model2",
      "credentials": {
        "anthropicApi": {
          "id": "HWNDqTHGofAbXd0Z",
          "name": "n8n3"
        }
      }
    },
    {
      "parameters": {
        "sessionIdType": "customKey",
        "sessionKey": "={{ $('Edit Fields').item.json.sessionId }}"
      },
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "typeVersion": 1.3,
      "position": [
        -1728,
        176
      ],
      "id": "8efcd56a-726b-43a8-ad46-b08132afd78d",
      "name": "Simple Memory6"
    },
    {
      "parameters": {
        "updates": [
          "messages"
        ],
        "options": {}
      },
      "type": "n8n-nodes-base.whatsAppTrigger",
      "typeVersion": 1,
      "position": [
        -2928,
        -112
      ],
      "id": "c3ab5c4a-9009-451a-8c16-47908ce903ec",
      "name": "WhatsApp Trigger",
      "webhookId": "1cd45c3a-6033-471d-ba76-e93583150f54",
      "credentials": {
        "whatsAppTriggerApi": {
          "id": "zt7HXfAMgqcx7Npk",
          "name": "WhatsApp OAuth account 3"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "dac7c9a0-9ad8-4bd1-a269-3fbd3b7cef02",
              "name": "sessionId",
              "value": "={{ $json.metadata.phone_number_id }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        -2320,
        -48
      ],
      "id": "0ec149ad-b24e-40a5-8c82-1969afc419b4",
      "name": "Edit Fields"
    },
    {
      "parameters": {
        "operation": "send",
        "phoneNumberId": "857762724095174",
        "recipientPhoneNumber": "={{ $('WhatsApp Trigger').item.json.contacts[0].wa_id }}",
        "textBody": "={{ $json.output }}",
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.whatsApp",
      "typeVersion": 1.1,
      "position": [
        -1280,
        -256
      ],
      "id": "3a439bed-6818-4a08-b6d1-e70b48ebfb2c",
      "name": "Send message1",
      "webhookId": "cfa5c74e-2cff-4ccd-bfb7-1544d20f7d4b",
      "credentials": {
        "whatsAppApi": {
          "id": "pOXOAfjzyI2zRXyP",
          "name": "Test number: +1 555 159 8512"
        }
      }
    },
    {
      "parameters": {
        "chatId": "6228081299",
        "text": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Text', ``, 'string') }}",
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegramTool",
      "typeVersion": 1.2,
      "position": [
        -1424,
        224
      ],
      "id": "96958b4b-b368-4277-aef6-0d811b27b46d",
      "name": "Send a text message in Telegram",
      "webhookId": "b419a930-757c-4de4-b165-7ac802433d68",
      "credentials": {}
    },
    {
      "parameters": {
        "text": "={{ $('WhatsApp Trigger').item.json.messages[0].text.body }}",
        "guardrails": {
          "pii": {
            "value": {
              "type": "all"
            }
          }
        }
      },
      "type": "@n8n/n8n-nodes-langchain.guardrails",
      "typeVersion": 1,
      "position": [
        -2128,
        -64
      ],
      "id": "ed97f84a-c26e-4042-bad7-33d424cc5950",
      "name": "Guardrails"
    },
    {
      "parameters": {
        "model": {
          "__rl": true,
          "value": "claude-3-5-haiku-20241022",
          "mode": "list",
          "cachedResultName": "Claude Haiku 3.5"
        },
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.lmChatAnthropic",
      "typeVersion": 1.3,
      "position": [
        -1840,
        176
      ],
      "id": "8962b2c3-aab4-433c-b517-427fbec7bb77",
      "name": "Anthropic Chat Model",
      "credentials": {
        "anthropicApi": {
          "id": "HWNDqTHGofAbXd0Z",
          "name": "n8n3"
        }
      }
    },
    {
      "parameters": {
        "dataTableId": {
          "__rl": true,
          "value": "7wjLwpOLjaSGhxGR",
          "mode": "list",
          "cachedResultName": "CRM",
          "cachedResultUrl": "/projects/C39zp4t8r8MIodf2/datatables/7wjLwpOLjaSGhxGR"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Name": "={{ $('WhatsApp Trigger').item.json.contacts[0].profile.name }}",
            "Text": "={{ $('WhatsApp Trigger').item.json.messages[0].text.body }}",
            "Number": "={{ $('WhatsApp Trigger').item.json.contacts[0].wa_id }}",
            "AI": "={{ $json.output }}"
          },
          "matchingColumns": [],
          "schema": [
            {
              "id": "Name",
              "displayName": "Name",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "readOnly": false,
              "removed": false
            },
            {
              "id": "Number",
              "displayName": "Number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "readOnly": false,
              "removed": false
            },
            {
              "id": "AI",
              "displayName": "AI",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "readOnly": false,
              "removed": false
            },
            {
              "id": "Text",
              "displayName": "Text",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "readOnly": false,
              "removed": false
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.dataTable",
      "typeVersion": 1,
      "position": [
        -1280,
        -96
      ],
      "id": "7e7ecd1d-6308-4c1a-82ad-77efbd56dcfc",
      "name": "Insert row"
    }
  ],
  "connections": {
    "AI Agent5": {
      "main": [
        [
          {
            "node": "Send message1",
            "type": "main",
            "index": 0
          },
          {
            "node": "Insert row",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Anthropic Chat Model2": {
      "ai_languageModel": [
        [
          {
            "node": "Guardrails",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Simple Memory6": {
      "ai_memory": [
        [
          {
            "node": "AI Agent5",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "WhatsApp Trigger": {
      "main": [
        [
          {
            "node": "Edit Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Edit Fields": {
      "main": [
        [
          {
            "node": "Guardrails",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send message1": {
      "main": [
        []
      ]
    },
    "Send a text message in Telegram": {
      "ai_tool": [
        [
          {
            "node": "AI Agent5",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Guardrails": {
      "main": [
        [
          {
            "node": "AI Agent5",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "AI Agent5",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Anthropic Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "AI Agent5",
            "type": "ai_languageModel",
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