from record import Record

def calculate_stats_from_file(all_records):
    #统计传入的历史记录
    total = 0
    win_times = 0
    total_tries = 0
    for r in all_records:
        total += 1
        if r.result == "win":
            win_times += 1
            total_tries +=r.tries
    average_tries = 0 if win_times == 0 else total_tries / win_times
    return total, win_times, average_tries

def calculate_rate(all_records):
    #计算不同难度下的胜率并返回
    rates={}
    for r in all_records:
        difficulty=r.difficulty
        if difficulty not in rates:
            rates[difficulty]={"total":0, "wins":0}
        rates[difficulty]["total"]+=1
        rates[difficulty]["wins"]+=1 if r.result == "win" else 0
    return rates