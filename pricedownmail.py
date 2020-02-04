from bs4 import BeautifulSoup
import requests
import smtplib
 
 # for amazon.in only
def amazon(URL,dprice,email):
  header= {'User-Agent': 'Enter your user agent'}
  result= requests.get(URL,headers=header)
  soup= BeautifulSoup(result.content, 'html.parser')
  price= soup.find(id= ['priceblock_ourprice','priceblock_dealprice']).get_text()
  price=price.replace(',','')
  convert=float(price[2:])
  if(convert<= float(dprice)):
      server= smtplib.SMTP('smtp.gmail.com',587 )
      server.ehlo()
      server.starttls()
      server.ehlo()
      server.login('enter email from which you want to send mail','enter password')
      subject= "ALERT ALERT ALERT"
      body= "PRICE FELL DOWN FOR YOUR AMAZON PRODUCT CLICK LINK TO CHECK: " +URL
      msg= f"Subject: {subject}\n\n{body}"

      server.sendmail('enter your email from which you want to send mail','enter password',email,msg)
      print("email sent")
      server.quit()

#for flipkart.com only
def flipkart(URL,dprice,email):
  header= {'User-Agent': 'enter your user agent'}
  result= requests.get(URL,headers=header)
  soup= BeautifulSoup(result.content, 'html.parser')
  price= soup.find('div',{'class':'_1vC4OE _3qQ9m1'}).get_text()
  price=price.replace(',','')
  convert=float(price[1:])
  if(convert<= float(dprice)):
      server= smtplib.SMTP('smtp.gmail.com',587 )
      server.ehlo()
      server.starttls()
      server.ehlo()
      server.login('enter your email from which you want to send mail','enter password')
      subject= "ALERT ALERT ALERT"
      body= "PRICE FELL DOWN FOR YOUR FLIPKART PRODUCT CLICK LINK TO CHECK: "+URL
      msg= f"Subject: {subject}\n\n{body}"

      server.sendmail('enter your email from which you want to send mail','enter password',email,msg)
      print("email sent")
      server.quit()

while True:
  site= input("ENTER SITE 'AMAZON' OR 'FLIPKART' OR QUIT TO END PROGRAM :")
  if site.lower() == 'flipkart':
    url= input("enter url of flipkart product: ")
    price= input("enter price: ")
    email= input("enter email on which you want alert: ")
    flipkart(url,price,email)
    time.sleep(60*60) #next email after 1 hour
    
  if site.lower() == 'amazon' :
    site= input("enter link of amazon product: ")
    price= input("enter price: ")
    email= input("enter email on which you want alert: ")
    amazon(site,price,email)
    time.sleep(60*60) #next email after 1 hr
  if site.lower() == 'quit' :
    break