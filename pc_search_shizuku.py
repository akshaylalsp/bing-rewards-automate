import subprocess
import time

words = [
    "acorn", "basil", "citrus", "durian", "echini",
    "fennel", "garlic", "hazeln", "indigo", "jasmin",
    "kelp", "lilac", "myrtle", "nutmeg", "orchid",
    "pollen", "quinoa", "rose", "sage", "thyme",
    "violet", "wheat", "xenon", "yarrow", "zinnia",
    "berry", "celery", "daikon", "eggnog", "fruity",
    "grassy", "hummus", "jalape", "kapok", "licor"
]

package = "com.brave.browser"
activity = "com.google.android.apps.chrome.IntentDispatcher"
url = "https://bing.com/search?q=test"

launch_app = [
    "sh","rish","-c",f"am start -n {package}/{activity} -d {url}"
]

def start_search():
    for i in words:
        
        subprocess.call(list(map(str,"sh rish -c".split()))+[f'input text {i}'])
        subprocess.call(list(map(str,"sh rish -c".split()))+['input keyevent KEYCODE_ENTER'])

        time.sleep(7)
        

subprocess.call(launch_app)
start_search()
