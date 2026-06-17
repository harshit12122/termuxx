import json
import os

FILE_NAME = "tasks.json"

# Default data
default_data = {
    "Kuldeep": {
        "phone": "919876543210",
        "tasks": []
    },
    "Rohit": {
        "phone": "919123456789",
        "tasks": []
    },
    "Nupur": {
        "phone": "919999999999",
        "tasks": []
    }
}
import time
import subprocess
import time
import urllib
from pynput.keyboard import Key, Controller
import pyautogui

keyboard = Controller()
def send_to_whatsapp_group(message, group):
    message = "".join(i+"\n" for i in message)
    encoded_message = urllib.parse.quote(message.replace("https", " "))
    phone_number = ""
    cmd = f'start whatsapp://send?phone={phone_number}^&text={encoded_message}'
    subprocess.Popen(["cmd", "/C", cmd], shell=True)
    time.sleep(2)

    # if len(group.split("\n")) >1: #assignments
    #     group = group.split("\n")
    #     for i in group:
    #         keyboard.type(i)
    #         time.sleep(3)
    #         print("Enter 1 pressed")
    #         keyboard.press(Key.enter)
    #         time.sleep(6)
    #     pyautogui.click(700,647) #send one
    #     time.sleep(2)# click send box
        
    # else:
    #     print(1)
    #     print("Typing", group)
    #     keyboard.type(group)
    #     time.sleep(6)
    #     print("Enter 2 pressed")
    #     keyboard.press(Key.enter)
    #     time.sleep(2)
    #     pyautogui.click(700,647) #send one
    #     time.sleep(2)# click send box
    #     pyautogui.click(985, 688)  # click send box
    #     time.sleep(2)

    # pyautogui.click(906, 14)  # click minimize box
    # time.sleep(2)

    # print("Message sent!")
    # time.sleep(3)




# Load data from JSON file
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return default_data


# Save data to JSON file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

while 1:
  # Load previous data
  data = load_data()
  names = list(data.keys())

  # Display users
  print("Users:")
  for i, name in enumerate(names, start=1):
      print(i, name)

  person_no = int(input("Select person: ")) - 1
  person = names[person_no]

  while True:
      print(f"\nSelected User: {person}")
      print("Phone:", data[person]["phone"])

      print("\n1. Input Task")
      print("2. View Tasks")
      print("3. Delete Task")
      print("4. Exit")
      print("5. Send Tasks")

      choice = int(input("Enter your choice: "))

      if choice == 1:
          task = input("Enter the task: ")
          data[person]["tasks"].append(task)
          save_data(data)
          print("Task added successfully.")

      elif choice == 2:
          tasks = data[person]["tasks"]

          if not tasks:
              print("No tasks found.")
          else:
              print("\nTasks:")
              for i, task in enumerate(tasks, start=1):
                  print(f"{i}. {task}")

      elif choice == 3:
          tasks = data[person]["tasks"]

          if not tasks:
              print("No tasks to delete.")
          else:
              print("\nTasks:")
              for i, task in enumerate(tasks, start=1):
                  print(f"{i}. {task}")

              task_no = int(input("Enter task number to delete: ")) - 1

              if 0 <= task_no < len(tasks):
                  deleted = tasks.pop(task_no)
                  save_data(data)
                  print(f"Deleted: {deleted}")
              else:
                  print("Invalid task number.")

      elif choice == 4:
          print("Exit")
          break

      elif choice == 5:
          tasks = data[person]["tasks"]
          print("Enter group name: ")
          group = data[person]["phone"]
          send_to_whatsapp_group(tasks, group)
      
      else:
          print("Invalid choice.")
          break
      

