def hours_to_minutes(hours):
    return hours * 60

def minutes_to_seconds(minutes):
    return minutes / 60

def total_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds or hours * 3600 or hours * 3600 + minutes * 60

def format_time(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours} hours amd {minutes} minutes"
def can_fit_task(available_hours, task_hours, task_minutes):
    return hours_to_minutes(available_hours) >= (hours_to_minutes(task_hours) + task_minutes)


def schedule_summary(task_name, hours, minutes):
    print(f"Task name: {task_name}")
    print(f"Duration: {format_time(hours)}")
    print(f"Total Minutes: {hours_to_minutes(hours)}")
    print(f"Total seconds: {total_seconds(hours)}")

def process(hours, available_hours, task_name):
    minutes = hours_to_minutes(hours)
    hours_to_seconds = hours *3600
    print("TIME CONVERTER AND SCHEDULER")
    print("="*40)
    print(f"Converting {hours} hours to minutes: {hours_to_minutes(hours)}")
    print()
    print(f"Total seconds for {format_time(minutes)}: {hours_to_seconds}")
    print()
    print(f"Formatting {minutes}: {format_time(hours)}")
    print()
    print(f"Can a {format_time(hours)} task fit in {available_hours} hours?")
    if hours_to_seconds(hours) > hours_to_seconds(available_hours):
        print("Yes, the task fits!")
    else:
        print("No, the task does not fit!")
    print("SCHEDULE SUMMARIES:")
    print(schedule_summary(task_name, hours, minutes))

process(2.5, 3.5, "Study")
    #print("-"*40)
    #print(f"Task: {task_name}")
    #print(f"  Duration: {format_time(hours)}")
    #print(f"  Total Minutes: {hours_to_minutes(hours)}")
    #print(f"  Total Seconds: {hours_to_seconds(hours)}")