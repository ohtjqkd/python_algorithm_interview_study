#다시푸세요

def solution(s):
    answer = []
    for b in s:
        i = 0
        while i < len(b)-2:
            if b[i:i+3] == '110':
                next_b = ''
                for j in range(len(b)):
                    if b[j:j+3] > '110':
                        next_b += '110' + b[j:i] + b[i+3:]
                        break
                    else:
                        next_b += b[j]
                b = next_b
            i += 1
        answer.append(b)
    return answer


s = ["1110","100111100","0111111010"]	

result = ["1101","100110110","0110110111"]
print(solution(s) == result)
