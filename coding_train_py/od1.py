# 给定一个字符串，只包含大写字母，求在包含同一字母的子串中
# 长度第K长的子串，相同字母只取最长的子串

# 输入：第一行 一个子串 1<len<=100 ，只包含大写字母
#           第二行为k的值

# 输出：输出连续出现次数第k多的字母的次数

# 例子：
# 输入
# AABAAA
# 2
# 输出
# 1
# 同一字母连续出现最多的A 3次
# 第二多2次 但A出现连续3次

# 输入

# AAAAHHHBBCDHHHH
# 3

# 输出
# 2

# 如果子串中只包含同一字母的子串数小于k，则输出-1
a="AAAAHHHBBCDHHHHk"
k=3

map={}
num=1
pre=a[0]
map[pre]=1
for i in range(1,len(a)):
    if a[i]==pre:
        num+=1
    else:
        if pre in map:
            map[pre]=max(map[pre],num)
        else:
            map[pre]=num
        num=1
        pre=a[i]
list=list(map.values())
list.sort(reverse=True)
if k > len(list):
    print(-1)
else:
    print(list[k-1])
print(list)