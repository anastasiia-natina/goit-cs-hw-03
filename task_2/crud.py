from pymongo import MongoClient
from bson.objectid import ObjectId
import traceback

# Підключення до локальної MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['cat_database']
collection = db['cats']

def create_cat(name, age, features):
    try:
        cat = {
            "name": name,
            "age": age,
            "features": features
        }
        result = collection.insert_one(cat)
        print(f"Cat inserted with id: {result.inserted_id}")
    except Exception as e:
        print("An error occurred while creating a cat:", e)
        traceback.print_exc()

def read_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print("An error occurred while reading all cats:", e)
        traceback.print_exc()

def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"No cat found with name: {name}")
    except Exception as e:
        print("An error occurred while reading the cat:", e)
        traceback.print_exc()

def update_cat_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count > 0:
            print(f"Updated age of cat with name {name} to {new_age}")
        else:
            print(f"No cat found with name: {name}")
    except Exception as e:
        print("An error occurred while updating the cat's age:", e)
        traceback.print_exc()

def add_feature_to_cat(name, new_feature):
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        if result.matched_count > 0:
            print(f"Added feature '{new_feature}' to cat with name {name}")
        else:
            print(f"No cat found with name: {name}")
    except Exception as e:
        print("An error occurred while adding a feature to the cat:", e)
        traceback.print_exc()

def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Deleted cat with name {name}")
        else:
            print(f"No cat found with name: {name}")
    except Exception as e:
        print("An error occurred while deleting the cat:", e)
        traceback.print_exc()

def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"Deleted {result.deleted_count} cats")
    except Exception as e:
        print("An error occurred while deleting all cats:", e)
        traceback.print_exc()

if __name__ == "__main__":
    while True:
        print("\n1. Create cat")
        print("2. Read all cats")
        print("3. Read cat by name")
        print("4. Update cat's age by name")
        print("5. Add feature to cat by name")
        print("6. Delete cat by name")
        print("7. Delete all cats")
        print("8. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter cat's name: ")
            age = int(input("Enter cat's age: "))
            features = input("Enter cat's features (comma separated): ").split(", ")
            create_cat(name, age, features)
        elif choice == '2':
            read_all_cats()
        elif choice == '3':
            name = input("Enter cat's name: ")
            read_cat_by_name(name)
        elif choice == '4':
            name = input("Enter cat's name: ")
            new_age = int(input("Enter new age: "))
            update_cat_age(name, new_age)
        elif choice == '5':
            name = input("Enter cat's name: ")
            new_feature = input("Enter new feature: ")
            add_feature_to_cat(name, new_feature)
        elif choice == '6':
            name = input("Enter cat's name: ")
            delete_cat_by_name(name)
        elif choice == '7':
            delete_all_cats()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")