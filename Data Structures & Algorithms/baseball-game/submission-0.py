class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            try:
                num = int(operations[i])
                record.append(num)
            except ValueError:
                if operations[i] == '+':
                    record.append(record[-2] + record[-1])
                elif operations[i] == 'D':
                    print(record)
                    record.append(record[-1] * 2)
                elif operations[i] == 'C':
                    record.pop()
                else:
                    record.append("bad")
            

        print(record)
        return sum(record)