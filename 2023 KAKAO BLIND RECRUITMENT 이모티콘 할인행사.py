def solution(users, emoticons):
    global answer
    dis = [0.6, 0.7, 0.8, 0.9]
    u=len(users)
    e=len(emoticons)

    def search(num,value_list):
        global answer
        if num==e:
            sub=0
            sell=0
            for j in range(u):
                temp=0
                for pri,di in value_list:
                    if users[j][0] <= 100-di*100:
                        temp+=pri
                if temp >= users[j][1]:
                    sub+=1
                else:
                    sell+=temp
            if sub>answer[0]:
                answer[0]=sub
                answer[1]=sell
            elif sub==answer[0] and sell>=answer[1]:
                answer[1]=sell


        else:
            for i in range(4):
                value_list[num]=[emoticons[num]*dis[i],dis[i]]
                search(num+1,value_list)

    answer = [-1, -1]
    value_list=[0]*e
    search(0,value_list)
    answer[1]=int(answer[1])
    return answer

a=solution(	[[10, 100]], [10,10,10,10, 5000])
print(a)