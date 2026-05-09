import binary_tree as bt


def test_clear():
    t = bt.create()
    d1 = bt.Data(10, 1)
    d2 = bt.Data(9, 2)
    d3 = bt.Data(13, 3)
    d4 = bt.Data(12, 4)
    d5 = bt.Data(16, 5)
    bt.insert(t, d1)
    bt.insert(t, d2)
    bt.insert(t, d3)
    bt.insert(t, d4)
    bt.insert(t, d5)
    bt.clear(t)
    is_true = t.root == None
    return is_true


def test_size_null():
    t = bt.create()
    bt.size(t)
    is_true = bt.size(t) == 0
    return is_true


def test_size_not_null():
    t = bt.create()
    d1 = bt.Data(10, 1)
    d2 = bt.Data(9, 2)
    d3 = bt.Data(13, 3)
    d4 = bt.Data(12, 4)
    d5 = bt.Data(16, 5)
    bt.insert(t, d1)
    bt.insert(t, d2)
    bt.insert(t, d3)
    bt.insert(t, d4)
    bt.insert(t, d5)
    is_true = bt.size(t) == 5
    return is_true


def test_insert_key_in():
    t = bt.create()
    d1 = bt.Data(10, 1)
    d2 = bt.Data(9, 2)
    d3 = bt.Data(9, 6)
    bt.insert(t, d1)
    bt.insert(t, d2)
    is_true = bt.insert(t, d3).value == 2
    return is_true


def test_insert_key_not():
    t = bt.create()
    d1 = bt.Data(10, 1)
    d2 = bt.Data(9, 2)
    bt.insert(t, d1)
    is_true = bt.insert(t, d2) == None
    return is_true


def test_delete_key_in():
    is_true = False
    t = bt.create()
    d1 = bt.Data(10, 1)
    d2 = bt.Data(9, 2)
    d3 = bt.Data(13, 3)
    d4 = bt.Data(12, 4)
    d5 = bt.Data(16, 5)
    bt.insert(t, d1)
    bt.insert(t, d2)
    bt.insert(t, d3)
    bt.insert(t, d4)
    bt.insert(t, d5)
    if bt.delete(t,13).value == 3:
        if t.root.right.data.key == 16 and t.root.right.left.data.key == 12:
            is_true = True
        else:
            is_true = False
    return is_true


def test_delete_key_not():
    t = bt.create()
    d1 = bt.Data(10, 1)
    d2 = bt.Data(9, 2)
    bt.insert(t, d1)
    bt.insert(t, d2)
    is_true = bt.delete(t, 18) == None
    return is_true


def run_all_tests():
    all_tests = [test_clear(), test_size_null(),test_size_not_null(),test_insert_key_not(),test_insert_key_in(),
                 test_delete_key_in(),test_delete_key_not()]
    all_tests_name = ["test_clear", "test_size_null","test_size_not_null","test_insert_key_not","test_insert_key_in",
                 "test_delete_key_in","test_delete_key_not"]
    tmp4 = 0
    for test in all_tests:
        if test == True:
            print(all_tests_name[tmp4],"  ","passed")
        else:
            print(all_tests_name[tmp4],"  ","failed")
        tmp4 = tmp4 + 1


run_all_tests()
