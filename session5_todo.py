import csv

quit = 0
todo_list = []
item_id = 0
while quit == 0:
    item = input('What is your task:')

    todo_list[item_id] = item
    item_id = item_id + 1
    end = input('Add more (y/n)?:')
    if end == 'n':
        quit = 1

field_names = ['id', 'task']
todo_dict = dict()
for index, value in enumerate(todo_list):
    todo_dict[index] = value


with open('todo.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames = field_names)

    spreadsheet.writeheader()
    spreadsheet.writerows(todo_dict)
