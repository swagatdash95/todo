import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from . import graphql

from .router import todo

graphql_app = GraphQLRouter(graphql.schema)

app = FastAPI()

app.include_router(todo.router)
app.include_router(graphql_app, prefix="/graphql")


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
