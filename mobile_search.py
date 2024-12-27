import subprocess
import time

package = "com.microsoft.bing"
activity = "com.microsoft.sapphire.app.browser.IntentDispatchActivity"
url = "https://bing.com/search?q=test"

words = [
    "apple", "banana", "cherry", "date", "fig", 
    "grape", "kiwi", "lemon", "mango", "orange", 
    "papaya", "quince", "raisin", "tomato", "melon", 
    "carrot", "beet", "olive", "peach", "pear", 
    "plum", "onion", "radish", "turnip", "apricot"
]

adb_command = [
    "adb", "shell", "am", "start",
    "-n", f"{package}/{activity}",
    "-d", url
]


def clear_text():
    for _ in range(10):
        subprocess.call("adb shell input keyevent 67")


def start_search():
    for i in words:
        subprocess.call("adb shell input keyevent KEYCODE_ENTER")
        subprocess.call(list(map(str,"adb shell input text a".split())))
        subprocess.call("adb shell input keyevent KEYCODE_TAB")
        subprocess.call("adb shell input keyevent KEYCODE_ENTER")
        clear_text()
        subprocess.call(list(map(str,"adb shell input text".split()))+[f'{i}'])
        subprocess.call("adb shell input keyevent KEYCODE_ENTER")
        time.sleep(7)
        

subprocess.call(adb_command)
start_search()