from juggler import Juggler
from peewee import *

"""
A menu - you need to add the database and fill in the functions. 
"""

def main():
    
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    """ Display all records in database by using select query"""

    all_jugglers = Juggler.select() # Select all jugglers

    if all_jugglers:
        print(format_string('All jugglers:')) # Print label using format function

    for juggler in all_jugglers:
        print(juggler) 


def search_by_name():
    """ User can search for a juggler by name and recieve all information on the object 
        by getting input from user and entering it into a select query - it then returns
        the results for use in the edit/delete methods"""

    juggler_name = input('Enter name of juggler: ') # Get search name

    # Select juggler where the name in database is equal to the inputted name - allow for only one answer to be safe
    juggler_results = Juggler.select().where(Juggler.name == juggler_name).limit(1)
    
    if juggler_results: # If juggler entered exists in database, print the index 0 to format results properly
        print(juggler_results[0])

        return juggler_results[0] # Return the results in order to be used in other functions

    else:
        print(format_string('Juggler not found')) 


def add_new_record():
    """ Function to take user input (name, country, number of catches) and enter it into database.
        ID will be automatically created. If user enters duplicate name in database, try/except will
        catch the IntegrityError and let the user know that the record already exists in the database. """

    # Get object attribute input from user 
    new_juggler_name = input('Enter juggler\'s name: ')
    new_juggler_country = input('Enter new juggler\'s country: ')
    new_juggler_num_catches = input('Enter new juggler\'s number of catches: ')

    try: # Try to add new object using the variables put in by user
        new_juggler = Juggler(name = new_juggler_name, country = new_juggler_country, num_catches = new_juggler_num_catches)
        new_juggler.save()
    except IntegrityError: # If the user attempts to add a duplicate record, show alert
        print(format_string('Error - juggler already exists'))


def edit_existing_record():
    """ Function that uses the search by name function to get input from user (name)
        and edit the record with the matching name. If the user enters a name that 
        exists in the database, it will update the object and database with the new number """

    juggler_to_update = search_by_name() # Call search by name function to get user input and query DB

    if juggler_to_update: # If the record exists in database, ask user to enter new number of catches
        updated_catches = int(input('Update number of catches: '))
        juggler_to_update.num_catches = updated_catches # Update object with new number of catches
        juggler_to_update.save()

        print(f'Record successfully updated to: "{juggler_to_update}"')


def delete_record():
    """ Function that uses search by name function to get user's input (juggler name)
        and delete object using the delete function where the inputted name matches
        that of one in the database """

    juggler_to_delete = search_by_name() # Call search by name function to get user input and query DB

    if juggler_to_delete: # If there was a matching name in the database, call delete function where name matches DB record
        rows_deleted = Juggler.delete().where(Juggler.name == juggler_to_delete.name).execute()
        if rows_deleted: # If the row was deleted, show confirmation to user
            print(f'"{juggler_to_delete}" successfully deleted')


def format_string(string):
    """ Format string function to make strings neater and more
        legible using new lines """
    return (f'\n{string}\n')


if __name__ == '__main__':
    main()