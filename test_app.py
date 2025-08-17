import uuid
from datetime import datetime, timezone
import pytest
from app import server, tasks  # import your Flask app and in-memory tasks list

@pytest.fixture
def client():
    server.config["TESTING"] = True
    with server.test_client() as client:
        yield client

def test_get_tasks_empty(client):
    tasks.clear()
    response = client.get("/todo/tasks")
    assert response.status_code == 200
    assert response.json == {"tasks": []}

def test_post_task(client):
    tasks.clear()
    data = {"task": "Write unit tests"}
    response = client.post("/todo/tasks", json=data)
    assert response.status_code == 201
    assert response.json["task"] == "Write unit tests"
    assert "id" in response.json
    assert "created" in response.json
    assert response.json["completed"] is False

def test_get_task_by_id(client):
    tasks.clear()
    # Add a task with proper datetime
    task = {
        "id": uuid.uuid4(),
        "task": "Read book",
        "created": datetime.now(timezone.utc),
        "completed": False
    }
    tasks.append(task)
    response = client.get(f"/todo/tasks/{task['id']}")
    assert response.status_code == 200
    assert response.json["task"] == "Read book"
    assert response.json["id"] == str(task["id"])  # Marshmallow serializes UUID to string

def test_put_task(client):
    tasks.clear()
    task = {
        "id": uuid.uuid4(),
        "task": "Original",
        "created": datetime.now(timezone.utc),
        "completed": False
    }
    tasks.append(task)
    update_data = {"task": "Updated", "completed": True}
    response = client.put(f"/todo/tasks/{task['id']}", json=update_data)
    assert response.status_code == 200
    assert response.json["task"] == "Updated"
    assert response.json["completed"] is True
    assert response.json["id"] == str(task["id"])

def test_delete_task(client):
    tasks.clear()
    task = {
        "id": uuid.uuid4(),
        "task": "To delete",
        "created": datetime.now(timezone.utc),
        "completed": False
    }
    tasks.append(task)
    response = client.delete(f"/todo/tasks/{task['id']}")
    assert response.status_code == 204
    # Ensure task is removed
    assert all(t["id"] != task["id"] for t in tasks)
