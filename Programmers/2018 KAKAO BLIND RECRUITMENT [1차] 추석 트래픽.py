import datetime

def solution(lines):
    # 로그의 시작 시간과 종료 시간을 밀리초로 변환하는 함수
    def get_times(log):
        time, t = log.split()[1:]
        t = float(t[:-1]) * 1000
        end_time = datetime.datetime.strptime('2016-09-15 ' + time, '%Y-%m-%d %H:%M:%S.%f')
        start_time = end_time - datetime.timedelta(milliseconds=t - 1)
        return int(start_time.timestamp() * 1000), int(end_time.timestamp() * 1000)

    # 모든 로그의 시작 시간과 종료 시간을 저장
    times = []
    for log in lines:
        start, end = get_times(log)
        times.append((start, end))

    # 최대 처리량 계산
    max_count = 0
    for time in times:
        count_start = count_end = 0
        start_range = (time[0], time[0] + 999)
        end_range = (time[1], time[1] + 999)
        for other in times:
            if other[0] <= start_range[1] and other[1] >= start_range[0]:
                count_start += 1
            if other[0] <= end_range[1] and other[1] >= end_range[0]:
                count_end += 1
        max_count = max(max_count, count_start, count_end)

    return max_count



