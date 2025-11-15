task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound (yes/no): ")


match priority:
    case "high":
        if time == "yes":
            print(
                f"Reminder: '{task}' is a high priority task that requires immediate attentiokn today!")
        else:
            print(
                f"'{task}' is a high priority task. consider completing it when you have free time.")
    case "medium":
        if time == "yes":
            print(
                f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(
                f"'{task}' is a medium priority task. consider completing it when you have free time.")
    case "low":
        if time == "yes":
            print(
                f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(
                f"'{task}' is a low priority task. consider completing it when you have free time.")
