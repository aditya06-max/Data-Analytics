import time
from plyer import notification

def water_reminder():
    while True:    # this is uded to create an infinite loop that will keep reminding the user to drink water
        notification.notify(   #This tells Windows (or Linux/Mac) to Show a desktop notification.
            title="Water Reminder",
            message="Time to drink water! Stay hydrated.",
            timeout=10   # this tells the notification to stay on the screen for 10 seconds before disappearing
        )
        time.sleep(3)  # Remind every 3 seconds for demonstration purposes (you can change this to a longer interval, e.g., 3600 for 1 hour)

water_reminder()        