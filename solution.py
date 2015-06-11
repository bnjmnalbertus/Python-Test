partition = []
num_rows = int(raw_input())
num_cols = int(raw_input())

for row in xrange(num_rows):
    in_list = map(int, raw_input().split(" "));
    for col in xrange(num_cols):
        if in_list[col] == 0:
            continue
        else:
            added = False
            added_list = -1
            for i in xrange(len(partition)):
                for p_i in partition[i]:
                    if (row - p_i[0] <= 1) and (abs(col - p_i[1]) <= 1):
                        if added:
                            partition[added_list].extend(partition[i])
                            partition[i] = []
                            #partition.append(partition.pop(added_list) + partition.pop(i))
                        else:
                            partition[i].append((row, col))
                            added = True
                            added_list = i
                        break
            if not added:
                partition.append([(row, col)])
            #print partition
print max(map(len, partition))
        
