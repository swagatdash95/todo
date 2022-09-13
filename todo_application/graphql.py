import json
import typing
import uuid
from pydantic import UUID4

import strawberry
from config import settings

from . import schemas


@strawberry.type
class Todo:
    """Model structure of a Todo Item"""
    todo_id: strawberry.ID  # UUID4 = Field(default_factory=uuid.uuid4)
    name: str = "Default Name"
    description: str = ""
    is_done: bool = False


@strawberry.type
class Todos:
    """Model for a List of Todo Items"""
    items: typing.List[Todo]


@strawberry.type
class Query:
    """Query for Strawberry Schema"""

    @strawberry.field
    def todo(self, todo_id: uuid.UUID) -> typing.Union[Todo, None]:
        """Resolver for todo"""

        item = schemas.Todos.fetch(todo_id)

        if item is None:
            return None

        return Todo(todo_id=str(item.todo_id), name=item.name, description=item.description, is_done=item.is_done)

    @strawberry.field
    def todos(self) -> typing.List[Todo]:
        """Resolver to get all Todos"""

        items = schemas.Todos.fetch_all()
        return [Todo(
            todo_id=value.todo_id,
            name=value.name,
            description=value.description,
            is_done=value.is_done
        ) for key, value in items.items()]


@strawberry.type
class Mutation:
    """Mutation class for the strawberry schema"""
    @strawberry.mutation
    def add_todo(self, name: str, description: typing.Optional[str] = "", is_done: typing.Optional[bool] = False) -> typing.Union[Todo, None]:
        """Add a new todo item"""
        item = schemas.Todos.add(schemas.Todo(todo_id=uuid.uuid4(), name=name,
                                              description=description, is_done=is_done))

        return Todo(todo_id=item.todo_id, name=item.name,
                    description=item.description, is_done=item.is_done)

    @strawberry.mutation
    def check_todo(self, todo_id: uuid.UUID) -> typing.Union[Todo, None]:
        """This method toggles an entry from the existing todo list between checked/unchecked"""
        item = schemas.Todos.check(todo_id)
        if item:
            return item

        return None


schema = strawberry.Schema(query=Query, mutation=Mutation)


# check strwberry mypy
# move graphql.py up a level
# rename schemas to models
# relay.dev - JS Graphql client
