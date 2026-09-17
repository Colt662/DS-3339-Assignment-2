# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''

    def __init__(self, name):
        self.name = name
        self.next = None


    def __str__(self):
        return f'Name: {self.name}'



# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''

    def __init__(self):
        self.head = None


    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node


    def add_end(self, name):
        #empty list, new head
        if self.head == None:
            self.head = Node(name)

        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = Node(name)


    def remove(self, name):
        current_node = self.head
        prev_node = current_node

        while current_node != None:
            if current_node.name == name:
                if current_node == self.head:
                    self.head = self.head.next

                else:
                    prev_node.next = current_node.next

                return #name found and removed, no need to continue
            
            prev_node = current_node
            current_node = current_node.next

        #return statement means loop only finishes when no name is removed
        print(f'{name} not found')


    def print_list(self):
        if self.head == None:
            print("The waitlist is empty")

        else:
            current_node = self.head
            while current_node != None:
                print(current_node)
                current_node = current_node.next

                
        
    


def waitlist_generator():
    # Create a new linked list instance
    customer_list = LinkedList()
    
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            customer_list.add_front(name)
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            customer_list.add_end(name)
            

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            customer_list.remove(name)
            
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            customer_list.print_list()
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break


        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()


'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:

- How does your list work?
It stores each item as a node with data and a pointer* to the address of the next node in the list. The list object itself only stores a head which points* to the first node in the list. Insertion into the list is done by swapping pointers* around in the area where the insertion takes places. Traversal can only go one way starting from the head and working towards the back of the list. Any operations done on nodes during traversal need to happen before traversing to the next node (or after coming around again).
*(I'm used to calling it a pointer, but I believe python technically calls what I used a "reference" to another variable. I'm not sure since don't know the details of Python that well and it serves the same purpose as a pointer regardless.)

- What role does the head play?
It provides the starting point to start traversing the list, without it there would be no way to access the first node since nothing would point to it. When the list is empty it points to nothing, and when it has items it points to the first node in the list. No nodes can exist before the head because they could not be accessed.

- When might a real engineer need a custom list like this?
When implementing a queue, deque, or stack. When fast access to the middle of the list is not very important/only the ends of the list are ever accessed (like in a queue or stack). When they need to be conscious of how the list is stored in memory. When the list will store an unknown amount of items. When they want to give the list specialized methods that built in lists don't have.

'''
