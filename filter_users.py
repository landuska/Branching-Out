import json


def load_file():
    """ Load the users file and return it as a dictionary """

    with open("users.json", "r") as file:
        users = json.load(file)
        return users


def filter_users_by_key(key, value):
    """ Filter users by a given key and value """

    users = load_file()

    for user in users:
        if isinstance(user[f"{key}"], str):
            user[key] = user[f"{key}"].lower()

    filtered_users = [user for user in users if user[key] == value]

    for user in filtered_users:
        print(user)


def main():
    filter_option = input("What would you like to filter by? ('name', 'age' or 'email'): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").lower().strip()
        filter_users_by_key("name", name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: ").strip())
        filter_users_by_key("age", age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").lower().strip()
        filter_users_by_key("email", email_to_search)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
