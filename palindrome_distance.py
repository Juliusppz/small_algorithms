def palindrome_distance_if_smaller(string, max_distance):
    n = len(string)
    if n == 1:
        return 0
    ind_dict = dict()  # this dict has O(k*n) space complexity, but could be reduced to k with less readability
    tmp_set_iter = set()  # O(k) space complexity
    tmp_set_iter_next = set()  # O(k) space complexity
    result_distances = set()  # O(k) space complexity

    ind_dict[(0, 0)] = 0
    tmp_set_iter.add((1, 1))
    for i in range(min(max_distance, n)):
        ind_dict[(0, i+1)] = i+1
        ind_dict[(i+1, 0)] = i+1

    diag_counter = 1
    # while iterates over ~n/2 diagonals of max width ~2k, resulting in space complexity O(n*k)
    while diag_counter <= n and (len(tmp_set_iter) > 0 or len(tmp_set_iter_next) > 0):  # ends early if no solution
        cur_set_iter = tmp_set_iter
        tmp_set_iter = tmp_set_iter_next
        tmp_set_iter_next = set()
        for element in cur_set_iter:
            if (element[0]-1, element[1]-1) not in ind_dict:
                continue
            if (element[0]-1, element[1]) in ind_dict and (element[0], element[0]-1) in ind_dict:
                if string[element[1]-1] == string[n-element[0]]:
                    value = min(ind_dict[(element[0]-1, element[1])]+1, ind_dict[(element[0], element[1]-1)]+1,
                                ind_dict[(element[0]-1, element[1]-1)])
                else:
                    value = min(ind_dict[(element[0]-1, element[1])]+1, ind_dict[(element[0], element[1]-1)]+1)
            elif (element[0]-1, element[1]) in ind_dict:
                if string[element[1]-1] == string[n-element[0]]:
                    value = min(ind_dict[(element[0]-1, element[1])]+1, ind_dict[(element[0]-1, element[1]-1)])
                else:
                    value = ind_dict[(element[0]-1, element[1])]+1
            elif (element[0], element[1]-1) in ind_dict:
                if string[element[1]-1] == string[n-element[0]]:
                    value = min(ind_dict[(element[0], element[1]-1)]+1, ind_dict[(element[0]-1, element[1]-1)])
                else:
                    value = ind_dict[(element[0], element[1]-1)]+1
            else:
                if string[element[1]-1] == string[n-element[0]]:
                    value = ind_dict[(element[0]-1, element[1]-1)]
                else:
                    value = ind_dict[(element[0]-1, element[1]-1)]+2
            if value <= max_distance:
                tmp_set_iter_next.add((element[0]+1, element[1]+1))
                ind_dict[element] = value
                if diag_counter >= n-1:
                    result_distances.add(value)
                tmp_set_iter.add((element[0], element[1]+1))
                tmp_set_iter.add((element[0]+1, element[1]))
        diag_counter += 1

    if len(result_distances) > 0:
        return min(result_distances)  # find min is O(k)
    else:
        return False
