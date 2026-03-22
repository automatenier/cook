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
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegramTrigger",
      "typeVersion": 1.2,
      "position": [
        -192,
        -128
      ],
      "id": "bb893463-3fb5-4a66-bd4e-b71c425da4c6",
      "name": "Telegram Trigger",
      "webhookId": "38e0c6f2-1918-44d2-bd90-cdf8cfa48935",
      "credentials": {
        "telegramApi": {
          "id": "RM2ySAxqKFma50k7",
          "name": "Telefit"
        }
      }
    },
    {
      "parameters": {
        "chatId": "={{ $json.message.from.id }}",
        "text": "Halo, Coach! 👋\nSelamat datang di Jo Consult.\n\nNama saya Jordan, \nsaya membantu Fitness Coach \nmembangun online program pertama\ndan mulai menjual jasanya\nsecara konsisten melalui media sosial \ndari konsep, sistem, sampai siap dijual.\n\nJika Anda merasa:\n❌ Viewers banyak tapi nga ada Leads  \n❌ Menarik interaksi \"dompet tipis”  \n❌ Kewalahan dengan balas DM \n❌ Kewalahan buat konten \n❌ Leads tidak konsisten\n\n👉 Anda ada di tempat yang tepat.\n\nFokus anda hanya ke aktivitas Coaching\nSemua tanpa pekerjaan admin, konten, sales didelegasi. \n\n🚀 Apa yang saya lakukan untuk bisnis Anda?\n\n**✅ Content & Stories Personality**\nMencari struktur konten viral\n dan ubah ide singkatmu jadi\n jadwal konten & story 1 bulan\n penuh hanya dalam hitungan menit dengan AI.\n\n✅ YouTube VSL Scripting & Filming\nUbah poin-poin ide menjadi script video \nYouTube/VSL yang persuasif dan siap rekam\n tanpa perlu pusing mikirin kata-kata.\n\n✅ Online Coaching Infrastructure\nSistem otomatisasi alur kerja: \nKlien bayar → akses program, \nonboarding, & grup langsung terkirim \notomatis tanpa campur tangan admin.\n\n✅ Smart Telegram Check-in System\nPantau progress harian klien \n(Steps, calories, Berat Badan) secara real-time tanpa perlu\n buka Spreadsheet manual satu-per-satu.\n\n\n🔍 Mau lihat cara kerjanya?\n\nSilakan coba demo perintah di bawah ini:\n\n/progress\n/client\n/score\n/konten\n/kalender\n/progress\n/dm\n/Sales\n/harian\n/bulanan\n",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        288,
        0
      ],
      "id": "73bc0547-95b9-4312-9b1f-43d129e7a442",
      "name": "Send a text message",
      "webhookId": "7778dafd-605b-41c3-bd3d-e5f999828e07",
      "credentials": {
        "telegramApi": {
          "id": "RM2ySAxqKFma50k7",
          "name": "Telefit"
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
            "version": 3
          },
          "conditions": [
            {
              "id": "d1826087-329f-4a0c-ae6d-98a35ffa27e6",
              "leftValue": "={{ $json.message.text }}",
              "rightValue": "/workout",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            },
            {
              "id": "ca5f1690-bf77-4b4d-93d6-c21c175092cb",
              "leftValue": "={{ $json.message.text }}",
              "rightValue": "/progress",
              "operator": {
                "type": "string",
                "operation": "contains"
              }
            },
            {
              "id": "d5016e0e-b806-4600-9ef0-e81ed690345d",
              "leftValue": "={{ $json.message.text}}",
              "rightValue": "/client",
              "operator": {
                "type": "string",
                "operation": "equals",
                "name": "filter.operator.equals"
              }
            },
            {
              "id": "4aed1bec-6e4b-41de-a9f1-5764dd65245a",
              "leftValue": "={{ $json.message.text }}",
              "rightValue": "/score",
              "operator": {
                "type": "string",
                "operation": "equals",
                "name": "filter.operator.equals"
              }
            },
            {
              "id": "3c4f65d4-190b-4bd0-af8b-f5f2ad6976de",
              "leftValue": "={{ $json.message.text }}",
              "rightValue": "/konten",
              "operator": {
                "type": "string",
                "operation": "equals",
                "name": "filter.operator.equals"
              }
            },
            {
              "id": "3993de3a-6747-4951-b27a-b3967e3855bd",
              "leftValue": "={{ $json.message.text }}",
              "rightValue": "/kalender",
              "operator": {
                "type": "string",
                "operation": "equals",
                "name": "filter.operator.equals"
              }
            },
            {
              "id": "40f475bb-b99f-40ee-b961-ec9a388a4e4c",
              "leftValue": "={{ $json.message.text }}",
              "rightValue": "/dm",
              "operator": {
                "type": "string",
                "operation": "equals",
                "name": "filter.operator.equals"
              }
            },
            {
              "id": "973be705-cea3-4bae-ac0f-8b1cd38cb7e2",
              "leftValue": "={{ $json.message.text }}",
              "rightValue": "sales",
              "operator": {
                "type": "string",
                "operation": "equals",
                "name": "filter.operator.equals"
              }
            },
            {
              "id": "e0697471-4d8b-493d-b635-94b2bbbed3a3",
              "leftValue": "={{ $json.message.text }}",
              "rightValue": "/harian",
              "operator": {
                "type": "string",
                "operation": "equals",
                "name": "filter.operator.equals"
              }
            },
            {
              "id": "9f137a5e-d2e6-4558-bc75-e5c42f05ecc7",
              "leftValue": "={{ $json.message.text }}",
              "rightValue": "/bulanan",
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
      "typeVersion": 2.3,
      "position": [
        80,
        -112
      ],
      "id": "f8c94fb0-654c-4658-9486-bf09cb1ec96f",
      "name": "Prompt"
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
              "id": "d1826087-329f-4a0c-ae6d-98a35ffa27e6",
              "leftValue": "={{ $json.message.text }}",
              "rightValue": "/workout",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ],
          "combinator": "or"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.3,
      "position": [
        576,
        -128
      ],
      "id": "aec3a1e0-88e3-4ae9-af68-30e60f61ea2e",
      "name": "/workout"
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
              "id": "d1826087-329f-4a0c-ae6d-98a35ffa27e6",
              "leftValue": "={{ $json.message.text }}",
              "rightValue": "/progress",
              "operator": {
                "type": "string",
                "operation": "contains"
              }
            }
          ],
          "combinator": "or"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.3,
      "position": [
        960,
        -128
      ],
      "id": "a611ce66-baf7-4323-b5df-c45445849821",
      "name": "/progress"
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
              "id": "d1826087-329f-4a0c-ae6d-98a35ffa27e6",
              "leftValue": "",
              "rightValue": "/client",
              "operator": {
                "type": "string",
                "operation": "contains"
              }
            }
          ],
          "combinator": "or"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.3,
      "position": [
        1392,
        -112
      ],
      "id": "22bd86fe-327b-4c43-af2f-d489629efb8e",
      "name": "/client"
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
              "id": "d1826087-329f-4a0c-ae6d-98a35ffa27e6",
              "leftValue": "",
              "rightValue": "/score",
              "operator": {
                "type": "string",
                "operation": "contains"
              }
            }
          ],
          "combinator": "or"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.3,
      "position": [
        1776,
        -96
      ],
      "id": "8043d3ee-e187-481b-9dd1-f478becc3ce4",
      "name": "/score"
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
              "id": "d1826087-329f-4a0c-ae6d-98a35ffa27e6",
              "leftValue": "",
              "rightValue": "/konten",
              "operator": {
                "type": "string",
                "operation": "contains"
              }
            }
          ],
          "combinator": "or"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.3,
      "position": [
        2128,
        -80
      ],
      "id": "e60d1433-d914-4e17-8c13-ae3cacaa28f6",
      "name": "/konten",
      "disabled": true
    },
    {
      "parameters": {
        "chatId": "={{ $('Telegram Trigger').item.json.message.from.id }}",
        "text": "progres",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        1136,
        -256
      ],
      "id": "df519870-6534-4c6e-94e7-fb4c0fa76d5f",
      "name": "Send a text message1",
      "webhookId": "9c3fd436-a821-410f-823d-bb6a29859be4",
      "credentials": {
        "telegramApi": {
          "id": "RM2ySAxqKFma50k7",
          "name": "Telefit"
        }
      }
    },
    {
      "parameters": {
        "chatId": "6228081299",
        "text": "client",
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        1536,
        -240
      ],
      "id": "f6661930-5fe9-4fd3-8fce-c180ba60be9d",
      "name": "Send a text message13",
      "webhookId": "9c3fd436-a821-410f-823d-bb6a29859be4",
      "credentials": {
        "telegramApi": {
          "id": "RM2ySAxqKFma50k7",
          "name": "Telefit"
        }
      }
    },
    {
      "parameters": {
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        2272,
        -192
      ],
      "id": "caa0ca4d-0436-4980-9235-871f4d968727",
      "name": "Send a text message14",
      "webhookId": "9c3fd436-a821-410f-823d-bb6a29859be4",
      "credentials": {
        "telegramApi": {
          "id": "RM2ySAxqKFma50k7",
          "name": "Telefit"
        }
      },
      "disabled": true
    },
    {
      "parameters": {
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        1968,
        -240
      ],
      "id": "b571b616-c152-408b-8feb-114b4160c1c9",
      "name": "Send a text message15",
      "webhookId": "9c3fd436-a821-410f-823d-bb6a29859be4",
      "credentials": {
        "telegramApi": {
          "id": "RM2ySAxqKFma50k7",
          "name": "Telefit"
        }
      },
      "disabled": true
    },
    {
      "parameters": {
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        2736,
        -208
      ],
      "id": "fa7a621c-b0b4-4044-ba63-5ccd2c43cfdd",
      "name": "Send a text message16",
      "webhookId": "9c3fd436-a821-410f-823d-bb6a29859be4",
      "credentials": {
        "telegramApi": {
          "id": "RM2ySAxqKFma50k7",
          "name": "Telefit"
        }
      },
      "disabled": true
    },
    {
      "parameters": {
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        3104,
        -176
      ],
      "id": "a57626b9-be98-46d5-8a7c-39a5357358e4",
      "name": "Send a text message17",
      "webhookId": "9c3fd436-a821-410f-823d-bb6a29859be4",
      "credentials": {
        "telegramApi": {
          "id": "RM2ySAxqKFma50k7",
          "name": "Telefit"
        }
      },
      "disabled": true
    },
    {
      "parameters": {
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        3424,
        -208
      ],
      "id": "926fc242-daa9-4f11-9429-bd653f6d49ed",
      "name": "Send a text message18",
      "webhookId": "9c3fd436-a821-410f-823d-bb6a29859be4",
      "credentials": {
        "telegramApi": {
          "id": "RM2ySAxqKFma50k7",
          "name": "Telefit"
        }
      },
      "disabled": true
    },
    {
      "parameters": {
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        3792,
        -208
      ],
      "id": "ef073d34-4249-454b-8a55-9d76962dbf58",
      "name": "Send a text message19",
      "webhookId": "9c3fd436-a821-410f-823d-bb6a29859be4",
      "credentials": {
        "telegramApi": {
          "id": "RM2ySAxqKFma50k7",
          "name": "Telefit"
        }
      },
      "disabled": true
    },
    {
      "parameters": {
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        4144,
        -208
      ],
      "id": "1c2a8e48-7025-44e9-99fe-c8051ddd36a0",
      "name": "Send a text message20",
      "webhookId": "9c3fd436-a821-410f-823d-bb6a29859be4",
      "credentials": {
        "telegramApi": {
          "id": "RM2ySAxqKFma50k7",
          "name": "Telefit"
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
              "id": "d1826087-329f-4a0c-ae6d-98a35ffa27e6",
              "leftValue": "",
              "rightValue": "/kalender",
              "operator": {
                "type": "string",
                "operation": "contains"
              }
            }
          ],
          "combinator": "or"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.3,
      "position": [
        2544,
        -80
      ],
      "id": "60f0f942-631f-4c29-a698-d1c55f76ca19",
      "name": "/kalender",
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
              "id": "d1826087-329f-4a0c-ae6d-98a35ffa27e6",
              "leftValue": "",
              "rightValue": "/dm",
              "operator": {
                "type": "string",
                "operation": "contains"
              }
            }
          ],
          "combinator": "or"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.3,
      "position": [
        2912,
        -80
      ],
      "id": "a53e3ebd-db99-452b-bb22-932842efe615",
      "name": "/DM",
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
              "id": "d1826087-329f-4a0c-ae6d-98a35ffa27e6",
              "leftValue": "",
              "rightValue": "/sales",
              "operator": {
                "type": "string",
                "operation": "contains"
              }
            }
          ],
          "combinator": "or"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.3,
      "position": [
        3280,
        -80
      ],
      "id": "e3d8f232-0133-46b1-b157-0a2355172642",
      "name": "/sales",
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
              "id": "d1826087-329f-4a0c-ae6d-98a35ffa27e6",
              "leftValue": "",
              "rightValue": "/harian",
              "operator": {
                "type": "string",
                "operation": "contains"
              }
            }
          ],
          "combinator": "or"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.3,
      "position": [
        3616,
        -80
      ],
      "id": "f6d3f5dc-ffb4-472b-a008-ed0fe58e8de7",
      "name": "/harian",
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
              "id": "d1826087-329f-4a0c-ae6d-98a35ffa27e6",
              "leftValue": "",
              "rightValue": "/bulanan",
              "operator": {
                "type": "string",
                "operation": "contains"
              }
            }
          ],
          "combinator": "or"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.3,
      "position": [
        3952,
        -80
      ],
      "id": "0f5427c4-bc3f-4ed2-ab85-47fcbaf197ed",
      "name": "/bulanan",
      "disabled": true
    },
    {
      "parameters": {
        "chatId": "={{ $('Telegram Trigger').item.json.message.from.id }}",
        "text": "Halo, Coach! 👋\nSelamat datang di Jo Consult.\n\nNama saya Jordan, \nsaya membantu Fitness Coach \nmembangun online program pertama\ndan mulai menjual jasanya\nsecara konsisten melalui media sosial \ndari konsep, sistem, sampai siap dijual.\n\nJika Anda merasa:\n❌ Viewers banyak tapi nga ada Leads  \n❌ Menarik interaksi \"dompet tipis”  \n❌ Kewalahan dengan balas DM \n❌ Kewalahan buat konten \n❌ Leads tidak konsisten\n\n👉 Anda ada di tempat yang tepat.\n\nFokus anda hanya ke aktivitas Coaching\nSemua tanpa pekerjaan admin, konten, sales didelegasi. \n\n🚀 Apa yang saya lakukan untuk bisnis Anda?\n\n**✅ Content & Stories Personality**\nMencari struktur konten viral\n dan ubah ide singkatmu jadi\n jadwal konten & story 1 bulan\n penuh hanya dalam hitungan menit dengan AI.\n\n✅ YouTube VSL Scripting & Filming\nUbah poin-poin ide menjadi script video \nYouTube/VSL yang persuasif dan siap rekam\n tanpa perlu pusing mikirin kata-kata.\n\n✅ Online Coaching Infrastructure\nSistem otomatisasi alur kerja: \nKlien bayar → akses program, \nonboarding, & grup langsung terkirim \notomatis tanpa campur tangan admin.\n\n✅ Smart Telegram Check-in System\nPantau progress harian klien \n(Steps, calories, Berat Badan) secara real-time tanpa perlu\n buka Spreadsheet manual satu-per-satu.\n\n\n🔍 Mau lihat cara kerjanya?\n\nSilakan coba demo perintah di bawah ini:\n\n/progress\n/client\n/score\n/Konten\n/kalender\n/progress\n/DM\n/Sales\n/harian\n/bulanan\n",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        784,
        -256
      ],
      "id": "fb79fede-7f3c-4dc0-9487-90ef6e2a72e8",
      "name": "workout",
      "webhookId": "7778dafd-605b-41c3-bd3d-e5f999828e07",
      "credentials": {
        "telegramApi": {
          "id": "RM2ySAxqKFma50k7",
          "name": "Telefit"
        }
      }
    }
  ],
  "connections": {
    "Telegram Trigger": {
      "main": [
        [
          {
            "node": "Prompt",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Prompt": {
      "main": [
        [
          {
            "node": "/workout",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Send a text message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "/workout": {
      "main": [
        [
          {
            "node": "workout",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "/progress",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "/progress": {
      "main": [
        [
          {
            "node": "Send a text message1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "/client",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "/client": {
      "main": [
        [
          {
            "node": "Send a text message13",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "/score",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "/score": {
      "main": [
        [
          {
            "node": "Send a text message15",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "/konten",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "/konten": {
      "main": [
        [
          {
            "node": "Send a text message14",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "/kalender",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "/kalender": {
      "main": [
        [
          {
            "node": "Send a text message16",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "/DM",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "/DM": {
      "main": [
        [
          {
            "node": "Send a text message17",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "/sales",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "/sales": {
      "main": [
        [
          {
            "node": "Send a text message18",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "/harian",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "/harian": {
      "main": [
        [
          {
            "node": "Send a text message19",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "/bulanan",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "/bulanan": {
      "main": [
        [
          {
            "node": "Send a text message20",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    }
  },
  "pinData": {},
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "3039fbd4cadb80067e54b2133333595ff57d847dd0124b88f494b4fc1d62ef2e"
  }
}