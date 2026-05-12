class Node:
    def __init__(self, parent, left, right, data):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data


class Tree:
    def __init__(self, root):
        self.root = root


class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value


def cmp_func(key1,key2):
    if key1 > key2:
        return 1
    if key1 == key2:
        return 0
    if key1 < key2:
        return -1

def create():
    tree = Tree(None)
    return tree


def clear(tree):
    tree.root = None
    return tree


def search_breadth(number,a):
    number = number + 1
    if a.right is None and a.left is None:
        return number
    if a.right is not None and a.left is None:
        return search_breadth(number,a.right)
    if a.right is None and a.left is not None:
        return search_breadth(number,a.left)
    if a.right is not None and a.left is not None:
        return search_breadth(number,a.right) + search_breadth(number,a.left) - number


def size(tree):
    number = 0
    return number if tree.root is None else search_breadth(number,tree.root)


def find(tree, key):
    if tree.root is None:
        return None
    a = tree.root
    while True:
        if cmp_func( key , a.data.key ) == 1:
            if a.right is None:
                return None
            a = a.right
        if cmp_func( key , a.data.key ) == -1:
            if a.left is None:
                return None
            a = a.left
        if cmp_func( key , a.data.key ) == 0:
            return a.data.value


def insert(tree, data):
    if tree.root is None:
        tree.root = Node(None,None,None,data)
        return None
    a = tree.root
    while True:
        if cmp_func( data.key , a.data.key ) == 1:
            if a.right is None:
                a.right = Node(a,None,None,data)
                return None
            a = a.right
        if cmp_func( data.key , a.data.key ) == -1:
            if a.left is None:
                a.left = Node(a,None,None,data)
                return None
            a = a.left
        if cmp_func( data.key , a.data.key ) == 0:
            ret = a.data
            a.data = data
            return ret


def delete(tree, key):
    a = tree.root
    d = 0
    while True:
        if cmp_func( key , a.data.key ) == 1:
            if a.right is None:
                return None
            a = a.right
            d = 1
        if cmp_func( key , a.data.key ) == -1:
            if a.left is None:
                return None
            a = a.left
            d = -1
        if cmp_func( key , a.data.key ) == 0:
            if d == 1:
                if a.right is None and a.left is None:
                    f = a.data
                    a = None
                    return f
                if a.right is None and a.left is not None:
                    f = a.data
                    a.parent.right = a.left
                    a.left.parent = a.parent
                    return f
                if a.right is not None and a.left is None:
                    f = a.data
                    a.parent.right = a.right
                    a.right.parent = a.parent
                    return f
                if a.right is not None and a.left is not None:
                    f = a.data
                    b = a.right
                    while b.left is not None:
                        b = b.left
                    a.parent.right = a.right
                    a.right.parent = a.parent
                    c  = Node(b, a.left, None, a.left.data)
                    b.left = c
                    return f
            else:
                if a.right is None and a.left is None:
                    f = a.data
                    a = None
                    return f
                if a.right is None and a.left is not None:
                    f = a.data
                    a.parent.left = a.left
                    a.left.parent = a.parent
                    return f
                if a.right is not None and a.left is None:
                    f = a.data
                    a.parent.left = a.right
                    a.right.parent = a.parent
                    return f
                if a.right is not None and a.left is not None:
                    f = a.data
                    b = a.right
                    while b.left is not None:
                        b = b.left
                    a.parent.left = a.right
                    a.right.parent = a.parent
                    c = Node(b, a.left, None, a.left.data)
                    b.left = c
                    return f


def function(s):
    s = s * 2


def rec(a,func):
    if a is not None:
        func(a.data.value)
        rec(a.left, func)
        rec(a.right, func)


def foreach(tree, func):
    a = tree.root
    rec(a, func)

if __name__ == "__main__":
    t = create()
    d1=Data(10,1)
    d2=Data(9,2)
    d3=Data(13,3)
    d4=Data(12,4)
    d5=Data(18,5)
    insert(t, d1)
    insert(t, d2)
    insert(t, d3)
    insert(t, d4)
    insert(t, d5)
    print(size(t))
