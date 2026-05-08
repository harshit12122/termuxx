import subprocess, time
import requests
time.sleep(5)

url = "https://harshitsukhija.vercel.app/pick/api/"
response = requests.get(url)
print(response.text)  
response = dict(response.json())
phone_number = response["number"]
subprocess.run(["termux-telephony-call", phone_number])












# def scroll_down():
#     # Swipe from bottom (middle-low) to top (middle-high)
#     # Syntax: adb shell input swipe <start_x> <start_y> <end_x> <end_y> <duration_ms>
#     subprocess.run("adb shell input swipe 500 1500 500 500 500", shell=True)

# scroll_down()

# def scroll_up():
#     # Swipe from bottom (middle-low) to top (middle-high)
#     # Syntax: adb shell input swipe <start_x> <start_y> <end_x> <end_y> <duration_ms>
#     subprocess.run("adb shell input swipe 500 500 500 1500", shell=True)

# scroll_up()

# import subprocess

# def click(x, y):
#     # Sends a 'tap' command to the specific X and Y coordinates
#     cmd = f"adb shell input tap {x} {y}"
#     subprocess.run(cmd, shell=True)

# # Example: Click at coordinates (500, 1000)
# click(500, 1000)