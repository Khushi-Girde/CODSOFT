import json, os

FILE = "mytasks.json"

def load():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save(data):
    with open(FILE, "w") as f: json.dump(data, f, indent=2)

def show(tasks):
    print("\n=== Your Tasks ===")
    if not tasks:
        print("No tasks yet!")
    for t in tasks:
        mark = "[✔]" if t["done"] else "[ ]"
        print(f"{t['id']:02d} {mark} {t['title']}")

def add(tasks):
    title = input("New task: ")
    if not title.strip(): return print("❌ Empty title")
    nid = max([t["id"] for t in tasks], default=0) + 1
    tasks.append({"id": nid, "title": title, "done": False})
    save(tasks)
    print("✅ Added")

def done(tasks):
    tid = int(input("Which ID completed? "))
    for t in tasks:
        if t["id"] == tid: t["done"]=True; save(tasks); print("🎉 Done!"); return
    print("❌ Not found")

def delete(tasks):
    tid = int(input("Which ID to delete? "))
    newlist=[t for t in tasks if t["id"]!=tid]
    if len(newlist)==len(tasks): print("❌ Not found")
    else: save(newlist); print("🗑️ Deleted")

def main():
    while True:
        tasks = load()
        print("\n1=Add  2=List  3=Mark Done  4=Delete  5=Exit")
        choice=input("Choose: ")
        if choice=="1": add(tasks)
        elif choice=="2": show(tasks)
        elif choice=="3": done(tasks)
        elif choice=="4": delete(tasks)
        elif choice=="5": break
        else: print("❌ Wrong choice")

if __name__=="__main__":
    main()

