from collections import deque

def solution(priorities, location):
    answer = 0
    
    priorities = deque(priorities)
    while priorities:
        len_ = len(priorities)
        n = priorities.popleft()
        location = (location-1) % len_ 
        
        flag = True
        # if any(cur[1] < q[1] for q in queue):
        for i in range(len_ -1):
            if priorities[i] > n:
                priorities.append(n)
                flag = False
                break
        
        
        if flag:
            if location == len_-1:
                return answer+1
            else:
                answer += 1

print(solution([2, 1, 3, 2], 2))