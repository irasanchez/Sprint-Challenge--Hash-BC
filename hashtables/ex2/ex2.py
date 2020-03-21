#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source  # first flight ticket source is "NONE"
        self.destination = destination  # last flight destination is "NONE"


def reconstruct_trip(tickets, length):
    print("\n\n\n\n\n")
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        # map the tickets to the hash table
        hash_table_insert(hashtable, ticket.source, ticket.destination)

        if ticket.source == "NONE":
            # if this is the first one, add it to the route, since we know where it goes. this also provides a starting point for the next part
            route[0] = ticket.destination

    # put the stops in the route
    for index, stop in enumerate(route):
        # set the next item in the list
        if index != 0:
            # print("INDEX IS NOT 0 OR LENGTH", index)
            previous_stop = route[index-1]
            print("PREV =>", previous_stop)
            current_stop = hash_table_retrieve(hashtable, previous_stop)
            route[index] = current_stop

        print(index, route[index])

    # take the last item off, since it'll be set to "NONE"
    route = route[:-1]

    return route
