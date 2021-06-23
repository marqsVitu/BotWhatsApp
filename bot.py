from selenium import webdriver
import time


class Bot:
    def __init__(self):
        self.mensagem = "Hey, teste do bot aqui"
        self.grupos = ["Eu"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def Envia(self):

        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chatbox = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chatbox.click()
            chatbox.send_keys(self.mensagem)
            botao = self.driver.find_element_by_xpath(
            f"//span[@data-icon='send']")
            time.sleep(5)
            botao.click()
            time.sleep(8)


bot = Bot()
bot.Envia()
