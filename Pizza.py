children=list(map(int,input().split()))
pizza=list(map(int,input().split()))
children_sum=0
pizza_sum=0
child_count=0
for i in range(0,len(pizza)):
  pizza_sum+=pizza[i]
for j in range(0,len(children)):
  children_sum+=children[j]
  if(children_sum<=pizza_sum):
    child_count+=1
print(child_count)
