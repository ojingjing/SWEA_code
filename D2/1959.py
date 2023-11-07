from collections import deque
t= int(input())

for q in range(t):
    n,m = map(int, input().split())
    n_list = deque(map(int ,input().split()))
    m_list = deque(map(int ,input().split()))

    if n>m :
        n_list , m_list = m_list , n_list

    result = []
    while (True):   
        if len(n_list) > len(m_list):
            break
        list_sum = 0
        for i in range(len(n_list)):
            list_sum += n_list[i] * m_list[i] 
        
        result.append(list_sum)
        m_list.popleft()

    print(f'#{q+1} {max(result)}')