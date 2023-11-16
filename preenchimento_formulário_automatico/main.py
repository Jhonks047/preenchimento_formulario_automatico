import time
from random import randint as r
from time import sleep as sp

from faker import Faker
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

service = Service(EdgeChromiumDriverManager().install())
nav = webdriver.Edge(service=service)
fk = Faker("pt_BR")


for c in range(0, 50):
    start_time = time.time()
    numeros_sorteados = []
    nav.get("https://forms.gle/R74nhYQrErFnLNvw8")


    multipla_escolha = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[{r(1, 5)}]/label/div/div[1]/div/div[3]/div'

    lista_suspensa = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[{r(3, 7)}]/span'

    escala_linear = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[{r(1, 10)}]/div[2]/div/div/div[3]/div'

    dia, mes, ano = r(1, 28), r(1, 12), r(1980, 2023)

    data_completa = f'{dia:02d}{mes:02d}{ano}'

    horario = [
        f'{r(0, 23):02d}',
        f'{r(0, 59):02d}'
    ]




    #Nome
    nav.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(fk.name())


    #Email
    nav.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(fk.email())



    #Múltipla escolha
    nav.find_element('xpath', multipla_escolha).click()



    #Caixa de seleção
    for _ in range(r(1, 5)):
        num = r(1, 5)
        while num in numeros_sorteados:
            num = r(1, 5)
        
        numeros_sorteados.append(num)
        
        nav.find_element('xpath', f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[{num}]/label/div/div[1]/div[2]').click()
    


    #Lista suspensa
    nav.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]/span').click()
    sp(0.3)
    nav.find_element('xpath', f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[{r(3, 7)}]/span').click()
    sp(0.3)


    #Escala linear
    nav.find_element('xpath', escala_linear).click()



    #Grade de múltipla escolha
    n = 0
    for __ in range(0, 5):
        nav.find_element('xpath', f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[{2+n}]/span/div[{r(2, 6)}]/div/div/div[3]/div').click()
        n += 2
    


    #Grade de caixa de seleção
    for _____ in range(2, 11, 2):
        numeros_sorteados2 = []
        for ___ in range(r(1, 5)):
            numero = r(1, 5)
            while numero in numeros_sorteados2:
                numero = r(1, 5)
            
            numeros_sorteados2.append(numero)
            
            nav.find_element('xpath', f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[{_____}]/label[{numero}]/div/div/div[2]').click()
        


    #Data dd/mm/aaaa
    nav.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input').send_keys(data_completa)


    #Horario
    nav.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys(horario[0])


    nav.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input').send_keys(horario[1])


    #Enviar
    nav.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tempo do {c+1}º formulário: {elapsed_time} segundos")