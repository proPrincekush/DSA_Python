# cook your dish here
def LongestArithmeticSubArray():
    lst = list(map(int,input().split()))
    
    subarr = []
    pd = lst[1]-lst[0]
    ans=curr=j = 2
    ans_sub_arr=curr_sub_arr = [lst[0],lst[1]]
    while(j < len(lst)):
        if(pd == (lst[j]-lst[j-1])):
            curr+=1
            curr_sub_arr.append(lst[j])
        else:
            pd=lst[j]-lst[j-1]
            curr = 2
            curr_sub_arr = [lst[j-1],lst[j]]
            
        if(curr>ans):
            ans = curr
            ans_sub_arr = curr_sub_arr
        j+=1
    print(ans)
    print(*ans_sub_arr)

LongestArithmeticSubArray()  