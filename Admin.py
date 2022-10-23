
import json


# define input_int function

def input_int(prompt):
    while True:
        inputNumberStr = input(prompt)
        try:
            inputNumber = int(inputNumberStr)
            break
        except:
            print("Please enter a number")
    return inputNumber


# Define input_something function

def input_something(prompt):
    while True:
        prompt = input(prompt)
        if prompt.strip().isdigit():
            print('gay')
            break
        return prompt



# Define saveDate() Function

def saveData(data_list):
    jsonData = json.dumps(data_list, indent=4)
    with open('data.txt', 'w') as jsonfile:
        jsonfile.write(jsonData)


# Here is where you attempt to open data.txt and read the data into a "data" variable.

try:
    with open('data.txt', 'r') as jsonfile:
        data = json.load(jsonfile)
    jsonfile.close()

# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.

except Exception:
    data = []
    print("Could not open data.txt")

# Print welcome message, then enter the endless loop which prompts the user for a choice.

print('Welcome to the Fast-Food Quiz Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower()
    if choice == 'a':
        # Add a new fast-food item.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
        foodName = input_something('Enter fast food item name: ')
        calories = input_int('Enter number of calories: ')
        fat = input_int('Enter fat in grams: ')
        protein = input_int('Enter protein in grams: ')
        carbohydrates = input_int('Enter carbohydrates in grams: ')
        sodium = input_int('Enter sodium in miligrams: ')
        cholestrol = input_int('Enter cholestrol in miligrams: ')

        dict = {'name': foodName, 'calories': calories, 'fat': fat, 'protein': protein, 'carbohydrates': carbohydrates,
                'sodium': sodium, 'cholestrol': cholestrol, }
        data.append(dict)
        saveData(data)
        print("Food item added.")


    # List the current fast-food items.

    elif choice == 'l':
        if len(data) == 0:  # if the list is empty, show empty list message
            print('Data not found.')

        else:  # otherwise, loop through the list and show each item
            print('List of menu items:')
            listNum = 1
            for item, Name in enumerate(data):
                print(listNum, ')', Name['name'])
                listNum += 1

        # Search the current fast-food items.

    elif choice == 's':
        counter = 0
        if len(data) == 0:
            print("No data found")
        else:
            inputMessage = "Type a fast-food item to search for: "
            searchString = input_something(inputMessage)
            for foodData in enumerate(data):
                if searchString.lower() in foodData[1]['name'].lower():
                    print(foodData[0] + 1, ") ", foodData[1]['name'])
                    counter = counter + 1

        # View a fast-food item.

    elif choice == 'v':

        if len(data) == 0:

            print('No data Saved')
        else:

            while True:

                listNum = input_int('Menu item number to view: ')

                try:

                    food = data[listNum - 1]

                    print(food['name'])

                    print('Calories: ', food['calories'])

                    print('Fat: ', food['fat'])

                    print('Protein: ', food['protein'])

                    print('Carbohydrates: ', food['carbohydrates'])

                    print('Sodium: ', food['sodium'])

                    print('Cholestrol: ', food['cholestrol'])

                    break

                except IndexError:

                    print('Invalid Index Number! Please enter an integer')



    # Delete a fast-food item.

    elif choice == 'd':
        if len(data) == 0:
            print("No data found")
        else:
            inputMessage = "Menu item number to delete: "
            indexNumber = input_int(inputMessage)
            if 0 <= indexNumber and indexNumber < len(data):
                del data[indexNumber]
                saveData(data)
                print("Menu item deleted.")
            else:
                print("Invalid number! Please enter an integer")

    # End the program.

    elif choice == 'q':
        print("Goodbye")
        break
    else:
        # Print "invalid choice" message.

        print("Invalid Choice!")

# If you have been paid to write this program, please delete this comment.
