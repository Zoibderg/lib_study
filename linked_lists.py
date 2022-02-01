class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.prev = prev
        self.data = data
        self.next = next
        

class LinkedList:
    def __init__(self):
        self.head = None
        
    def print(self):
        if self.head is None:
            return 'Linked list is empty.'

        itr = self.head
        llstr = '[ '
        while itr:
            llstr += str(itr.data) + ',' + ' ' if itr.next else str(itr.data) + ' ' + ']'
            itr = itr.next
        
        return llstr

    def print_reverse(self):
        if self.head is None:
            return 'Linked list is empty.'

        last_node = self.get_last_node()
        itr = last_node
        llstr = '[ '
        while itr:
            llstr += str(itr.data) + ',' + ' ' if itr.prev else str(itr.data) + ' ' + ']'
            itr = itr.prev

        return llstr

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def get_length(self):
        count = 0
        itr = self.head
        
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_start(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = Node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next: itr = itr.next
        itr.next = Node(data, None, itr)

    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_length(): raise Exception("Invaild Index")

        if index == 0:
            self.insert_at_start(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length(): raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head

        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        itr = self.head

        while itr:
            if itr.data == data_after:
                itr.next
                node = Node(data_to_insert, itr.next, itr.prev)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        idx = 0
        itr = self.head

        while itr:
            if itr.data == data:
                self.remove_at_index(idx)
                break
            idx += 1
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    length = ll.get_length()
    values = ll.print()
    valuesr = ll.print_reverse()
    liststr = 'Linked List: {} \nReversed: {} \nLength: {}'.format((values),(valuesr), (length))
    print(liststr)
