''' [review] 프로그래머스 조이스틱
1. 알파벳을 변경하기 위한 조작 횟수
2. 커서 이동을 위한 조작 횟수
두 개로 문제를 나누어 생각할 수 있음.
'''

# 현재 위치 i를 방문 처리하고 start와 end로 이동해서 리턴
def move(i):
    visited[i] = True
    
    start = i + 1
    move()
    
    
def solution(name):
    len_name = len(name)
    idx = [i for i, ch in enumerate(name) if name[i] != 'A']
    start = idx[0]
    end = idx[-1]
    
    '''

    '''
    
    for _ in range(len_name):
        
    
    answer = 0
    for i in range(i-1):
        if (idx[i+1] - idx[i]) 
        
        
    
    return answer