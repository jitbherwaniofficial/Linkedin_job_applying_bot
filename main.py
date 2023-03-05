from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

url = "https://www.linkedin.com/jobs/search/?currentJobId=3478270485&distance=&f_AL=&f_BE=&f_C=&f_CR=&f_CT=&f_E=&f_EA=&f_EL=&f_ES=&f_ET=&f_F=&f_FCE=&f_GC=&f_I=&f_JC=&f_JIYN=&f_JT=&f_LF=&f_PP=&f_SB=&f_SB2=&f_SB3=&f_T=&f_TP=&f_TPR=&f_WT=2&keywords=angular%20developer&latLong=&refresh=true&sortBy=&start=0"

driver.get(url)
driver.maximize_window()

signin = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]").click()
time.sleep(5)
email = driver.find_element_by_xpath('//*[@id="username"]')
email.send_keys(your_email)
password  = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(your_password)
password.send_keys(Keys.ENTER)

time.sleep(5)
jobs = []
jobs = driver.find_elements_by_css_selector('.ember-view .job-card-container .job-card-list__entity-lockup .artdeco-entity-lockup__content .artdeco-entity-lockup__title a')
for link in jobs:
    jobs.append(link)
print(jobs)

# if jobs == "Angular Developer":
#     jobs.click()
#     apply_btn = driver.find_element_by_css_selector('.jobs-apply-button').click()
#     next_btn = driver.find_element_by_css_selector('.artdeco-button__text').click()
#     choose = driver.find_element_by_css_selector('.artdeco-button__text').click()
#     next__btn = driver.find_element_by_css_selector('.artdeco-button__text').click()
#     text = driver.find_element_by_css_selector('.artdeco-text-input--input').send_keys('1')
#     review = driver.find_element_by_css_selector('.artdeco-button__text').click()
#     submit = driver.find_element_by_css_selector('.artdeco-button__text').click()

#     time.sleep(500)