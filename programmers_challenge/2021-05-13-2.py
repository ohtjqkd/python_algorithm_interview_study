def solution(numbers):
    answer = []
    for n in numbers:
        origin = n
        exp = 0
        while n > 0:
            if n % 2 == 0:
                break
            else:
                n //= 2
                exp += 1
        origin += 2 ** exp
        if exp != 0:
            origin -= 2 ** (exp-1)
        answer.append(origin)
    return answer

numbers = [2,7]

solution(numbers)
result = [3,11]