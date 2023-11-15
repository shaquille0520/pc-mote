from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from flask import Flask, render_template, request, jsonify
import time
import os
options = Options()
options.add_experimental_option("excludeSwitches",["enable-automation"])
app = Flask(__name__)
driver = webdriver.Chrome(options = options)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    data = request.get_json()
    user_input = data['userInput']
    driver.get(user_input)
    while True:
        try:
            driver.execute_script('document.getElementsByTagName("video")[0].play()')
            print('Video is playing.')
            driver.fullscreen_window()
            break   
        except:
            os.system('clear') 
            print('starting video')
            time.sleep(1)

@app.route('/pause_video', methods=['POST'])
def pause():
    driver.execute_script('document.getElementsByTagName("video")[0].pause()')

@app.route('/play_video', methods=['POST'])
def play():
    driver.execute_script('document.getElementsByTagName("video")[0].play()')

@app.route('/forward', methods=['POST'])
def forward():
    driver.execute_script('document.getElementsByTagName("video")[0].currentTime += 30;')

@app.route('/back', methods=['POST'])
def back():
    driver.execute_script('document.getElementsByTagName("video")[0].currentTime -= 30;')

if __name__ == '__main__':
    app.run(host='192.168.0.111', port=5000)


