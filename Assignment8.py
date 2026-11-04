import time

class Queue:

    def __init__(self, size):
        self.size = size
        self.count = 0
        self.front = 0
        self.rear = -1
        self.table = [None] * size

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

    def enqueue(self, record):
        if self.isFull():
            print("Queue is full. Cannot enqueue.")
            return

        jobNum, numPages = record

        if numPages < 1 or numPages > 100:
            print("Invalid number of pages.")
            print("Print job must have between 1 and 100 pages.")
            return

        self.rear = (self.rear + 1) % self.size
        self.table[self.rear] = record
        self.count += 1
        print("Print job", jobNum, "added successfully.")


    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty. Cannot dequeue.")
            return None

        record = self.table[self.front]
        self.table[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return record

    def displayQueue(self):
        if self.isEmpty():
            print("Queue is empty.")
            return

        print("Current print jobs in the queue:")
        print("--------------------------------")
        print(f"{'Job Number':<15}{'Number of Pages':<10}")
        print("--------------------------------")
        for i in range(self.count):
            index = (self.front + i) % self.size
            jobNum, numPages = self.table[index]
            print(f"{jobNum:<15}{numPages:<10}")
        print("--------------------------------")

def main():
    pages_per_minute = 18
    printer_queue = Queue(5)

    option = ""
    print("===============")
    print("     PRINTER SIMULATION")
    print("===============")
    print("Printer speed:", pages_per_minute, "pages per minute")
    print("Maximum queue size:", printer_queue.size)

    while option != "4":
        print("\nMenu:")
        print("1. Add a print job")
        print("2. Process the next print job")
        print("3. Display the current queue")
        print("4. Exit")
        option = input("Enter your choice (1-4): ")

        if option == "1":

            try:
                jobNum = int(input("Enter job number: "))
                numPages = int(input("Enter number of pages: "))

                printer_queue.enqueue((jobNum, numPages))

            except ValueError:
                print("Please enter valid integer values.")

        
        elif option == "2":

            if printer_queue.isEmpty():
                print("No print jobs available.")

            else:

                record = printer_queue.dequeue()

                jobNum = record[0]
                numPages = record[1]

                print("\nPrinting Job:", jobNum)
                print("Number of pages:", numPages)

                
                printing_time = numPages / pages_per_minute * 60

                print("Printing in progress...")

                time.sleep(printing_time)

                print("Job", jobNum, "finished printing.")

        
        elif option == "3":

            printer_queue.displayQueue()

        
        elif option == "4":

            print("Printer application shutting down.")

        else:

            print("Invalid option. Please select 1 through 4.")

if __name__ == "__main__":
    main()
