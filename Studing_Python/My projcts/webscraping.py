# 1st step install and import modules
 #-- pip/pip3 install lxml
 #-- pip/pip3 install requests
 #-- pip/pip3 install beatifulsoup4
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title = []
company_name = []
locations_name = []
skill = []
links = []
responsibilities = []
page_num = 0

while True:
    # 2nd step use requests to fetch the url
    try:
        result = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={page_num}")

        # 3rd step save page content/markup
        src = result.content
        #print(src)

        # 4th step create soup object to parse content
        soup = BeautifulSoup(src, "lxml")
        #print(soup)

        page_limit = int(soup.find("strong").text)
        
        if (page_num > page_limit // 15):
            print("pages ended")
            break


        # 5th step find the elements containing info we need
        #-- job titles, job skills, company names, location names
        job_titles = soup.find_all("h2", {"class":"css-m604qf" } )
        company_names = soup.find_all("a", {"class":"css-17s97q8"})
        locations_names = soup.find_all("span", {"class":"css-5wys0k"})
        job_skills = soup.find_all("div", {"class":"css-y4udm8"})



        # 6th step loop over returned lists to extract needed info into other lists
        for i in range(len(job_titles)):
            job_title.append(job_titles[i].text)
            links.append(job_titles[i].find("a").attrs['href'])
            company_name.append(company_names[i].text)
            locations_name.append(locations_names[i].text)
            skill.append(job_skills[i].text)
        page_num += 1
    except:
        print("error occurred")
        break
    print("page switched")


for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    requirements = soup.find("div", {"class":"css-1t5f0fr"}).ul
    respon_text = ""
    for li in requirements.find_all("li"):
        respon_text += li.text+"| "
    respon_text = respon_text[:-2]
    responsibilities.append(respon_text)






#print(job_title, company_name, locations_name, skill)
# 7th step create csv file and fill it with value
file_list = [job_title, company_name, locations_name, skill, links, responsibilities]
exported = zip_longest(*file_list)
with open("/Users/ehab/Desktop/jobtutorials.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Job title", "company name", "Job location", "Job skills", "links", "responsibilities"])
    wr.writerows(exported)
# 8th step to fetch the link of the job and fetch in page details



