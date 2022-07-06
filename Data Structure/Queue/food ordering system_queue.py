
from collections import deque
import queue
import time
import threading


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

food_order_q=Queue() 
def place_order(orders):
    
    for item in orders:  
        print("Order Placed for:",item)
        food_order_q.enqueue(item)
        time.sleep(0.5)

def serve_order():
    time.sleep(1)
    while queue!=0:
        order=food_order_q.dequeue()
        print(order,": Delivered")
        time.sleep(1.5)
    
    
   
if __name__=='__main__':
    orders = ['Pizza','Samosa','Maagi','Biryani','Burger']

    t1=threading.Thread(target=place_order,args=(orders,))
    t2=threading.Thread(target=serve_order)

    t1.start()
    t2.start()

   




