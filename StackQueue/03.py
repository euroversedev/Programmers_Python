from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    time = 0
    
    sum_bridge = 0
    while truck_weights or any(i for i in bridge):
        # 다리 위에 있는 애들 앞으로 보내고
        sum_bridge -= bridge.popleft()
        bridge.append(0)

        # 대기중인 트럭 진입시키기
        if truck_weights and sum_bridge + truck_weights[0] <= weight:
            w = truck_weights.popleft()
            sum_bridge += w
            bridge[-1] = w
            
        time += 1
    
    answer = time
    return answer

