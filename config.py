from utils import save_int_input
#难度
difficulties = {
        1: {"low": 1, "high": 50, "times": 5,"name":"easy"},
        2: {"low": 1, "high": 100, "times": 7,"name":"normal"},
        3: {"low": 1, "high": 200, "times": 10,"name":"hard"},
    }
def custom_diff():
    #自定义难度
    low=save_int_input("input your low number")
    high=save_int_input("input your high number")
    times=save_int_input("input your times number")
    return low,high,times