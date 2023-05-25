import pandas as pd
from selenium import webdriver
from time import sleep as slp
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico)
browser.maximize_window()
