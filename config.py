from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """This class inhertis Pydantic's BaseSettings class to create config values for the app"""
    storage_path: str = Field(default="./todo_storage.json",
                              env="TODO_STORAGE_PATH")
    graphql_storage_path: str = Field(
        default="./graphql_todo_storage.json", env="GRAPHQL_TODO_STORAGE_PATH")


settings = Settings()
