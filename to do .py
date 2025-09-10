# 3.	To-Do List Manager: Add, view, and delete tasks from a list (saves to a .txt file)
Task=[]


def menu():
    print("here is menu of your to do list")
    print("1. Add task")
    print("2. view")
    print("3. delete")
    print("3. Mark as done")
    print("5. exit")
def add():
    try:
        task=input("enter the task")
        Task.append({"Task":task,"done":False})
    except:
        print("enter the task name not integer or any")
def view():
    for i,t in enumerate(Task):
        status="✅" if t.get("done") else "❌"
        print(f"{i+1} {status}{t["Task"]}")
def delete():
    view()
    print("choose the task you wanna delete")
    try:
        choice=int(input("enter the task no"))
        Task.pop[choice-1]
    except:
        print("enter  valid no")
def mark():
    view()
    choice=int(input("enter the number you task number you wanna to check its done"))
    Task[choice-1]["done"]==True
while True:
    menu()
    try:

        choice=int(input("enter the no"))
        if choice==1:
            add()
        elif choice==2:
            view()
        elif choice==3:
            delete()
        elif choice==4:
            mark()
        elif choice==5:
            print("good bye")
            break
        
        else:
            print("choose a number shown in menu")
    except:
        print("enter a valid integer")
    
        


