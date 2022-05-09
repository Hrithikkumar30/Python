# n = int(input())
# per_bag_items=10
# i=0
# j=0
# while(i <n):
#     items=int(input())
#     i+=1
#     while(j<i):
#         print(items//per_bag_items)
#         j+=1

n = int(input())
total_money = 100
i=0


while(i<n):
    num = int(input())
    i+=1
    print(total_money-num)
    