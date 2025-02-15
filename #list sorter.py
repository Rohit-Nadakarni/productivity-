#list sorter 
# Taking tasks as input
task1 = str(input("Enter your 1st task: "))
task2 = str(input("Enter your 2nd task: "))
task3 = str(input("Enter your 3rd task: "))
task4 = str(input("Enter your 4th task: "))
task5 = str(input("Enter your 5th task: "))
task6 = str(input("Enter your 6th task: "))

# Lists to categorize tasks
urgent = list()
important = list()
not_urgent_but_important = list()
not_urgent_nor_important = list()

# Function to categorize tasks
def categorize_task(task):
    task_cat = int(input(f"Enter the category for '{task}' (1-4):\n"
                         "1. Urgent and Important (Do Now)\n"
                         "2. Not Urgent but Important (Schedule)\n"
                         "3. Urgent but Not Important (Delegate)\n"
                         "4. Not Urgent and Not Important (Delete)\n"
                         "Your choice: "))
    if task_cat == 1:
        urgent.append(task)
    elif task_cat == 2:
        important.append(task)
    elif task_cat == 3:
        not_urgent_but_important.append(task)
    elif task_cat == 4:
        not_urgent_nor_important.append(task)
    else:
        print("Invalid input, please try again.")
        categorize_task(task)  # Re-ask if input is invalid

# Categorize all tasks
categorize_task(task1)
categorize_task(task2)
categorize_task(task3)
categorize_task(task4)
categorize_task(task5)
categorize_task(task6)

# Display the tasks in Eisenhower Matrix format
print("\nEisenhower Matrix:")
print("\n1. Urgent and Important (Do Now):")
for task in urgent:
    print(f" - {task}")

print("\n2. Not Urgent but Important (Schedule):")
for task in important:
    print(f" - {task}")

print("\n3. Urgent but Not Important (Delegate):")
for task in not_urgent_but_important:
    print(f" - {task}")

print("\n4. Not Urgent and Not Important (Delete):")
for task in not_urgent_nor_important:
    print(f" - {task}")
