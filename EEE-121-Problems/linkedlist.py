class LLNode:
  def __init__(self, data=0, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev

class LinkedList:
  def __init__(self):
    self.head = LLNode(0)
    self.tail = LLNode(0)
    
  def access(self, k):
    temp = self.head
    while k >= 0 and temp.next != None:
      temp = temp.next
      k -= 1
    return temp

  def insert(self, new_element, k=0):
    temp = self.access(k-1)

    # Inserting into empty list
    if self.head.next == None and self.tail.prev == None:
        new_node = LLNode(new_element, next=self.tail, prev=self.head)
        self.tail.prev = new_node
    else:
        new_node = LLNode(new_element, next=temp.next, prev=temp)
        temp.next.prev = new_node
    temp.next = new_node
    return

  def delete(self, k=0):
    temp = self.access(k-1)
    to_delete = temp.next
    # When more than one element
    if self.head.next != None and self.tail.prev != None:
        to_delete.next.prev = temp
    temp.next = to_delete.next
    del to_delete
        
    return
  
  def print_forward(self):
    temp = self.head.next
    out = ""
    while temp != self.tail: # You may change this to temp != self.tail if implemented
        out = out + str(temp.data) + " -> "
        temp = temp.next
    print(out)
    return
  
  def print_backward(self):
    temp = self.tail.prev
    out = ""
    while temp != self.head: # You may change this to temp != self.head if implemented
      out = out + str(temp.data) + " <- "
      temp = temp.prev
    print(out)
    return

# You shouldn't need to modify anything below this line

n = int(input())
LL = LinkedList()
for i in range(n):
    call = input().split()
    if call[0] == "insert":
      LL.insert(int(call[2]), int(call[1]))
    elif call[0] == "delete":
      LL.delete(int(call[1]))
    else:
      print("Invalid Command")

LL.print_forward()
LL.print_backward()
