# dashboard.py
import json

# Load data
with open('data.json', 'r') as file:
    data = json.load(file)

# Display Dashboard
print("\n🧠 Engineer's Dashboard")
print("=" * 30)

# Engineer Overview
print("\n👩‍💻 Engineer Stats:")
for engineer in data:
    print(f"- {engineer['engineer']}: {engineer['tickets_closed']} tickets closed, {engineer['hours_logged']} hours logged")

# Summary
total_tickets = sum(e['tickets_closed'] for e in data)
total_hours = sum(e['hours_logged'] for e in data)
avg_hours = total_hours / len(data)

print("\n📊 Summary:")
print(f"Total Tickets Closed: {total_tickets}")
print(f"Total Hours Logged: {total_hours}")
print(f"Average Hours per Engineer: {avg_hours:.1f}")
