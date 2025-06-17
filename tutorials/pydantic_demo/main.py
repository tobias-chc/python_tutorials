import os
import json
from datetime import date, timedelta
from tutorials.pydantic_demo.models import Employee
from tutorials.pydantic_demo.validate_call import send_invoice
from tutorials.pydantic_demo.settings_management import AppConfig


def models_example():
    # EXAMPLE 1: Object instantiation using explicit values
    test_employee = Employee(
        name="Tobias",
        email="tobias@pydantic.com",
        date_of_birth="1995-12-02",
        salary=1000,
        department="IT",
        elected_benefits=False,
    )

    print(f"Created Employee: {test_employee}\n")

    # EXAMPLE 2: Object instantiation from dict
    employee_as_dict = {
        "name": "Tobias",
        "email": "tobias@pydantic.com",
        "date_of_birth": "1995-12-02",
        "salary": 1000,
        "department": "IT",
        "elected_benefits": False,
    }
    employee_from_dict = Employee.model_validate(employee_as_dict)
    print(f"Created Employee: {employee_from_dict}\n")

    # EXAMPLE 3: Go from object to dict represantation
    ## Serialize the object to JSON string
    json_string = employee_from_dict.model_dump_json()
    ## Deserialize the JSON string back into a dictionary:
    employee_dump_dict = json.loads(json_string)
    ## Remove the 'employee_id' key from the dictionary
    employee_dump_dict.pop("employee_id")

    print(f"Is the dict dump method ok: {employee_dump_dict == employee_as_dict}", "\n")


def fields_example():
    # EXAMPLE 1: Incorrect data
    print("--- EXAMPLE 1: Incorrect data ---")
    incorrect_employee_data = {
        "name": "",
        "email": "tobias@pydantik.com",
        "birth_date": "1995-12-02",
        "salary": -10,
        "department": "IT",
        "elected_benefits": True,
    }

    try:
        Employee.model_validate(incorrect_employee_data)
    except Exception as e:
        print(f"Error: {e}\n")

    # EXAMPLE 2: Correct data
    print("\n--- EXAMPLE 2: Correct Data ---")
    employee_data = {
        "name": "Tobias",
        "email": "tobias@pydantic.com",
        "birth_date": "1995-12-02",
        "salary": 1000,
        "department": "ENGINEERING",
        "elected_benefits": True,
    }

    test_employee = Employee.model_validate(employee_data)
    print(f"Created Employee: {test_employee}\n")

    # EXAMPLE 2.1: Getting `repr=False` values
    print("--- EXAMPLE 2.1: Getting `repr=False` values ---")
    print(f"Getting DoB value: {test_employee.date_of_birth}")
    print(f"Getting salary value: {test_employee.salary}\n")

    # EXAMPLE 2.2: Updating `frozen=True` values
    print("--- EXAMPLE 2.2: Updating `frozen=True` values ---")
    try:
        test_employee.name = "Jesus"
    except Exception as e:
        print(f"Error: {e}\n")


def field_validator_example():
    print("--- EXAMPLE 1: Young employee ---")
    young_employee_data = {
        "name": "Emily",
        "email": "emily@pydantic.com",
        "birth_date": date.today() - timedelta(days=365 * 17),
        "salary": 1000,
        "department": "ENGINEERING",
        "elected_benefits": True,
    }
    try:
        Employee.model_validate(young_employee_data)
    except Exception as e:
        print(f"Error: {e}\n")


def model_validator_example():
    print("--- EXAMPLE 1: IT employee ---")
    it_employee_data = {
        "name": "Tobias",
        "email": "tobias@pydantic.com",
        "birth_date": "1995-12-03",
        "salary": 1000,
        "department": "IT",
        "elected_benefits": True,
    }
    try:
        Employee.model_validate(it_employee_data)
    except Exception as e:
        print(f"Error: {e}\n")


def validate_call_example():
    print("\n--- EXAMPLE 1: Wrong data ---")
    try:
        send_invoice(
            client_name="",
            client_email="lasdfakedomain.com",
            items_purchased=["pie", 13],
            amount_owed=0,
        )
    except Exception as e:
        print(f"Error: {e}\n")
    print("\n--- EXAMPLE 2: Correct Data ---")
    email_str = send_invoice(
        client_name="Skinny Pete",
        client_email="skinnyp@fakedomain.com",
        items_purchased=["pie", "iphone"],
        amount_owed=1300.0,
    )
    print(f"Created email: {email_str}\n")


def settings_management_example():
    # Define your environment variables here (replace with your actual values)
    env_vars = {
        "database_host": "http://localhost:5432",  # Example URL
        "database_user": "admin",
        "database_password": "password123",
        "api_key": "FAKEEMKDIV2424545JSFIDSINF34369",
    }
    # Set the validated variables as environment variables
    for key, value in env_vars.items():
        os.environ[key] = value

    print(f"Created AppConfig: {AppConfig()}\n")


if __name__ == "__main__":
    # Creating models from: explict values, dict
    models_example()

    # Using field validation
    fields_example()

    print("--- EXAMPLES: `field_validators ---")
    # Using `field_validators`
    field_validator_example()

    print("--- EXAMPLES: `model_validator ---")
    # Using `model_validator`
    model_validator_example()

    print("--- EXAMPLES: `validate_call` ---")
    # Using 'validate_call'
    validate_call_example()

    # Using 'pydantic_settings'
    print("--- EXAMPLES: Settings Management ---")
    settings_management_example()
