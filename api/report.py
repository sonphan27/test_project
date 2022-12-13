#!/usr/bin/python3
import requests
from members import list_members, map_members
 
 
def format_tasks(tasks):
  report_tasks= []
  for task in tasks:
    if not task["idMembers"]:
      continue
    for member_id in task["idMembers"]:
      if member_id in map_members.keys():
        format_task = {
          'name': task['name'],
          'member': map_members[member_id]["fullName"],
          'member_id': member_id,
          'url': task['url'],
        }
        report_tasks.append(format_task)
  return report_tasks
 
def generate_card(task):
  # assign = ' | '.join([members[mem_id]['fullName'] for mem_id in task['member']])
  return {
    "@type": "MessageCard",
    "@context": "https://schema.org/extensions",
    "summary": f"Work report for {task['member']}",
    "themeColor": "0076D7",
    "title": task["name"],
    "sections": [
        {
          "activityTitle": f'**{task["member"]}**: Morning, today I will do this task',
          "activitySubtitle": "**Flower Meister International> In-progress**",
          "activityImage": map_members[task["member_id"]]["avatarUrl"] + "/60.png",
          "facts": [
            {
              "name": "Board:",
              "value": "FMI Sprint"
            },
            {
              "name": "Assigned to:",
              "value": task["member"]
            }
          ],
          "text": ''
        }
      ],
      "potentialAction": [
        {
          "@type": "OpenUri",
          "name": "View in Trello",
          "targets": [
            {
              "os": "default",
              "uri": task['url']
            }
          ]
        }
      ]
  }
 
credentials = {
 'key': 'b3e408e6cce96a1ce575527f610b3885',
 'token': '123c88d46cb251880ab572ac46cfe6ce3d19f60d483cba94cac2edcb35a2ec21'
}

board_id = '5b4d2cebf11b93ca5c1daa29'
list_in_progress_id = '5b4d2d268a2f4a1b411d2d6a'
list_in_review_id = '5ca70e41a6ae81759dbf193f'
trello_in_progress_card_url = f'https://api.trello.com/1/lists/{list_in_progress_id}/cards?fields=name,idMembers,url,pic'
trello_in_review_card_url = f'https://api.trello.com/1/lists/{list_in_review_id}/cards?fields=name,idMembers,url,pic'

teams_channel_report = 'https://otanitradingltd.webhook.office.com/webhookb2/fe39f790-e219-4cfa-8b4c-ca1b856401a2@918e8b14-7c6d-4a7a-9aa1-44d2b9b3a3ec/IncomingWebhook/2e7ca9d3572e4863b1687d12325ed92b/277973ea-8797-48ad-ba34-bfa764f353c6'

def run():
  tasks = requests.get(trello_in_progress_card_url, params=credentials)
  
  tasks.raise_for_status()
  report_tasks = format_tasks(tasks.json())

  for task in report_tasks:
    card = generate_card(task)
    print(card)
    requests.post(teams_channel_report, json=card)
# %%
