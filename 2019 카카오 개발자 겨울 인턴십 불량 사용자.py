# def solution(user_id, banned_id):
#     global answer_list
#     def dfs(bans,cur):
#         global answer_list
#         if len(bans)==1:
#             for i in range(len(bans[0])):
#                 if bans[0][i] in cur : continue
#                 cur.append(bans[0][i])
#                 if set(cur) not in answer_list:
#                     answer_list.append(set(cur))
#             return
#         for i in range(len(bans[0])):
#             if bans[0][i] in cur : continue
#             dfs(bans[1:],cur+[bans[0][i]])
#         return
#     answer_list=[]
#     ban = {}
#     ban_cnt={}
#     bans=[[] for _ in range(len(banned_id))]
#     idx = []
#     for b in banned_id:
#         if b not in ban_cnt:
#             ban_cnt[b]=0
#             ban[b] = []
#         else:
#             ban_cnt[b]+=1
#         temp = [[],0]
#         for i in range(len(b)):
#             if b[i] == '*':
#                 temp[0].append(i)
#         idx.append(temp)
#     for u in user_id:
#         length = len(u)
#         for i in range(len(idx)):
#             if idx[i][0][-1] >= length : continue
#             temp = list(u)
#             for x in idx[i][0]:
#                 temp[x] = '*'
#             mojaik= ''.join(temp)
#             if mojaik in ban :
#                 bans[i].append(u)
#                 ban[mojaik].append(u)
#                 idx[i][1]+=1
#                 # break
#     dfs(bans,[])
#     return len(answer_list)
#
# a=solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
# print(a)


from itertools import permutations

def is_match(user, banned):
    if len(user) != len(banned):
        return False
    for i in range(len(user)):
        if banned[i] != '*' and banned[i] != user[i]:
            return False
    return True

def solution(user_id, banned_id):
    answer_set = set()
    for perm in permutations(user_id, len(banned_id)):
        if all(is_match(user, banned) for user, banned in zip(perm, banned_id)):
            answer_set.add(tuple(sorted(perm)))

    return len(answer_set)
