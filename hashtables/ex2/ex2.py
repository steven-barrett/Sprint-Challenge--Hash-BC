#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    hashtable = HashTable(length)
    route = [None] * length
    # print(tickets)
    # insert tickets in ht /// source and destination from class
    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)

    # count for iteration
    count = 0
    # current/start location
    key = "NONE"
    # while the last element in the route list is None, it means we haven't hit the end, so keep going
    while route[-1] is None:
        # find where the next flight is, store it here. The return of the hash_retrieve is the key of the next flight
        next_flight = hash_table_retrieve(hashtable, key)
        # add the flight to the route list
        route[count] = next_flight        
        # increment in order to keep moving through list
        count += 1
        # change key to where you're at on the list now
        key = next_flight

    print(route)
    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets, 3)