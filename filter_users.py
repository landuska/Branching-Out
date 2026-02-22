import json


def load_file():
    with open("users.json", "r") as file:
        users = json.load(file)
        return users


def filter_users_by_key(key, value):
    users = load_file()

    for user in users:
        if isinstance(user[f"{key}"], str):
            user[f"{key}"] = user[f"{key}"].lower()

    filtered_users = [user for user in users if user[f"{key}"] == value]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? ('name' or 'age'): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").lower().strip()
        filter_users_by_key("name", name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: ").strip())
        filter_users_by_key("age", age_to_search)
    else:
        print("Filtering by that option is not yet supported.")
