#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    answer = []
    for index, item in enumerate(weights):
        weight_left = limit - item
        # print('looking for key', weight_left,
        hash_table_retrieve(ht, weight_left)
        if hash_table_retrieve(ht, weight_left) != None:
            # print('found item') 
            if hash_table_retrieve(ht, weight_left) > index:
                answer.append(hash_table_retrieve(ht, weight_left))
                answer.append(index)
            else:
                answer.append(index)
                answer.append(hash_table_retrieve(ht, weight_left))
        hash_table_insert(ht, item, index)
    # print(answer)
    if len(answer) == 2:
        return tuple(answer)
    else:
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
