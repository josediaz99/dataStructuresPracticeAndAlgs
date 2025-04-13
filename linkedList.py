class Node: 
    """
    object for storing a single node of linked list
    models two attributes data & link to the next node in list
    """
    data = None
    nextNode = None
    
    def __init__(self,data):
        self.data = data
        
    def __repr__(self):
        return "<Node data: %s" % self.data
    
class linkedList:
    """
    singly linked list
    """
    def __init__(self):
        self.head = None

    def __repr__(self):
        """
        returns a string representation of thew list 
        takes o(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.nextNode is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.nextNode
            
        return'->'.join(nodes) 


    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        returns the number of nodes in the list
        takes O(n) time
        """
        current = self.head
        count = 0

        while current:#goes through the loop until it reaches the end
            count += 1
            current = current.nextNode

        return count

    def add(self , data):
        """
        adds a new node containing data at the head of the list
        takes o(1) time
        """
        newNode = Node(data)
        newNode.nextNode = self.head
        self.head = newNode

    def search(self,key):
        """
        search for first node that mathes key
        returns node or none if not found

        takes o(n)
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.nextNode
            return None
    
    def insert(self, data, index):
        """
        inserts new node containing data at index position
        insertion takes o(1) 
        finding node takes o(n)
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = Node.nextNode
                position -= 1

            prev = current
            next = current.nextNode

            prev.nextNode = new
            new.nextNode = next

        def remove(self,key):
            """
            removes a node from linkedList which matches our key
            returns the node or None if key doesnt exist
            takes o(n)
            """
            current = self.head
            previous = None
            found = False

            while current and not found:
                if current.data == key and current is self.head:
                    found = True
                    self.head = current.nextNode
                elif current.data == key:
                    found = True
                    previous.nextNode = current.nextNode
                else:
                    previous = current
                    current = current.nextNode

            return current

                