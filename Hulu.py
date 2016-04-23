
import requests
import pickle
from bs4 import BeautifulSoup
res = requests.get("https://tw.taobao.com/product/%E5%A4%9A%E6%A8%A3%E5%B1%8B-%E8%91%AB%E8%98%86-%E4%BF%9D%E6%BA%AB%E6%9D%AF.htm")
soup = BeautifulSoup(res.text,"html.parser")
#id = 1
#itemsoup = soup.select(".clearfix")
def get_data():
    id = 1
    #hululist = []
    hulustr = ""
    for i in soup.select(".item"):
        """
        #print(id, i.select("strong")[0].text, i.select(".title")[0].text.strip(), i.select(".J_NickPopup")[0].text)
        hululist.append(id)
        hululist.append(i.select("strong")[0].text)
        hululist.append(i.select(".title")[0].text.strip())
        hululist.append('\n')
        #hululist.append(id+i.select("strong")[0].text+i.select(".title")[0].text.strip())
        #hululist.append(i.select(".J_NickPopup")[].text)
        """
        hulustr += str(id)+" - $"+i.select("strong")[0].text+" - "
        if i.select(".J_NickPopup") != []:
            hulustr += i.select(".J_NickPopup")[0].text+" : "
        else:
            pass
        hulustr += i.select(".title")[0].text.strip()+'\n'
        id += 1
        #print(i.select(".J_NickPopup"))
    #return str(hululist)
    return hulustr



with open("hulu_list.txt", "w", encoding='utf-8') as list:
    #pickle.dump(get_data(),list)
    list.writelines(get_data())
    #list.write(str(get_data()))
