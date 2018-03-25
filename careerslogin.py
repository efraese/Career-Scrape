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
driver.implicitly_wait(3)
driver.get("https://nucareers.northeastern.edu/myAccount/dashboard.htm")
student = driver.find_element_by_xpath("""/html/body/div[3]/div/div/div[3]/div/div/div/div[3]/h2[1]/a[1]""")
student.click()
driver.implicitly_wait(3)
postings = driver.find_element_by_xpath("""//*[@id="mainContentDiv"]/div[2]/div/div[1]/div/a[2]""")
postings.click()
driver.implicitly_wait(3)
coop_postings = driver.find_element_by_xpath("""//*[@id="searchPostings"]/div[2]/div/ul/li[1]/a""")
coop_postings.click()
driver.implicitly_wait(3)
#all_postings = driver.find_element_by_xpath("""//*[@id="quickSearchCountsContainer"]/table[1]/tbody/tr[2]/td[2]/a""")
for_my_program = driver.find_element_by_xpath("""//*[@id="quickSearchCountsContainer"]/table[1]/tbody/tr[1]/td[2]/a""")
for_my_program.click()
driver.implicitly_wait(3)

filename = "jobdata.csv"
f = open(filename, "w")

headers = "job_title, company_name, state, city, link \n"
f.write(headers)

base_url = "https://nucareers.northeastern.edu/postings.htm?pId="

pages = driver.find_elements_by_class_name("orbis-posting-actions")[3].find_elements_by_tag_name("li")
num_pages_remaining = len(pages)-4
old_job = ""
new_job = ""
while(num_pages_remaining > 0):
    while(old_job == new_job):
        jobs = driver.find_elements_by_class_name("searchResult")
        new_job = jobs[0]
    for job in jobs:
        tds = job.find_elements_by_tag_name("td")
        job_title = tds[3].text.replace(",", " ").replace("ã", "a")

        job_link = base_url + job.get_attribute("id")[7:]

        company_name = tds[4].text.replace(",", " ").replace("ä", "a").replace("ã", "a")

        state = tds[8].text.replace(",", " ").replace("ä", "a").replace("ã", "a")
        city = tds[9].text.replace(",", " ").replace("ä", "a").replace("ã", "a")

        row = job_title + "," + company_name + "," + state + "," + city + "," + job_link + "\n"

        f.write(row)
    next_page = driver.find_element_by_xpath("""//*[@id="postingsTablePlaceholder"]/div[4]/div/ul/li[""" +str(len(pages)-1)+ """]/a""")
    next_page.click()
    driver.implicitly_wait(3)
    num_pages_remaining -= 1
    old_job = new_job
    
f.close()



    
    
