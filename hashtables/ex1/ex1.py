#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(0, len(weights)):
        hash_table_insert(ht , weights[i] , i )
    
    for j in range(0, len(weights)):
        found_value = hash_table_retrieve(ht, (limit - weights[j]))
        if found_value is not None:
            if found_value > j:
                return (found_value, j)
            else:
                return (j, found_value)
    ##why this indent            
    return None
        
                

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

weights = [4, 6, 10, 15, 16]
limit = 21

answer = get_indices_of_item_weights(weights, 5, limit)
print(answer)
