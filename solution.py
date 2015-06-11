
def add_node(row, col, partition, num_cols):
    # This function adds a node to the partition list. To do this, it checks
    # each connected component in the partition to find adjacent nodes. When
    # an adjacent node is found, the new node is added to the adjacent node's
    # component or, if the new node has already been added to another
    # component, then the two adjacent components are unified. Finally, in the
    # case where no adjacent node is found, a new component containing only
    # the new node is added to the partition.

    # Parameters:
    # row       the row of the new node
    # col       the column of the new node
    # partition a list of connected components, each one itself a list of nodes
    # num_cols  the number of columns in the input
    added = -1
    for i in xrange(len(partition)):
        for p_i in reversed(partition[i]):
            if row - (p_i // num_cols) > 1:
                # Only compare nodes in the current or immediately previous 
                # row. This works as long as individual connected components
                # are sorted.
                break
            if abs(col - (p_i % num_cols)) <= 1:
                if added != -1:
                    # If the new node has already been added to another
                    # component, adjacency to another component requires that
                    # the two connected components be unified.
                    partition[added].extend(partition[i])
                    partition[added].sort()
                    partition[i] = []
                else:
                    # Add the new node to the connected component of the first-
                    # matched, adjacent node.
                    partition[i].append((row * num_cols) + col)
                    added = i
                break
    if added == -1:
        # If no existing nodes are found to be adjacent, then create a new
        # component for the newly-created node.
        partition.append([(row * num_cols) + col])

def main():
    partition = []
    num_rows = int(raw_input())
    num_cols = int(raw_input())

    for row in xrange(num_rows):
        in_list = map(int, raw_input().split(" "));
        for col in xrange(num_cols):
            if in_list[col] == 0:
                continue
            else:
                add_node(row, col, partition, num_cols)
    print max(map(len, partition))
        
if __name__ == "__main__":
    #main()
    import cProfile
    cProfile.run('main()')
