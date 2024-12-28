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
    "sh","rish","-c",f"am start -n {package}/{activity} -d {url}"
]


def clear_text():
    for _ in range(10):
        subprocess.call(list(map(str,"sh rish -c".split()))+['input keyevent 67'])


def start_search():
    for i in words:
        subprocess.call(list(map(str,"sh rish -c".split()))+['input keyevent KEYCODE_ENTER'])
        subprocess.call(list(map(str,"sh rish -c".split()))+['input text a'])
        subprocess.call(list(map(str,"sh rish -c".split()))+['input keyevent KEYCODE_TAB'])
        subprocess.call(list(map(str,"sh rish -c".split()))+['input keyevent KEYCODE_ENTER'])
        clear_text()
        subprocess.call(list(map(str,"sh rish -c".split()))+[f'input text {i}'])
        subprocess.call(list(map(str,"sh rish -c".split()))+['input keyevent KEYCODE_ENTER'])
        time.sleep(7)
        

subprocess.call(launch_app)
start_search()
