---
tags:
  - consulting
---
{
  "nodes": [
    {
      "parameters": {
        "formTitle": "Terima Beres Social media JOConsult",
        "formDescription": "Invoice For",
        "formFields": {
          "values": [
            {
              "fieldLabel": "Nama",
              "requiredField": true
            },
            {
              "fieldLabel": "Email",
              "fieldType": "email"
            },
            {
              "fieldLabel": "Handle Akun Instagram"
            },
            {
              "fieldLabel": "Paket",
              "fieldType": "radio",
              "fieldOptions": {
                "values": [
                  {
                    "option": "Terima Beres 90 Hari"
                  },
                  {
                    "option": "Setup 1-Kali"
                  },
                  {
                    "option": "Scale & AI 90 Hari"
                  }
                ]
              }
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.formTrigger",
      "typeVersion": 2.3,
      "position": [
        -96,
        0
      ],
      "id": "6a760a38-31d2-4354-a2fb-c4371d03c172",
      "name": "On form submission",
      "webhookId": "6a7174b9-d94c-423b-aa30-ef42fdf174f0"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "d90cf6db-1d3a-49cc-90c2-a17165e7c6b9",
              "name": "submittedAt",
              "value": "={{ $now.setZone('Asia/Jakarta').toFormat('HH:mm/MM-dd-yyyy') }}\n",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        112,
        0
      ],
      "id": "b0f1eb7e-ae96-4c6a-bb24-27c854bf76c2",
      "name": "Edit Fields"
    },
    {
      "parameters": {
        "jsCode": "// 1. Define the HTML template with CSS\n"
      },
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        320,
        0
      ],
      "id": "27604cae-0f3d-403e-bb1a-ebd7b6e4681c",
      "name": "Code in JavaScript"
    },
    {
      "parameters": {
        "html_content": "={{ $json.html }}",
        "output_format": "file"
      },
      "type": "n8n-nodes-htmlcsstopdf.htmlcsstopdf",
      "typeVersion": 1,
      "position": [
        624,
        0
      ],
      "id": "547c6818-481a-417f-98c9-0d9f1b887c4b",
      "name": "HTML to PDF",
      "credentials": {
        "htmlcsstopdfApi": {
          "id": "7W5yfX38bTv8kjkt",
          "name": "HTML to PDF account 3"
        }
      }
    },
    {
      "parameters": {
        "sendTo": "={{ $('On form submission').item.json.Email }}",
        "subject": "=Jo Consult {{ $('On form submission').item.json.Paket }}",
        "message": "=Hi {{ $('On form submission').item.json.Nama }}, Here is the invoice for your {{ $('On form submission').item.json.Paket }} package. Please find the PDF attached. If you have any questions, feel free to reply to this email. Best regards, JO Consult",
        "options": {
          "appendAttribution": false,
          "attachmentsUi": {
            "attachmentsBinary": [
              {}
            ]
          }
        }
      },
      "type": "n8n-nodes-base.gmail",
      "typeVersion": 2.1,
      "position": [
        832,
        0
      ],
      "id": "0c96066e-2c3f-420d-95f6-fd934ccb9de7",
      "name": "Send a message",
      "webhookId": "a92a6a1f-131f-40a5-b783-1a2f5323d8b6",
      "credentials": {
        "gmailOAuth2": {
          "id": "cP9chxdpNDQB0Sck",
          "name": "0701"
        }
      }
    },
    {
      "parameters": {
        "content": "Embed Juga Bukti Transaksinya di Email"
      },
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        528,
        160
      ],
      "typeVersion": 1,
      "id": "08dd2a95-b767-4fd0-b42c-63f37ec2617a",
      "name": "Sticky Note"
    }
  ],
  "connections": {
    "On form submission": {
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
            "node": "Code in JavaScript",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Code in JavaScript": {
      "main": [
        [
          {
            "node": "HTML to PDF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTML to PDF": {
      "main": [
        [
          {
            "node": "Send a message",
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