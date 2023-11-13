from database import collection

new_form: list[dict[str,str]] = [
    {
        "name": "Registering a user with a phone number",
        "user_phone": "phone",
        "password": "text",
    },
    {
        "name": "Registering a user with a phone number",
        "user_email": "email",
        "password": "text",
    },
    {
        "name": "Filling out a user profile",
        "username": "text",
        "first_name": "text",
        "last_name": "text",
        "date_of_birth": "date",
        "user_phone": "phone",
        "user_email": "email",
    }
]

result = collection.insert_many(new_form)