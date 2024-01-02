todo_list =[]
    
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Quit")
        
    choice = input("Enter your choice: ")
        
    if choice == '1':
        task = input("Enter the task: ")
        todo_list.append(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        todo_list.remove(task)
    elif choice == '3':
        print(todo_list)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


