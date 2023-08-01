from Board import Board
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class Driver:    
    def __init__(self):
        self.url = 'https://play2048.co/'
        chrome_options = Options() 
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
        self.driver.get(self.url)
        self.body = self.driver.find_element_by_tag_name('body')
        self.moves = {
            0: Keys.ARROW_UP,
            1: Keys.ARROW_DOWN,
            2: Keys.ARROW_LEFT,
            3: Keys.ARROW_RIGHT
        }
    
    def getBoard(self):
        matrix = [[0 for i in range(4)] for j in range(4)]
        tiles = self.driver.find_elements_by_class_name('tile')
        
        for tile in tiles:
            cls = tile.get_attribute('class')
            col, row = cls.split('tile-position-')[1].split(' ')[0].split('-')
            col, row = int(col)-1, int(row)-1
            num = int(cls.split('tile tile-')[1].split(' ')[0])
            if num > matrix[row][col]:
                matrix[row][col] = num
        
        return Board(matrix)
    
    def move(self, moveCode):
        self.body.send_keys(self.moves[moveCode])
        time.sleep(0.1)