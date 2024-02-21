import copy
from datetime import datetime

from django.shortcuts import render

from Classes.CalcClasses import ProjectPrice
from commercial_offer.models import Offer


# Create your views here.
def offer(request):
    return render(request, 'commercial_offer/offer/offer.html', )


def result(request):
    try:
        last_id = Offer.objects.latest('id')
        kp_number = int(last_id.id) + 1
    except:
        kp_number = 1
    user_text = request.GET['usertext']
    town = request.GET['town']
    pro_ject = request.GET['project']
    pro_ject_2 = request.GET['project_2']
    pro_ject_3 = request.GET['project_3']
    area = request.GET['area']
    customer_name = request.GET['customer']
    draftsmens = request.GET['draftsmens']
    designers = request.GET['designers']
    profitnorm = request.GET['profitnorm']
    ptype = str(type(pro_ject))
    rooms = request.GET['rooms']
    checkbox = request.GET['inlineRadioOptions']
    data_now = f'{datetime.now().day}.{datetime.now().month}.{datetime.now().year}'
    shema_vis_list = ['обмеры',
                      'электрика',
                      'планировка',
                      'кладочный план',
                      'демонтаж',
                      'план ТП',
                      'развертки',
                      'ведомость',
                      'план пола',
                      'план потолка',
                      'мебельные конструкции',
                      'схематичная визуализация',
                      'обложка',
                      'электрика освещение',
                      'электрика розетки',
                      'узлы потолка',
                      'примечание',
                      'ведомость электроустановки',
                      'ведомость дверей',
                      'схема разверток стен',
                      'cхема сан.тех.приборов'

                      ]
    dp_list = ['обмеры',
               'электрика',
               'планировка',
               'кладочный план',
               'демонтаж',
               'план ТП',
               'развертки',
               'ведомость',
               'план пола',
               'план потолка',
               'мебельные конструкции',
               'визуализация',
               'обложка',
               'электрика освещение',
               'электрика розетки',
               'узлы потолка',
               'примечание',
               'ведомость электроустановки',
               'ведомость дверей',
               'схема разверток стен',
               'cхема сан.тех.приборов'
               ]
    dp_list_c = ['обмеры',
                 'электрика',
                 'планировка',
                 'кладочный план',
                 'демонтаж',
                 'план ТП',
                 'развертки',
                 'ведомость',
                 'план пола',
                 'план потолка',
                 'мебельные конструкции',
                 'визуализация',
                 'обложка',
                 'электрика освещение',
                 'электрика розетки',
                 'узлы потолка',
                 'примечание',
                 'ведомость электроустановки',
                 'ведомость дверей',
                 'схема разверток стен',
                 'cхема сан.тех.приборов',
                 'комплектация',]
    dp_list_a = ['обмеры',
                 'электрика',
                 'планировка',
                 'кладочный план',
                 'демонтаж',
                 'план ТП',
                 'развертки',
                 'ведомость',
                 'план пола',
                 'план потолка',
                 'мебельные конструкции',
                 'визуализация',
                 'обложка',
                 'электрика освещение',
                 'электрика розетки',
                 'узлы потолка',
                 'примечание',
                 'ведомость электроустановки',
                 'ведомость дверей',
                 'схема разверток стен',
                 'cхема сан.тех.приборов',
                 'авторский надзор',
                 ]

    def make_project_list(form_data):
        p_choice = []
        title = 'None'
        if form_data == "1":
            p_choice.append('обмеры')
            title = "обмеры"
        elif form_data == "2":
            p_choice.append('электрика')
            title = "электрика"
        elif form_data == "3":
            p_choice.append('планировка')
            title = "планировка"
        elif form_data == "4":
            p_choice.append('кладочный план')
            title = "кладочный план"
        elif form_data == "5":
            p_choice.append('демонтаж')
            title = "демонтаж"
        elif form_data == "6":
            p_choice.append('план тёплого пола')
            title = "план тёплого пола"
        elif form_data == "7":
            p_choice.append('развертки')
            title = "развертки"
        elif form_data == "8":
            p_choice.append('ведомость')
            title = "ведомость"
        elif form_data == "9":
            p_choice.append('план пола')
            title = "план пола"
        elif form_data == "10":
            p_choice.append('план потолка')
            title = "план потолка"
        elif form_data == "11":
            p_choice.append('мебельные конструкции')
            title = "мебельные конструкции"
        elif form_data == "12":
            p_choice.append('визуализация')
            title = ""
        elif form_data == "13":
            p_choice.clear()
            p_choice.append('обмеры')
            p_choice.append('план пола')
            p_choice.append('кладочный план')
            p_choice.append('электрика')
            p_choice.append('демонтаж')
            p_choice.append('планировка')
            p_choice.append('план тёплого пола')
            title = "фор-проект"
        elif form_data == "14":
            p_choice.append('альбом планировочных решений')
            title = "альбом планировочных решений"
        elif form_data == "15":
            p_choice.append('обложка')
            title = "обложка"
        elif form_data == "16":
            p_choice.append('электрика освещение')
            title = "электрика освещение"
        elif form_data == "17":
            p_choice.append('электрика розетки')
            title = "электрика розетки"
        elif form_data == "18":
            p_choice.append('узлы потолка')
            title = "узлы потолка"
        elif form_data == "19":
            p_choice.append('примечание')
            title = "примечание"
        elif form_data == "20":
            p_choice.append('ведомость электроустановки')
            title = "ведомость электроустановки"
        elif form_data == "21":
            p_choice.append('ведомость дверей')
            title = "ведомость дверей"
        elif form_data == "22":
            p_choice.append('схема разверток стен')
            title = "схема разверток стен"
        elif form_data == "23":
            p_choice.append('cхема сан.тех.приборов')
            title = "cхема сан.тех.приборов"
        elif form_data == "24":
            p_choice.append('комплектация')
            title = "комплектация"
        elif form_data == "25":
            p_choice.append('комплектация')
            title = "Авторский надзор"
        elif form_data == "26":
            p_choice = dp_list_c
            title = "Проект с комплектацией"
        elif form_data == "27":
            p_choice = dp_list
            title = "Полный дизайн проект"
        elif form_data == "28":
            p_choice = dp_list_a
            title = "Проект с авторским надзором"
        elif form_data == "29":
            p_choice = shema_vis_list
            title = "Проект со схематичной визуализацией"
        return p_choice, title

    first_list = make_project_list(pro_ject)
    second_list = make_project_list(pro_ject_2)
    third_list = make_project_list(pro_ject_3)

    newInterior = ProjectPrice(square=int(area), spaces=int(rooms), typeof=1,
                               content=first_list[0],
                               designers=int(designers),
                               draftsmen=int(draftsmens),
                               profit_norm_perm=int(profitnorm))

    newInterior_2 = ProjectPrice(square=int(area), spaces=int(rooms), typeof=1,
                                 content=second_list[0],
                                 designers=int(designers),
                                 draftsmen=int(draftsmens),
                                 profit_norm_perm=int(profitnorm))

    newInterior_3 = ProjectPrice(square=int(area), spaces=int(rooms), typeof=1,
                                 content=third_list[0],
                                 designers=int(designers),
                                 draftsmen=int(draftsmens),
                                 profit_norm_perm=int(profitnorm))

    first_title = f'{make_project_list(pro_ject)[1].capitalize()}'
    second_title = f'{make_project_list(pro_ject_2)[1].capitalize()}'
    third_title = f'{make_project_list(pro_ject_3)[1].capitalize()}'
    first_list_1 = make_project_list(pro_ject)[0]
    second_list_1 = make_project_list(pro_ject_2)[0]
    third_list_1 = make_project_list(pro_ject_3)[0]

    price_1 = round(newInterior.calculate_price_per_meter(), 0)
    price_2 = round(newInterior_2.calculate_price_per_meter(), 0)
    price_3 = round(newInterior_3.calculate_price_per_meter(), 0)
    time_1 = newInterior.time_of_visualization() + newInterior.time_of_blueprints() + 2
    time_2 = newInterior_2.time_of_visualization() + newInterior_2.time_of_blueprints() + 2
    time_3 = newInterior_3.time_of_visualization() + newInterior_3.time_of_blueprints() + 2
    cost_1 = int(price_1) * int(newInterior.square)
    cost_2 = int(price_2) * int(newInterior_2.square)
    cost_3 = int(price_3) * int(newInterior_3.square)
    discount = cost_1 * (-0.1)
    cost_minus_discount = cost_1 + discount
    empty_list = []
    aditional_title_1 = "Вариант 1."
    aditional_title_2 = "Вариант 2."
    aditional_title_3 = "Вариант 3."
    rubles_1 = "рублей"
    rubles_2 = "рублей"
    rubles_3 = "рублей"
    rubles_m_1 = "рублей за кв.м"
    rubles_m_2 = "рублей за кв.м"
    rubles_m_3 = "рублей за кв.м"
    price_1n = "Цена: "
    price_2n = "Цена: "
    price_3n = "Цена: "
    coast1 = "Стоимость: "
    coast2 = "Стоимость: "
    coast3 = "Стоимость: "
    time_text_1 = "Срок выполнения работ в рабочих днях без учета времени на согласование с заказчиком: "
    time_text_2 = "Срок выполнения работ в рабочих днях без учета времени на согласование с заказчиком: "
    time_text_3 = "Срок выполнения работ в рабочих днях без учета времени на согласование с заказчиком: "
    title_for_bd = f"{user_text}_{customer_name}_{cost_1}"

    # todo Проверить вручную, правильно ли считает калькулятор стоимости. Когда заводишь много дизайнеров, то цена становится меньше.
    # todo Понять почему. Переписать метод
    # todo Нужна привязка к договору на физ лицо...
    # todo Нужен хендлер со ссылкой на url
    if checkbox != "option1":
        new_offer = Offer(title=title_for_bd,
                          town=town,
                          offer_number=kp_number,
                          value=cost_1,
                          published=data_now,
                          area=area,
                          address=user_text,
                          project_composition="FDP")
        new_offer.save()

        return render(request, 'result.html', {'first_title': first_title,
                                               'usertext': user_text,
                                               'second_title': second_title,
                                               'third_title': third_title,
                                               'p_type': ptype,
                                               'proj': first_list,
                                               'proj_2': second_list,
                                               'proj_3': third_list,
                                               'area': area,
                                               'data_now': data_now,
                                               'first_list_of_service': first_list_1,
                                               'second_list_of_service': second_list_1,
                                               'third_list_of_service': third_list_1,
                                               'price_1': price_1,
                                               'price_2': price_2,
                                               'price_3': price_3,
                                               'time_text_1': time_text_1,
                                               'time_text_2': time_text_2,
                                               'time_text_3': time_text_3,
                                               'time_1': time_1,
                                               'time_2': time_2,
                                               'time_3': time_3,
                                               'cost_3': cost_3,
                                               'cost_2': cost_2,
                                               'cost_1': cost_1,
                                               'customer_name': customer_name,
                                               'discount': discount,
                                               'cost_minus_discount': cost_minus_discount,
                                               'checkbox': checkbox,
                                               'aditional_title_1': aditional_title_1,
                                               'aditional_title_2': aditional_title_2,
                                               'aditional_title_3': aditional_title_3,
                                               'rubles_1': rubles_1,
                                               'rubles_2': rubles_2,
                                               'rubles_3': rubles_3,
                                               'rubles_m_1': rubles_m_1,
                                               'rubles_m_2': rubles_m_2,
                                               'rubles_m_3': rubles_m_3,
                                               'price_1n': price_1n,
                                               'price_2n': price_2n,
                                               'price_3n': price_3n,
                                               'coast1': coast1,
                                               'coast2': coast2,
                                               'coast3': coast3,
                                               'kp_number': kp_number,
                                               'town': town,

                                               })
    else:
        new_offer = Offer(title=title_for_bd,
                          town=town,
                          offer_number=kp_number,
                          value=cost_1,
                          published=data_now,
                          area=area,
                          address=user_text,
                          project_composition="FDP")
        new_offer.save()
        return render(request, 'result.html', {'first_title': first_title,
                                               'usertext': user_text,
                                               'second_title': " ",
                                               'third_title': " ",
                                               'p_type': ptype,
                                               'proj': first_list,
                                               'proj_2': empty_list,
                                               'proj_3': empty_list,
                                               'area': area,
                                               'data_now': data_now,
                                               'first_list_of_service': first_list_1,
                                               'second_list_of_service': empty_list,
                                               'third_list_of_service': empty_list,
                                               'price_1': price_1,
                                               'price_2': " ",
                                               'price_3': " ",
                                               'time_1': time_1,
                                               'time_2': " ",
                                               'time_3': " ",
                                               'time_text_1': time_text_1,
                                               'time_text_2': " ",
                                               'time_text_3': " ",
                                               'cost_3': " ",
                                               'cost_2': " ",
                                               'cost_1': cost_1,
                                               'customer_name': customer_name,
                                               'discount': discount,
                                               'cost_minus_discount': cost_minus_discount,
                                               'checkbox': checkbox,
                                               'aditional_title_1': " ",
                                               'aditional_title_2': " ",
                                               'aditional_title_3': " ",
                                               'rubles_1': rubles_1,
                                               'rubles_2': " ",
                                               'rubles_3': " ",
                                               'rubles_m_1': rubles_m_1,
                                               'rubles_m_2': " ",
                                               'rubles_m_3': " ",
                                               'price_1n': price_1n,
                                               'price_2n': " ",
                                               'price_3n': " ",
                                               'coast1': coast1,
                                               'coast2': " ",
                                               'coast3': " ",
                                               'kp_number': kp_number,
                                               'town': town,

                                               })
