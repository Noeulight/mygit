import itertools

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(nums):
    com = list(itertools.combinations(nums, 3))
    result = []
    answer = 0
    
    for ele in com:
        _sum = sum(ele)
        if is_prime(_sum):
            result.append(ele)
            answer += 1
    
    return answer

nums = [1,2,7,6,4]
print(solution(nums))