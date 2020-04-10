class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def consolidate(llist_1, llist_2):
    found = {}
    current_item_1 = llist_1.head
    current_item_2 = llist_2.head
    while current_item_1 != None or current_item_2 != None:
        if current_item_1 != None:
            if current_item_1.value in found:
                found[current_item_1.value] |= 1
            else:
                found[current_item_1.value] = 0 | 1
            current_item_1 = current_item_1.next

        if current_item_2 != None:
            if current_item_2.value in found:
                found[current_item_2.value] |= 2
            else:
                found[current_item_2.value] = 0 | 2
            current_item_2 = current_item_2.next

    return found


def union(llist_1, llist_2):
    found = consolidate(llist_1, llist_2)
    output = []
    for key, _ in found.items():
        output.append(key)

    return output


def intersection(llist_1, llist_2):
    found = consolidate(llist_1, llist_2)
    output = []
    for key, value in found.items():
        if value & 3 == 3:
            output.append(key)

    return output


def test_case_helper(
    testcase, element_1, element_2, expected_union, expected_intersection
):
    print()
    print(testcase)
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    assert sorted(union(linked_list_1, linked_list_2)) == expected_union
    assert sorted(intersection(linked_list_1, linked_list_2)) == expected_intersection
    print(f"union([{linked_list_1}], [{linked_list_2}]) = {expected_union}")
    print(
        f"intersection([{linked_list_1}], [{linked_list_2}]) = {expected_intersection}"
    )
    print()


def test_case_1():
    """
      Testing case with duplicate entries found in the same list with union and intersection
    """
    test_case_helper(
        "Testing case with duplicate entries found in the same list with union and intersection",
        [3, 2, 4, 35, 6, 65, 6, 4, 3, 21],
        [6, 32, 4, 9, 6, 1, 11, 21, 1],
        [1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65],
        [4, 6, 21],
    )


def test_case_2():
    """
      Testing case with duplicate entries found in the same list with no intersection
    """
    test_case_helper(
        "Testing case with duplicate entries found in the same list with no intersection",
        [3, 2, 4, 35, 6, 65, 6, 4, 3, 23],
        [1, 7, 8, 9, 11, 21, 1],
        [1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65],
        [],
    )


def test_case_3():
    """
      Testing case with no common entries both lists with no intersection
    """
    test_case_helper(
        "Testing case with no common entries both lists with no intersection",
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [],
    )


def test_all():
    test_case_1()
    test_case_2()
    test_case_3()


test_all()
