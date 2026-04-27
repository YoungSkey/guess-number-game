from game import Game
from record_manager import read_records

def main():
    G=Game("game_history.txt")
    #G.run()
    total, win_times, average_tries, rates = read_records(G.file_path)
    #以下均为打印统计数据
    print(f"Total times: {total}")
    print(f"Wins: {win_times}")
    print(f"Average tries:{average_tries}")
    print("\nWin rate by difficulty:")
    for diff,date in rates.items():
        total=int(date["total"])
        win=int(date["wins"])
        rate = 0 if total == 0 else win / total * 100
        print(f"{diff}: {rate:.1f}% ({win}/{total})")

if __name__ == "__main__":
    main()