def add_row(prev_row, curr_row, partition):
    for col in xrange(len(curr_row)):
        if curr_row[col] == 0:
            continue
        else:
            # When the current row and column of the input contains a 1,
            # check for adjacent nodes (grid values of 1). If any
            # adjacent nodes are found (among previously-seen nodes), add
            # the new node to the adjacent node's connected component. This
            # entails setting the current node's grid value to value of the
            # index of the connected component (in partition), then
            # incrementing the size of the connected component in
            # partition.
            # Note that we store each index plus 1 in the grid, since 0
            # indicates that no node exists there.
            added = 0

            if col > 0 and curr_row[col - 1] != 0:
                # The previous node exists, so copy the index of its
                # connected component into the current node and into added
                # and increment its size in partition.
                curr_row[col] = curr_row[col - 1]
                partition[curr_row[col] - 1] += 1
                added = curr_row[col]

            for x in [col - 1, col, col + 1]:
                # Check the adjacent positions in the previous row for an
                # adjacent node.
                if x < 0:
                    continue
                if x >= len(curr_row):
                    break
                if prev_row[x] != 0:
                    # An adjacent node is found in the previous row.
                    if added != 0:
                        # The new node has already been added to a
                        # component. Update indices in the previous row to
                        # replace the new component with the existing one,
                        # and add the newly-discovered components size to
                        # that of the existing one in the partition.
                        component = prev_row[x]
                        if added != component:
                            prev_row = map(lambda y: added if y == component else y, prev_row)
                            partition[added - 1] += partition[component - 1]
                            partition[component - 1] = 0
                    else:
                        # Add the new node to the connected component of
                        # the adjacent node.
                        curr_row[col] = prev_row[x]
                        partition[curr_row[col] - 1] += 1
                        added = curr_row[col]

            if added == 0:
                # If no nodes were found adjacent to the new node, create a
                # new, empty connected component and put the new node into
                # it.
                partition.append(1)
                curr_row[col] = len(partition)

    return (curr_row, partition)

def main():
    # This function computes the sizes of the connected components of the graph
    # and prints the largest.
    partition = [] # A list of ints representing the size of each component
    num_rows = int(raw_input()) # Number of rows in the input
    num_cols = int(raw_input()) # Number of columns per row
    in_list = [0] * num_cols    # Lists representing the current and previous
    prev_list = [0] * num_cols  # rows are initialized to all-zeros.

    for row in xrange(num_rows):
        in_list = map(int, raw_input().split(" "))

        if len(in_list) != num_cols:
            print "Row {0} has the wrong number of columns!".format(row)
            return 1

        (prev_list, partition) = add_row(prev_list, in_list, partition)

    print max(partition)
        
if __name__ == "__main__":
    main()
