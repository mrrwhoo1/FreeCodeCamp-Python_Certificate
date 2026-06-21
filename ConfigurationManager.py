"""
Build a User Configuration Manager
In this lab, you will build a User Configuration Manager that allows users to manage their settings such as theme, language, and notifications. You will implement functions to add, update, delete, and view user settings.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should define a function named add_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair

add_setting function should:

Convert the key and value to lowercase.
If the key setting exists, return Setting '[key]' already exists! Cannot add a new setting with this name.
If the key setting doesn't exist, add the key-value pair to the given dictionary of settings and return Setting '[key]' added with value '[value]' successfully!.
The messages returned should have the key and value in lowercase.
You should define a function named update_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair.

update_setting function should:

Convert the key and value to lowercase.
If the key setting exists, update its value in the given dictionary of settings and return: Setting '[key]' updated to '[value]' successfully!
If the key setting doesn't exist, return Setting '[key]' does not exist! Cannot update a non-existing setting.
The messages returned should have the key and value in lowercase.
You should define a function named delete_setting with two parameters representing a dictionary of settings and a key.

delete_setting function should:

Convert the key passed to lowercase.
If the key setting exists, remove the key-value pair from the given dictionary of settings and return Setting '[key]' deleted successfully!
If the key setting does not exist, return Setting not found!
The messages returned should have the key in lowercase.
You should define a function named view_settings with one parameter representing a dictionary of settings.

view_settings function should:

Return No settings available. if the given dictionary of settings is empty.
If the dictionary contains any settings, return a string displaying the settings. The string should start with Current User Settings: followed by the key-value pairs, each on a new line and with the key capitalized. For example, view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}) should return:
Current User Settings:
Theme: dark
Notifications: enabled
Volume: high

For testing the code, you should create a dictionary named test_settings to store some user configuration preferences.
"""


def add_setting(settings: dict, settings_pair: tuple):
    lower_dict = {
        str(k).lower() if isinstance(k, str) else str(k): str(v).lower()
        if isinstance(v, str)
        else str(v)
        for k, v in settings.items()
    }

    new_key = str(settings_pair[0]).lower()
    new_value = str(settings_pair[1]).lower()

    if new_key in lower_dict:
        return f"Setting '{new_key}' already exists! Cannot add a new setting with this name."
    else:
        settings[new_key] = new_value
        return f"Setting '{new_key}' added with value '{new_value}' successfully!"

    return lower_dict


test_settings = {}
test_pairs = ("theme", "dark")

result = add_setting(test_settings, test_pairs)

print(result)
print(test_settings)


def update_setting(settings: dict, settings_pair: tuple):

    new_key = str(settings_pair[0]).lower()
    new_value = str(settings_pair[1]).lower()

    if new_key in settings:
        settings[new_key] = new_value
        return f"Setting '{new_key}' updated to '{new_value}' successfully!"
    else:
        return (
            f"Setting '{new_key}' does not exist! Cannot update a non-existing setting."
        )


def delete_setting(settings: dict, key):

    key = str(key).lower()

    if key in settings:
        settings.pop(key, None)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


delete_test_pairs = ("theme", "blue")
delete_result = (test_settings, delete_test_pairs)


def view_settings(settings: dict):
    if not settings:
        return "No settings available."

    output = "Current User Settings:\n"

    for k, v in settings.items():
        output += f"{k.title()}: {v}\n"

    return output
