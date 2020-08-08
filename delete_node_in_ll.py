# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def delete_node(node):
    print("NODE: " + node)

if __name__ == '__main__':
    linked_list = list()
    linked_list.append( ListNode(4) )
    linked_list.append( ListNode(5) )
    linked_list[0].next = linked_list[1]
    linked_list.append( ListNode(1) )
    linked_list[1].next = linked_list[2]

    print( delete_node(5) )
    print(linked_list)