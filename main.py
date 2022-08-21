import time
from selenium import webdriver

def log(log_text):
    log_text = str(time.strftime("%Y.%m.%d %H:%M:%S")) + " ➾ " + log_text
    print(log_text)
    log_file = open("log.txt", "a", encoding='utf-8')
    log_file.write(log_text + "\n")
    log_file.close()


urun_url = input("Ürün Linki Sonuna / Koymayın: ") #'https://www.trendyol.com/trendypassion/sirt-pusula-baskili-tshirt-p-260271556'  Ürün URL NOT SONUNA / KOYMAYIN
global_delay = 0.5
driver = webdriver.Chrome()
log('Bu program Can Tarafından Yapılmıştır.')
log('https://fastuptime.com ve https://speedsmm.com üzerinden bize ulaşabilirsiniz.')
log('Program başlatıldı')


try:
    driver.get(urun_url + "/yorumlar")
    time.sleep(5)
    kac_yorum_var = driver.find_element('xpath', "/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[4]/div").text
    kac_yorum_var = kac_yorum_var.replace(" yorumlu", "")
    kac_yorum_var = kac_yorum_var.split(",")[1]
    log('Toplam ' + kac_yorum_var + ' yorum var.')
    kac_yorum_var = kac_yorum_var.replace(" ", "")
    time.sleep(global_delay)
    for i in range(int(kac_yorum_var)):
        try:
            #/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[4]/div/div/div[4]/span/span[1]
            #/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[5]/div/div/div[4]/span/span[1]
            yorum = driver.find_element("xpath",'/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[' + str(i) + ']/div/div/div[4]/span/span[1]').text
            print(yorum)
            log('Yorum: '+ yorum)
            yorum_file = open("yorumlar.txt", "a", encoding='utf-8')
            yorum_file.write(yorum + "\n")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(global_delay)
        except:
            continue
except Exception as e:
    log('Hata: ' + str(e))
    log('Program sonlandı')
    driver.quit()
    exit()