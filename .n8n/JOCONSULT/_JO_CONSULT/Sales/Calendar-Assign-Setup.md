---
tags:
  - consulting
---
{
  "nodes": [
    {
      "parameters": {
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        },
        "calendarId": {
          "__rl": true,
          "value": "20c1143ba7aebef51350e53a750fab94be9e75050db7325cbd4c266250d162f3@group.calendar.google.com",
          "mode": "list",
          "cachedResultName": "Consulting"
        },
        "triggerOn": "eventCreated",
        "options": {}
      },
      "type": "n8n-nodes-base.googleCalendarTrigger",
      "typeVersion": 1,
      "position": [
        0,
        0
      ],
      "id": "471e1c7b-9765-49d0-84eb-f20ec34762e2",
      "name": "Google Calendar Trigger",
      "credentials": {
        "googleCalendarOAuth2Api": {
          "id": "bUNI4lpvoiQwOKnx",
          "name": "Google Calendar account 6"
        }
      }
    },
    {
      "parameters": {
        "chatId": "-5121227224",
        "text": "ds",
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        208,
        0
      ],
      "id": "bd68efc2-fda8-468f-9cdd-3c2a10b50c59",
      "name": "Send a text message",
      "webhookId": "28f5bf7d-856c-40e2-b318-c158cb84ee55",
      "credentials": {
        "telegramApi": {
          "id": "gQZgqeIABIxBw8u8",
          "name": "joconsultbot"
        }
      }
    }
  ],
  "connections": {
    "Google Calendar Trigger": {
      "main": [
        [
          {
            "node": "Send a text message",
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