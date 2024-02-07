import math
import svgwrite
from MODELS import sketches as sk
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

forwardlist = ['форвард', 'forward', 'форвард', 'fun Ward', 'forward ', 'форвардер', 'вперед', 'прямо']
rightlist = ['right', 'рейд']
leftlist = ['left', 'лифт', 'лофт', 'лет', 'лифта', 'левая', 'влево']
proemlisstart = ['начало проёма']
proemlistend = ['конец проёма', 'один конец проёма']
windowliststart = ['начало окна']
windowlistend = ['конец окна']
drawingstart = ['помещение']
celingheight = ['высота потолка', 'высота помещения']
doorheight = ['высота проёма']
windowheight = ['высота окна']
windowsillist = ['высота подоконника']


class PycairoPaint():

    def __init__(self,
                 measure: str,
                 curent_x: int = 5, curent_y: int = 5, scale: int = 200, lengh: int = 0, index: int = 0, angel: int = 0,
                 path: str = 'plan_final', filename_svg: str = 'noname.svg'):
        self.measure = measure  # Вводная информация
        self.curent_x = curent_x  # Текущие координаты по x
        self.curent_y = curent_y  # Текущие координаты по y
        self.scale = scale  # масштаб на который делится расстояние
        self.angel = angel
        self.lengh = lengh  # длина отрезка
        self.start_x = 1
        self.start_y = 1
        self.index = index
        self.path = path
        self.pdf_scale = 15
        self.filename_svg = filename_svg

    def filename_pdf(self):
        a = self.filename_svg.split('.')
        return f'{a[0]}.pdf'

    def StartDrawing(self):
        pass

    def radians(self):
        return math.radians(self.angel)

    def Forwardlist(self):
        big_list_of_measures = []
        forward_values_list = []
        list_of_measures = self.measure
        a = list_of_measures.split(' ')
        list_len = (len(a))  # Длина списка
        for n in range(0, list_len, 2):
            element = a[n:n + 2]
            big_list_of_measures.append(element)
        n = 0
        for elements in big_list_of_measures:
            n += 1
            word_to_look = (elements[0])
            if word_to_look.lower() in drawingstart:
                self.StartDrawing()

            elif word_to_look.lower() in forwardlist:
                val = elements[1]
                forward_values_list.append(val)

        return forward_values_list

    def CurentAngel(self):

        def List_of_angels():

            right_list = ['right', 'рейд', 'Right']
            left_list = ['left', 'лифт', 'лофт', 'лет', 'лифта', 'левая', 'влево']

            big_list_of_measures = []
            list_of_add_angels = [0]
            list_of_measures = self.measure
            a = list_of_measures.split(' ')
            list_len = (len(a))  # Длина списка
            for n in range(0, list_len, 2):
                element = a[n:n + 2]
                big_list_of_measures.append(element)
            n = 0
            for elements in big_list_of_measures:
                n += 1
                word_to_look = (elements[0])

                if word_to_look.lower() in left_list:
                    val = int(elements[1])
                    self.Resize_minus(val)
                    list_of_add_angels.append(self.angel)

                elif word_to_look.lower() in right_list:
                    val2 = int(elements[1])
                    self.Resize_plus(val2)
                    list_of_add_angels.append(self.angel)

            return list_of_add_angels

        a = List_of_angels()
        self.angel = 0
        return (a)

    def Calc_x(self):
        forward = self.Forwardlist()
        current_tangent = self.CurentAngel()
        return self.curent_x + (float(forward[self.index]) / float(self.scale)) * math.cos(
            math.radians(float(current_tangent[self.index])))

    def Calc_y(self):
        # Достать словарик с длиной:
        fwdlst = self.Forwardlist()
        carentang = self.CurentAngel()
        return self.curent_y + (float(fwdlst[self.index]) / float(self.scale)) * math.sin(
            math.radians(float(carentang[self.index])))

    def Drawing(self):
        dwg = svgwrite.Drawing(self.filename_svg, profile='tiny')
        big_list_of_measures = []
        forward_values_list = []

        list_of_measures = self.measure
        a = list_of_measures.split(' ')
        list_len = (len(a))  # Длина списка
        for n in range(0, list_len, 2):
            element = a[n:n + 2]
            big_list_of_measures.append(element)
        n = 0
        for elements in big_list_of_measures:
            n += 1
            word_to_look = (elements[0])
            if word_to_look.lower() in drawingstart:
                self.StartDrawing()

            elif word_to_look.lower() in forwardlist:
                val = elements[1]
                forward_values_list.append(val)
        fwds = 0
        for items in forward_values_list:
            fwds += int(items)
        print(f'Sum of forwards: {fwds}')
        cfc = 10000 / fwds
        self.StartDrawing()
        len_FVL = len(forward_values_list)
        counter = 0
        final_coords_dict = {}
        for values in range(0, len_FVL):
            self.index = counter
            self.lengh = forward_values_list[self.index]
            self.curent_x = self.Calc_x()
            self.curent_y = self.Calc_y()
            final_coords_dict[counter] = [self.curent_x, self.curent_y]  # Происходит запись в словарь
            counter += 1
            self.dict_of_coords = final_coords_dict
            print(f'Width: {self.WidthCounter()}')
            coefficient = cfc
            for i in range(0, (len(final_coords_dict))):  # +1
                if i + 1 < len(final_coords_dict):

                    dwg.add(dwg.line((float(final_coords_dict[i][0] * self.pdf_scale * coefficient),
                                      float(final_coords_dict[i][1] * self.pdf_scale * coefficient)),
                                     (float(final_coords_dict[i + 1][0] * self.pdf_scale * coefficient),
                                      float(final_coords_dict[i + 1][1] * self.pdf_scale * coefficient)),
                                     stroke=svgwrite.rgb(50, 50, 79, '%')))

                else:
                    continue
        self.dict_of_coords = final_coords_dict
        sch = int(len(final_coords_dict)) - 1
        print(f'{sch}')
        coefficient = cfc

        dwg.add(dwg.line((final_coords_dict[sch][0] * self.pdf_scale * coefficient,
                          final_coords_dict[sch][1] * self.pdf_scale * coefficient),
                         (final_coords_dict[0][0] * self.pdf_scale * coefficient,
                          final_coords_dict[0][1] * self.pdf_scale * coefficient),
                         stroke=svgwrite.rgb(50, 50, 79, '%')))
        dwg.stroke(width=2)
        dwg.save()

    def WidthCounter(self):
        dict1 = self.dict_of_coords
        a = 0
        for items in dict1:
            a += dict1[items][0] * self.pdf_scale
        return a

    def HeightCounter(self):
        dict1 = self.dict_of_coords
        a = 0
        for items in dict1:
            a += dict1[items][1] * self.pdf_scale
        return a

    def Resize_minus(self, val):
        self.angel -= val

    def Resize_plus(self, val):
        self.angel += val


if __name__ == '__main__':
    print(f'скрипт запущен')
    new_picture = PycairoPaint(measure=sk.text2, filename_svg='new_file7.svg', scale=150)
    new_picture.Drawing()
    print(f'скрипт выполнил работу\n')

    drawing = svg2rlg(new_picture.filename_svg)
    renderPDF.drawToFile(drawing, new_picture.filename_pdf(), autoSize=0)
