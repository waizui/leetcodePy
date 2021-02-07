"""
返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。
如果没有和至少为 K 的非空子数组，返回 -1 。
示例 1：
输入：A = [1], K = 1
输出：1
示例 2：
输入：A = [1,2], K = 4
输出：-1
示例 3：
输入：A = [2,-1,2], K = 3
输出：3
提示：
1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
"""

import collections


#单调队列法 
def shortestSubarray(A:list, K:int):
    ans=len(A)+1    
    presum=[len(A)+1]
    
    for i in range(len(A)):
        presum.append(presum[-1]+A[i])

    monoQ=collections.deque()

    for y in range(len(presum)):
        #如果一直是单调增加的presum则momoQ会一直增大，如果数组A中间有负数就会导致presum不单调增加
        #必须是队列单调增，如果前面有在monoQ中有值大于当前y 那么需要pop掉，不然下面的while会多算一次（此次不会更新ans所以造成时间浪费）
        while monoQ and presum[y]<=presum[monoQ[-1]]:
            monoQ.pop()
        #更新最短子序列
        while monoQ and presum[y]>=presum[monoQ[0]]+K:
            ans=min(ans,y-monoQ.popleft())#pop掉是加入后面的y也可以与对应此monoq的presum值构成大于k的连续数组，但是数组长不可能会比当前的y短，为避免性能浪费，需要pop最小的momoQ
        monoQ.append(y)

    return ans if ans < len(A)+1 else -1


