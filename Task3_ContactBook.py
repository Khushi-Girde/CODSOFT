import json, os

BOOK="contacts.json"

def load():
    return json.load(open(BOOK)) if os.path.exists(BOOK) else []

def save(data):
    with open(BOOK,"w") as f: json.dump(data,f,indent=2)

def show(contacts):
    print("\n--- CONTACTS ---")
    for c in contacts:
        print(f"{c['name']} | {c['phone']} | {c['email']} | {c['address']}")

def add(contacts):
    name=input("Name: "); phone=input("Phone: "); email=input("Email: "); addr=input("Address: ")
    contacts.append({"name":name,"phone":phone,"email":email,"address":addr})
    save(contacts); print("✅ Added")

def search(contacts):
    key=input("Search by name/phone: ")
    for c in contacts:
        if key in (c["name"],c["phone"]): print("Found:",c); return
    print("❌ Not found")

def update(contacts):
    key=input("Name to update: ")
    for c in contacts:
        if c["name"]==key:
            c["phone"]=input("New phone: ")
            c["email"]=input("New email: ")
            c["address"]=input("New address: ")
            save(contacts); print("✅ Updated"); return
    print("❌ Not found")

def delete(contacts):
    key=input("Name to delete: ")
    new=[c for c in contacts if c["name"]!=key]
    if len(new)==len(contacts): print("❌ Not found")
    else: save(new); print("🗑️ Deleted")

def main():
    while True:
        contacts=load()
        print("\n1=Add 2=Show 3=Search 4=Update 5=Delete 6=Exit")
        c=input("Choice: ")
        if c=="1": add(contacts)
        elif c=="2": show(contacts)
        elif c=="3": search(contacts)
        elif c=="4": update(contacts)
        elif c=="5": delete(contacts)
        elif c=="6": break
        else: print("❌ Wrong choice")

if __name__=="__main__":
    main()
