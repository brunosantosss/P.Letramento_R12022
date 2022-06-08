import pyttsx3, cv2, os, re
from time import sleep
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pytesseract import pytesseract

voice = pyttsx3.init()
pytesseract.tesseract_cmd = r"C:\Users\Bruno\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def IsNumeric(param):
    format_num = re.compile(r'^[1-9][0-9]*$')
    result = re.match(format_num, param)

    if result:
        return True
    else:
        return False

def Voice(text):
    voice.say(text)
    voice.runAndWait()

def ReadImage():
    caminho_do_arquivo = askopenfilename(filetypes = (("Imagens JPEG", "*.jpeg"), ("Imagens PNG", "*.png"), ("Arquivo PDF", "*.pdf")))

    if caminho_do_arquivo:
        img = cv2.imread(caminho_do_arquivo)

        img_texto = pytesseract.image_to_string(img, lang='por')

        os.system('cls')
        print("=" * 215)
        Voice("Preparando para leitura")
        print(img_texto)
        print("=" * 215)
        Voice(img_texto)
        os.system('cls')
        ShowOptions()
    else: 
        Voice("Nenhuma imagem selecionada")
        os.system('cls')
        ShowOptions()

def ShowOptions():
    print("=" * 215)
    print('\t\t\t\t\t\t\t\t\t\t\t\tAplicativo de Acessibilidade\n')

    print('.1 Escolher Imagem')
    print('.2 Voltar')
    print('\n')
    print("=" * 215)

    Voice('Digite 1 para escolher a imagem para leitura')
    Voice('Digite 2 para voltar ao menu')
    Menu_Option = input('--> Digite aqui a opção que deseja executar: ')
    if IsNumeric(Menu_Option):
        if Menu_Option == '1': # Escolher Imagem
            Voice("Selecione a imagem que deseja realizar a leitura")
            ReadImage()
        elif Menu_Option == '2': # Voltar
            os.system('cls')
            ShowMenu()
        else:
            os.system('cls')
            ShowOptions()
    else:
        os.system('cls')
        Voice("Opção invalida")
        ShowOptions()

def ShowMenu():
    print("=" * 215)
    print('\t\t\t\t\t\t\t\t\t\t\t\tAplicativo de Acessibilidade\n')

    print('.1 Iniciar aplicação')
    print('.2 Encerrar aplicação')
    print('\n')
    print('=' * 215)
    
    Voice('Digite 1 para iniciar aplicação')
    Voice('Digite 2 para fechar aplicação')
    Menu_Option = input('--> Digite aqui a opção que deseja executar: ')
    
    if IsNumeric(Menu_Option):
        if Menu_Option == '1': # Iniciar Aplicacao
            os.system('cls')
            ShowOptions()
        elif Menu_Option == '2': # Encerrar Aplicacao
            os.system('cls')
            Voice('Encerrando aplicação...')
            sleep(2)
            exit()
        else:
            os.system('cls')
            Voice('Opção invalida!\n')
            ShowMenu()
    else:
        os.system('cls')
        Voice('Opção invalida!\n')
        ShowMenu()

os.system('cls')
ShowMenu()