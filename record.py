class Record:
    def __init__(self,result,tries,difficulty):
        self.result = result
        self.tries = tries
        self.difficulty = difficulty

    def to_line(self):
        #用于写入历史文件
        return f"{self.result},{self.tries},{self.difficulty}\n"

    @staticmethod
    def from_line(line):
        #读取历史记录文件，获取每一行的历史记录
        parts = line.strip().split(",")
        if len(parts) != 3:
            return None
        result,tries,difficulty = parts
        tries=None if tries == "None" else int(tries)
        return Record(result,tries,difficulty)