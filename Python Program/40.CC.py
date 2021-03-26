def collect_todos(n):
    todo_list = []
    for i in range(0, n):
        todo = input("Enter a todo: ")
        todo_list.append(todo)
    return todo_list


n = int(input("How many todos would you like to add?\n"))
todos = collect_todos(n)
print(todos)
