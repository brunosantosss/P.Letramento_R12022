from pytesseract import pytesseract
import pyttsx3
import cv2

# Lendo a imagem
img = cv2.imread("elo.jpeg")

# Iniciando o motor de reproducao da voz
voice = pyttsx3.init()

# Caminho de instalacao do executavel do tesseract 
caminho_tesseract = r"C:\Users\Bruno\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = caminho_tesseract

# Transformando a imagem para string
img_texto = pytesseract.image_to_string(img, lang='por')

print(img_texto)
voice.say(img_texto)
voice.runAndWait()
