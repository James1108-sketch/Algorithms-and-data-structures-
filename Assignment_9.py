def hash_function(key, table_size):
    total = 0
    for character in key:
        total += ord(character)

    return total % table_size

def load_data(filename, table_size):

    table = [[] for _ in range(table_size)]
    with open(filename, 'r', encoding='utf-8') as infile:
        header = infile.readline()

        for line in infile:
            data = line.strip().split('\t')
            if len(data) >= 7:

                record = (
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6]
                )

            vin = record[0]
            index = hash_function(vin, table_size)

            table[index].append(record)
    return table

def find_record(table, key):
    index = hash_function(key, len(table))
    for record in table[index]:
        if record[0] == key:
            return index, record
    return index, None

def display_record(record):

    print("\nRecord Found")
    print("-----------------------------")
    print("VIN: ", record[0])
    print("City: ", record[1])
    print("State: ", record[2])
    print("Postal Code: ", record[3])
    print("Model year: ", record[4])
    print("Make: ", record[5])
    print("Model: ", record[6])
    print("-----------------------------\n")

def add_record(table):
    print("\nAdd a New Record")
    vin = input("Enter VIN: ").strip()
    index, exisitng = find_record(table, vin)
    if exisitng is not None:
        print("Record with this VIN already exists.")
        return

    city = input("Enter City: ").strip()
    state = input("Enter State: ").strip()
    postal_code = input("Enter Postal Code: ").strip()
    model_year = input("Enter Model Year: ").strip()
    make = input("Enter Make: ").strip()
    model = input("Enter Model: ").strip()

    new_record = (
        vin,
        city,
        state,
        postal_code,
        model_year,
        make,
        model
    )

    print("\nNew Record:")
    display_record(new_record)

    confirmation = input("Do you want to add this record? (y/n): ").upper()
    if confirmation == 'Y':
        index = hash_function(vin, len(table))
        table[index].append(new_record)
        print("Record added successfully.")
        print("Hash table index:", index)
    else:
        print("Record addition canceled.")

def find_record_menu(table):
    print("\nFind a Record")
    vin = input("Enter VIN to search: ").strip()
    index, record = find_record(table, vin)
    if record is None:
        print("Record not found.")
        print("Hash table index:", index)
        return
    print("\nHash table index:", index)
    display_record(record)
    submenu(table, index, record)

def submenu(table, index, record):
    while True:
        print("\nSubmenu Options:")
        print("D. Delete Record")
        print("E. Update Record")
        print("F. Return to Main Menu")
        choice = input("Enter your choice (D-F): ").strip()

        if choice == 'D':
            confirmation = input("Are you sure you want to delete this record? (y/n): ").upper()
            if confirmation == 'Y':
                table[index].remove(record)
                print("Record deleted successfully.")

            else:
                print("Record deletion canceled.")
            return
        elif choice == 'E':
        
            update_record(table, index, record)
            return
        elif choice == 'F':
            return
        else:
            print("Invalid choice. Please try again.")

def update_record(table, index, record):

    while True:
        print("\nUpdate Record Options:")
        print("G. Make")
        print("H. Model")
        print("I. City")
        print("J. State")
        print("K. Postal Code")
        print("L. Model Year")
        print("M. Return to main menu")
        choice = input("Enter your choice (G-M): ").strip()

        updated = list(record)

        if choice == 'G':
            new_value = input("Enter new Make: ").strip()
            updated[5] = new_value
        elif choice == 'H':
            new_value = input("Enter new Model: ").strip()
            updated[6] = new_value
        elif choice == 'I':
            new_city = input("Enter new City: ").strip()
            updated[1] = new_city
        elif choice == 'J':
            new_state = input("Enter new State: ").strip()
            updated[2] = new_state
        elif choice == 'K':
            new_postal_code = input("Enter new Postal Code: ").strip()
            updated[3] = new_postal_code
        elif choice == 'L':
            new_model_year = input("Enter new Model Year: ").strip()
            updated[4] = new_model_year
        elif choice == 'M':
            return
        else:
            print("Invalid choice. Please try again.")
            continue

        new_record = tuple(updated)
        print("\nUpdated Record:")
        display_record(new_record)

        confirmation = input("Do you want to save these changes? (y/n): ").upper()
        if confirmation == 'Y':
            position = table[index].index(record)
            table[index][position] = new_record
            print("Record updated successfully.")
            return
        else:
            print("Update canceled.")

def display_table(table):
    print("\nHash Table Contents:")
    for index in range(len(table)):
        print("\nIndex:", index)
        if len(table[index]) == 0:
            print(" [None]")
        else:
            for record in table[index]:
                print(" ", record)

def main():
    filename = "electirc_car.txt"
    table_size = 101

    print("==============")
    print("     ELECTRIC CAR HASH TABLE     ")
    print("================================")

    try:
        table = load_data(filename, table_size)
        print("Data loaded successfully")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        print("Make sure the file is in the correct directory.")
        return

    while True:
        print("\nMain Menu Options:")
        print("A. Add a new Record")
        print("B. Find a Record")
        print("C. Display Hash Table")
        print("D. Exit")
        choice = input("Enter your choice (A-D): ").strip()

        if choice == 'A':
            add_record(table)
        elif choice == 'B':
            find_record_menu(table)
        elif choice == 'C':
            display_table(table)
        elif choice == 'D':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()