class CacheNode(object):
    def __init__(self, key, value):
        self.next = None
        self.previous = None
        self.key = key
        self.value = value

    def __str__(self):
        return f"CacheNode({self.key}, {self.value})"


class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.head = None
        self.tail = None
        self.cache = dict()
        self.__capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            node = self.cache[key]
            if node != self.tail:
                if node == self.head:
                    # handle 2 nodes self.head.previous.previous == None
                    next_head = self.head.next

                    if next_head.next == None:
                        # 2 node in queue use case
                        node.previous = next_head
                        next_head.next = node
                    else:
                        node.previous = self.tail
                        self.tail.next = node

                    node.next = None
                    next_head.previous = None
                    self.head = next_head
                    self.tail = node
                else:
                    node_next = node.next
                    node_previous = node.previous

                    node.next = None
                    node.previous = self.tail

                    node_next.previous = node_previous
                    node_previous.next = node_next

                    self.tail.next = node
                    self.tail = node

            return node.value

        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        node = CacheNode(key, value)
        if self.__capacity - len(self.cache) > 0:
            if self.tail == None:
                self.tail = node
                self.head = node
            else:
                node.previous = self.tail
                self.tail.next = node
                self.tail = node
        else:
            self.head.next.previous = None
            del self.cache[self.head.key]
            self.head = self.head.next
            self.tail.next = node
            node.previous = self.tail
            self.tail = node

        self.cache[key] = node

    def __str__(self):
        output = ["########## LRU Cache ##########"]
        output.append(f"cache count left: {self.__capacity - len(self.cache)}")
        output.append("---------- Cache ----------")
        for key in self.cache:
            output.append(f"{key}: {self.cache[key]}")
        output.append("---------- Queue ----------")
        current_node = self.head
        while current_node is not None:
            suffix = ""
            if current_node == self.head:
                suffix = " (Head)"
            elif current_node == self.tail:
                suffix = " (Tail)"
            output.append(f"{current_node}{suffix}")
            current_node = current_node.next

        return "\n".join(output)


def validate_cache(cache, expected_nodes):
    print("----Validating Cache----")
    assert len(cache) == len(expected_nodes)
    for node in expected_nodes:
        assert node.key in cache
        cache_node = cache[node.key]
        assert cache_node.value == node.value
        print(f"Expected {node} to be {cache_node}")


def validate_queue(tail, expected_tail):
    print("----Validating Queue----")
    current_cache_node = tail
    current_expected_node = expected_tail
    while current_cache_node != None or current_expected_node != None:
        assert current_cache_node.value == current_expected_node.value
        if current_cache_node.previous != None:
            assert (
                current_cache_node.previous.value
                == current_expected_node.previous.value
            )
        else:
            assert current_expected_node.previous == None
        if current_cache_node.next != None:
            assert current_cache_node.next.value == current_expected_node.next.value
        else:
            assert current_expected_node.next == None

        print(f"Expected {current_expected_node} to be {current_cache_node}")
        print(
            f"Expected next {current_expected_node.next} to be {current_cache_node.next}"
        )
        print(
            f"Expected previous {current_expected_node.previous} to be {current_cache_node.previous}"
        )
        current_cache_node = current_cache_node.previous
        current_expected_node = current_expected_node.previous


def test_lru_set_empty():
    """
    This function tests the setting of an item when the cache is empty
    Result: 
      cache: (1, 1)
      queue: (1, 1)
  """
    print("****Validating LRU setting 1 element****")
    lru_cache = LRU_Cache(5)
    lru_cache.set(1, 1)

    node = CacheNode(1, 1)
    validate_cache(lru_cache.cache, [node])

    validate_queue(lru_cache.tail, node)


def test_lru_set_empty_with_get():
    """
    This function tests the setting of an item when the cache is empty with get
    Result: 
      cache: (1, 1)
      queue: (1, 1)
  """
    print("****Validating LRU setting 1 element with get****")
    lru_cache = LRU_Cache(5)
    lru_cache.set(1, 1)
    lru_cache.get(1)

    node = CacheNode(1, 1)
    validate_cache(lru_cache.cache, [node])

    validate_queue(lru_cache.tail, node)


def test_lru_set_2_elements():
    """
    This function tests the setting of 2 item when the cache is empty
    Result: 
      cache: (1, 1), (2, 2)
      queue: enqueue -> (2, 2) -> (1, 1) -> dequeue  
  """
    print("****Validating LRU setting 2 elements****")
    lru_cache = LRU_Cache(5)
    lru_cache.set(1, 1)
    lru_cache.set(2, 2)

    nodeOne = CacheNode(1, 1)
    nodeTwo = CacheNode(2, 2)
    validate_cache(lru_cache.cache, [nodeOne, nodeTwo])

    nodeTwo.previous = nodeOne
    nodeOne.next = nodeTwo
    validate_queue(lru_cache.tail, nodeTwo)


def test_lru_set_2_elements_with_get_tail():
    """
    This function tests the setting of 2 item when the cache is empty and performing a get for tail element
    Result: 
      cache: (1, 1), (2, 2)
      queue: enqueue -> (2, 2) -> (1, 1) -> dequeue    
  """
    print("****Validating LRU setting 2 elements with get tail****")
    lru_cache = LRU_Cache(5)
    lru_cache.set(1, 1)
    lru_cache.set(2, 2)
    lru_cache.get(2)

    nodeOne = CacheNode(1, 1)
    nodeTwo = CacheNode(2, 2)
    validate_cache(lru_cache.cache, [nodeOne, nodeTwo])

    nodeTwo.previous = nodeOne
    nodeOne.next = nodeTwo
    validate_queue(lru_cache.tail, nodeTwo)


def test_lru_set_2_elements_with_get_head():
    """
    This function tests the setting of 2 item when the cache is empty and performing a get for head element
    Result: 
      cache: (1, 1), (2, 2)
      queue: enqueue -> (1, 1) -> (2, 2) -> dequeue
  """
    print("****Validating LRU setting 2 elements with get head****")
    lru_cache = LRU_Cache(5)
    lru_cache.set(1, 1)
    lru_cache.set(2, 2)
    lru_cache.get(1)

    nodeOne = CacheNode(1, 1)
    nodeTwo = CacheNode(2, 2)
    validate_cache(lru_cache.cache, [nodeOne, nodeTwo])

    nodeOne.previous = nodeTwo
    nodeTwo.next = nodeOne
    validate_queue(lru_cache.tail, nodeOne)


def test_lru_set_5_elements():
    """
    This function tests the setting of 5 item when the cache is empty
    Result: 
      cache: (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
      queue: enqueue -> (5, 5) -> (4, 4) -> (3, 3) -> (2, 2) -> (1, 1) -> dequeue
  """
    print("****Validating LRU setting 5 elements****")
    lru_cache = LRU_Cache(5)
    lru_cache.set(1, 1)
    lru_cache.set(2, 2)
    lru_cache.set(3, 3)
    lru_cache.set(4, 4)
    lru_cache.set(5, 5)

    nodeOne = CacheNode(1, 1)
    nodeTwo = CacheNode(2, 2)
    nodeThree = CacheNode(3, 3)
    nodeFour = CacheNode(4, 4)
    nodeFive = CacheNode(5, 5)
    validate_cache(lru_cache.cache, [nodeOne, nodeTwo, nodeThree, nodeFour, nodeFive])

    nodeFive.previous = nodeFour
    nodeFour.next = nodeFive
    nodeFour.previous = nodeThree
    nodeThree.next = nodeFour
    nodeThree.previous = nodeTwo
    nodeTwo.next = nodeThree
    nodeTwo.previous = nodeOne
    nodeOne.next = nodeTwo
    validate_queue(lru_cache.tail, nodeFive)


def test_lru_set_5_elements_with_get_tail():
    """
    This function tests the setting of 5 item when the cache is empty with get tail
    Result: 
      cache: (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
      queue: enqueue -> (5, 5) -> (4, 4) -> (3, 3) -> (2, 2) -> (1, 1) -> dequeue
  """
    print("****Validating LRU setting 5 elements with get tail****")
    lru_cache = LRU_Cache(5)
    lru_cache.set(1, 1)
    lru_cache.set(2, 2)
    lru_cache.set(3, 3)
    lru_cache.set(4, 4)
    lru_cache.set(5, 5)
    lru_cache.get(5)

    nodeOne = CacheNode(1, 1)
    nodeTwo = CacheNode(2, 2)
    nodeThree = CacheNode(3, 3)
    nodeFour = CacheNode(4, 4)
    nodeFive = CacheNode(5, 5)
    validate_cache(lru_cache.cache, [nodeOne, nodeTwo, nodeThree, nodeFour, nodeFive])

    nodeFive.previous = nodeFour
    nodeFour.next = nodeFive
    nodeFour.previous = nodeThree
    nodeThree.next = nodeFour
    nodeThree.previous = nodeTwo
    nodeTwo.next = nodeThree
    nodeTwo.previous = nodeOne
    nodeOne.next = nodeTwo
    validate_queue(lru_cache.tail, nodeFive)


def test_lru_set_5_elements_with_get_head():
    """
    This function tests the setting of 5 item when the cache is empty with get head
    Result: 
      cache: (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
      queue: enqueue -> (1, 1) -> (5, 5) -> (4, 4) -> (3, 3) -> (2, 2) -> dequeue 
  """
    print("****Validating LRU setting 5 elements with get head****")
    lru_cache = LRU_Cache(5)
    lru_cache.set(1, 1)
    lru_cache.set(2, 2)
    lru_cache.set(3, 3)
    lru_cache.set(4, 4)
    lru_cache.set(5, 5)
    lru_cache.get(1)

    nodeOne = CacheNode(1, 1)
    nodeTwo = CacheNode(2, 2)
    nodeThree = CacheNode(3, 3)
    nodeFour = CacheNode(4, 4)
    nodeFive = CacheNode(5, 5)
    validate_cache(lru_cache.cache, [nodeOne, nodeTwo, nodeThree, nodeFour, nodeFive])

    nodeOne.previous = nodeFive
    nodeFive.next = nodeOne
    nodeFive.previous = nodeFour
    nodeFour.next = nodeFive
    nodeFour.previous = nodeThree
    nodeThree.next = nodeFour
    nodeThree.previous = nodeTwo
    nodeTwo.next = nodeThree
    validate_queue(lru_cache.tail, nodeOne)


def test_lru_set_5_elements_with_get_middle():
    """
    This function tests the setting of 5 item when the cache is empty with get middle element in queue
    Result: 
      cache: (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
      queue: enqueue -> (3, 3) -> (5, 5) -> (4, 4) -> (2, 2) -> (1, 1) -> dequeue
  """
    print("****Validating LRU setting 5 elements with get middle****")
    lru_cache = LRU_Cache(5)
    lru_cache.set(1, 1)
    lru_cache.set(2, 2)
    lru_cache.set(3, 3)
    lru_cache.set(4, 4)
    lru_cache.set(5, 5)
    lru_cache.get(3)

    nodeOne = CacheNode(1, 1)
    nodeTwo = CacheNode(2, 2)
    nodeThree = CacheNode(3, 3)
    nodeFour = CacheNode(4, 4)
    nodeFive = CacheNode(5, 5)
    validate_cache(lru_cache.cache, [nodeOne, nodeTwo, nodeThree, nodeFour, nodeFive])

    nodeThree.previous = nodeFive
    nodeFive.next = nodeThree
    nodeFive.previous = nodeFour
    nodeFour.next = nodeFive
    nodeFour.previous = nodeTwo
    nodeTwo.next = nodeFour
    nodeTwo.previous = nodeOne
    nodeOne.next = nodeTwo
    validate_queue(lru_cache.tail, nodeThree)


def test_lru_set_6_elements():
    """
    This function tests the setting of 6 item when the cache is empty
    Result: 
      cache: (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)
      queue: enqueue -> (6, 6) -> (5, 5) -> (4, 4) -> (3, 3) -> (2, 2) -> dequeue
  """
    print("****Validating LRU setting 6 elements and removing the oldest****")
    lru_cache = LRU_Cache(5)
    lru_cache.set(1, 1)
    lru_cache.set(2, 2)
    lru_cache.set(3, 3)
    lru_cache.set(4, 4)
    lru_cache.set(5, 5)
    lru_cache.set(6, 6)

    nodeTwo = CacheNode(2, 2)
    nodeThree = CacheNode(3, 3)
    nodeFour = CacheNode(4, 4)
    nodeFive = CacheNode(5, 5)
    nodeSix = CacheNode(6, 6)
    validate_cache(lru_cache.cache, [nodeTwo, nodeThree, nodeFour, nodeFive, nodeSix])

    nodeSix.previous = nodeFive
    nodeFive.next = nodeSix
    nodeFive.previous = nodeFour
    nodeFour.next = nodeFive
    nodeFour.previous = nodeThree
    nodeThree.next = nodeFour
    nodeThree.previous = nodeTwo
    nodeTwo.next = nodeThree
    validate_queue(lru_cache.tail, nodeSix)


def test_lru_get_cache_hit():
    """
    This function tests the getting of an item when the cache contains it
    Result: 
      cache: (1, 1), (2, 2), (3, 3)
      queue: enqueue -> (2, 2) -> (3, 3) -> (1, 1) -> dequeue
      value: 2
  """
    print("****Validating LRU cache missed****")
    lru_cache = LRU_Cache(5)
    lru_cache.set(1, 1)
    lru_cache.set(2, 2)
    lru_cache.set(3, 3)

    result = lru_cache.get(2)
    assert result == 2

    nodeOne = CacheNode(1, 1)
    nodeTwo = CacheNode(2, 2)
    nodeThree = CacheNode(3, 3)
    validate_cache(lru_cache.cache, [nodeOne, nodeTwo, nodeThree])

    nodeTwo.previous = nodeThree
    nodeThree.next = nodeTwo
    nodeThree.previous = nodeOne
    nodeOne.next = nodeThree
    validate_queue(lru_cache.tail, nodeTwo)

    print(f"Cache hit value: {result}")


def test_lru_get_cache_missed():
    """
    This function tests the getting of an item when the cache does not contain it
    Result: 
      cache: (1, 1), (2, 2), (3, 3)
      queue: enqueue -> (3, 3) -> (2, 2) -> (1, 1) -> dequeue
      value: -1
  """
    print("****Validating LRU cache missed****")
    lru_cache = LRU_Cache(5)
    lru_cache.set(1, 1)
    lru_cache.set(2, 2)
    lru_cache.set(3, 3)

    result = lru_cache.get(7)
    assert result == -1

    nodeOne = CacheNode(1, 1)
    nodeTwo = CacheNode(2, 2)
    nodeThree = CacheNode(3, 3)
    validate_cache(lru_cache.cache, [nodeOne, nodeTwo, nodeThree])

    nodeThree.previous = nodeTwo
    nodeTwo.next = nodeThree
    nodeTwo.previous = nodeOne
    nodeOne.next = nodeTwo
    validate_queue(lru_cache.tail, nodeThree)

    print(f"Cache hit value: {result}")


def test_all():
    test_lru_set_empty()
    print()
    test_lru_set_empty_with_get()
    print()
    test_lru_set_2_elements()
    print()
    test_lru_set_2_elements_with_get_tail()
    print()
    test_lru_set_2_elements_with_get_head()
    print()
    test_lru_set_5_elements()
    print()
    test_lru_set_5_elements_with_get_tail()
    print()
    test_lru_set_5_elements_with_get_head()
    print()
    test_lru_set_5_elements_with_get_middle()
    print()
    test_lru_set_6_elements()
    print()
    test_lru_get_cache_hit()
    print()
    test_lru_get_cache_missed()


test_all()


# our_cache = LRU_Cache(5)
# print(str(our_cache))

# our_cache.set(1, 1)
# print(str(our_cache))

# print(our_cache.get(1))  # return 1
# print(str(our_cache))

# our_cache.set(2, 2)
# print(str(our_cache))

# print(our_cache.get(1))  # return 1
# print(str(our_cache))

# our_cache.set(3, 3)
# print(str(our_cache))
# our_cache.set(4, 4)
# print(str(our_cache))

# print(our_cache.get(1))  # returns 1
# print(str(our_cache))
# print(our_cache.get(2))  # returns 2
# print(str(our_cache))
# print(our_cache.get(9))  # returns -1 because 9 is not present in the cache
# print(str(our_cache))

# our_cache.set(5, 5)
# print(str(our_cache))
# our_cache.set(6, 6)
# print(str(our_cache))

# print(our_cache.get(3))
# print(str(our_cache))

# our_cache.set(None, None)
# print(str(our_cache))

# our_cache.set(7, 7)
# print(str(our_cache))

# print(our_cache.get(None))  # returns None
# print(str(our_cache))

# print(our_cache.get(7))  # returns 7
# print(str(our_cache))

# print(our_cache.get(5))  # returns 5
# print(str(our_cache))

# print(our_cache.get(2))  # returns 2
# print(str(our_cache))

# print(our_cache.get(6))  # returns 6
# print(str(our_cache))

# print(our_cache.get(7))  # returns 7
# print(str(our_cache))

# our_cache.set(8, 8)
# print(str(our_cache))
