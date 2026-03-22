---
tags:
  - consulting
---
{
  "nodes": [
    {
      "parameters": {
        "formTitle": "Form Konsultasi JO Consult",
        "formFields": {
          "values": [
            {
              "fieldLabel": "Nama",
              "requiredField": true
            },
            {
              "fieldLabel": "Email",
              "requiredField": true
            },
            {
              "fieldLabel": "Akun Instagram @",
              "requiredField": true
            },
            {
              "fieldLabel": "No. Whatsapp Aktif",
              "requiredField": true
            },
            {
              "fieldLabel": "Berapa pendapatan bulanan Anda (Rp)?\n(Ini adalah total pendapatan keseluruhan, bukan hanya dari coaching)",
              "fieldType": "radio",
              "fieldOptions": {
                "values": [
                  {
                    "option": "0 - 10 Juta IDR"
                  },
                  {
                    "option": "10 - 25 Juta IDR"
                  },
                  {
                    "option": "25 - 85 Juta IDR"
                  }
                ]
              },
              "requiredField": true
            },
            {
              "fieldLabel": "Apa hambatan terbesar yang menghentikan Anda untuk memulai atau mengembangkan bisnis Anda?",
              "fieldType": "radio",
              "fieldOptions": {
                "values": [
                  {
                    "option": "Struktur konten/penawaran (offer)"
                  },
                  {
                    "option": "Corong penjualan (funnels)/sistem"
                  },
                  {
                    "option": "Closing penjualan"
                  },
                  {
                    "option": "Semua di atas (Saya butuh bimbingan 1:1)"
                  }
                ]
              },
              "requiredField": true
            },
            {
              "fieldLabel": "Pada skala 1-10, seberapa berkomitmen Anda untuk berinvestasi pada diri sendiri saat ini jika penawarannya cocok? jujur saja di sini :/ ",
              "requiredField": true
            },
            {
              "fieldLabel": "Apa yang membuat Anda memutuskan bahwa sekaranglah saatnya untuk bekerja sama dengan saya?",
              "fieldType": "radio",
              "fieldOptions": {
                "values": [
                  {
                    "option": "Video Youtube Anda"
                  },
                  {
                    "option": "Konten durasi pendek/reels/iklan"
                  },
                  {
                    "option": "Story IG Anda"
                  }
                ]
              },
              "requiredField": true
            },
            {
              "fieldLabel": "JO-Consulting adalah Mentorship 1-on-1 selama 90 Hari yang membantu coach online menghasilkan Rp50 Juta/bulan. Jika kita cocok saat diskusi di telepon, berapa banyak dana yang sudah Anda SIAPKAN untuk DIINVESTASIKAN HARI INI? (IDR)",
              "fieldType": "radio",
              "fieldOptions": {
                "values": [
                  {
                    "option": "Saya punya kurang dari Rp4 JT (Mohon jangan melakukan booking)"
                  },
                  {
                    "option": "Saya punya 4 - 20 JT"
                  },
                  {
                    "option": "Saya punya 20 - 50 JT"
                  },
                  {
                    "option": "Saya punya 50 - 90 JT"
                  },
                  {
                    "option": "90 JT ++ Rupiah"
                  }
                ]
              },
              "requiredField": true
            },
            {
              "fieldLabel": "Karena saya sibuk menjalankan bisnis saya, menyelamatkan dunia, dan membantu para coach menghasilkan banyak uang, jika Anda tidak hadir pada jadwal telepon yang ditentukan, Anda tidak akan bisa menjadwal ulang tanpa pemberitahuan lebih lanjut. Apakah Anda setuju untuk hadir tepat waktu sesuai jadwal?",
              "fieldType": "radio",
              "fieldOptions": {
                "values": [
                  {
                    "option": "Ya"
                  },
                  {
                    "option": "Jika saya perlu menjadwal ulang, saya akan memberi tahu Anda"
                  }
                ]
              }
            }
          ]
        },
        "options": {
          "appendAttribution": false,
          "respondWithOptions": {
            "values": {
              "respondWith": "redirect",
              "redirectUrl": "https://calendar.app.google/TbSQusZiBYSPzbxC8"
            }
          },
          "customCss": ":root {\n\t--font-family: 'Inter', 'Open Sans', sans-serif;\n\t/* Colors pulled from your logo */\n\t--color-background: #F4F7FF;\n\t--color-card-bg: #ffffff;\n\t--color-card-border: #dbdfe7;\n\t\n    /* Primary Purple from logo */\n\t--color-focus-border: #6B63AB; \n    /* Primary Blue from logo */\n\t--color-submit-btn-bg: #00AEEF; \n\t--color-submit-btn-text: #ffffff;\n    \n\t--color-header: #4A4E69;\n\t--color-label: #555555;\n\t--color-input-text: #333333;\n    --color-html-link: #00AEEF;\n    --color-required: #6B63AB;\n    \n\t--border-radius-card: 12px;\n\t--border-radius-input: 8px;\n    --container-width: 500px;\n}\n\n/* 1. Remove n8n Logo/Footer */\nfooter, .n8n-form-footer, div[class*=\"footer\"] {\n    display: none !important;\n}\n\n/* 2. Insert Your Logo at the Top */\n.n8n-form-card::before {\n    content: \"\";\n    display: block;\n    width: 100%;\n    height: 120px; /* Adjust height as needed */\n    background-image: url('YOUR_IMAGE_URL_HERE');\n    background-size: contain;\n    background-repeat: no-repeat;\n    background-position: center;\n    margin-bottom: 20px;\n}\n\n/* 3. Button Hover Effect (Gradient) */\nbutton[type=\"submit\"] {\n    background: linear-gradient(135deg, #6B63AB 0%, #00AEEF 100%) !important;\n    border: none !important;\n    font-weight: 600 !important;\n    transition: opacity 0.2s;\n}\n\nbutton[type=\"submit\"]:hover {\n    opacity: 0.9;\n}"
        }
      },
      "type": "n8n-nodes-base.formTrigger",
      "typeVersion": 2.3,
      "position": [
        32,
        -144
      ],
      "id": "c136233a-166a-4593-b076-d49d6d7e28f9",
      "name": "On form submission1",
      "webhookId": "1c7172e4-e7b3-43d7-a6fc-bef3df818a70"
    },
    {
      "parameters": {
        "dataTableId": {
          "__rl": true,
          "value": "3oN1vNokM2tKn7Sm",
          "mode": "list",
          "cachedResultName": "Form-Salescall",
          "cachedResultUrl": "/projects/C39zp4t8r8MIodf2/datatables/3oN1vNokM2tKn7Sm"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Nama": "={{ $json.Nama }}",
            "Email": "={{ $json.Email }}",
            "IG": "={{ $json.IG }}",
            "WA": "={{ $json.WA }}",
            "Income": "={{ $json.Income }}",
            "Skala": "={{ $json.Skala }}",
            "Kenapa": "={{ $json.Kenapa }}",
            "Konfirmasi": "={{ $json.Konfirmasi }}",
            "Hambatan": "={{ $json.Hambatan }}"
          },
          "matchingColumns": [],
          "schema": [
            {
              "id": "Nama",
              "displayName": "Nama",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "readOnly": false,
              "removed": false
            },
            {
              "id": "Email",
              "displayName": "Email",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "readOnly": false,
              "removed": false
            },
            {
              "id": "IG",
              "displayName": "IG",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "readOnly": false,
              "removed": false
            },
            {
              "id": "WA",
              "displayName": "WA",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "readOnly": false,
              "removed": false
            },
            {
              "id": "Income",
              "displayName": "Income",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "readOnly": false,
              "removed": false
            },
            {
              "id": "Skala",
              "displayName": "Skala",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "readOnly": false,
              "removed": false
            },
            {
              "id": "Kenapa",
              "displayName": "Kenapa",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "readOnly": false,
              "removed": false
            },
            {
              "id": "Konfirmasi",
              "displayName": "Konfirmasi",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "readOnly": false,
              "removed": false
            },
            {
              "id": "Hambatan",
              "displayName": "Hambatan",
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
        544,
        -144
      ],
      "id": "a8d04240-5041-4acb-b3a5-967b14223587",
      "name": "Insert row"
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
        1296,
        0
      ],
      "id": "4c7b1f0c-849c-4712-b428-6b697810eae4",
      "name": "Append row in sheet",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "xNFdBVlbfdG0Muij",
          "name": "HTSReal1"
        }
      },
      "disabled": true
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
        1376,
        -128
      ],
      "id": "7af0a85e-39d3-45cd-9b63-1ca77cb23145",
      "name": "Analyze document",
      "credentials": {
        "anthropicApi": {
          "id": "HWNDqTHGofAbXd0Z",
          "name": "n8n3"
        }
      },
      "disabled": true
    },
    {
      "parameters": {
        "keys": {
          "key": [
            {
              "currentKey": "Akun Instagram @",
              "newKey": "IG"
            },
            {
              "currentKey": "No. Whatsapp Aktif",
              "newKey": "WA"
            },
            {
              "currentKey": "Berapa pendapatan bulanan Anda (Rp)?\n(Ini adalah total pendapatan keseluruhan, bukan hanya dari coaching)",
              "newKey": "Income"
            },
            {
              "currentKey": "Pada skala 1-10, seberapa berkomitmen Anda untuk berinvestasi pada diri sendiri saat ini jika penawarannya cocok? jujur saja di sini :/ ",
              "newKey": "Skala"
            },
            {
              "currentKey": "Apa yang membuat Anda memutuskan bahwa sekaranglah saatnya untuk bekerja sama dengan saya?",
              "newKey": "Kenapa"
            },
            {
              "currentKey": "JO-Consulting adalah Mentorship 1-on-1 selama 90 Hari yang membantu coach online menghasilkan Rp50 Juta/bulan. Jika kita cocok saat diskusi di telepon, berapa banyak dana yang sudah Anda SIAPKAN untuk DIINVESTASIKAN HARI INI? (IDR)",
              "newKey": "Konfirmasi"
            },
            {
              "currentKey": "Apa hambatan terbesar yang menghentikan Anda untuk memulai atau mengembangkan bisnis Anda?",
              "newKey": "Hambatan"
            }
          ]
        },
        "additionalOptions": {}
      },
      "type": "n8n-nodes-base.renameKeys",
      "typeVersion": 1,
      "position": [
        336,
        -144
      ],
      "id": "991d53bf-9ac3-4bb2-967f-dfa4d3ae969a",
      "name": "Rename Keys"
    },
    {
      "parameters": {
        "operation": "sendAndWait",
        "options": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        1648,
        0
      ],
      "id": "5377f232-8d69-4add-bc16-5e23a77ac269",
      "name": "Send message and wait for response",
      "webhookId": "1e175b68-d0c0-4428-af87-6ba68830bbe1",
      "credentials": {
        "telegramApi": {
          "id": "5BjZgtWlAghx9Zit",
          "name": "Reel Analyzer"
        }
      },
      "disabled": true
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
              "id": "13c5d719-13dc-4944-9b9c-c9072d39858d",
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
        1856,
        0
      ],
      "id": "bab1b55a-5edf-4b87-b521-37f041145245",
      "name": "Filter"
    },
    {
      "parameters": {
        "chatId": "6228081299",
        "text": "=Form baru submit\nNama: {{ $('On form submission1').item.json.Nama }}\nCek di data tables",
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        704,
        -144
      ],
      "id": "2e8c65c9-f6bd-415f-93c2-6810ff7a5e32",
      "name": "Send a text message",
      "webhookId": "6594673d-70cd-4041-9e73-b0ab7410512c",
      "credentials": {
        "telegramApi": {
          "id": "tgPSmpiTxYY4jbBA",
          "name": "VA-JOBOT"
        }
      }
    },
    {
      "parameters": {
        "method": "POST",
        "options": {}
      },
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.3,
      "position": [
        880,
        -144
      ],
      "id": "2a6128c1-5f33-460c-9b0f-cad5ec5d1498",
      "name": "HTTP Request"
    },
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
        16,
        256
      ],
      "id": "8b06cc53-fdb7-4cde-85e8-8863ef828e43",
      "name": "On form submission",
      "webhookId": "95e685a6-57be-4aed-a886-ddbe2b86e1a8"
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
        224,
        256
      ],
      "id": "91aef727-8b12-436e-b08b-35f4f9a02159",
      "name": "Edit Fields"
    },
    {
      "parameters": {
        "jsCode": "// 1. Define the HTML template with CSS\n"
      },
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        432,
        256
      ],
      "id": "681e36a4-fff4-4a46-a49b-f2528392cc50",
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
        736,
        256
      ],
      "id": "f50ed042-8d75-445a-837b-b112f4414d52",
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
        944,
        256
      ],
      "id": "733ed28f-bfc8-4ceb-9d81-40f799523e03",
      "name": "Send a message",
      "webhookId": "c61416f9-61aa-404a-be1c-954d7d99978a",
      "credentials": {
        "gmailOAuth2": {
          "id": "cP9chxdpNDQB0Sck",
          "name": "0701"
        }
      }
    }
  ],
  "connections": {
    "On form submission1": {
      "main": [
        [
          {
            "node": "Rename Keys",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Insert row": {
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
    "Append row in sheet": {
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
    "Rename Keys": {
      "main": [
        [
          {
            "node": "Insert row",
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
            "node": "Filter",
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
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
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