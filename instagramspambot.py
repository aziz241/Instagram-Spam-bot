from selenium import webdriver
from time import sleep
import os
i = 0
j = 1
sayac = 0
os.system("pause")
driver = webdriver.Chrome()
dosya = open('hesaplar.txt')
liste = dosya.readlines()
print("*******İNSTAGRAM SPAM BOTU*******")
print("SORUMLULUK KULLANICIYA AİTTİR...")
print("TÜM HAKLARI SAKLIDIR @BASKAN")
sikayetedilecekhesap = input("Sikayet edilecek hesap adını eksiksiz giriniz: ")
sikayetsecim = int(input("Şikayet türü seçiniz: \n1-SPAM\n2-BUNDAN HOŞLANMADIM\n3-İNTİHAR KENDİNE ZARAR VERME\n4-YASADIŞI ÜRÜN SATIŞI\n5-ÇIPLAKLIK - CİNSELLİK\n6-NEFRET SÖYLEMİ VE SEMBOLLERİ\n7-ŞİDDET VEYA TEHLİKELİ ÖRGÜT\n8-ZORBALIK VEYA TACİZ\n9-SAHTEKARLIK DOLANDIRICILIK\n10-YANLIŞ BİLGİLER\n:"))
while sikayetsecim < 0 or sikayetsecim > 11:
    print("Geçersiz tuşlama otomatik çıkış etkin...")
    break
if sikayetsecim == 1:
    print("SPAM işlemi başladı")
    for y in liste:
        driver.get('https://www.instagram.com')
        sleep(4)
        username = driver.find_element_by_name('username').send_keys(liste[i])
        password = driver.find_element_by_name('password').send_keys(liste[j])
        sleep(4)
        girisbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[3]/button')
        if girisbutton:
            girisbutton.click()
        sleep(7)
        simdidegil = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil:
            simdidegil.click()
        sleep(7)
        simdidegil2 = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil2:
            simdidegil2.click()
        sleep(7)
        aramakutusu = driver.find_element_by_xpath('//input[@type="text"]').send_keys(sikayetedilecekhesap)
        sleep(7)
        profile = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
        sleep(7)
        sikayetbutonbasım = driver.find_element_by_class_name('wpO6b').click()
        sleep(7)
        sikayet = driver.find_element_by_xpath('//button[contains(text(), "Kullanıcıyı Şikayet Et")]').click()
        sleep(8)
        spam = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div').click()
        sleep(8)
        # kapatbuton = driver.find_element_by_class_name('//button[contains(text(), "Kapat")]').click()
        i += 2
        j += 2
        driver.execute_script("window.open('');")
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sleep(2)
        driver.delete_all_cookies()
        sleep(1)
        driver.close()
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sayac += 1
        print("Hesap sayısı: ",sayac)
elif sikayetsecim == 2:
    print("SEÇİLEN İŞLEM: BUNDAN HOŞLANMADIM \nİŞLEM BAŞLADI")
    for y in liste:
        driver.get('https://www.instagram.com')
        sleep(4)
        username = driver.find_element_by_name('username').send_keys(liste[i])
        password = driver.find_element_by_name('password').send_keys(liste[j])
        sleep(4)
        girisbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[3]/button')
        if girisbutton:
            girisbutton.click()
        sleep(7)
        simdidegil = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil:
            simdidegil.click()
        sleep(7)
        simdidegil2 = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil2:
            simdidegil2.click()
        sleep(7)
        aramakutusu = driver.find_element_by_xpath('//input[@type="text"]').send_keys(sikayetedilecekhesap)
        sleep(7)
        profile = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
        sleep(7)
        sikayetbutonbasım = driver.find_element_by_class_name('wpO6b').click()
        sleep(7)
        sikayet = driver.find_element_by_xpath('//button[contains(text(), "Kullanıcıyı Şikayet Et")]').click()
        sleep(8)
        uygunsuz = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(8)
        hesapsikayet = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(3)
        olmamasıgerekenicerik = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div').click()
        sleep(3)
        bundanhoslanmadım = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div').click()
        sleep(3)
        i += 2
        j += 2
        driver.execute_script("window.open('');")
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sleep(2)
        driver.delete_all_cookies()
        sleep(1)
        driver.close()
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sayac += 1
        print("Hesap sayısı: ", sayac)
elif sikayetsecim == 3:
    print("SEÇİLEN İŞLEM: İNTİHAR KENDİNE ZARAR VERME\nİŞLEM BAŞLADI")
    for y in liste:
        driver.get('https://www.instagram.com')
        sleep(4)
        username = driver.find_element_by_name('username').send_keys(liste[i])
        password = driver.find_element_by_name('password').send_keys(liste[j])
        sleep(4)
        girisbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[3]/button')
        if girisbutton:
            girisbutton.click()
        sleep(7)
        simdidegil = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil:
            simdidegil.click()
        sleep(7)
        simdidegil2 = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil2:
            simdidegil2.click()
        sleep(7)
        aramakutusu = driver.find_element_by_xpath('//input[@type="text"]').send_keys(sikayetedilecekhesap)
        sleep(7)
        profile = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
        sleep(7)
        sikayetbutonbasım = driver.find_element_by_class_name('wpO6b').click()
        sleep(7)
        sikayet = driver.find_element_by_xpath('//button[contains(text(), "Kullanıcıyı Şikayet Et")]').click()
        sleep(8)
        uygunsuz = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(8)
        hesapsikayet = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(3)
        olmamasıgerekenicerik = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div').click()
        sleep(3)
        kendinezarar = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(3)
        i += 2
        j += 2
        driver.execute_script("window.open('');")
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sleep(2)
        driver.delete_all_cookies()
        sleep(1)
        driver.close()
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sayac += 1
        print("Hesap sayısı: ", sayac)
elif sikayetsecim == 4:
    sikayetsecim2 = int(input("HANGİ ÜRÜNÜN TİCARETİ YAPILIYOR:\n1-Uyuşturucu\n2-Silah\n3-Nesli tükenmekte olan hayvan\n:"))
    print("İşlem Başladı")
    while sikayetsecim2 < 0 or sikayetsecim > 4:
        print("GEÇERSİZ SEÇİM OTOMATİK ÇIKIŞ ETKİN..")
        break
    for y in liste:
        driver.get('https://www.instagram.com')
        sleep(4)
        username = driver.find_element_by_name('username').send_keys(liste[i])
        password = driver.find_element_by_name('password').send_keys(liste[j])
        sleep(4)
        girisbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[3]/button')
        if girisbutton:
            girisbutton.click()
        sleep(7)
        simdidegil = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil:
            simdidegil.click()
        sleep(7)
        simdidegil2 = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil2:
            simdidegil2.click()
        sleep(7)
        aramakutusu = driver.find_element_by_xpath('//input[@type="text"]').send_keys(sikayetedilecekhesap)
        sleep(7)
        profile = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
        sleep(7)
        sikayetbutonbasım = driver.find_element_by_class_name('wpO6b').click()
        sleep(7)
        sikayet = driver.find_element_by_xpath('//button[contains(text(), "Kullanıcıyı Şikayet Et")]').click()
        sleep(8)
        uygunsuz = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(8)
        hesapsikayet = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(3)
        olmamasıgerekenicerik = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div').click()
        sleep(3)
        yasakürünticaret = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[3]/div').click()
        sleep(3)
        if sikayetsecim2 == 1:
            sec = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/fieldset/div[1]/label/div').click()
            sec2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[6]/button').click()
            sleep(3)
        elif sikayetsecim2 == 2:
            sec = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/fieldset/div[2]/label/div').click()
            sec2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[6]/button').click()
            sleep(3)
        elif sikayetsecim2 == 3:
            sec = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/fieldset/div[3]/label/div').click()
            sec2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[6]/button').click()
            sleep(3)
        i += 2
        j += 2
        driver.execute_script("window.open('');")
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sleep(2)
        driver.delete_all_cookies()
        sleep(1)
        driver.close()
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sayac += 1
        print("Hesap sayısı: ", sayac)
elif sikayetsecim == 5:
    sikayetsecim2 = int(input("HANGİ TÜR İHLAL MEVCUT:\n1-Çıplaklık ve Pornografi\n2-Cinsel istismar veya cinsel ilişki talebi\n3-Rızasız paylaşılan mahrem görüntüler\n4-Çocuk çıplaklığı\n:"))
    while sikayetsecim2 < 0 or sikayetsecim > 5:
        print("GEÇERSİZ SEÇİM OTOMATİK ÇIKIŞ ETKİN..")
        break
    print("İşlem Başladı")
    for y in liste:
        driver.get('https://www.instagram.com')
        sleep(4)
        username = driver.find_element_by_name('username').send_keys(liste[i])
        password = driver.find_element_by_name('password').send_keys(liste[j])
        sleep(4)
        girisbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[3]/button')
        if girisbutton:
            girisbutton.click()
        sleep(7)
        simdidegil = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil:
            simdidegil.click()
        sleep(7)
        simdidegil2 = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil2:
            simdidegil2.click()
        sleep(7)
        aramakutusu = driver.find_element_by_xpath('//input[@type="text"]').send_keys(sikayetedilecekhesap)
        sleep(7)
        profile = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
        sleep(7)
        sikayetbutonbasım = driver.find_element_by_class_name('wpO6b').click()
        sleep(7)
        sikayet = driver.find_element_by_xpath('//button[contains(text(), "Kullanıcıyı Şikayet Et")]').click()
        sleep(8)
        uygunsuz = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(8)
        hesapsikayet = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(3)
        olmamasıgerekenicerik = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div').click()
        sleep(3)
        yasakgörüntü = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[4]/div').click()
        sleep(3)
        if sikayetsecim2 == 1:
            sec = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/fieldset/div[1]/label/div').click()
            sec2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[6]/button').click()
            sleep(3)
        elif sikayetsecim2 == 2:
            sec = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/fieldset/div[2]/label/div').click()
            sec2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[6]/button').click()
            sleep(3)
        elif sikayetsecim2 == 3:
            sec = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/fieldset/div[3]/label/div').click()
            sec2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[6]/button').click()
        elif sikayetsecim2 == 4:
            sec = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/fieldset/div[4]/label/div').click()
            sec2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[6]/button').click()
            sleep(3)
        i += 2
        j += 2
        driver.execute_script("window.open('');")
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sleep(2)
        driver.delete_all_cookies()
        sleep(1)
        driver.close()
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sayac += 1
        print("Hesap sayısı: ", sayac)
elif sikayetsecim == 6:
    print("SEÇİLEN İŞLEM: NEFRET SÖYLEMİ VEYA SEMBOLLERİ \nİŞLEM BAŞLADI")
    for y in liste:
        driver.get('https://www.instagram.com')
        sleep(4)
        username = driver.find_element_by_name('username').send_keys(liste[i])
        password = driver.find_element_by_name('password').send_keys(liste[j])
        sleep(4)
        girisbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[3]/button')
        if girisbutton:
            girisbutton.click()
        sleep(7)
        simdidegil = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil:
            simdidegil.click()
        sleep(7)
        simdidegil2 = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil2:
            simdidegil2.click()
        sleep(7)
        aramakutusu = driver.find_element_by_xpath('//input[@type="text"]').send_keys(sikayetedilecekhesap)
        sleep(7)
        profile = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
        sleep(7)
        sikayetbutonbasım = driver.find_element_by_class_name('wpO6b').click()
        sleep(7)
        sikayet = driver.find_element_by_xpath('//button[contains(text(), "Kullanıcıyı Şikayet Et")]').click()
        sleep(8)
        uygunsuz = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(8)
        hesapsikayet = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(3)
        olmamasıgerekenicerik = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div').click()
        sleep(3)
        nefretsöylemi = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[5]/div').click()
        sleep(3)
        gönder = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/button')
        sleep(2)
        i += 2
        j += 2
        driver.execute_script("window.open('');")
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sleep(2)
        driver.delete_all_cookies()
        sleep(1)
        driver.close()
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sayac += 1
        print("Hesap sayısı: ", sayac)
elif sikayetsecim == 7:
    print("SEÇİLEN İŞLEM: ŞİDDET VEYA TEHLİKELİ ÖRGÜT")
    sikayetsecim2 = int(input("HANGİ TÜR İHLAL MEVCUT:\n1-ŞİDDET TEHDİDİ\n2-HAYVAN İSTİSMARI\n3-ÖLÜM VEYA AĞIR YARALAMA\n4-TEHLİKELİ ÖRGÜTLER VEYA KİŞİLER\n:"))
    print("İşlem Başladı")
    while sikayetsecim2 < 0 or sikayetsecim > 5:
        print("GEÇERSİZ SEÇİM OTOMATİK ÇIKIŞ ETKİN..")
        break
    print("İşlem Başladı")
    for y in liste:
        driver.get('https://www.instagram.com')
        sleep(4)
        username = driver.find_element_by_name('username').send_keys(liste[i])
        password = driver.find_element_by_name('password').send_keys(liste[j])
        sleep(4)
        girisbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[3]/button')
        if girisbutton:
            girisbutton.click()
        sleep(7)
        simdidegil = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil:
            simdidegil.click()
        sleep(7)
        simdidegil2 = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil2:
            simdidegil2.click()
        sleep(7)
        aramakutusu = driver.find_element_by_xpath('//input[@type="text"]').send_keys(sikayetedilecekhesap)
        sleep(7)
        profile = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
        sleep(7)
        sikayetbutonbasım = driver.find_element_by_class_name('wpO6b').click()
        sleep(7)
        sikayet = driver.find_element_by_xpath('//button[contains(text(), "Kullanıcıyı Şikayet Et")]').click()
        sleep(8)
        uygunsuz = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(8)
        hesapsikayet = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(3)
        olmamasıgerekenicerik = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div').click()
        sleep(3)
        yasakgörüntü = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[4]/div').click()
        sleep(3)
        if sikayetsecim2 == 1:
            sec = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/fieldset/div[1]/label/div').click()
            sec2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[6]/button').click()
            sleep(3)
        elif sikayetsecim2 == 2:
            sec = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/fieldset/div[2]/label/div').click()
            sec2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[6]/button').click()
            sleep(3)
        elif sikayetsecim2 == 3:
            sec = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/fieldset/div[3]/label/div').click()
            sec2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[6]/button').click()
        elif sikayetsecim2 == 4:
            sec = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/fieldset/div[4]/label/div').click()
            sec2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[6]/button').click()
            sleep(3)
        i += 2
        j += 2
        driver.execute_script("window.open('');")
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sleep(2)
        driver.delete_all_cookies()
        sleep(1)
        driver.close()
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sayac += 1
        print("Hesap sayısı: ", sayac)
elif sikayetsecim == 8:
    print("SEÇİLEN İŞLEM: ZORBALIK VEYA TACİZ")
    sikayetsecim2 = int(input("KİME YAPILIYOR:\n1-BEN\n2-TANIDIĞIM BİRİ\n3-BAŞKA BİRİSİ\n:"))
    print("İşlem Başladı")
    while sikayetsecim2 < 0 or sikayetsecim > 5:
        print("GEÇERSİZ SEÇİM OTOMATİK ÇIKIŞ ETKİN..")
        break
    print("İşlem Başladı")
    for y in liste:
        driver.get('https://www.instagram.com')
        sleep(4)
        username = driver.find_element_by_name('username').send_keys(liste[i])
        password = driver.find_element_by_name('password').send_keys(liste[j])
        sleep(4)
        girisbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[3]/button')
        if girisbutton:
            girisbutton.click()
        sleep(7)
        simdidegil = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil:
            simdidegil.click()
        sleep(7)
        simdidegil2 = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil2:
            simdidegil2.click()
        sleep(7)
        aramakutusu = driver.find_element_by_xpath('//input[@type="text"]').send_keys(sikayetedilecekhesap)
        sleep(7)
        profile = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
        sleep(7)
        sikayetbutonbasım = driver.find_element_by_class_name('wpO6b').click()
        sleep(7)
        sikayet = driver.find_element_by_xpath('//button[contains(text(), "Kullanıcıyı Şikayet Et")]').click()
        sleep(8)
        uygunsuz = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(8)
        hesapsikayet = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(3)
        olmamasıgerekenicerik = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div').click()
        sleep(3)
        yasakgörüntü = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[4]/div').click()
        sleep(3)
        if sikayetsecim2 == 1:
            sec = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div').click()
            sec2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/button').click()
            sleep(2)
        elif sikayetsecim2 == 2:
            sec = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
            sleep(2)
        elif sikayetsecim2 == 3:
            sec = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[3]/div').click()
            sleep(2)
        i += 2
        j += 2
        driver.execute_script("window.open('');")
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sleep(2)
        driver.delete_all_cookies()
        sleep(1)
        driver.close()
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sayac += 1
        print("Hesap sayısı: ", sayac)
elif sikayetsecim == 9:
    print("SEÇİLEN İŞLEM: SAHTEKARLIK VE DOLANDIRICILIK")
    print("İŞLEM BAŞLADI")
    for y in liste:
        driver.get('https://www.instagram.com')
        sleep(4)
        username = driver.find_element_by_name('username').send_keys(liste[i])
        password = driver.find_element_by_name('password').send_keys(liste[j])
        sleep(4)
        girisbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[3]/button')
        if girisbutton:
            girisbutton.click()
        sleep(7)
        simdidegil = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil:
            simdidegil.click()
        sleep(7)
        simdidegil2 = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil2:
            simdidegil2.click()
        sleep(7)
        aramakutusu = driver.find_element_by_xpath('//input[@type="text"]').send_keys(sikayetedilecekhesap)
        sleep(7)
        profile = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
        sleep(7)
        sikayetbutonbasım = driver.find_element_by_class_name('wpO6b').click()
        sleep(7)
        sikayet = driver.find_element_by_xpath('//button[contains(text(), "Kullanıcıyı Şikayet Et")]').click()
        sleep(8)
        uygunsuz = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(8)
        hesapsikayet = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(3)
        olmamasıgerekenicerik = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div').click()
        sleep(3)
        sahtekarlık = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[9]/div').click()
        sleep(3)
        i += 2
        j += 2
        driver.execute_script("window.open('');")
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sleep(2)
        driver.delete_all_cookies()
        sleep(1)
        driver.close()
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sayac += 1
        print("Hesap sayısı: ", sayac)
elif sikayetsecim == 10:
    print("SEÇİLEN İŞLEM: YANLIŞ BİLGİLER")
    print("İŞLEM BAŞLADI")
    for y in liste:
        driver.get('https://www.instagram.com')
        sleep(4)
        username = driver.find_element_by_name('username').send_keys(liste[i])
        password = driver.find_element_by_name('password').send_keys(liste[j])
        sleep(4)
        girisbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[3]/button')
        if girisbutton:
            girisbutton.click()
        sleep(7)
        simdidegil = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil:
            simdidegil.click()
        sleep(7)
        simdidegil2 = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        if simdidegil2:
            simdidegil2.click()
        sleep(7)
        aramakutusu = driver.find_element_by_xpath('//input[@type="text"]').send_keys(sikayetedilecekhesap)
        sleep(7)
        profile = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
        sleep(7)
        sikayetbutonbasım = driver.find_element_by_class_name('wpO6b').click()
        sleep(7)
        sikayet = driver.find_element_by_xpath('//button[contains(text(), "Kullanıcıyı Şikayet Et")]').click()
        sleep(8)
        uygunsuz = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(8)
        hesapsikayet = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(3)
        olmamasıgerekenicerik = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div').click()
        sleep(3)
        yanlısbilgi = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[10]/div').click()
        sleep(3)
        i += 2
        j += 2
        driver.execute_script("window.open('');")
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sleep(2)
        driver.delete_all_cookies()
        sleep(1)
        driver.close()
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        sayac += 1
        print("Hesap sayısı: ", sayac)




