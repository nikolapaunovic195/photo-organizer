import json

def load_folder_data():
    print("Loading data from folder_config.json...")
    # Check if folder_config.json file exists
    try:
        with open('folder_config.json', 'r') as file:
            data = json.load(file)
            print("Data loaded successfully!")
    except FileNotFoundError:
        print("folder_config.json not found. Starting configuration in first run mode...")
        data = {}
    
    return data

def main():
    folder_data = load_folder_data()

    print("""
        WARNING: The current version of the photo organizer requires the pillow library to be installed.
        If you haven't installed it yet, please run the following command in your terminal: 'pip install pillow'
        If you have already installed it, you can skip this step.

          """)
    
    print("Welcome to the photo organizer setup!")
    print("INFO: All paths entered must be absolute paths without quotes. Categories are NOT case sensitive and will be saved as upper-case.")
    
    if not folder_data:
        print("No folders are currently setup.")

    
    choice = "X"

    while choice.upper() != "Q" and choice.upper() != "S":
        print("""
        What would you like to do?
        1. Add a folder
        2. Remove a folder
        3. View current folders
        S. Save and exit
        Q. Quit without saving
        """)

        choice = input("Enter your choice: ")
        
        # Add a folder
        if choice == "1":
            folder_category = input("Enter the category of the folder: ").upper()
            folder_name = input("Enter the name of the folder: ")
            folder_path = input("Enter the path of the folder: ")

            if folder_category not in folder_data:
                folder_data[folder_category] = {}
            
            folder_data[folder_category][folder_name] = {"path": folder_path}
            print("Folder added successfully!")

        # Remove a folder
        elif choice == "2":
            folder_category = input("Enter the category of the folder: ").upper()
            folder_name = input("Enter the name of the folder: ")

            if folder_category in folder_data:
                if folder_name in folder_data[folder_category]:
                    del folder_data[folder_category][folder_name]
                    print("Folder removed successfully!")
                    # Remove category if no folders are left
                    if not folder_data[folder_category]:
                        del folder_data[folder_category]
                else:
                    print("Folder not found.")
            else:
                print("Category not found.")

        # View current folders
        elif choice == "3":
            print("The following folder structure was found in the config file:")
            for key, value in folder_data.items():
                print(f"Category: {key}")
                for folder, path in value.items():
                    print(f"    {folder}: {path['path']}")

        # Save and exit
        elif choice.upper() == "S":
            with open('folder_config.json', 'w') as file:
                json.dump(folder_data, file)
            print("Data saved successfully!")

        # Quit without saving
        elif choice.upper() == "Q":
            print("Exiting without saving...")

        # Invalid choice
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()