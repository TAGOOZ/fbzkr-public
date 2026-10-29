import undetected_chromedriver as uc
import pickle
import subprocess
import re
import os

def get_chrome_version():
    for cmd in ['google-chrome --version', 'chromium-browser --version', 'chromium --version']:
        try:
            out = subprocess.check_output(cmd.split()).decode()
            match = re.search(r'(\d+)\.', out)
            if match:
                return int(match.group(1))
        except:
            pass
    return None

chrome_ver = get_chrome_version()
print(f"Detected Chrome version: {chrome_ver}")

options = uc.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920,1080')

if chrome_ver:
    driver = uc.Chrome(version_main=chrome_ver, use_subprocess=True, options=options)
else:
    driver = uc.Chrome(use_subprocess=True, options=options)

driver.get("https://www.facebook.com")
print("A browser window opened.")
print("Log into Facebook manually, then come back here and press Enter.")
input()

cookies = driver.get_cookies()
with open('cookies.pkl', 'wb') as f:
    pickle.dump(cookies, f)

print(f"Saved {len(cookies)} cookies to cookies.pkl")
driver.quit()
