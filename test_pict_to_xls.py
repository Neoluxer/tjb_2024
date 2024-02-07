from openpyxl import load_workbook
from openpyxl.drawing.image import Image
from openpyxl import Workbook
wb = Workbook()

# grab the active worksheet
ws = wb.active


# получаем объект изображения
logo = Image("logo.png")

# чтобы не заполнять весь лист логотипом
# можно изменить размер, атрибутами объекта
logo.height = 150
logo.width = 150

# добавляем объект изображение в ячейку "A3"
ws.add_image(logo, "A3")

# сохраняем
wb.save(filename="hello_world_logo.xlsx")