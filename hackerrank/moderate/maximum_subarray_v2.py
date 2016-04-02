# https://www.hackerrank.com/challenges/maxsubarray
# status - complete
# time started - 3:50pm
# time started - 4:08pm
# solution - O(n) time with O(c) memory

num_tests = int(raw_input().strip())

answers = []
for t in xrange(num_tests):
    a_size = int(raw_input().strip())
    a = [int(x) for x in raw_input().strip().split()]
    # KADANES ALGO O(n) vvvv
    total_sum = a[0] #TODO
    local_sum = a[0]
    max_non_cont_sum = a[0] #noncontinguous
    for x in a[1:]:
        if x > 0:
            if max_non_cont_sum >= 0:
                max_non_cont_sum += x
            else:
                max_non_cont_sum = x
        else:
            max_non_cont_sum = max(max_non_cont_sum, x)

        local_sum = max(local_sum + x, x)
        if local_sum > total_sum:
            total_sum = local_sum

    answers.append((total_sum, max_non_cont_sum))

for a in answers:
    print a[0], a[1]
