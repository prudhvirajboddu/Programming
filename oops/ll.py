from typing import List


class Node:
    def __init__(self,value=None) -> None:
        self.value=value
        self.next=None

class ListNode:
    def __init__(self) -> None:
        self.headval=None

l=ListNode()

l.headval=Node("mon")

e=Node()