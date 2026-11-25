
# Q).Write a Python class Queue that implements a basic queue data structure with the enqueue
#  and dequeue methods. 
# The enqueue method should add an element to the rear of the queue, and the dequeue
#  method should remove and return the remaining element from the queue.
# Additionally, include a method is_empty to check if the queue is empty.


class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if self.is_empty():  #check how it work
            print("Queue is empty")
            return ()
        else:
            val = self.queue.pop(0)
            return val,self.queue
    def is_empty(self):
        if self.queue:
            return False
        return True
    def display(self):
        print(f"The remaining Queue : {self.queue}")

# Admin@CarnivalTMZ

q = Queue()


while True:
    print("Queue Data Structure")
    choice = input("Enter your choice\n1.Enqueue\n2.Dequeue\n3.Check Empty\n4.Display\n5.Exit\n")
    if choice == "1":
        data = int(input("Enter Value : "))
        q.enqueue(data)
    elif choice == "2":
        data = q.dequeue()
        print(data)
        if len(data):
            rqueue = data[1]

            print(f"The Remaining Queue {rqueue}")
    elif choice == "3":
        check = q.is_empty()
        if check:
            print("Queue is empty")
        else:
            print("Queue is not empty")

    elif choice == "4":
        q.display()
    elif choice == "5":
        print("Existed")
        break
    else:
        print("Wrong choice !!")
        continue