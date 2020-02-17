#!/usr/bin/env python

# QUIP ONSITE 1.5 hrs total (about 70 min coding)

import heapq

# import sys

k = 10


document_id_to_name = {}
my_heap = None


# document-ids.txt, document-views.txt
def start():
    for row in open("document-ids.txt"):
        row = row.rstrip()
        docu_id, *rest = row.split(" ")
        docu_name = " ".join(rest)
        document_id_to_name[docu_id] = [docu_name, 0]

    for row in open("document-views.txt"):
        docu_id = row.rstrip()
        viewed(docu_id)
    # Must use the global keyword or python will assume its a local variable
    # due to the reassignment
    global my_heap
    my_heap = [(-lst[1], key) for key, lst in document_id_to_name.items()]
    # print(my_heap)
    heapq.heapify(my_heap)


def viewed(docu_id):
    document_id_to_name[docu_id][1] += 1
    if not my_heap:
        return
    heapq.heappush(my_heap, (-document_id_to_name[docu_id][1], docu_id))


def view_document(document_id):
    viewed(document_id)


def get_suggestions():
    seen = set()
    i = 1
    output = []
    while i <= k:
        data = heapq.heappop(my_heap)
        if data[1] not in seen:
            output.append([document_id_to_name[data[1]][0], data[1], -data[0]])
            i += 1
        seen.add(data[1])
    # Add back in the nodes (ignoring those that were extra) - this is incase
    # suggestion is called again in the loop
    for item in output:
        my_heap.append((-item[2], item[1]))
        heapq.heapify(my_heap)
    return output

    # STARTER CODE:

    # return [["Gone with the Wind", "34722", 12],
    #     ["War and Peace", "7612", 18],
    #     ["Pride and Prejudice", "23454", 1],
    #     ["Quip New Engineer Handbook", "2682", 55]]


if __name__ == "__main__":
    start()
    while True:
        print("Waiting for input...")
        line = input()
        if line == "s":
            print("Suggestions")
            print(
                "\n".join([str(suggestion) for suggestion in get_suggestions()])
                + "\n"
            )
        elif line[0] == "v":
            print("Viewing document %s\n" % line[2:])
            view_document(line[2:])
        else:
            print("Input must be 's' or 'v <document_id>'.\n")
