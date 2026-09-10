class LinkedList:
    
    def __init__(self):
        self.headDummy = ListNode()
        self.tail = self.headDummy
    
    def get(self, index: int) -> int:
        cur = self.headDummy.next
        i = 0
        while cur != None:
            if i == index:
                return cur.val
            if i < 0:
                return -1
            cur = cur.next
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        headNode = ListNode()
        headNode.val = val
        if self.headDummy.next != None:
            headNode.next = self.headDummy.next
        else:
            self.tail = headNode
        self.headDummy.next = headNode
        
        cur = self.headDummy.next
        while cur != None:
            print("Node val: ", cur.val)
            cur = cur.next

    def insertTail(self, val: int) -> None:
        tailNode = ListNode()
        tailNode.val = val
        self.tail.next = tailNode
        self.tail = tailNode
        self.tail.next = None

    def remove(self, index: int) -> bool:
        prev = self.headDummy
        cur = self.headDummy.next
        i = 0
        while cur != None:
            if i > index:
                return False

            if i == index:
                if cur == self.tail:
                    self.tail = prev
                    prev.next = None
                    return True
                prev.next = cur.next
                return True
            prev = prev.next
            cur = cur.next
            i += 1

        return False

    def getValues(self) -> List[int]:
        my_array = []
        cur = self.headDummy.next
        while cur != None:
            my_array.append(cur.val)
            cur = cur.next

        return my_array

class ListNode:
    def __init__(self):
        self.val = 0
        self.next = None