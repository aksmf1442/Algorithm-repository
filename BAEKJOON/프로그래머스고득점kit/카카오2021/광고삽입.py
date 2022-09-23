# def solution(play_time, adv_time, logs):
#     play_time = str_to_int(play_time)  # 1
#     adv_time = str_to_int(adv_time)
#     all_time = [0 for i in range(play_time + 1)]
#
#     for l in logs:  # 2
#         start, end = l.split('-')
#         start = str_to_int(start)
#         end = str_to_int(end)
#         all_time[start] += 1
#         all_time[end] -= 1
#
#     for i in range(1, len(all_time)):  # 3
#         all_time[i] = all_time[i] + all_time[i - 1]
#     print(all_time)
#     for i in range(1, len(all_time)):  # 4
#         all_time[i] = all_time[i] + all_time[i - 1]
#
#
#     most_view = 0  # 5
#     max_time = 0
#     for i in range(adv_time - 1, play_time):
#         if i >= adv_time:
#             if most_view < all_time[i] - all_time[i - adv_time]:
#                 most_view = all_time[i] - all_time[i - adv_time]
#                 max_time = i - adv_time + 1
#         else:
#             if most_view < all_time[i]:
#                 most_view = all_time[i]
#                 max_time = i - adv_time + 1
#
#     return int_to_str(max_time)
#
#
# def str_to_int(time):
#     h, m, s = time.split(':')
#     return int(h) * 3600 + int(m) * 60 + int(s)
#
#
def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s


def datetoInt(time):
    time = time.split(":")
    hour = int(time[0])
    minute = int(time[1])
    second = int(time[2])

    return hour * 3600 + minute * 60 + second


def solution(play_time, adv_time, logs):
    answer = 0
    play_time = datetoInt(play_time)
    adv_time = datetoInt(adv_time)
    dp = [0] * (play_time + 1)
    n = len(dp)
    for l in logs:
        splitedTime = l.split("-")
        start = datetoInt(splitedTime[0])
        end = datetoInt(splitedTime[1])
        dp[start] += 1
        dp[end] -= 1

    for idx in range(1, n):
        dp[idx] = dp[idx - 1] + dp[idx]

    for idx in range(1, n):
        dp[idx] = dp[idx - 1] + dp[idx]

    most_view = 0  # 5
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < dp[i] - dp[i - adv_time]:
                most_view = dp[i] - dp[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < dp[i]:
                most_view = dp[i]
                max_time = i - adv_time + 1

    return int_to_str(max_time)


print(solution("02:03:55", "00:14:15",
               ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30",
                "01:30:59-01:53:29"]))
