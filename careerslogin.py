from selenium import webdriver
chrome = "/Users/fuzzyeric30/Desktop/chromedriver"
driver = webdriver.Chrome(chrome)
driver.get("https://neuidmsso.neu.edu/cas-server/login?service=https%3A%2F%2Fneuidmsso.neu.edu%2Fidp%2FAuthn%2FExtCas%3Fconversation%3De1s1&entityId=https%3A%2F%2Fnucareers.northeastern.edu%2Fshibboleth")
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
my_username = input("Enter your Username: ")
my_password = input("Enter your Password: ")
username.send_keys(my_username)
password.send_keys(my_password)
login = driver.find_element_by_xpath("""//*[@id="fm1"]/div[3]/input[4]""")
login.submit()
driver.get("https://nucareers.northeastern.edu/myAccount/dashboard.htm")
student = driver.find_element_by_xpath("""/html/body/div[3]/div/div/div[3]/div/div/div/div[3]/h2[1]/a[1]""")
student.click()
postings = driver.find_element_by_xpath("""//*[@id="mainContentDiv"]/div[2]/div/div[1]/div/a[2]""")
postings.click()
coop_postings = driver.find_element_by_xpath("""//*[@id="searchPostings"]/div[2]/div/ul/li[1]/a""")
coop_postings.click()
for_my_program = driver.find_element_by_xpath("""//*[@id="quickSearchCountsContainer"]/table[1]/tbody/tr[1]/td[2]/a""")
for_my_program.click()