from multiprocessing import Pool

def mt_solve(grid):
    return

def solve(grid):
    # This function partitions a 2-dimensional array of 1's and 0's into its
    # connected components. The result is a list of connected-component sizes.
    partition = [0]
    prev_row = [0] * len(grid[0])
    for row in xrange(len(grid)):
        curr_row = grid[row]
        for col in xrange(len(grid[row])):
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
                    if x >= len(curr_row):
                        break
                    if prev_row[x] != 0:
                        if added != 0:
                            component = prev_row[x]
                            if added != component:
                                # Update entries in current and previous rows
                                # to unify component indices.
                                for y in xrange(col - 1, len(prev_row)):
                                    prev_row[y] = added if prev_row[y] == component else prev_row[y]
                                for y in xrange(col):
                                    curr_row[y] = added if curr_row[y] == component else curr_row[y]

                                partition[added] += partition[component]
                                partition[component] = 0
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

        if len(grid[row]) != num_cols:
            print "Row {0} has the wrong number of columns!".format(row)
            return 1

    print max(solve(grid))
        
if __name__ == "__main__":
    main()
