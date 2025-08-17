from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")  
db = client["crud_demo"]              # Database name
collection = db["users"]              # Collection (like a table)

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("MongoDB CRUD with Tkinter")
root.geometry("500x400")

tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Id").grid(row=1, column=0, padx=10, pady=5)

name_entry = tk.Entry(root)
age_entry = tk.Entry(root)

name_entry.grid(row=0, column=1, padx=10, pady=5)
age_entry.grid(row=1, column=1, padx=10, pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.grid(row=6, column=0, columnspan=2, pady=10)

def insert_record():
    name = name_entry.get()
    Id = Id_entry.get()
    if name and age:
        collection.insert_one({"name": name, "id": int(Id)})
        messagebox.showinfo("Success", "Record Inserted")
        show_records()
    else:
        messagebox.showwarning("Input Error", "Enter both Name and Id")

def show_records():
    listbox.delete(0, tk.END)
    for doc in collection.find():
        listbox.insert(tk.END, f"{doc['_id']} | {doc['name']} | {doc['Id']}")

def delete_record():
    selected = listbox.curselection()
    if selected:
        record = listbox.get(selected[0])
        record_id = record.split("|")[0].strip()
        collection.delete_one({"_id": eval(record_id)})
        messagebox.showinfo("Deleted", "Record Deleted")
        show_records()
    else:
        messagebox.showwarning("Select Error", "Select a record to delete")

def update_record():
    selected = listbox.curselection()
    if selected:
        record = listbox.get(selected[0])
        record_id = record.split("|")[0].strip()
        name = name_entry.get()
        Id = Id_entry.get()
        if name and Id:
            collection.update_one(
                {"_id": eval(record_id)},
                {"$set": {"name": name, "Id": int(Id)}}
            )
            messagebox.showinfo("Updated", "Record Updated")
            show_records()
        else:
            messagebox.showwarning("Input Error", "Enter both Name and Age")

tk.Button(root, text="Insert", command=insert_record).grid(row=2, column=0, pady=10)
tk.Button(root, text="Update", command=update_record).grid(row=2, column=1, pady=10)
tk.Button(root, text="Delete", command=delete_record).grid(row=3, column=0, pady=10)
tk.Button(root, text="Show Records", command=show_records).grid(row=3, column=1, pady=10)

show_records()
root.mainloop()
