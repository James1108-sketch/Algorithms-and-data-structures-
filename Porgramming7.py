def load_records(filename):
    table = []

    with open(filename, 'r') as infile:
        for line in infile:
            data = line.split()

            if len(data) == 6:
                record = (
                    int(data[0]),
                    data[1],
                    data[2],
                    data[3],
                    float(data[4]),
                    int(data[5])
                )
                table.append(record)

        table.sort(key=lambda record: record[0])
        return table

def find_records_using_key(table, key):
    low = 0
    high = len(table) - 1

    while low <= high:
        middle = (low + high) // 2
        if table[middle][0] == key:
            return middle
        elif table[middle][0] < key:
            low = middle + 1
        else:
            high = middle -1

    return -1

def display_headings():
    print("-" * 76)
    print(
        f"{'prod num':<10}"
        f"{'region':<12}"
        f"{'prod code':<12}"
        f"{'prod name':<16}"
        f"{'price':<10}"
        f"{'quantity':<12}"
    )
    print("-" * 76)

def display_record(record):
    print(
        f"{record[0]:<10}"
        f"{record[1]:<12}"
        f"{record[2]:<12}"
        f"{record[3]:<16}"
        f"{record[4]:<10.2f}"
        f"{record[5]:<12}"
    )

def display_records_on_screen(table):
    if not table:
        print("No records to display.")
        return

    display_headings()
    for record in table:
        display_record(record)

        print("-" * 76)
        print(f"Total records: {len(table)}")

def delete_first_record(table):
    if not table:
        print("No records to delete.")
        return

    print("Deleted record:")
    display_headings()
    display_record(table[0])

    confirm = input("Are you sure you want to delete this record? (Y/N): ").strip().lower()
    if confirm == 'y':
        table.pop(0)
        print("Record deleted.")
    else:
        print("Deletion canceled.")

def display_largest_price(table):
    if not table:
        print("No records to analyze.")
        return

    largest_index = 0

    for index in range(1, len(table)):
        if table[index][4] > table[largest_index][4]:
            largest_index = index

    print("Record with the largest price:")
    display_headings()
    display_record(table[largest_index])

def print_report(table):
    try:
        with open("report.txt", "w") as outfile:
            title = "Sales Report"
            outfile.write(title.center(76) + "\n")
            outfile.write("=" * 76 + "\n")

            outfile.write(
                f"{'prod num':<10}"
                f"{'region':<12}"
                f"{'prod code':<12}"
                f"{'prod name':<16}"
                f"{'price':<10}"
                f"{'quantity':<12}\n"
            )

        outfile.write("=" * 76 + "\n")

        for record in table:
            outfile.write(
                f"{record[0]:<10}"
                f"{record[1]:<12}"
                f"{record[2]:<12}"
                f"{record[3]:<16}"
                f"{record[4]:<10.2f}"
                f"{record[5]:<12}\n"
            )

        outfile.write("=" * 76 + "\n")

        print("Report written to report.txt")

    except OSError as error:
        print("Error: Could not write to report.txt", error)

def delete_record_at_address_location(table, location):
    if 0 <= location < len(table):
        return table.pop(location)

    return None

def delete_using_key(table, key):
    try:
        key = int(input("Enter the product number to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    location = find_records_using_key(table, key)
    if location == -1:
        print("Record not found. No record deleted.")
        return

    print("Record found:")
    display_headings()
    display_record(table[location])

    confirm = input("Are you sure you want to delete this record? (Y/N): ").strip().lower()
    if confirm == 'y':
        deleted_record = delete_record_at_address_location(table, location)
        print("Deleted record:", deleted_record)
    else:
        print("Deletion canceled.")

def add_new_record_using_key(table):
    try:
        key = int(input("Enter the product number to add: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    if find_records_using_key(table, key) != -1:
        print("Record with this product number already exists. No record added.")
        return

    region = input("Enter region (no spaces): ").strip()
    prod_code = input("Enter product code (no spaces): ").strip()
    prod_name = input("Enter product name (no spaces): ").strip()

    if not region or not prod_code or not prod_name:
        print("Invalid input. Region, product code, and product name cannot be empty.")
        return

    try:
        price = float(input("Enter price: "))
        units_sold = int(input("Enter quantity sold: "))

        if price < 0 or units_sold < 0:
            print("Price and quantity sold must be non-negative.")
            return

    except ValueError:
        print("Invalid input. Price must be a number and quantity sold must be an integer.")
        return

    new_record = (key, region, prod_code, prod_name, price, units_sold)

    print("\nNew record to be added:")
    display_headings()
    display_record(new_record)

    confirm = input("Are you sure you want to add this record? (Y/N): ").strip().lower()
    if confirm == 'y':
        low = 0
        high = len(table)

        while low < high:
            middle = (low + high) // 2

            if table[middle][0] < key:
                low = middle + 1
            else:
                high = middle

        table.insert(low, new_record)
        print("Record added successfully.")
    else:
        print("Addition canceled.")

def update_record_using_key(table):
    try:
        key = int(input("Enter the product number to update: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    location = find_records_using_key(table, key)
    if location == -1:
        print("Record not found. No record updated.")
        return

    record = table[location]

    print("\ncurrent record:")
    display_headings()
    display_record(record)

    while True:
        print("\nUPDATE SUBMENU")
        print("A. region")
        print("B. product code")
        print("C. product name")
        print("D. price")
        print("E. quantity sold")
        print("F. Exit update submenu")

        choice = input("Enter your choice (A-F): ").strip().upper()

        if choice == 'F':
            return

        field_position = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5
        } 

        if choice not in field_position:
            print("Invalid choice. Please select a valid option.")
            continue

        field_index = field_position[choice]

        if field_index == 1:
            new_value = input("Enter new region: ").strip()
            if not new_value:
                print("Invalid input. Region cannot be empty.")
                continue

        elif field_index == 2:
            new_value = input("Enter new product code: ").strip()
            if not new_value:
                print("Invalid input. Product code cannot be empty.")
                continue

        elif field_index == 3:
            new_value = input("Enter new product name: ").strip()
            if not new_value:
                print("Invalid input. Product name cannot be empty.")
                continue

        elif field_index == 4:
            try:
                new_value = float(input("Enter new price: "))
                if new_value < 0:
                    print("Price must be non-negative.")
                    continue
            except ValueError:
                print("Invalid input. Price must be a number.")
                continue

            else:
                try:
                    new_value = int(input("Enter new quantity sold: "))
                    if new_value < 0:
                        print("Quantity sold must be non-negative.")
                        continue
                except ValueError:
                    print("Invalid input. Quantity sold must be an integer.")
                    continue

        updated_values = list(record)
        updated_values[field_index] = new_value
        updated_record = tuple(updated_values)

        print("\nUpdated record:")
        display_headings()
        display_record(updated_record)

        confirm = input("Are you sure you want to update this record? (Y/N): ").strip().lower()
        if confirm == 'y':
            table[location] = updated_record
            print("Record updated successfully.")
        else:
            print("Update canceled.")

        return

def main():
    try:
        table = load_records("salesrec.txt")
    except FileNotFoundError:
        print("Error: salesrec.txt file not found.")
        print("Please ensure the file exists in the current directory.")
        return
    except(ValueError, OSError) as error:
        print("Error loading records:", error)
        return

    print("records loaded:", len(table))

    option = '0'

    while option != '8':
        print("\nMAIN MENU")
        print("1. Display records on screen")
        print("2. Delete first record")
        print("3. Display record with largest price")
        print("4. Print report to file")
        print("5. Delete record using product number")
        print("6. Add new record using product number")
        print("7. Update record using product number")
        print("8. Exit program")

        option = input("Enter your choice (1-8): ").strip()

        if option == '1':
            display_records_on_screen(table)
        elif option == '2':
            delete_first_record(table)
        elif option == '3':
            display_largest_price(table)
        elif option == '4':
            print_report(table)
        elif option == '5':
            delete_using_key(table)
        elif option == '6':
            add_new_record_using_key(table)
        elif option == '7':
            update_record_using_key(table)
        elif option == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

        print("Application finished")

if __name__ == "__main__":
    main()