class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    # Write your code here
    '''self.head=Node
    temp=Node(data)
    temp.next=self.head
    self.head=temp
    #head=temp'''
    new = Node(data)
    temp = self.head
    if temp is None:
        self.head = new
    else:
        while temp.next is not None:
            temp = temp.next
            temp.next = new

  def pop(self) -> None:
    # Write your code here
    temp=self.head
    if temp is None:
      return None
    else:
      temp=self.head
      self.head=temp.next
      pop(temp)

  def status(self):
    """
    It prints all the elements of stack.
    """
    # Write your code here
    self.head=Node
    temp=self.head
    while temp!=None:
      temp=temp.next
      print(temp,"=>")
    else:
      print("None")


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
