#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


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
    # Add tickets to the hash table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # First item has a 'NONE' value
    route[0] = hash_table_retrieve(hashtable, 'NONE')

    # Start with 1, since 0th is confirmed
    for i in range(1, length):
        # Next destination uses the previous key as destination value
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    # Remove the destination 'NONE' value
    return route[0:length-1]


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets, 3)