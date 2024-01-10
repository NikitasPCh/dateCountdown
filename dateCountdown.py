import tkinter as tk
from datetime import date

# Format current day
today = date.today()
fToday = today.strftime("%A, %B %d %Y")

# Days remaining calculation
daysInYear = 365
todaysNumber = int(today.strftime("%j"))
currentYear = int(today.strftime("%Y"))
if currentYear % 4 == 0:
    daysInYear = 366
    remainingDays = daysInYear - todaysNumber
else:
    remainingDays = daysInYear - todaysNumber

root = tk.Tk()
root.title("Date Countdown")
root.geometry("600x600")
# Today's date
todayLabel = tk.Label(root, text = f'Today is {fToday}')
todayLabel.pack(pady = 20, ipadx = 10, ipady = 10)
# Countdown
countdownLabel = tk.Label(root, text = f'There are {remainingDays} days remaining until the end of {currentYear}')
countdownLabel.pack(pady = 20)

root.mainloop()