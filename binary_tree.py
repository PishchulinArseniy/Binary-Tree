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


def create():
    tree = Tree(None)
    return tree


def clear(tree):
    tree.root = None
    return tree


def R(number,a):
    number = number + 1
    if a.right is None and a.left is None:
        return number
    if a.right is not None and a.left is None:
        return R(number,a.right)
    if a.right is None and a.left is not None:
        return R(number,a.left)
    if a.right is not None and a.left is not None:
        return R(number,a.right) + R(number,a.left) - number


def size(tree):
    number = 0
    if tree.root is None:
        return number
    else:
        a = tree.root
        return R( number , a)


def find(tree, key):
    if tree.root is None:
        return None
    else :
        a = tree.root
        tmp = 1
        right_len = 0
        left_len = 0
        while tmp == 1:
            if key > a.data.key:
                if a.right is None:
                    tmp = 0
                    return None
                else:
                    a = a.right
                    right_len = right_len + 1
            if key < a.data.key:
                if a.left is None:
                    tmp = 0
                    return None
                else:
                    a = a.left
                    left_len = left_len + 1
            if key == a.data.key:
                tmp = 0
                return a.data.value


def insert(tree, data):
    if tree.root is None:
        tree.root = Node(None,None,None,data)
        return None
    else :
        a = tree.root
        tmp = 1
        while tmp == 1:
            if data.key > a.data.key:
                if a.right is None:
                    a.right = Node(a,None,None,data)
                    tmp = 0
                    return None
                else :
                    a = a.right
            if data.key < a.data.key:
                if a.left is None:
                    a.left = Node(a,None,None,data)
                    tmp = 0
                    return None
                else :
                    a = a.left
            if data.key == a.data.key:
                ret = a.data
                a.data = data
                tmp = 0
                return ret


def delete(tree, key):
    a = tree.root
    tmp = 1
    d = 0
    while tmp == 1:
        if key > a.data.key:
            if a.right is None:
                return None
            else:
                a = a.right
                d = 1
        if key < a.data.key:
            if a.left is None:
                return None
            else:
                a = a.left
                d = -1
        if key == a.data.key:
            tmp = 0
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
    d5=Data(12,5)
    insert(t, d1)
    insert(t, d2)
    insert(t, d3)
    insert(t, d4)
    insert(t, d5)
    foreach(t, function(3))
