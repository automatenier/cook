---
tags:
  - automation
---
{
  "nodes": [
    {
      "parameters": {},
      "type": "n8n-nodes-base.errorTrigger",
      "typeVersion": 1,
      "position": [
        -32,
        0
      ],
      "id": "fd18d24a-62cc-4e19-b6c1-4dde9a7af6bc",
      "name": "Error Trigger"
    },
    {
      "parameters": {
        "chatId": "6228081299",
        "text": "=Workflow Error {{ $json.workflow.name }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        304,
        0
      ],
      "id": "ac16d300-a801-4f61-91d2-9713a7bc71f4",
      "name": "Send a text message",
      "webhookId": "4c21e65a-865b-4b32-864a-e97dac737922",
      "credentials": {}
    }
  ],
  "connections": {
    "Error Trigger": {
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