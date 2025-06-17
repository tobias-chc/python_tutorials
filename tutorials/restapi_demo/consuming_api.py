import requests
import json

API_URL = "https://jsonplaceholder.typicode.com/todos"


def get_example(id: int = 10):
    response = requests.get(f"{API_URL}/{id}")
    print(f"response.json(): {response.json()}")
    print(f"response.status_code: {response.status_code}")
    print(f"response.headers['Content-Type']: {response.headers['Content-Type']}")


def post_example():
    todo = {"userId": 1, "title": "Buy fairy", "completed": False}

    print("-- Example 1 --")
    response = requests.post(API_URL, json=todo)
    print(f"response.json(): {response.json()}")
    print(f"response.status_code: {response.status_code}")

    print("-- Example 2 --")
    headers = {"Content-Type": "application/json"}
    response = requests.post(API_URL, data=json.dumps(todo), headers=headers)
    print(f"response.json(): {response.json()}")
    print(f"response.status_code: {response.status_code}")


def put_example(id: int = 10):
    api_url = f"{API_URL}/{id}"
    response = requests.get(api_url)
    print(f"response.json(): {response.json()}")

    todo = {"userId": 1, "title": "Buy milk", "completed": False}
    response = requests.put(api_url, json=todo)
    print(f"updated response.json(): {response.json()}")
    print(f"response.status_code: {response.status_code}")


def patch_example(id: int = 10):
    # Used for partial modifications
    api_url = f"{API_URL}/{id}"
    todo = {"title": "Mow lawn"}
    response = requests.patch(api_url, json=todo)
    print(f"updated response.json(): {response.json()}")
    print(f"response.status_code: {response.status_code}")


def delete_example(id: int = 10):
    # empty json expected
    api_url = f"{API_URL}/{id}"
    response = requests.delete(api_url)
    print(f"updated response.json(): {response.json()}")
    print(f"response.status_code: {response.status_code}")


if "__main__" == __name__:
    print("-- GET method --\n")
    get_example()

    print("\n-- POST method --\n")
    post_example()

    print("\n-- PUT method --\n")
    put_example()

    print("\n-- PATCH method --\n")
    patch_example()

    print("\n-- DELETE method --\n")
    delete_example()
