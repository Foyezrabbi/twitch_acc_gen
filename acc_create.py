import random
from time import sleep
from selenium import webdriver  # 4.1.5
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from stuff.fak import name
from stuff.passw import pass_gen
from stuff.temp_mail import mail


def generate_username():
    username = name()
    with open('./data/usernames_used.txt', 'r') as f:
        if username in f.read():
            return generate_username()
    return username


def generate_month():
    return random.randint(1, 12)


def generate_day():
    return random.randint(1, 28)


def generate_year():
    return random.randint(1970, 2001)


def generate_password():
    return pass_gen()


while True:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_extension('./driver/extension_5_1_1_0.crx')
    # driver = webdriver.Chrome(executable_path="C:\\Users\\Himu\\Downloads\\chromedriver.exe",
    #                           options=chrome_options)
    driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe",
                              options=chrome_options)

    driver.get("http://www.twitch.tv/")

    delay = 3  # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[2]/button')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")



    # Click sign up
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[2]/button').click()

    username = generate_username()
    password = generate_password()
    email = username + "@gmail.com"

    print(f"""
USERNAME {username}
PASSWORD {password}
""")

    month = generate_month()
    day = generate_day()
    year = generate_year()

    sleep(1)

    # username
    driver.find_element(By.ID, 'signup-username').send_keys(username)

    # password
    driver.find_element(By.ID, 'password-input').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="password-input-confirmation"]').send_keys(password)

    # month
    select = Select(driver.find_element(By.XPATH,
                                        '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[1]/select'))
    select.select_by_value(str(month))

    # day
    driver.find_element(By.XPATH,
                        '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[2]/div/input').send_keys(
        str(day))

    # year
    driver.find_element(By.XPATH,
                        '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[3]/div/input').send_keys(
        str(year))

    # Switches to email
    driver.find_element(By.XPATH,
                        '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[4]/div/div[2]/button/div').click()

    sleep(0.5)

    # email.
    driver.find_element(By.ID, 'email-input').send_keys(email)

    sleep(0.5)

    # Submits form.
    driver.find_element(By.XPATH,
                        '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[5]/button/div/div').click()

    # you have to complete the captcha.

    while True:
        do_quit = False
        try:
            driver.find_element(By.XPATH,
                                '/html/body/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/input')
            break
        except:
            try:
                driver.find_element(By.XPATH,
                                    '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/div[2]/strong')
                driver.quit()
                print("Error in sign up")
                do_quit = True
                break
            except:
                sleep(0.1)
    if do_quit:
        break

    driver.find_element(By.XPATH,
                        '/html/body/div[3]/div/div/div/div/div/div/div/div/div/div/div[3]/div[2]/button').click()
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div/div[3]/div[2]/button').click()

    with open("./data/acc_list.txt", "a") as f:
        f.write(username + ":::" + password + "\n")
    with open("./data/usernames_used.txt", "a") as f:
        f.write(username + "\n")

    sleep(2)
    driver.quit()

try:
    sleep(10)
except:
    print("Error")
