#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.next = None


    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(self, sep):
    #while node:
     #   fptr.write(str(node.data))

        val = self.head

        while val is not None:
           print(val.data)
           val = val.next

def reverse(self):
    prev = None
    curr = self.head
    nex = curr.next

    while curr:
        curr.next = prev
        prev = curr
        curr = nex

        if nex:
            nex = nex.next
    return prev


llist = SinglyLinkedList()

llist.insert_node(5)
llist.insert_node(10)
llist.insert_node(16)

print_singly_linked_list(llist, '')

print("now rev")
llist = reverse(llist)

print_singly_linked_list(llist, '')
