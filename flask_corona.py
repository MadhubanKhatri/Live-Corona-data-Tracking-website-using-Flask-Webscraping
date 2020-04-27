from flask import Flask,render_template
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

url = "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
data = r.content
soup = BeautifulSoup(data,'html.parser')
cases = soup.find_all('div',class_='maincounter-number')
total_cases = cases[0].get_text().strip()
total_deaths = cases[1].get_text().strip()
total_recovery = cases[2].get_text().strip()

@app.route("/")
def home():
    return "<h1><a href=/coronavirus>Get Update</a></h1>"

@app.route("/coronavirus")
def corona():
    return render_template("Scrapedata.html",Cases=total_cases,Deaths=total_deaths,Recovery=total_recovery)




app.run(debug=True)