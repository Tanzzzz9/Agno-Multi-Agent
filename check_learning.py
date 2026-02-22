from learning.storage import get_all_learnings

print("Stored Learnings:")
for item in get_all_learnings():
    print("-", item)
