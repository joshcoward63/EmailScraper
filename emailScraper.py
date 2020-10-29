"""Initial Setup"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

"""Start of Main Program"""

# path = input("Please enter a URL\n")
urlList = ["http://www.bgibson.com/Company/Staff-Directory","https://www.cl.cam.ac.uk/~jac22/", "https://www.cl.cam.ac.uk/~bjc63/", "https://www.cl.cam.ac.uk/~jac22/", "https://www.cl.cam.ac.uk/~ah793/", "https://www.cl.cam.ac.uk/~ad260/", "https://sites.google.com/view/jinghan/contact", "http://miguelballesteros.com/"] 
driver.get("https://www.cl.cam.ac.uk/~ah793/")

def BSULayout():
    """ Boise State emails"""
    emails = []
    i = 1
    articles = driver.find_elements_by_tag_name("li")
    for article in articles:
        xpath = "/html/body/main/div[3]/div/div/div/div[2]/ul/li[" + str(i) + "]/div[2]/div[3]/div[3]/a/span"
        xpath2 = "/html/body/main/div[3]/div/div/div/div[2]/ul/li[" + str(i) + "]/div[1]/div[3]/div[3]/a/span"
        try:
            email = article.find_element_by_xpath(xpath)
            emails.append(email.text)
            i+=1
        except:
            try:
                email = article.find_element_by_xpath(xpath2)            
                emails.append(email.text)
                i+=1
            except:
                pass
    return emails
def bGibsonLayout():
    """bggibson"""
    i = 1
    emails = []
    pageSizeButton = driver.find_element_by_id("dnn_ctr704_View_grdAdUsers_ctl00_ctl03_ctl01_PageSizeComboBox").click()
    
    time.sleep(1)
    maxSizeButton = driver.find_element_by_xpath("/html/body/form/div[1]/div/div/ul/li[3]").click()
    time.sleep(3)
    
     
    articles = driver.find_elements_by_tag_name("tr")
    for article in articles:
        try:
            xpath = "/html/body/form/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/table/tbody/tr[" + str(i) + "]/td[7]"
            email = article.find_element_by_xpath(xpath)
            emails.append(email.text)
            i+= 1
        except:
            pass

    return emails

# /html/body/div[4]/div/div/p[3]/br
# /html/body/div[4]/div/div[3]/div/p[1]
# /html/body/div[4]/div/div[3]/div/p[1]
# /html/body/pre/a[10]

def clCamLayout():
    i = 1
    emails = []
    try:
        email = driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div/p[1]")
        emails.append(email.text)
    except :
        try:
            email = driver.find_element_by_xpath("/html/body/div[4]/div/div/p[3]/br")
            emails.append(email.text)
        except:
            try:
                email = driver.find_element_by_xpath("/html/body/pre")
                emails.append(email.text)
            except :
                pass
    return emails


def cleanEmail(email):
    email = email.replace("E-mail: ","")
    email = email.replace("Cal: agenda + bio + family + week + pix + office hours\nPPP: papers + professments + projects + blog", "")
    email= email.replace("+"," ")
    email = email.replace(" do NOT post - I may not pick it up for months", "")
    email = email.replace("Sober October 2020 for Macmillan Cancer Support", "")
    email = email.replace("\n","")
    email = email.replace("Email", "")
    email = email.replace(" [at] ", "@")
    return email


emails = clCamLayout()
""" Print out all scraped emails"""
i = 1
for email in emails:
    if len(email) > 2:   
        email = cleanEmail(email)    
        print(str(i) + ". " + email)
        i+=1


