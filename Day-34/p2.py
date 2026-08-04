# create an endless loop where each element in the queue is a dictionary containing two properties: 'name' and 'priority_order'. 
# Higher priority gets served first.

# In every iteration:

# The program should print the queue.

# The user should have two options:

# Add an element (with name and priority)

# Dequeue the queue to get the element at the front element.

# Hint:
# Priority Queue uses min heap so plan accordingly.

import heapq

index_dict=[]

def add_element(queue, name, priority):
    global index_dict
    index_dict.append((priority, name))
    heapq.heapify(index_dict)
    queue.append((name, priority))
    print("Element added:", (name, priority))

def dequeue_element(queue):
    global index_dict
    if index_dict:
        priority, name = heapq.heappop(index_dict)
        queue.remove((name, priority))
        print("Element dequeued:", (name, priority))
    else:
        print("Queue is empty")

def print_queue(queue):
    if queue:
        print("Current Queue:")
        for item in queue:
            print(item)
    else:
        print("Queue is empty")

def main():
    queue = []
    while True:
        print_queue(queue)
        print("Options:")
        print("1. Add element")
        print("2. Dequeue element")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            priority = int(input("Enter priority : "))
            add_element(queue, name, priority)
        elif choice == '2':
            dequeue_element(queue)
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")
        
if __name__ == "__main__":
    main()

