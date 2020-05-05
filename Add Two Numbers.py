import math
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def print_node(self, node):
        while (node is not None) and (node.get_data is not None):
            print(node.data)
            node = node.next

    def add_two_numbers(node1, node2):
        summ = 0
        count_1 = 0
        count_2 = 0
        #multiplier_1 = 1
        #multiplier_2 = 1
        while (node1 is not None) or (node2 is not None):
            #multiplier_1 = multiplier_1*(10**count_1)
            #multiplier_2 = multiplier_2*(10**count_2)
            if node1.data != None:
                sum_1 = int(node1.data)*(10**count_1)
            else:
                sum_1 = 0
            if node2.data != None:
                sum_2 = int(node2.data)*(10**count_2)
            else:
                sum_2 = 0
            summ = summ + sum_1 + sum_2
            if node1 != None and node1.data != None:
                count_1 = count_1 + 1
            else:
                count_1 = 0
            if node2 != None and node2.data != None:
                count_2 = count_2 + 1
            else:
                count_2 = 0
            
            node1 = node1.next
            node2 = node2.next
  
            

            print(count_1, count_2)
            print(summ)
        
        #print(summ)

    def reverseNumberAndConvertTolist(num):
        # get the number at the very end by using modulus.
        # Then append to an empty list
        if num == None or num == 0:
            print(0)
        else:
            node = Node()
            while num != 0:
                last = num%10 # This will give us the last number
                node = Node.addNodeToEnd(node,last)
                node.print_node(node)
                print("pause")
                num = num//10             

            #node.print_node(node)
            return

    def addNodeToEnd(head, val):
        if head == None:
            head = Node(val)
        else:
            current = head
            while current.next != None:
                current = current.next
            current.next = Node(val)
        return head

## First create two random lists here
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node1.next = node2
node2.next = node3
#node1.print_node(node1)

node4 = Node(5)
node5 = Node(6)
node6 = Node(7)
node4.next = node5
node5.next = node6

#Node.add_two_numbers(node1, node4)
Node.reverseNumberAndConvertTolist(123)


'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        summ = 0
        count_1 = 0
        count_2 = 0
        while (l1 is not None) or (l2 is not None):
            if l1 != None and l1.val != None:
                sum1 = l1.val*(10**count_1)
            else:
                sum1 = 0
            if l2 != None and l2.val != None:
                sum2 = l2.val*(10**count_2)
            else:
                sum2 = 0
            
            summ = summ + sum1 + sum2
            if l1 != None and l1.val != None:
                count_1 = count_1 + 1
            else:
                count_1 = 0
                
            if l2 != None and l2.val != None:
                count_2 = count_2 + 1
            else:
                count_2 = 0
             
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            
        print(summ)
        new_node = self.createList(summ)
        if new_node == None:
            return new_node
        else:
            return new_node.next
        
    def createList(self, num):
        if num == 0 or num == None:
            print("hello")
            node = ListNode(None)
            node = self.addToEnd(node,num)
            return node
        else:
            node = ListNode(None)
            while num != 0:
                last = num%10
                node = self.addToEnd(node, last)
                num = num//10
                
            return node
        
    def addToEnd(self, head, last):
        if head == None:
            head = ListNode(last)
        else:
            current = head
            while current.next != None:
                current = current.next
            current.next = ListNode(last)
        return head

'''
