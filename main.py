# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path

"""
Программа переобразует ПДФ файл в МП3
Для начала установим библиотеку pdfplumber gtts art
"""


def pdf_to_mp3(file_path='test.pdf', language='ru'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        #  return 'File exists!' # yesli putb faila vernyi vozvrat
        print(f"['+'] Original file: {Path(file_path).name}")
        print("[+] Processing...")


        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        # hod - udalyaem  perenosy stranict?probely i simvoly
            # with open('text1.txt', 'w') as file:
            #     file.write(text)
            # text = text.replace('\n', '')
            #
            # with open('text2.txt', 'w') as file:
            #     file.write(text)
        # hod2 perevodim text v audiofile
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f"{file_name}.mp3")

        return f"[+] {file_name}.mp3 saved succesfully!\n---Have a good day!---"
    else:
        return 'File not exists, chek the file path'


def main():
    tprint("PDF>>TO>>MP3", font='bulbhead')
    file_path = input("\nEnter a file's path: ")
    language = input("Choose language, for example 'en' or 'ru': ")
    print(pdf_to_mp3(file_path, language=language))

    #1 print(pdf_to_mp3(file_path='/home/kja/pythonProject/PDFtoMP3/pdf_files/стихи.pdf'))


if __name__ == '__main__':
    main()
