import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        minutes, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(minutes, secs)
        print(timer, end="\r")  # 显示倒计时，\r表示不换行
        time.sleep(1)
        seconds -= 1

    print("时间到！专注时间结束。")

if __name__ == "__main__":
    focus_minutes = int(input("请输入专注时间（分钟）: "))
    countdown(focus_minutes)
