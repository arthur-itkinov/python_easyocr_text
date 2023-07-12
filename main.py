import os.path
import easyocr


def text_recognition(file_path, text_file_name='resullt.txt'):
    reader = easyocr.Reader(['ru', 'en'], gpu=False)
    result = reader.readtext(file_path, detail=0, paragraph=True, text_threshold=0.8)
    with open(text_file_name, 'w', encoding='utf-8') as file:
        for line in result:
            file.write(f"{line}\n\n")

    return result

def main():
    file_path = input('Enter a file path: ')
    if not os.path.exists(file_path):
        print('картинки не существует')
    print(text_recognition(file_path=file_path))



if __name__ == '__main__':
    main()
