import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017/')

db = client['cats_db']
collection = db['cats']

def create_cat(name, age, features):
    try:
        cat = {
            "name": name,
            "age": age,
            "features": features
        }
        collection.insert_one(cat)
        print(f"Кіт {name} доданий до бази даних.")
    except Exception as e:
        print(f"Помилка при додаванні кота: {e}")

def read_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Помилка при читанні котів: {e}")

def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кіт з ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка при пошуку кота: {e}")

def update_cat_age(name, age):
    try:
        result = collection.update_one({"name": name}, {"set": {"age": age}})
        if result.matched_count > 0:
            print(f"Вік кота {name} оновлено до {age}.")
        else:
            print(f"Кіт з ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка при оновленні віку кота: {e}")

def add_feature_to_cat(name, feature):
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": feature}})
        if result.matched_count > 0:
            print(f"Характеристика '{feature}' додана до кота {name}.")
        else:
            print(f"Кіт з ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка при додаванні характеристики до кота: {e}")

def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кіт з ім'ям {name} видалений.")
        else:
            print(f"Кіт з ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка при видаленні кота: {e}")

def delete_all_cats():
    try:
        collection.delete_many({})
        print("Всі коти видалені з бази даних.")
    except Exception as e:
        print(f"Помилка при видаленні всіх котів: {e}")

if __name__ == "__main__":
    create_cat("Barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    read_all_cats()
    read_cat_by_name("Barsik")
    update_cat_age("Barsik", 4)
    add_feature_to_cat("Barsik", "грає з м'ячем")
    delete_cat_by_name("Barsik")
    delete_all_cats()