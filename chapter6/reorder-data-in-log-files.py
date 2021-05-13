# leete no. 937

class Solution:
    def reorderLogFiles(self, logs: list) -> list:
        dig_array, let_array = [], []
        for log in logs:
            splited = log.split(" ")
            if splited[1].isdigit():
                dig_array.append(log)
            else:
                let_array.append(log)
        let_array.sort(key = lambda x: (x.split(" ")[1:], x.split(" ")[0]))
        return let_array + dig_array

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

print(Solution().reorderLogFiles(logs))