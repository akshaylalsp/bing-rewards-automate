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

launch_app = [
    "sh","rish","-c",
    "am", "start",
    "-n", f"{package}/{activity}",
    "-d", url
]


def clear_text():
    for _ in range(10):
        subprocess.call(list(map(str,"sh rish -c input keyevent 67".split())))


def start_search():
    for i in words:
        subprocess.call(list(map(str,"sh rish -c input keyevent KEYCODE_ENTER".split())))
        subprocess.call(list(map(str,"sh rish -c input text a".split())))
        subprocess.call(list(map(str,"sh rish -c input keyevent KEYCODE_TAB".split())))
        subprocess.call(list(map(str,"sh rish -c input keyevent KEYCODE_ENTER".split())))
        clear_text()
        subprocess.call(list(map(str,"sh rish -c input text".split()))+[f'{i}'])
        subprocess.call(list(map(str,"sh rish -c input keyevent KEYCODE_ENTER".split())))
        time.sleep(7)
        

subprocess.call(launch_app)
start_search()