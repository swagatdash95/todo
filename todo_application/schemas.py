import json
import uuid
from typing import Dict, Union, List

from config import settings
from pydantic import UUID4, BaseModel, Field


class Todo(BaseModel):
    """Model structure of a Todo Item"""
    todo_id: UUID4 = Field(default_factory=uuid.uuid4)
    name: str
    description: str = ""
    is_done: bool = False


class Todos(BaseModel):
    """Model for a List of Todo Items"""
    items: Dict[str, Todo]  # Dict[str, Todo] Change List to Dict so that you don't have to loop

    @staticmethod
    def fetch(todo_id: UUID4) -> Union[Todo, None]:
        """This method fetches a specific Todo Item with its ID"""
        todos = Todos.parse_file(settings.storage_path)
        if str(todo_id) in todos.items:
            return todos.items[str(todo_id)]

        return None

    @staticmethod
    def fetch_all() -> Dict[str, Todo]:
        """This method fetches a specific Todo Item with its ID"""
        todos = Todos.parse_file(settings.storage_path)

        return todos.items

    @staticmethod
    def add(item: Todo) -> Todo:
        """This method adds an entry to the existing todo list"""

        todos = Todos.parse_file(settings.storage_path)
        with open(settings.storage_path, "w+",  encoding="utf-8") as todo_items:
            # todos.items[str(uuid.uuid4())] = item
            todos.items[str(item.todo_id)] = item
            todo_items.write(todos.json())
        return item

    @staticmethod
    # Have methods type annotated
    def delete(todo_id: UUID4) -> Union[Todo, None]:
        """This method deletes an entry from the existing todo list"""
        todos = Todos.parse_file(settings.storage_path)
        item_deleted = todos.items.pop(str(todo_id), None)

        if item_deleted:
            with open(settings.storage_path, "w", encoding="utf-8") as todo_items:
                todo_items.write(todos.json())
        return item_deleted  # return deleted one

    @staticmethod
    def check(todo_id: UUID4) -> Union[Todo, None]:
        """This method toggles an entry from the existing todo list between checked/unchecked"""
        is_updated = False
        todos = Todos.parse_file(settings.storage_path)

        if str(todo_id) in todos.items:
            todos.items[str(todo_id)].is_done = not todos.items[str(
                todo_id)].is_done
            updated_item = todos.items[str(todo_id)]
            is_updated = True

        if is_updated:
            with open(settings.storage_path, "w", encoding="utf-8") as todo_items:
                todo_items.write(todos.json())
            return updated_item

        return None  # Return updated item

# Use snake case
# ItemName -> Name
# ReqTodo -> Todo
# Todos model - List[Todo]
# Todos.parse_file() - parse the file and give JSON
# static methods (write, add, Delete) in Todos to write todo items to file using json()
# USe UUI4 type for ID of Todo
# pytest test cases - later


# Check Pathlib for settings
