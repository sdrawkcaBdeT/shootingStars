import time

def sleep_with_progress(total_time_minutes, interval_minutes):
    total_time_seconds = total_time_minutes * 60
    interval_seconds = interval_minutes * 60

    for remaining_time in range(total_time_seconds, 0, -interval_seconds):
        remaining_time = min(remaining_time, interval_seconds)
        print(f"Sleeping for {remaining_time // 60} minutes...")
        time.sleep(remaining_time)



