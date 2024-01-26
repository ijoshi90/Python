import random
import datetime

def get_time():
    return datetime.datetime(1, 1, 1, 0, 3, random.randint(41, 58)).strftime('%H:%M:%S')


def getOverallTime(lst):
    # Extracting the times from the list
    times = [time.split(':') for time in lst]

    # Converting the times to seconds
    seconds = [int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2]) for time in times]

    # Adding the element at index 1 to the maximum time between indexes 2 to 8
    seconds[9] += seconds[1] + max(seconds[2:9])

    # Converting the total seconds back to hh:mm:ss format
    hours, seconds[9] = divmod(seconds[9], 3600)
    minutes, seconds[9] = divmod(seconds[9], 60)

    # Returning the total time in the required format
    return f"{hours:02d}:{minutes:02d}:{seconds[9]:02d}"


if __name__ == '__main__':

    init = get_time()
    times = ['01:00:00', '02:00:00', '03:00:00', '04:00:00', '05:00:00', '06:00:00', '07:00:00', '08:00:00', '09:00:00']
    times.append(init)
    print(times)
    result = getOverallTime(times)

    print("Overall time : {}".format(result))
