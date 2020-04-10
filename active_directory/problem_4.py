class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def get_group_users(root_group):
    users = set()

    def recurse_group(parent_group):
        for user in parent_group.get_users():
            users.add(user)

        for group in parent_group.get_groups():
            recurse_group(group)

    recurse_group(root_group)
    return users


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group == None:
        return False
    return user in get_group_users(group)


def test_is_user_in_group_helper(usecase, username, group, expected_found):
    print(usecase)
    output = is_user_in_group(username, group)
    assert output == expected_found
    print(
        f"{username}{'' if expected_found else ' not'} in Group [name: {group.get_name()}, users: {get_group_users(group)}]"
    )


def test_user_not_in_null_group():
    """
      Testing user not found if group provided is None
    """
    print("test user not in None group")
    username = "not_found"
    output = is_user_in_group(username, None)
    assert output == False
    print(f"{username} not in Group: {None}")


def test_user_not_in_empty_group():
    """
      Testing user not found if provided group with no parent or child has no users
    """
    group = Group("empty")
    username = "not_found"
    test_is_user_in_group_helper("test user not in empty group", username, group, False)


def test_user_not_in_individual_group():
    """
      Testing user not found if provided group with no parent or child has one users that has a different name
    """
    group = Group("empty")
    group.add_user("found")
    username = "not_found"
    test_is_user_in_group_helper(
        "test user not in individual group", username, group, False
    )


def test_user_not_in_individual_group_with_multiple_users():
    """
      Testing user not found if provided group with no parent or child has multiple users with different names
    """
    group = Group("empty")
    group.add_user("found1")
    group.add_user("found2")
    group.add_user("found3")
    username = "not_found"
    test_is_user_in_group_helper(
        "test user not in individual group with multiple users", username, group, False
    )


def test_user_in_individual_group():
    """
      Testing user found if provided group with no parent or child has single user with same name
    """
    group = Group("individual")
    group.add_user("found")
    username = "found"
    test_is_user_in_group_helper("test user in individual group", username, group, True)


def test_user_in_individual_group_with_multiple_users():
    """
      Testing user found if provided group with no parent or child has multiple users and one with same name
    """
    group = Group("individual")
    group.add_user("found1")
    group.add_user("found2")
    group.add_user("found3")
    username = "found2"
    test_is_user_in_group_helper(
        "test user in individual group with multiple users", username, group, True
    )


def test_user_not_in_parent_child_group():
    """
      Testing user not found if provided group has child group with no users with same name
    """
    parent = Group("parent")
    parent.add_user("parent_found")
    child = Group("child")
    child.add_user("child_found")
    parent.add_group(child)
    username = "not_found"
    test_is_user_in_group_helper(
        "test user not in parent child group", username, parent, False
    )


def test_user_in_child_of_parent_child_group():
    """
      Testing user found if provided group has child group with one users with same name
    """
    parent = Group("parent")
    parent.add_user("parent_found")
    child = Group("child")
    child.add_user("child_found")
    parent.add_group(child)
    username = "child_found"
    test_is_user_in_group_helper(
        "test user in child of parent child group", username, parent, True
    )


def test_user_in_grandchild_of_parent_child_group():
    """
      Testing user found if provided group has grandchild group with one users with same name
    """
    parent = Group("parent")
    parent.add_user("parent_found")
    child = Group("child")
    child.add_user("child_found")
    parent.add_group(child)
    grandchild = Group("grandchild")
    grandchild.add_user("grandchild_found")
    child.add_group(grandchild)
    username = "grandchild_found"
    test_is_user_in_group_helper(
        "test user in child of parent child group", username, parent, True
    )


def test_is_user_in_group():
    test_user_not_in_null_group()
    print()
    test_user_not_in_empty_group()
    print()
    test_user_not_in_individual_group()
    print()
    test_user_not_in_individual_group_with_multiple_users()
    print()
    test_user_in_individual_group()
    print()
    test_user_in_individual_group_with_multiple_users()
    print()
    test_user_not_in_parent_child_group()
    print()
    test_user_in_child_of_parent_child_group()
    print()
    test_user_in_grandchild_of_parent_child_group()


test_is_user_in_group()
