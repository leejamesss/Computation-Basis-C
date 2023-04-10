str=input()
#给定一个只包含小写字母的字符串，请你找到最后一个仅出现一次的字符。如果没有，输出no。
#例如：输入：abaccdeff
#输出：b
#输入：aabccd
#输出：no

#思路：遍历字符串，用字典存储每个字符出现的次数，再遍历一次字符串，找到最后一个出现次数为1的字符
#时间复杂度：O(n)


#方法一：用字典存储每个字符出现的次数，再遍历一次字符串，找到最后一个出现次数为1的字符
def findLastChar(str):
    dic={}
    for i in str:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in str[::-1]:
        if dic[i]==1:
            return i
    return 'no'

print(findLastChar(str))
