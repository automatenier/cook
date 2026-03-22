---
tags:
  - automation
---
{
  "nodes": [
    {
      "parameters": {},
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [
        0,
        0
      ],
      "id": "b7db6f1f-6c3b-4679-aeee-39e43567dda2",
      "name": "When clicking ‘Execute workflow’"
    },
    {
      "parameters": {
        "operation": "Run actor and get dataset",
        "actorId": {
          "__rl": true,
          "value": "https://console.apify.com/actors/p7UMdpQnjKmmpR21D",
          "mode": "url"
        }
      },
      "type": "@apify/n8n-nodes-apify.apify",
      "typeVersion": 1,
      "position": [
        208,
        0
      ],
      "id": "71145fbc-edb1-435c-8ee4-84d5477a5b37",
      "name": "Run an Actor and get dataset",
      "credentials": {
        "apifyApi": {
          "id": "AuMAM42YTZ9Ue9DQ",
          "name": "Apify account"
        }
      }
    }
  ],
  "connections": {
    "When clicking ‘Execute workflow’": {
      "main": [
        [
          {
            "node": "Run an Actor and get dataset",
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