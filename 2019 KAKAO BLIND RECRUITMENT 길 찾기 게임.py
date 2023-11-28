from collections import deque
def solution(nodeinfo,root_x):
    global later
    later=[]
    def make_tree(arr):
        global later
        temp_y=nodeinfo[0][1]
        root_list=[]
        for i in range(len(nodeinfo)):
            if nodeinfo[i][1]==temp_y:
                root_list.append(nodeinfo[i])
            else:
                nodeinfo=nodeinfo[i:]
                break

        if len(root_list)==1:
            l,r=[],[]
            c_x=root_list[0][0]
            for i in range(len(nodeinfo)):
                if nodeinfo[i][0] < c_x:
                    l.append(nodeinfo[i])
                else:
                    r.append(nodeinfo[i])

        else:
            l, lr, rl, rr = [], [], [], []
            ll_x,lr_x,rl_x,rr_x=
            for i in range(len(nodeinfo)):






    cnt=1
    answer = [[]]
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(cnt)
        cnt+=1
    nodeinfo.sort(key=lambda x: (-x[1],x[0]))
    print(nodeinfo)
    tree={}
    q=deque([])
    pre=[nodeinfo[0][2]]
    root_y=nodeinfo[1]
    root_list=[nodeinfo[0]]
    for i in range(1,len(nodeinfo)):
        pre.append(nodeinfo[i][2])
        if nodeinfo[i][1]<root_y:
            root_list=temp[:]
        else:
            for j in range(len(root_list)):


            temp.append(nodeinfo[i])

    return answer

a=solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])