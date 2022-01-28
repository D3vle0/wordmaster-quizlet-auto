from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
from dotenv import load_dotenv
import time

print("🚀 Quizlet WordMaster Auto Solver\n")

load_dotenv(verbose=True)
QUIZLET_PW = os.getenv('QUIZLET_PW')
exec(open('wordlist.py').read())
wordlist = word_dict

service = Service("./chromedriver")
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
browser = webdriver.Chrome(service=service, options=options)
browser.set_window_size(820, 600)

browser.get("https://accounts.google.com/o/oauth2/auth/identifier?response_type=code&redirect_uri=https%3A%2F%2Fquizlet.com%2Fgoogle-login&client_id=520305074949.apps.googleusercontent.com&scope=profile%20email&access_type=online&approval_prompt=auto&state=%7B%22state%22%3A%2289XDfHzr4qrGVgGsytGFUH%22%2C%22reauth%22%3Afalse%2C%22from%22%3A%22https%3A%5C%2F%5C%2Fquizlet.com%5C%2Fko%22%2C%22signupOrigin%22%3A%22global-signup-modal-google%22%2C%22screenName%22%3A%22Homepage%5C%2Findex%22%7D&flowName=GeneralOAuthFlow")
browser.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys("choice7203@dimigo.hs.kr")
browser.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(str(QUIZLET_PW))
browser.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
while 1:
    if browser.current_url == "https://quizlet.com/latest":
        break
    time.sleep(1)
print("🔑 Login success!")
browser.get("https://quizlet.com/d3vle0/folders/word-master/write")

# restart quiz
browser.find_element(By.XPATH, '//*[@id="AssistantModeTarget"]/div/div/div/div[1]/div/aside/div[2]/div[3]/div/button').click()
browser.find_element(By.XPATH, '/html/body/div[10]/div/div[2]/div/div[1]/div[2]/div/div/div/span[2]/input').click()
browser.find_element(By.XPATH, '/html/body/div[10]/div/div[2]/div/div[3]/div/div[2]/div/div/button').click()
time.sleep(1)
prob_number = browser.find_element(By.XPATH, '//*[@id="AssistantModeTarget"]/div/div/div/div[1]/div/aside/div[2]/div[2]/div/div/div[1]/div[2]/div[2]').text
time.sleep(1)

print("🔥 Attacking...")
for i in range(int(prob_number)):
    try:
        prob = browser.find_element(By.XPATH, '//*[@id="AssistantModeTarget"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div').text
        answer = wordlist[prob]
        browser.find_element(By.XPATH, '//*[@id="AssistantModeTarget"]/div/div/div/div[2]/div/div/div[2]/form/div[1]/div/label/div/div/div[2]/textarea').send_keys(answer)
        browser.find_element(By.XPATH, '//*[@id="AssistantModeTarget"]/div/div/div/div[2]/div/div/div[2]/form/div[2]/button').click()
    except:
        print(f"💥 Error occured in {prob}")
        browser.find_element(By.XPATH, '//*[@id="AssistantModeTarget"]/div/div/div/div[2]/div/div/div[2]/form/div[1]/div/label/div/div/div[2]/textarea').send_keys("a")
        browser.find_element(By.XPATH, '//*[@id="AssistantModeTarget"]/div/div/div/div[2]/div/div/div[2]/form/div[2]/button').click()
        time.sleep(0.5)
        browser.find_element(By.XPATH, '//*[@id="AssistantModeTarget"]/div/div/div/div[2]/div/div/div/div[2]/div/button/span').click()
    time.sleep(0.5)
now = time.localtime()
browser.save_screenshot("%02d%02d%02d-%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec) + ".png")
print("🌈 Done!")