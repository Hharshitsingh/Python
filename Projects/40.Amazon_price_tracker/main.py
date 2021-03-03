import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
url = "https://www.amazon.in/Let-Us-Python-Yashavant-Kanetkar/dp/9388511565/?_encoding=UTF8&pd_rd_w=rQNEo&pf_rd_p=25041c4e-bc5b-4063-99b1-635043c8cad4&pf_rd_r=GMVKF9PV45NPNG1ECQ8P&pd_rd_r=4ac87622-4c10-4db7-a0dd-887ae2e148f4&pd_rd_wg=mYkey&ref_=pd_gw_ci_mcx_mr_hp_d"
header = {
    # http://myhttpheader.com/
    "User-agent" : "",
    "Accept-Language":""
}
MY_EMAIL = ""
MY_PASSWORD = ""   

response = requests.get(url, headers = header)

soup = BeautifulSoup(response.content, "lxml")

title = soup.find(id = "productTitle").get_text().replace("\n", "")
# print(title)
price = soup.find(id="soldByThirdParty").get_text()


price_without_currency = float(((price.split("₹")[1]).split("\xa0")[1]).replace("\n", ""))
# print((price_without_currency))
# print(type(price_without_currency))

if price_without_currency < 270:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="",
            msg=f"Subject:Price Drop!\n\nNow, {title} Price {price_without_currency}, if You want to buy click on link {url}"
            )