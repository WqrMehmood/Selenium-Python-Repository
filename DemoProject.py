# selenium 4
import random

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC




#options = Options()
#options.binary_location = "C:\\Users\hp\Downloads\chromedriver_win32\Chromedriver.exe"
# options.add_argument('--headless')

#driver = webdriver.Chrome(
 #   service=ChromeService(ChromeDriverManager().install()),
 #   options=options,
#)

#setting up chrome driver

#serv_obj=Service("C:\\Users\hp\Downloads\chromedriver_win32\Chromedriver.exe")
#driver=webdriver.Chrome(service=serv_obj)

#to disbale notifications
option1=Options()
option1.add_argument("--disable-notifications")

#Driversetup
driver=webdriver.Chrome(executable_path="C:\\Users\hp\Downloads\chromedriver_win32\Chromedriver.exe",chrome_options=option1)




# Load Website
driver.get('https://dev.christianfilipina.com/')
driver.maximize_window()
wait = WebDriverWait(driver, timeout=10)

print('Page: ', driver.title)

# import pdb;pdb.set_trace()

# Find Next Button and click on it
next_button_xpath = '/html/body/div[3]/div[3]/div[2]/div[1]/div/div/div/form/div[1]/button'
wait.until(EC.visibility_of_element_located((By.XPATH, next_button_xpath)))
next_button = driver.find_element(By.XPATH, next_button_xpath)
next_button.click()

# Find Next Button and click on it (Age slide)
nb_age_xpath = '/html/body/div[3]/div[3]/div[2]/div[1]/div/div/div/form/div[2]/button'
wait.until(EC.visibility_of_element_located((By.XPATH, nb_age_xpath)))
nb_age = driver.find_element(By.XPATH, nb_age_xpath)
nb_age.click()
# driver.implicitly_wait(30)

# DOB Slide
# driver.implicitly_wait(30)
month_xpath = '/html/body/div[3]/div[3]/div[2]/div[1]/div/div/div/form/div[3]/select[1]'
wait.until(EC.visibility_of_element_located((By.XPATH, month_xpath)))
month_select = driver.find_element(By.XPATH, month_xpath)
month_object = Select(month_select)

day_xpath = '/html/body/div[3]/div[3]/div[2]/div[1]/div/div/div/form/div[3]/select[2]'
wait.until(EC.visibility_of_element_located((By.XPATH, day_xpath)))
day_select = driver.find_element(By.XPATH, day_xpath)
day_object = Select(day_select)

year_xpath = '/html/body/div[3]/div[3]/div[2]/div[1]/div/div/div/form/div[3]/select[3]'
wait.until(EC.visibility_of_element_located((By.XPATH, year_xpath)))
year_select = driver.find_element(By.XPATH, year_xpath)
year_object = Select(year_select)

month_object.select_by_index(3)
day_object.select_by_index(1)
year_object.select_by_value("1992")

# driver.implicitly_wait(10)
dob_xpath = "/html/body/div[3]/div[3]/div[2]/div[1]/div/div/div/form/div[3]/button"
wait.until(EC.visibility_of_element_located((By.XPATH, dob_xpath)))
nb_dob = driver.find_element(By.XPATH, dob_xpath)
nb_dob.click()
# driver.implicitly_wait(10)

# Name Slide

names = ['John', 'William', 'James', 'Charles', 'George', 'Frank', 'Joseph', 'Thomas', 'Henry', 'Robert', 'Edward',
         'Harry', 'Walter', 'Arthur', 'Fred', 'Albert', 'Samuel', 'David', 'Louis', 'Joe', 'Charlie', 'Clarence',
         'Richard', 'Andrew', 'Daniel', 'Ernest', 'Will', 'Jesse', 'Oscar', 'Lewis', 'Peter', 'Benjamin', 'Frederick',
         'Willie', 'Alfred', 'Sam', 'Roy', 'Herbert', 'Jacob', 'Tom', 'Elmer', 'Carl', 'Lee', 'Howard', 'Martin',
         'Michael', 'Bert', 'Herman', 'Jim', 'Francis', 'Harvey', 'Earl', 'Eugene', 'Ralph', 'Ed', 'Claude', 'Edwin',
         'Ben', 'Charley', 'Paul', 'Edgar', 'Isaac', 'Otto', 'Luther', 'Lawrence', 'Ira', 'Patrick', 'Guy', 'Oliver',
         'Theodore', 'Hugh', 'Clyde', 'Alexander', 'August', 'Floyd', 'Homer', 'Jack', 'Leonard', 'Horace', 'Marion',
         'Philip', 'Allen', 'Archie', 'Stephen', 'Chester', 'Willis', 'Raymond', 'Rufus', 'Warren', 'Jessie', 'Milton',
         'Alex', 'Leo', 'Julius', 'Ray', 'Sidney', 'Bernard', 'Dan', 'Jerry', 'Calvin']

name = random.choice(names)
name_xpath = "/html/body/div[3]/div[3]/div[2]/div[1]/div/div/div/form/div[4]/input"
wait.until(EC.visibility_of_element_located((By.XPATH, name_xpath)))
name_input = driver.find_element(By.XPATH, name_xpath)
name_input.send_keys(name + Keys.ENTER)
# driver.implicitly_wait(10)

# Email Slide
email_xpath = '/html/body/div[3]/div[3]/div[2]/div[1]/div/div/div/form/div[5]/input'
wait.until(EC.visibility_of_element_located((By.XPATH, email_xpath)))
email_input = driver.find_element(By.XPATH, email_xpath)
email_input.send_keys(f"{name}{random.randint(0, 9999)}@{random.randint(0, 9)}mail.com" + Keys.ENTER)
# driver.implicitly_wait(10)

# Password Slide
password_xpath = '/html/body/div[3]/div[3]/div[2]/div[1]/div/div/div/form/div[6]/input'
wait.until(EC.visibility_of_element_located((By.XPATH, password_xpath)))
password_input = driver.find_element(By.XPATH, password_xpath)
password_input.send_keys("pakistan1234" + Keys.ENTER)
# driver.implicitly_wait(10)

# About Yourself
about_xpath = '/html/body/div[3]/div[3]/div[2]/div[1]/div/div/div/form/div[7]/textarea'
wait.until(EC.visibility_of_element_located((By.XPATH, about_xpath)))
about_textarea = driver.find_element(By.XPATH, about_xpath)
about_textarea.send_keys("Hello World")

about_btn_xpath = '/html/body/div[3]/div[3]/div[2]/div[1]/div/div/div/form/div[7]/button'
wait.until(EC.visibility_of_element_located((By.XPATH, about_btn_xpath)))
next_button_about = driver.find_element(By.XPATH, about_btn_xpath)
next_button_about.click()
# driver.implicitly_wait(10)

# Profile Slide
pf_next_xpath = '/html/body/div[3]/div[3]/div[2]/div[1]/div/div/div/form/div[8]/button'
wait.until(EC.visibility_of_element_located((By.XPATH, pf_next_xpath)))
next_button_profile = driver.find_element(By.XPATH, pf_next_xpath)
next_button_profile.click()
# driver.implicitly_wait(10)

# Popup
#popup_xpath = '/html/body/div[26]/div[1]/div/div/div[6]/a[1]'
#wait.until(EC.visibility_of_element_located((By.XPATH, popup_xpath)))
#popup_button = driver.find_element(By.XPATH, popup_xpath)
#popup_button.click()
#driver.implicitly_wait(10)

# Survey
xpath_one = "/html/body/div[9]/div/div/div[1]/div[1]/label/input"
wait.until(EC.visibility_of_element_located((By.XPATH, xpath_one)))
q_one = driver.find_element(By.XPATH, xpath_one)
q_one.click()

xpath_two = "/html/body/div[9]/div/div/div[2]/div[1]/label/input"
wait.until(EC.visibility_of_element_located((By.XPATH, xpath_two)))
q_two = driver.find_element(By.XPATH, xpath_two)
q_two.click()

xpath_three = "/html/body/div[9]/div/div/div[3]/div[2]/label/input"
wait.until(EC.visibility_of_element_located((By.XPATH, xpath_three)))
q_three = driver.find_element(By.XPATH, xpath_three)
q_three.click()

xpath_four = "/html/body/div[9]/div/div/div[4]/div[2]/label/input"
wait.until(EC.visibility_of_element_located((By.XPATH, xpath_four)))
q_four = driver.find_element(By.XPATH, xpath_four)
q_four.click()

xpath_five = "/html/body/div[9]/div/div/div[5]/div[1]/label/input"
wait.until(EC.visibility_of_element_located((By.XPATH, xpath_five)))
q_five = driver.find_element(By.XPATH, xpath_five)
q_five.click()

xpath_six = "/html/body/div[9]/div/div/div[6]/div[2]/label/input"
wait.until(EC.visibility_of_element_located((By.XPATH, xpath_six)))
q_six = driver.find_element(By.XPATH, xpath_six)
q_six.click()

xpath_seven = "/html/body/div[9]/div/div/div[7]/div[1]/label/input"
wait.until(EC.visibility_of_element_located((By.XPATH, xpath_seven)))
q_seven = driver.find_element(By.XPATH, xpath_seven)
q_seven.click()

xpath_eight = "/html/body/div[9]/div/div/div[8]/div[1]/label/input"
wait.until(EC.visibility_of_element_located((By.XPATH, xpath_eight)))
q_eight = driver.find_element(By.XPATH, xpath_eight)
q_eight.click()

xpath_nine = "/html/body/div[9]/div/div/div[9]/div/textarea"
wait.until(EC.visibility_of_element_located((By.XPATH, xpath_nine)))
q_nine = driver.find_element(By.XPATH, xpath_nine)
q_nine.send_keys("Hello World")

xpath_sbtn = "/html/body/div[9]/div/div/div[9]/div/button"
wait.until(EC.visibility_of_element_located((By.XPATH, xpath_sbtn)))
q_nine_btn = driver.find_element(By.XPATH, xpath_sbtn)
q_nine_btn.click()

# Phone Number
xpath_phone = "/html/body/div[9]/div/div/form/p[3]/input"
wait.until(EC.visibility_of_element_located((By.XPATH, xpath_phone)))
phone_input = driver.find_element(By.XPATH, xpath_phone)
phone_input.send_keys("9999999999999")


xpath_complete_btn = "/html/body/div[9]/div/div/form/p[4]/button"
wait.until(EC.visibility_of_element_located((By.XPATH, xpath_complete_btn)))
complete_btn = driver.find_element(By.XPATH, xpath_complete_btn)
complete_btn.click()

# till save button

# Edit Page
#xpath_save_edit = "/html/body/div[9]/div/div/form/p[4]/button"
#wait.until(EC.visibility_of_element_located((By.XPATH, xpath_save_edit)))
#save_edit_btn = driver.find_element(By.XPATH, xpath_save_edit)
#save_edit_btn.click()



#logout process
driver.implicitly_wait(time_to_wait=10)
driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div[4]/div[1]/a[2]").click()
driver.implicitly_wait(time_to_wait=10)
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()


#Members_Login_button=driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/nav/div/div[2]/ul/li[5]/a")
#Members_Login_button.click()


#driver.implicitly_wait(time_to_wait=10)

driver.find_element(By.XPATH,"/html/body/div[8]/div[1]/div/form/table/tbody/tr[4]/td[2]/input").click()

# user name field
driver.find_element(By.XPATH,"/html/body/div[8]/div[1]/div/form/table/tbody/tr[2]/td[2]/input").send_keys("wqr6526@gmail.com")
driver.implicitly_wait(time_to_wait=5)
driver.find_element(By.XPATH,"/html/body/div[8]/div[1]/div/form/table/tbody/tr[3]/td[2]/input").send_keys("qwerty12345")
driver.implicitly_wait(time_to_wait=5)
driver.find_element(By.XPATH,"/html/body/div[8]/div[1]/div/form/table/tbody/tr[5]/td[2]/input").click()

#driver.find_element(By.XPATH,"//a[normalize-space()='Allow']").click()
#driver.implicitly_wait(time_to_wait=10)
#driver.switch_to.alert.accept()





#driver.find_element(By.XPATH,"//a[@class='close_popup']").click()


#logout process

driver.implicitly_wait(time_to_wait=10)
driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div[4]/div[1]/a[2]").click()
driver.implicitly_wait(time_to_wait=10)
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()








# Edit Page (Save button 1)
#xpath_save_edit = "/html/body/div[20]/div[3]/div/input"
#wait.until(EC.visibility_of_element_located((By.XPATH, xpath_save_edit)))
#driver.find_element(By.XPATH,"/html/body/div[20]/div[3]/div/input").click()
#save_edit_btn = driver.find_element(By.XPATH, xpath_save_edit)

#save_edit_btn.click()


# Edit Page 2 (Save button 2)
#xpath_save_edit2 = "/
# html/body/div[19]/div[2]/div/div[2]/form/div[12]/div/input"
#wait.until(EC.visibility_of_element_located((By.XPATH, xpath_save_edit2)))
#save_edit_btn2 = driver.find_element(By.XPATH, xpath_save_edit2)
#save_edit_btn2.click()


