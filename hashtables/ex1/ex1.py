#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    for index in range(0, length):
        # Set weight to that indexed value
        weight = weights[index]
        # Get the difference between 21 and weight
        difference = limit - weight
        
        # Validate if the result of difference is in hash
        validate = hash_table_retrieve(ht, difference)
        
        # If validate returns a value
        if validate is not None:
            # Return that key value result
            return (index, validate)

        # Insert the hash table, weight, and index
        hash_table_insert(ht, weight, index)

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
