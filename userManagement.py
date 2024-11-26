import tkinter as tk
from tkinter import messagebox

# Classes for User and Group
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"

class Group:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, user):
        self.members.append(user)

    def display_members(self):
        if not self.members:
            return "No members in this group."
        return "\n".join(str(member) for member in self.members)

# Global data storage
users = []
groups = []

# Functions for GUI actions
def create_user():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()

    if not name or not email or not password:
        messagebox.showerror("Error", "All fields are required.")
        return

    users.append(User(name, email, password))
    messagebox.showinfo("Success", "User created successfully!")
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)

def create_group():
    group_name = entry_group_name.get()
    if not group_name:
        messagebox.showerror("Error", "Group name is required.")
        return

    groups.append(Group(group_name))
    messagebox.showinfo("Success", "Group created successfully!")
    entry_group_name.delete(0, tk.END)

def add_user_to_group():
    group_name = entry_group_for_user.get()
    user_name = entry_user_for_group.get()

    group = next((grp for grp in groups if grp.name == group_name), None)
    user = next((usr for usr in users if usr.name == user_name), None)

    if not group:
        messagebox.showerror("Error", "Group not found.")
        return
    if not user:
        messagebox.showerror("Error", "User not found.")
        return

    group.add_member(user)
    messagebox.showinfo("Success", f"User '{user.name}' added to group '{group.name}'.")

def list_users():
    if not users:
        messagebox.showinfo("Users", "No users available.")
        return
    user_list = "\n".join(str(user) for user in users)
    messagebox.showinfo("Users", user_list)

def list_groups():
    if not groups:
        messagebox.showinfo("Groups", "No groups available.")
        return
    group_list = "\n".join(f"{group.name} ({len(group.members)} members)" for group in groups)
    messagebox.showinfo("Groups", group_list)

def display_group_members():
    group_name = entry_display_group_members.get()
    group = next((grp for grp in groups if grp.name == group_name), None)

    if not group:
        messagebox.showerror("Error", "Group not found.")
        return

    members = group.display_members()
    messagebox.showinfo(f"Members of {group.name}", members)

# Create GUI
root = tk.Tk()
root.title("User and Group Management System")

# User creation frame
frame_user = tk.LabelFrame(root, text="Create User")
frame_user.pack(fill="both", padx=10, pady=10)

tk.Label(frame_user, text="Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_user)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_user, text="Email:").grid(row=1, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_user)
entry_email.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_user, text="Password:").grid(row=2, column=0, padx=5, pady=5)
entry_password = tk.Entry(frame_user, show="*")
entry_password.grid(row=2, column=1, padx=5, pady=5)

tk.Button(frame_user, text="Create User", command=create_user).grid(row=3, column=0, columnspan=2, pady=10)

# Group creation frame
frame_group = tk.LabelFrame(root, text="Create Group")
frame_group.pack(fill="both", padx=10, pady=10)

tk.Label(frame_group, text="Group Name:").grid(row=0, column=0, padx=5, pady=5)
entry_group_name = tk.Entry(frame_group)
entry_group_name.grid(row=0, column=1, padx=5, pady=5)

tk.Button(frame_group, text="Create Group", command=create_group).grid(row=1, column=0, columnspan=2, pady=10)

# Add user to group frame
frame_add_to_group = tk.LabelFrame(root, text="Add User to Group")
frame_add_to_group.pack(fill="both", padx=10, pady=10)

tk.Label(frame_add_to_group, text="Group Name:").grid(row=0, column=0, padx=5, pady=5)
entry_group_for_user = tk.Entry(frame_add_to_group)
entry_group_for_user.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_add_to_group, text="User Name:").grid(row=1, column=0, padx=5, pady=5)
entry_user_for_group = tk.Entry(frame_add_to_group)
entry_user_for_group.grid(row=1, column=1, padx=5, pady=5)

tk.Button(frame_add_to_group, text="Add User to Group", command=add_user_to_group).grid(row=2, column=0, columnspan=2, pady=10)

# Display and list frame
frame_display = tk.LabelFrame(root, text="Display Information")
frame_display.pack(fill="both", padx=10, pady=10)

tk.Button(frame_display, text="List Users", command=list_users).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_display, text="List Groups", command=list_groups).grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_display, text="Group Name:").grid(row=1, column=0, padx=5, pady=5)
entry_display_group_members = tk.Entry(frame_display)
entry_display_group_members.grid(row=1, column=1, padx=5, pady=5)

tk.Button(frame_display, text="Display Group Members", command=display_group_members).grid(row=2, column=0, columnspan=2, pady=10)

# Run the GUI loop
root.mainloop()
