import tkinter as tk
from tkinter import ttk

def update_option_menu(menu, options):
    # Clear existing options
    menu['menu'].delete(0, 'end')
    # Add new options
    for option in options:
        menu['menu'].add_command(label=option, command=tk._setit(menu._tkvar, option))

def main():
    root = tk.Tk()

    # Sample dictionary with 'None' and other values
    my_dict = {"Option 1": 1, "Option 2": 2, "None": None, "Option 3": 3}

    # Extract options excluding 'None'
    options = [key for key in my_dict if key != "None"]

    # Variable to hold the selected option
    selected_option = tk.StringVar(root)
    selected_option.set("Option 1")  # Default selection

    # Create the OptionMenu widget
    option_menu = ttk.OptionMenu(root, selected_option, *options)
    option_menu.pack()

    # Function to update the OptionMenu with new options
    def update_options():
        # Update options excluding 'None'
        updated_options = [key for key in my_dict if key != "None"]
        update_option_menu(option_menu, updated_options)

    # Button to trigger updating options
    update_button = tk.Button(root, text="Update Options", command=update_options)
    update_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
