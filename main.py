from pymongo import MongoClient, errors


try:
    cluster = MongoClient("mongodb+srv://leonid200955:4AxJcfAlABT8lmYs@cluster0.az2mc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = cluster["Test1"]
    collection = db["users"]

except errors.ConnectionError as e:
    print(f"Connection error {e}")
    exit()



def add_user(name, age, email):
    user = {
        "name": name,
        "age": age,
        "email": email
    }
    try:
        collection.insert_one(user)
        print(f"User {name} was added to collection users")
    except errors.PyMongoError as e:
        print(f"Error while adding user {e}")
    

def find_user(name):
    try:
        user = collection.find_one({"name": name})
        if user:
            print(f"Finded user \nName - {user.get("name")}\nAge - {user.get("age")}\nEmail - {user.get("email")}")
        else:
            print(f"User with name {name} not found")
    except errors.PyMongoError as e:
        print(f"Error while finding user {e}")

def update_user(name, data):
    try:
        result = collection.update_one({"name": name}, {"$set": data})
        if result.modified_count > 0:
            print(f"Information about user {name} was updated")
        else:
            print(f"User with name {name} not found")
    except errors.PyMongoError as e:
        print(f"Error while deleting user {e}")


def delete_user(name):
    try: 
        result = collection.delete_one({"name": name})

        if result.deleted_count > 0:
            print(f"User {name} was deleted")
        else:
            print(f"User {name} not found")
            
    except errors.PyMongoError as e:
        print(f"Error while deleting {e}")


if __name__ == "__main__":
    while True:
        print("Menu\n1 - Add user\n2 - Find user\n3 - Update user data\n4 - Delete user\n5 - Quit")

        option = int(input("Enter > "))

        match option:

            case 1:
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                email = input("Enter email: ")
                add_user(name, age, email)
            case 2:
                name = input("Enter name: ")
                find_user(name)
            case 3:
                name = input("Enter username for updating: ")
                age = int(input("Enter age: "))
                email = input("Enter email: ")
                update_user(name, {"age": age, "email" : email})
            
            case 4:
                name = input("Enter username to deleting: ")
                delete_user(name)

            case 5:
                print("Exit!")
                break

            case _:
                print("Invalid option")
                