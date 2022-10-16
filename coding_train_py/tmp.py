
tree=[3,5,7,-1,-1,2,4]
min_leaf=9999
res=[0]
def dfs(tree,path,index):
    global min_leaf
    left=index*2+1
    right=index*2+2
    if left>=len(tree) and right>=len(tree):
        leaf=tree[index]
        if leaf != -1 and leaf<min_leaf:
            min_leaf=leaf
            res.extend(path)
        return
    path.append(left)
    dfs(tree,path,left)
    path.remove(left)

    path.append(right)
    dfs(tree,path,right)
    path.remove(right)
path=[]
dfs(tree,path,0)
result=[tree[x] for x in res]
print(result)