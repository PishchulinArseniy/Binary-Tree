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
    return bt.size(t) == 0


def test_size_null():
    t = bt.create()
    bt.size(t)
    return bt.size(t) == 0


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
    return bt.size(t) == 5


def test_insert_key_in():
    t = bt.create()
    d1 = bt.Data(10, 1)
    d2 = bt.Data(9, 2)
    d3 = bt.Data(9, 6)
    bt.insert(t, d1)
    bt.insert(t, d2)
    return bt.insert(t, d3) == d2


def test_insert_key_not():
    t = bt.create()
    d1 = bt.Data(10, 1)
    d2 = bt.Data(9, 2)
    bt.insert(t, d1)
    return bt.insert(t, d2) == None


def test_delete_key_in():
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
    return bt.delete(t,13).value == 3


def test_delete_key_not():
    t = bt.create()
    d1 = bt.Data(10, 1)
    d2 = bt.Data(9, 2)
    bt.insert(t, d1)
    bt.insert(t, d2)
    return bt.delete(t, 18) == None


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
