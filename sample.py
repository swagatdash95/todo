import json

with open("./todo_storage.json", "r+",  encoding="utf-8") as todo_items:
    print("ITEMS:", todo_items)
    todo_list = json.load(todo_items)
    todo_list.append({
        "id": "fb4f9c35-c54f-460f-a779-7f80a118b1cf",
        "name": "Get Grocery",
        "is_done": False
    })
    todo_items.seek(0)
    json.dump(todo_list, todo_items, indent=2)
