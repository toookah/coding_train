# 3. 用数组储存二叉树，找到到达最小节点的路径
# https://blog.csdn.net/weixin_44052055/article/details/124078351
# 3 5 7 -1 -1 2 4
#  3(0)
#  5(1)          7(2)
# -1(3) -1(4)    2(5)  4(6)

path=[]
tree=[3,5,7,-1,-1,2,4]
res=[0]
min_leaf=float("inf")
def dfs(path,tree,index):
    global min_leaf,res
    left=2*index+1
    right=2*index+2
    if left>=len(tree) and right>=len(tree):
        leaf=tree[index]
        if leaf != -1 and leaf<min_leaf:
            min_leaf=leaf
            res.extend(path)
        return
    
    path.append(left)
    dfs(path,tree,left)
    path.remove(left)

    path.append(right)
    dfs(path,tree,right)
    path.remove(right)

dfs(path,tree,0)
res=[tree[idx] for idx in res]
print(res)
