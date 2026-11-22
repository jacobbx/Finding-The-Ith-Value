
import random
import copy


def select_k_sorted(unsorted_first, k):
    
    unsorted = copy.deepcopy(unsorted_first)
        
    if unsorted is None:
        raise ValueError

    if not unsorted:
        raise ValueError
    
    try:
        unsorted[0]
    except TypeError:
        raise ValueError
    except IndexError:
        raise ValueError
            
    if len(unsorted) == 0:
        raise ValueError
    
    if k <= 0 or k > len(unsorted):
        raise IndexError
    
    unsorted = list(unsorted_first)

    if len(unsorted) == 1:
        return unsorted[0]
    
    while len(unsorted) > 1:
        
        unsorted1, unsorted2, pivot = partition(unsorted)
        
        if k <= len(unsorted1):
            unsorted = unsorted1
            if len(unsorted) == 1:
                return unsorted[0]
        else:
            if k == len(unsorted1) + 1:
                return pivot
            else:
                unsorted = unsorted2
                k -= (len(unsorted1) + 1)
                if len(unsorted) == 1:
                    return unsorted[0]


def partition(unsorted):
    unsorted_less_than = []
    unsorted_greater_than_or_equal = []
    
    pivot = random.randint(0, len(unsorted) - 1)
        
    x = unsorted.pop(pivot)
    
    while len(unsorted) > 0:
        y = unsorted.pop(0)
        if y < x:
            unsorted_less_than.append(y)
        elif y >= x:
            unsorted_greater_than_or_equal.append(y)
            
    return unsorted_less_than, unsorted_greater_than_or_equal, x


if __name__ == "__main__":
    my_set = {1, 4, 2}
    # is_indexable = True
    # string_test = "hi"
    # int = 12
    
    # print(select_k_sorted(my_set, 2))
    
    unsorted1 = [4, 9, 2, 1, 3, 7, 6, 8, 5]
    sorted1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    unsorted2 = [10, 14, 11, 15, 12, 13, 16, 18, 17]
    sorted2 = [10, 11, 12, 13, 14, 15, 16, 17, 18]
    
    single_sequence = [1]
    two_value_sequence = [2, 1]
    sorted = [1, 2]
    
    same_values = [1, 1, 1, 1, 1, 0, 0, 0, 0]
    same_values_sorted = [0, 0, 0, 0, 1, 1, 1, 1, 1]
    
    tuple_test = (4, 9, 2, 1, 3, 7, 6, 8, 5)
    string_test2 = "492137685"
    
    print(select_k_sorted(string_test2, 4))
