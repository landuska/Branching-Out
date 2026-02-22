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
        if isinstance(user[key], str):
            user[key] = user[f"{key}"].lower()

    filtered_users = [user for user in users if user[key] == value]

    for user in filtered_users:
        print(user)


def is_input_correct(user_input):
    """ Validate the user input and return True, if input correct """

    if not user_input:
        print("Please enter a valid value")
        return False
    return True


def user_choice():
    while True:
        filter_option = input("What would you like to filter by? ('name', 'age' or 'email'): ").strip().lower()

        if not is_input_correct(filter_option):
            continue

        if filter_option == "name":
            name_to_search = input("Enter a name to filter users: ").lower().strip()

            if not is_input_correct(name_to_search):
                continue

            filter_users_by_key("name", name_to_search)

        elif filter_option == "age":
            try:
                age_to_search = int(input("Enter an age to filter users: ").strip())
            except ValueError:
                print("Please enter a valid number")
                continue

            if not is_input_correct(age_to_search):
                continue

            filter_users_by_key("age", age_to_search)

        elif filter_option == "email":
            email_to_search = input("Enter an email to filter users: ").lower().strip()

            if not is_input_correct(email_to_search):
                continue

            if "@" not in email_to_search or "." not in email_to_search:
                print("Please enter a valid email address")
                continue

            filter_users_by_key("email", email_to_search)
        else:
            print("Filtering by that option is not yet supported.")


def main():
    user_choice()


if __name__ == "__main__":
    main()
