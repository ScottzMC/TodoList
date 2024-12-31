# main.py
from menu import display_menu, handle_choice

def main():
    """
    Main function to handle the user input.
    """
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        if not handle_choice(choice):
            break

# Run the application
if __name__ == "__main__":
    main()
