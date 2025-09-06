def new_list():
    list = {
        "elements": [],
        "size" : 0
    }
    return list

def get_element(my_list, index):
    return my_list["elements"] [index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"] [keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def size(lst):
    return lst["size"]

def first_element(lst):
    if lst["size"] > 0:
        return lst["elements"][0]
    return None

def add_first(lst, element):
    """Inserta element al inicio del array-list."""
    lst["elements"].insert(0, element)
    lst["size"] += 1
    return lst

def add_last(lst, element):
    """Inserta element al final del array-list."""
    lst["elements"].append(element)
    lst["size"] += 1
    return lst

def is_empty(lst):
    return lst["size"] == 0

def last_element(lst):
    if lst["size"] > 0:
        return lst["elements"][lst["size"] - 1]
    return None

def delete_element(lst, index):
    if index >= 0 and index < lst["size"]:
        element = lst["elements"].pop(index)
        lst["size"] -= 1
        return element
    return None

def remove_first(lst):
    if lst["size"] > 0:
        element = lst["elements"].pop(0)
        lst["size"] -= 1
        return element
    return None

def remove_last(lst):
    if lst["size"] > 0:
        element = lst["elements"].pop()
        lst["size"] -= 1
        return element
    return None

def insert_element(lst, index, element):
    if index >= 0 and index <= lst["size"]:
        lst["elements"].insert(index, element)
        lst["size"] += 1
        return True
    return False

def change_element(lst, index, new_element):
    if index >= 0 and index < lst["size"]:
        lst["elements"][index] = new_element
        return True
    return False

def change_info(lst, old_element, new_element, cmp_function):
    index = is_present(lst, old_element, cmp_function)
    if index != -1:
        lst["elements"][index] = new_element
        return True
    return False

def exchange(lst, index1, index2):
    if (index1 >= 0 and index1 < lst["size"]) and (index2 >= 0 and index2 < lst["size"]):
        temp = lst["elements"][index1]
        lst["elements"][index1] = lst["elements"][index2]
        lst["elements"][index2] = temp
        return True
    return False

def sub_list(lst, start_index, end_index):
    if (start_index >= 0 and start_index < lst["size"]) and (end_index >= 0 and end_index < lst["size"]) and (start_index <= end_index):
        new_lst = new_list()
        for i in range(start_index, end_index + 1):
            add_last(new_lst, lst["elements"][i])
        return new_lst
    return None


    