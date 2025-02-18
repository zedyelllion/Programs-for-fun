def mcs(a):
    dp = []
    dp.append(a[-1])
    for i in range (len(a)-1):
        if (dp[i] > 0):
            dp.append(dp[i] + a[-i-2])
        else :
            dp.append(a[-i-2])
    if(max(dp) < 0):
        return 
    end_index = dp.index(max(dp))
    for i in range(end_index):
        j = end_index - i
        if(dp[j] < 0):
            break
    begin_index = j
    print(begin_index)
    print(end_index)
    cut = a[-end_index-1:-begin_index-1]
    return cut
    
a = [-1,-100]
b = mcs(a)
print(b)

#(i): One can brute force the problem by trying all possible subsequences. By choosing distinct starting
# and ending index, there are roughly n^2/2 possible combinations, and the calculation of each subsequence
# may take O(n) time, thus the algorithm will run in O(n^3), much slower compared to dp solution.

#(ii): We can record the maximum subsequence starting at index i, we do this recording process backward. 
#If the elements after a[-i] sums postive, then we add it up to a[-i] and record it to dp[i-1]. Otherwise,
#if the sum is negative, then there's no need to include them, thus we just record the value of
# a[-i] to dp[i-1]. The algorithm takes big theta(n) time because it has to go over the entire list once.
# Then all values in the dp[] is filled up. Then the algorithm can look for the max value in dp, and go 
#backward to find the last bigger than 0 value in dp. Record these two indices and output the subsequnce.
# This takes big theta(n) time. Thus the algorithm takes big theta(n) time overall(traversing the list for twice).

