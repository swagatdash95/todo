from fastapi import APIRouter, status, Response
from pydantic import UUID4

from .. import schemas

router = APIRouter()


@router.get('/', tags=["Todo"])
def index():
    """Base Path"""
    return {'data': {'title': 'to-do application'}}


# Get specific ID
@router.get('/todo', tags=["Todo"])
def fetch(todo_id: UUID4, response: Response):
    """API to fetch a particular Todo Item with ID"""
    result = schemas.Todos.fetch(todo_id)
    if result:
        return result
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"details": "ID not Found"}


# rest end points should be location of resources
@router.post('/todo', tags=["Todo"])
def create(request: schemas.Todo, response: Response):
    """API to create a Todo Item"""
    result = schemas.Todos.add(request)
    if result:
        return request
    else:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {"details": "Couldn't add"}


# path param for resource and query params for filtering
@router.delete('/todo/{todo_id}', tags=["Todo"])
def delete(todo_id: UUID4, response: Response):
    """API to delete a Todo Item"""
    result = schemas.Todos.delete(todo_id)
    if result:
        return result.json()
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"details": "ID not found"}


@router.put('/todo/{todo_id}/check', tags=["Todo"])
def mark_checked(todo_id: UUID4, response: Response):
    """API to delete a Todo Item"""
    result = schemas.Todos.check(todo_id)
    if result:
        return result.json()
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"details": "ID not found"}
# use double quotes
