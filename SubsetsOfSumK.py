import math

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

# O(n^2)时间复杂度 太慢了
def findSubsetLen(arr:list,K:int):
    left= 0
    right=len(arr)
    hasUpdated=False

    if len(arr)==0:
        return -1

    sum=0

    for i in range(len(arr)):
        if not arr[i]:
            continue

        for j in range(i,len(arr)):
            if not arr[j] and arr[j]!=0:
                break
            sum+=arr[j]
            if sum>=K:
                if j-i<right-left:
                    left=i
                    right=j+1
                    hasUpdated=True
                break
        sum=0

    return (right-left) if hasUpdated else -1 


instr=input("请输入数字 用空格隔开 回车确定\n")

nums=[int(i) for i in instr.split(' ')]

k=input("请输入K")

re=findSubsetLen(nums,k)

print("最短的非空连续子数组的长度为"+str(re))
