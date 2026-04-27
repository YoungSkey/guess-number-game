import random
from config import difficulties,custom_diff
from record_manager import save_record
from utils import save_int_input,yes_no_input
from record import Record

class Game:

    def __init__(self,file_path):
        self.best_score = None#最好的成绩
        self.records=[]#每轮游戏的记录
        self.file_path = file_path

    def choose_difficulty(self):
        """
        choose difficulty
        选择游戏的难度
        :return: 无
        """
        while True:
            print("\nChoose difficulty:")
            print("1. Easy (1-50, 5 chances)")
            print("2. Normal (1-100, 7 chances)")
            print("3. Hard (1-200, 10 chances)")
            print("4.custom your difficulty")

            choice = save_int_input("choose your grade of difficulty(1-4):")
            if choice ==4:
                self.low,self.high,self.max_times=custom_diff()
                self.difficulty ="custom difficulty"
                break
            if choice not in difficulties:
                print("invalid choice")
                continue
            self.low = difficulties[choice]["low"]
            self.high = difficulties[choice]["high"]
            self.max_times = difficulties[choice]["times"]  # 最多尝试的次数
            self.difficulty=difficulties[choice]["name"]
            break

    def get_target(self):
        #获取目标值
        self.target = random.randint(self.low, self.high)

    def play_game(self):
        """
        play game
        :return:
        """
        print(f"you have {self.max_times} chances to guess the target")

        times = 1
        self.used_times = None
        self.all_guesses = []

        while times <= self.max_times:
            guess = save_int_input(f"guess a number between {self.low} and {self.high}:", (self.low, self.high))
            self.all_guesses.append(guess)#记录一共猜过的数字
            if guess == self.target:
                self.used_times = times#更新猜对使用的次数
                break
            else:
                out = "high" if guess > self.target else "low"
                print(f"Too {out}! {self.max_times - times} chances left")
            times += 1

    def over_game(self):
        if self.used_times is None:
            print("Game Over")#若没有猜对则输出
        else:
            print(f"Congratulations! you win in {self.used_times} tries!")
        print(f"Your guesses:{self.all_guesses}")#打印所有猜过的数字
        if self.best_score is None:
            print("Best score: None yet")
        else:
            print(f"Best score is {self.best_score}")

    def re_game(self):
        #选择重新游戏或者退出
        return yes_no_input("Play again? (y/n):")

    def print_history(self):
        print("Game History:")
        for i, it in enumerate(self.records, 1):
            if it.result == "win":
                print(f"{i}. {it.result} in {it.tries} tries ({it.difficulty})")
            else:
                print(f"{i}. {it.result} ({it.difficulty})")

    def run(self):

        is_running = True

        while is_running:
            # 开始选择难度
            self.choose_difficulty()
            # 获取目标数
            self.get_target()
            # 游戏开始
            self.play_game()
            # 更新数据
            if self.used_times is not None:
                self.records.append(Record("win", self.used_times,self.difficulty))
                if self.best_score is None:
                    self.best_score = self.used_times
                else:
                    self.best_score = min(self.best_score, self.used_times)
            else:
                self.records.append(Record("lose", self.used_times,self.difficulty))
            # 保存历史数据
            save_record(self.file_path, self.records[-1])
            # 游戏结算
            self.over_game()
            # 继续游戏或者退出选择
            is_running = self.re_game()
            # 打印历史记录
            self.print_history()