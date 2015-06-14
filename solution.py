import cProfile

def neighbors(key, dict1):
    # Remove entries adjacent to key in dict1 and add them to list1.
    list1 = []
    for x in [(key[0]-1, key[1]-1),(key[0], key[1]-1),(key[0]+1, key[1]-1),(key[0]-1, key[1]),(key[0]+1, key[1]),(key[0]-1, key[1]+1),(key[0], key[1]+1),(key[0]+1, key[1]+1)]:
        if x in dict1:
            del dict1[x]
            list1.append(x)
    return (list1, dict1)

def grid2dict(grid):
    # Convert the grid of 1's and 0's to a dictionary of coordinate pairs.
    dict1 = {}
    rows = len(grid)
    cols = len(grid[0])

    for row in xrange(rows):
        for col in xrange(cols):
            if grid[row][col] != 0:
                dict1[(row, col)] = None
    return dict1

def solve2(grid):
    # Compute the size of the largest connected component using BFS.
    partition = []
    dict1 = grid2dict(grid)

    while dict1:
        i = 0
        list1 = [dict1.popitem()[0]]
        while i < len(list1):
            (list2, dict1) = neighbors(list1[i], dict1)
            list1.extend(list2)
            i += 1
        partition.append(len(list1))
    return max(partition)
    

def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    # This function partitions a 2-dimensional array of 1's and 0's into its
    # connected components. The result is a list of connected-component sizes.
    partition = [0]
    prev_row = [0] * cols
    for row in xrange(rows):
        curr_row = grid[row]
        for col in xrange(cols):
            if curr_row[col] == 0:
                continue
            else:
                added = 0
                if col > 0 and curr_row[col - 1] != 0:
                    curr_row[col] = curr_row[col - 1]
                    partition[curr_row[col]] += 1
                    added = curr_row[col]

                for x in [col - 1, col, col + 1]:
                    if x < 0:
                        continue
                    if x >= cols:
                        break
                    if prev_row[x] != 0:
                        if added != 0:
                            component = prev_row[x]
                            if added != component:
                                # Update entries in current and previous rows
                                # to unify component indices.
                                for y in xrange(col - 1, cols):
                                    prev_row[y] = added if prev_row[y] == component else prev_row[y]
                                for y in xrange(col):
                                    curr_row[y] = added if curr_row[y] == component else curr_row[y]

                                partition[added] += partition[component]
                        else:
                            curr_row[col] = prev_row[x]
                            partition[curr_row[col]] += 1
                            added = curr_row[col]

                if added == 0:
                    partition.append(1)
                    curr_row[col] = len(partition) - 1

        prev_row = curr_row

    return partition

def main():
    num_rows = int(raw_input())
    num_cols = int(raw_input())
    grid = []

    for row in xrange(num_rows):
        grid.append(map(int, raw_input().split(" ")))

        #if len(grid[row]) != num_cols:
        #    print "Row {0} has the wrong number of columns!".format(row)
        #    return 1

    #print max(solve(grid))
    print solve2(grid)
        
if __name__ == "__main__":
    main()
    #cProfile.run("main()")
