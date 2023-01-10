#!/usr/bin/python3
""" Singly linked list """


class Node:
    """ initialize attribute data and next_node """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ get the value of data """
        return (self.__data)

    @data.setter
    def data(self, value):
        """ set attribute value """
        if (not isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ get the next node """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ set the next node """
        if (not isinstance(value, Node)) and (value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ class of a singly linked list """

    def __init__(self):
        """ initialize """
        self.__head = None

    def sorted_insert(self, value):
        """ sort linked list in ascending order """
        newNode = Node(value)
        if self.__head is None:
            self.__head = newNode
        elif (value <= self.__head.data):
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            tmp = self.__head
            while (tmp.next_node) and (tmp.next_node.data < value):
                tmp = tmp.next_node
            newNode.next_node = tmp.next_node
            tmp.next_node = newNode

    def __str__(self):
        """ replace print() in singlylinked list. print the list """
        data = []
        tmp = self.__head
        while tmp:
            data.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(data))
