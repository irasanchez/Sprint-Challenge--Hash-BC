#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # start answer as none, so it returns properly if no changes are made
    answer = None
    # insert (weight, index) pairs in the hash table
    for index, weight in enumerate(weights):
        hash_table_insert(ht, weight, index)

    # now that we've added the items to ht, we can go through and check
    for index, weight in enumerate(weights):
        key = limit - weight

        # if the key exists
        if hash_table_retrieve(ht, key) is not None:
            # reset the answer if this is the first one we've found
            if answer is None:
                answer = (index,)
            else:
                # add to the answer if it's not the first one
                answer = answer + (index,)

    # if the answer's been changed at this point at all by the above loop,
    if answer is not None:
        # check to see if we have a pair
        if len(answer) == 2:
            if answer[1] > answer[0]:
                # correct the order if not in the right order already
                answer = (answer[1], answer[0])

    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
