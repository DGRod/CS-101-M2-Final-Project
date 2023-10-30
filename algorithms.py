from objects import regional_list, LinkedList


def search_list(linked_list, target):
    current_node = linked_list.head_node

    while current_node:
        if str(current_node.value) == target:
            return current_node.value
        current_node = current_node.get_next_node()

    return None

def dfs(node, target, path=None):
    if node.value == target:
        return node
    
    else:
        return dfs(node.get_next_node, target)

#search_list(regional_list, "North Africa").traverse()
print(regional_list.head_node.value)


