# ## Read input as specified in the question.
# ## Print output as specified in the question.
# def findLeader(l,n):
#     leader=[]
#     for i in range(n):
#         if(i==n-1):

#             break
#         elif(l[i+1]<=l[i]):
#             if(l[i] not in leader):
#                 leader.append(l[i])
#             if(l[i+1] not in leader):
#                 print(l[i+1])
#                 leader.append(l[i+1])
                
#     return leader

# n=int(input("Enter the size of list-:\n"))
# l = [int(item) for item in input().split()]

# print("List-:",l)    
# leader=findLeader(l,n)
# print("Leader-:",leader)    
def find_leaders(arr):
    leaders = []
    max_right = arr[-1]
    leaders.append(max_right)

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] >= max_right:
            max_right = arr[i]
            leaders.append(max_right)

    leaders.reverse()
    return leaders

# Example usage:
n=int(input())
l = [int(item) for item in input().split()]
leader_elements = find_leaders(l)
print(*leader_elements)