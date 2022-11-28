def permute(lst, f=0):
    #base case - no more swaps we can make
    if f >= len(lst):
        print(lst)
        return

    for s in range(f, len(lst)):
        lst[f], lst[s] = lst[s], lst[f]
        permute(lst, f+1)
        lst[f], lst[s] = lst[s], lst[f]


permute([1,2,3])