from stats import calculate_stats_from_file,calculate_rate
from record import Record

def save_record(file_path,record):
    #将历史记录写入文件中
    with open(file_path, "a") as f:
        f.write(record.to_line())

def read_records(file_path):
    #读取历史记录文件后统计数据
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            all_records= []
            for line in lines:
                record = Record.from_line(line)
                if record is not None:
                    all_records.append(record)
            total, win_times, average_tries=calculate_stats_from_file(all_records)
            rates=calculate_rate(all_records)
            return total, win_times, average_tries, rates
    except FileNotFoundError:
        print("No history file found")
        return 0, 0, 0,{}