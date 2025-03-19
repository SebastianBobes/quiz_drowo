from datetime import datetime


def calculate_time_difference(start_time, end_time):
    date_format = "%Y-%m-%d %H:%M:%S"

    start_time_2 = datetime.strptime(start_time, date_format)
    end_time_2 = datetime.strptime(end_time, date_format)

    time_difference = end_time_2 - start_time_2

    total_seconds = time_difference.total_seconds()

    minutes = total_seconds // 60
    seconds = total_seconds % 60


    return(f"{int(minutes)}:{int(seconds)}")

