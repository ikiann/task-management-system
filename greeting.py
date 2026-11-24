tasks = [
    {"title": "Complete Python homework", "priority": "High", "completed": False},
    {"title": "Review Git commands", "priority": "Medium", "completed": True},
    {"title": "Read Chapter 2", "priority": "Low", "completed": False},
    {"title": "Have Fun", "priority": "Super High", "completed": True}
]

print("Task Management System")
print("----------------------")

for task in tasks:
    status = "Completed" if task["completed"] else "Pending"
    print("Task:", task["title"])
    print("Priority:", task["priority"])
    print("Status:", status)
    print("----------------------")
