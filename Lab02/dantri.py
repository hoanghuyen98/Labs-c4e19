# 1. Download webpage
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "http://dantri.com.vn"
# # 1.1 Ope a coection
# conn = urlopen(url)
# # 1.2 Read data
# data = conn.read()
# # 1.3 Decode
# html = data.decode("utf-8")
# # print(html)
html_content = urlopen(url).read().decode("utf-8")
# print(html)
 
# save to file
# html_file = open("dantri.html", "wb") # write
# html_file.write(data)
# html_file.close()

# 2. Extract ROI ( region of interest )
# html, xml, xhtml
soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())
ul = soup.find("ul", "ul1 ulnew")
# Note : chỉ Class mới viết ul = soup.find("ul", "ul1 ulnew")
# print(ul.prettify())

# 3. Extract info
li_list = ul.find_all("li") # tim tat ca cac the li
new_list = []
for li in li_list
    a = li.h4.a
    title = a.string
    href = url + a['href']
    news = {
        'Title': title,
        'Link' : href 
    }
    new_list.append(news)
    
# lấy a đi vào h4
# h4 = li.find("h4")
# a = h4.find("a")
    
# # print(li_list) # 1 list nên ko prettify
# print(li.prettify())

# 4. Save data to excel
pyexcel.save_as(records=new_list, dest_file_name="dantri.xlsx")



