# 删除链表中的节点
# https://leetcode-cn.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 跳过 node.next 节点
        node.val = node.next.val
        node.next = node.next.next
        
        '''
        while node.next != None:
            node.val = node.next.val
            prev, node = node, node.next
        prev.next = None
        '''
