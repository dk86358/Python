def task_reminder(time_string):
    if time_string == "8:00 a.m.":
        task = "Check overnight images"
    elif time_string == "11:30 a.m.":
        task = "Run the TPS reports"
    elif time_string == "5:30 p.m.":
        task = "Reboot servers"
    else:
        task = "Provide IT support to employees"
    return task

# Now to call the function we will use this 
print(task_reminder("8:00 a.m."))
print(task_reminder("11:30 a.m."))
print(task_reminder("10:00 a.m."))
