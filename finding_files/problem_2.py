from os import listdir
from os.path import isfile, isdir, exists, realpath, relpath, dirname, join
from collections import deque

BASE_DIR = dirname(realpath(__file__))


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    full_path = join(BASE_DIR, path)
    if exists(full_path) == False:
        return []

    found_paths = set()

    def recurse_path(search_path):
        if isfile(search_path) == True:
            if search_path.endswith(suffix) == False:
                return False
            else:
                found_paths.add(relpath(search_path, BASE_DIR))
                return True
        else:
            suffix_found = False
            for child_path in listdir(search_path):
                if recurse_path(join(search_path, child_path)):
                    found_paths.add(relpath(search_path, BASE_DIR))
                    suffix_found = True

            return suffix_found

    recurse_path(full_path)
    return list(found_paths)


def test_find_files_handles_hidden_files():
    """
      This test checks that hidden files starting with . are handled
    """
    print(f"Testing handling hiddens file")
    result = find_files(".c", "testdir/subdir4")
    assert result == []
    print(f"Expect find_files('.c', 'testdir/subdir4'): {result} to be {None}")


def test_find_files_invalid_path():
    """
      This test checks that the code handles an invalid path being supplied
    """
    print(f"Testing invalid path")
    result = find_files(".c", "invalid")
    assert result == []
    print(f"Expect find_files('.c', 'invalid'): {result} to be {None}")


def test_find_files_suffix_not_found():
    """
      This test checks that the code handles a path that does not contain the supplied suffix. 
      '.c' is used in the examples
    """
    print(f"Testing suffix not found")
    result = find_files(".c", "empty")
    assert result == []
    print(f"Expect find_files('.c', 'empty'): {result} to be {None}")


def test_find_files_suffix_found_in_root():
    """
      This test checks that the code finds the suffix '.c' that is only located at only the root of the path
    """
    print(f"Testing suffix found in root")
    result = find_files(".c", "testdir/subdir5")
    expected = ["testdir/subdir5", "testdir/subdir5/a.c"]
    assert result == expected
    print(f"Expect find_files('.c', 'testdir/subdir5'): {result} to be {expected}")


def test_find_files_suffix_found_in_multiple_levels():
    """
      This test checks that the code finds the suffix '.c' that is only located in multiple path trees in the structure
    """
    print(f"Testing suffix found in multiple levels")
    result = sorted(find_files(".c", "testdir"))
    expected = sorted(
        [
            "testdir",
            "testdir/subdir1",
            "testdir/subdir1/a.c",
            "testdir/subdir3",
            "testdir/subdir3/subsubdir1",
            "testdir/subdir3/subsubdir1/b.c",
            "testdir/subdir5",
            "testdir/subdir5/a.c",
            "testdir/t1.c",
        ]
    )
    assert result == expected
    print(f"Expect find_files('.c', 'testdir'): {result} to be {expected}")


def test_find_files():
    test_find_files_handles_hidden_files()
    print()
    test_find_files_invalid_path()
    print()
    test_find_files_suffix_not_found()
    print()
    test_find_files_suffix_found_in_root()
    print()
    test_find_files_suffix_found_in_multiple_levels()
    print()
    print("Complete all tests")


test_find_files()
