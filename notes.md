uper day 1

understand phase:

    first task is to implement HashTable class and HashTable entry class, code for these has already been started

    second task is to implement a good hashing function, recommnded to use either DJB2 or FNV-1, allowed to google for pseudocode

    third task is to implement hash_index to return an index value for a key

    fourth task is to implement put(), get(), and delete() methods

plan phase:

    complete class layout

    find pseudocode for hashing algorithm

    implement class methods

uper day 2

understand phase:

    modify put(), get(), and delete() to handle collisions via chaining

    compute and maintain load factor; load factor is the ratio of size to capacity, for this assignment, if the load factor is above 70%, double the size of the hashtable, if it is below 20%, stretch goal is to reduce the size of the hash table by half

plan phase:

    *** do first
    put(), get(), and delete() methods will now be written for linked lists instead of a list; the linked lists will still be contained within a list, so will still need the index algorithm to determine where on the list the methods will go
        to add value, hash for index, if index has no value, the key and the value become an entry at that index, specifically, it will become the head of a linked list at that index, otherwise the key-value becomes the head of the linked list at that index and the head of that linked list becomes the new key-values next node

        to search value, hash for index, if index has no value, return none, otherwise traverse the linked list at that index
            if the head is the value, return it, otherwise continue through the linked list, if the value is found, return it, otherwise, return none

        to delete value, hash for index, if the index has no value, return none, otherwise traverse the linked list at that index
            if the head is the value, assign the key-value of the head's next pointer to the new head, and assign the head's next pointer to none, otherwise, travers the list for the value

            if the value is in the linked list, make the next pointer of the node before the target point to the node after the target, make the target's next pointer point to none

            if the target is not in the linked list, return none 

    the list size counter will increment whenever a key and value is added, and then it will decrement whenever a key and value are removed

    load factor will keep track of the ratio size to capacity, if the load factor gets abover .7, double the hashtable size, if there's time, work on halfing the table when load factor gets below .2

    when resizing, doubling should trigger on put() operations, and halving should trigger on delete() operations; resize function should also redistribute key-value pairs across resized hash table

