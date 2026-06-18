def task():
    tasks = []
    print("-------- WELCOME TO ROHIT TASK MANAGEMENT APP --------")
    total_task = int(input("How many task you want to add : "))
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i} = ").upper()
        tasks.append(task_name)
    print(f"Today's task are :\n{tasks}")
    while True:
        operation = int(input("Enter 1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit  : "))
        if operation == 1:
            add = input("Enter task you want to add : ").upper()
            tasks.append(add)
            print(f"Task {add} has been successfully added .....")
        elif operation == 2:
            update_val = input("Enter the task you want to be update = ").upper()
            if update_val in tasks:
                up = input("Enter new task : ").upper()
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"Updated task {up}")
        elif operation == 3:
            del_val = input("Which task you want to be deleted : ").upper()
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted !!")
        elif operation == 4:
            print(f"Total task = {tasks}")
        elif operation == 5:
            print("GOOD BYE .....!  HAVE A NICE DAY ....... ")
            break
        else:
            print("Invalid choice !!!!")
task()