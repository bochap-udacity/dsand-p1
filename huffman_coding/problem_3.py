import sys
from itertools import count
from collections import Counter
from heapq import heappop, heappush


class HuffmanNode:
    def __init__(self, key=None, frequency=None, left=None, right=None):
        self.left = left
        self.right = right
        self.key = []
        self.frequency = frequency
        if key == None and frequency == None:
            self.frequency = left.frequency + right.frequency
            self.key = left.key + right.key
        else:
            self.key.append(key)

    def __str__(self):
        return f"frequency: {self.frequency}{f', key: {self.key}' if self.key != None else ''}"


def traverse_tree(root):
    def recurse_node(node, level=0):
        if node == None:
            return

        print(f"{'':<{level*2}}{str(node)}")
        recurse_node(node.left, level + 1)
        recurse_node(node.right, level + 1)

    recurse_node(root)


def construct_huffman_tree(data):
    character_frequency = sorted(Counter(data).items(), key=lambda c: c[1])
    queue = []
    counter = count()
    for index in range(0, len(character_frequency)):
        character = character_frequency[index]
        node = HuffmanNode(character[0], character[1])
        heappush(queue, [node.frequency, next(counter), node])

    while len(queue) > 1:
        _, _, left = heappop(queue)
        if len(queue) == 0:
            heappush(queue, [left.frequency, next(counter), left])
            return

        _, _, right = heappop(queue)
        parent = HuffmanNode(left=left, right=right)
        heappush(queue, [parent.frequency, next(counter), parent])

    _, _, output = queue[0]
    return output


def huffman_encoding(data, debug=False):
    if data == None:
        return None, None

    if data == "":
        return "", None

    tree = construct_huffman_tree(data)
    if tree.left == None and tree.right == None:
        return "0" * len(data), tree

    def recurse_tree(node, value):
        if len(node.key) == 1 and node.key[0] == value:
            return ""

        if node.left != None and value in node.left.key:
            return "0" + recurse_tree(node.left, value)

        return "1" + recurse_tree(node.right, value)

    encoded = []
    for character in data:
        encoded_character = recurse_tree(tree, character)
        encoded.append("".join(encoded_character))

    if debug == True:
        print("".join(encoded))
        traverse_tree(tree)

    return "".join(encoded), tree


def huffman_decoding(data, tree):
    if data == None:
        return None

    if data == "":
        return ""

    if tree.left == None and tree.right == None:
        return tree.frequency * tree.key[0]

    decoded = []
    path_finder = tree
    for index in range(len(data)):
        if data[index] == "0":
            path_finder = path_finder.left
        else:
            path_finder = path_finder.right

        if path_finder.left == None and path_finder.right == None:
            decoded.append(path_finder.key[0])
            path_finder = tree

    return "".join(decoded)


def test_encode_multi_character(
    test_case, raw_value, expected_encoded_data, expected_frequency
):
    print(test_case)
    encoded_data, tree = huffman_encoding(raw_value)
    assert encoded_data == expected_encoded_data
    assert tree.frequency == expected_frequency
    print(
        f"huffman_encoding('{raw_value}') expects encoded: {encoded_data}, tree: {tree}"
    )


def test_encode_none():
    """
      Test encoding input None
    """
    print("Testing encoding None")
    encoded_data, tree = huffman_encoding(None)
    assert encoded_data == None
    assert tree == None
    print(f"huffman_encoding('{None}') expects encoded: {encoded_data}, tree: {tree}")


def test_encode_empty_string():
    """
      Test encoding input empty string ""
    """
    print("Testing encoding empty string")
    encoded_data, tree = huffman_encoding("")
    assert encoded_data == ""
    assert tree == None
    print(f"huffman_encoding('') expects encoded: {encoded_data}, tree: {tree}")


def test_encode_single_character():
    """
      Test encoding input single character string "a"
    """
    print("Testing encoding single character")
    encoded_data, tree = huffman_encoding("a")
    assert encoded_data == "0"
    assert tree.key == HuffmanNode("a").key
    assert tree.left == None
    assert tree.right == None
    assert tree.frequency == 1
    print(f"huffman_encoding('a') expects encoded: {encoded_data}, tree: {tree}")


def test_encode_2_characters():
    """
      Test encoding input 2 character string "ab"
    """
    test_encode_multi_character("Testing encoding 2 characters", "ab", "01", 2)


def test_encode_3_characters():
    """
      Test encoding input 3 character string "abc"
    """
    test_encode_multi_character("Testing encoding 3 characters", "abc", "10110", 3)


def test_encode_4_characters():
    """
      Test encoding input 4 character string "abcd"
    """
    test_encode_multi_character("Testing encoding 4 characters", "abcd", "00011011", 4)


def test_encode_4_repeated_characters():
    """
      Test encoding input 4 character string "aaaa"
    """
    test_encode_multi_character(
        "Testing encoding 4 repeated characters", "aaaa", "0000", 4
    )


def test_encode_word_bird():
    """
      Test encoding input word string "bird"
    """
    test_encode_multi_character("Testing encoding word 'bird'", "bird", "00011011", 4)


def test_encode_sentence():
    """
      Test encoding input sentence string "The bird is the word"
    """
    test_encode_multi_character(
        "Testing encoding sentence string 'The bird is the word'",
        "The bird is the word",
        "0110111011111100111000001010110000100011010011110111111010101011001010",
        20,
    )


def test_huffman_encoding():
    test_encode_none()
    print()
    test_encode_empty_string()
    print()
    test_encode_single_character()
    print()
    test_encode_2_characters()
    print()
    test_encode_3_characters()
    print()
    test_encode_4_characters()
    print()
    test_encode_4_repeated_characters()
    print()
    test_encode_word_bird()
    print()
    test_encode_sentence()


def test_decode_multi_character(test_case, raw_value, expected_decoded_data):
    print()
    print(test_case)
    encoded_data, tree = huffman_encoding(raw_value)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == expected_decoded_data
    print(f"huffman_decoding('{encoded_data},{tree}') expects decoded: {decoded_data}")
    print()


def test_decode_none():
    """
      Test decoding input None
    """
    print()
    print("Testing decoding None")
    encoded_data, tree = huffman_encoding(None)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == None

    print(f"huffman_decoding({None}, {tree}) expects decoded: {decoded_data}")
    print()


def test_decode_empty():
    """
      Test decoding input ''
    """
    print("Testing decoding ''")
    encoded_data, tree = huffman_encoding("")
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == ""

    print(f"huffman_decoding({encoded_data}, {tree}) expects decoded: {decoded_data}")
    print()


def test_decode_single_character():
    """
      Test decoding input single character string "a"
    """
    print("Testing decoding single character")
    encoded_data, tree = huffman_encoding("a")
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == "a"
    print(f"huffman_decoding({encoded_data}, {tree}) decoded: {decoded_data}")


def test_decode_2_characters():
    """
      Test decoding input 2 character string "ab"
    """
    test_decode_multi_character("Testing decoding 2 characters", "ab", "ab")


def test_decode_3_characters():
    """
      Test decoding input 3 character string "abc"
    """
    test_decode_multi_character("Testing decoding 3 characters", "abc", "abc")


def test_decode_4_characters():
    """
      Test decoding input 4 character string "abcd"
    """
    test_decode_multi_character("Testing decoding 4 characters", "abcd", "abcd")


def test_decode_4_repeated_characters():
    """
      Test decoding input 4 character string "aaaa"
    """
    test_decode_multi_character("Testing decoding 4 characters", "aaaa", "aaaa")


def test_decode_word_bird():
    """
      Test decoding input word string "bird"
    """
    test_decode_multi_character("Testing decoding word 'bird'", "bird", "bird")


def test_decode_sentence():
    """
      Test decoding input sentence string "The bird is the word"
    """
    test_decode_multi_character(
        "Testing encoding sentence string 'The bird is the word'",
        "The bird is the word",
        "The bird is the word",
    )


def test_huffman_decoding():
    test_decode_none()
    test_decode_empty()
    test_decode_single_character()
    test_decode_2_characters()
    test_decode_3_characters()
    test_decode_4_repeated_characters()
    test_decode_word_bird()
    test_decode_sentence()


def test_all():
    test_huffman_encoding()
    test_huffman_decoding()


if __name__ == "__main__":
    test_all()

    test_huffman_encoding()

    a_great_sentence = "The bird is the word"
    print()
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(
        "The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))
        )
    )
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))
