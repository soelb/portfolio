# dashboard.py

import json

# Load data
with open('data.json', 'r') as file:
    data = json.load(file)

# Display Dashboard
print("\n📊 Engineer's Dashboard")
print("=" * 30)

# Systems Status
print("\n🖥️  System Status:")
for system in data['systems']:
    print(f"  - {system['name']}: {system['status']}")

# Tasks
print("\n📝 Tasks:")
for task in data['tasks']:
    status_icon = {
        "done": "✅",
        "in progress": "🔄",
        "pending": "🕒"
    }.get(task['status'], "❓")
    print(f"  - {task['title']} [{status_icon}]")
