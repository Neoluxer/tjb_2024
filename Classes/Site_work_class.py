# -*- coding: utf-8 -*-
from datetime import *


class SiteArticle():
    """
    Класс SiteArticle используется для создания статьи для Портфолио на сайте

    """

    def __str__(self):  # Магический дандр метод форматирования вывода print(p): Дело(Название=1, Сделано?=1)
        return f'HTML: {self.article_name} {self.data}\n'

    def __init__(self, article_name: str = 'не указан',
                 adress_of_object: str = 'г.Москва, ул. Пушкина, д.Колотушкина',
                 how_mutch_rooms: str = '3',
                 area: str = '120',
                 ceiling_height: str = '2.8',
                 style: str = 'Современный',
                 authors: str = 'Завада О.А, Кандалов В.А.',
                 link_to_blueprints: str = 'https://www.neoluxe.ru/upload/iblock/e1b/e1b3905645344be60deed046b1d2f8fb.pdf',
                 about_customer: str = 'Заказчик первый раз обратился в нашу студию 6 лет назад и мы разработали для него планировочное решение.',
                 situation: str = 'До приобретения квартиры, заказчики смотрели похожую квартиру с перепланировкой. Эта квартира им понравилась, но приобрели идентичную,',
                 picture_before_url: str = 'https://www.neoluxe.ru/bitrix/templates/2015_assets/img/logo.png',
                 picture_after_url: str = 'https://www.neoluxe.ru/bitrix/templates/2015_assets/img/logo.png',
                 illustration1_url: str = 'https://www.neoluxe.ru/bitrix/templates/2015_assets/img/logo.png',
                 podpis_1: str = 'подпись к картинке',
                 features_of_the_layout1: str = 'Свободное пространство. Объединены гостиная, кухня и прихожая.',
                 features_of_the_layout2: str = 'Большая удобная кухня',
                 features_of_the_layout3: str = 'Расширенная прихожая',
                 budget: str = '2000000',
                 Wish_1_title: str = 'Пожелание номер один',
                 Wish_1_text: str = 'Большая кухня',
                 Wish_1_picture_url: str = 'https://www.neoluxe.ru/bitrix/templates/2015_assets/img/logo.png',
                 Wish_2_title: str = 'Пожелание номер два',
                 Wish_2_text: str = 'Объеденить кухню и гостиную',
                 Wish_2_picture_url: str = 'https://www.neoluxe.ru/bitrix/templates/2015_assets/img/logo.png',
                 Wish_3_title: str = 'Пожелание номер три',
                 Wish_3_text: str = 'Избавиться от коридоров',
                 Wish_3_picture_url: str = 'https://www.neoluxe.ru/bitrix/templates/2015_assets/img/logo.png',
                 Wish_4_title: str = 'Пожелание номер четыре',
                 Wish_4_text: str = 'Организовать системы хранения',
                 Wish_4_picture_url: str = 'https://www.neoluxe.ru/bitrix/templates/2015_assets/img/logo.png',
                 Wish_5_title: str = 'Пожелание номер пять',
                 Wish_5_text: str = 'Светлая современная квартира',
                 Wish_5_picture_url: str = 'https://www.neoluxe.ru/bitrix/templates/2015_assets/img/logo.png',
                 Wish_6_title: str = 'Пожелание номер шесть',
                 Wish_6_text: str = 'Функциональная планировка',
                 Wish_6_picture_url: str = 'https://www.neoluxe.ru/bitrix/templates/2015_assets/img/logo.png',
                 What_we_do_with_floor_plan1: str = 'Убрали коридор',
                 What_we_do_with_floor_plan2: str = 'Добавили просторную гардеробную',
                 What_we_do_with_floor_plan3: str = 'Объеденили кухню и гостиную',
                 What_we_do_with_floor_plan4: str = 'Разместили в санузле большую ванну 80х190',
                 What_we_do_with_floor_plan5: str = 'Нашли в центре квартиры место для дивана длинной 2,6 метра.',
                 florplan_url: str = 'https://www.neoluxe.ru/bitrix/templates/2015_assets/img/logo.png',
                 floor_covering: str = 'Керамогранит Italon, Wonder Desert, Contempora Burn',
                 doors: str = 'Sofia',
                 sofa: str = 'Estetica, Miami Кресла: Knoll Saarinen Conference',
                 chairs: str = 'Cosmorelax Allegra',
                 lighting_fixtures: str = 'Центрсвет',
                 plumbing: str = 'LaufenPro S Rimless Биде подвесноe Laufen Pro S.Накладная раковина;'
                                 ' KartellbyLaufen Ванна RIHOLUGO ВТ04 190х80 см; Шторка на ванну;'
                                 ' RadawayEOSIIPND Смеситель для раковины из стены; Hansgrohe Talis. Смеситель для биде;'
                                 ' Hansgrohe Talis 32240000 Душевая стойка;'
                                 ' Hansgrohe Croma 220 Showerpipe 27223000 с термостатом',
                 link_to_the_moodboard: str = 'https://www.neoluxe.ru/bitrix/templates/2015_assets/img/logo.png',
                 the_last_header: str = 'Делаем детскую на будущее',
                 the_last_text: str = 'Что делать, если планируешь детскую комнату в квартире,'
                                      ' а ребенок пока только в планах? Если отталкиваться от'
                                      ' моего опыта как дизайнеров и отца двоих детей,'
                                      ' то я посоветовал бы сделать нейтральный интерьер,'
                                      ' который потом можно легко трансформировать под любой из возможных сценариев.'
                                      ' До рождения ребенка эту комнату можно использовать как кабинет.'
                                      ' В 2018 году мы переделывали 2 кабинета наших заказчиков в детские. В первом случае - для двойни.'
                                      ' Во втором - для девочки.Переделка оказалась косметической.',
                 main_picture: str = '/upload/medialibrary/822/8220b4cab0ef4c034b7cd162fc75d606.jpg'
                 ):
        self.article_name = article_name
        self.data = datetime.now()
        self.adress_of_object = adress_of_object
        self.how_mutch_rooms = how_mutch_rooms
        self.area = area
        self.ceiling_height = ceiling_height
        self.style = style
        self.authors = authors
        self.link_to_blueprints = link_to_blueprints
        self.about_customer = about_customer
        self.situation = situation
        self.picture_before_url = picture_before_url
        self.picture_after_url = picture_after_url
        self.illustration1_url = illustration1_url
        self.podpis_1 = podpis_1
        self.features_of_the_layout1 = features_of_the_layout1
        self.features_of_the_layout2 = features_of_the_layout2
        self.features_of_the_layout3 = features_of_the_layout3
        self.budget = budget
        self.Wish_1_title = Wish_1_title
        self.Wish_1_text = Wish_1_text
        self.Wish_1_picture_url = Wish_1_picture_url
        self.Wish_2_title = Wish_2_title
        self.Wish_2_text = Wish_2_text
        self.Wish_2_picture_url = Wish_2_picture_url
        self.Wish_3_title = Wish_3_title
        self.Wish_3_text = Wish_3_text
        self.Wish_3_picture_url = Wish_3_picture_url
        self.Wish_4_title = Wish_4_title
        self.Wish_4_text = Wish_4_text
        self.Wish_4_picture_url = Wish_4_picture_url
        self.Wish_5_title = Wish_5_title
        self.Wish_5_text = Wish_5_text
        self.Wish_5_picture_url = Wish_5_picture_url
        self.Wish_6_title = Wish_6_title
        self.Wish_6_text = Wish_6_text
        self.Wish_6_picture_url = Wish_6_picture_url
        self.What_we_do_with_floor_plan1 = What_we_do_with_floor_plan1
        self.What_we_do_with_floor_plan2 = What_we_do_with_floor_plan2
        self.What_we_do_with_floor_plan3 = What_we_do_with_floor_plan3
        self.What_we_do_with_floor_plan4 = What_we_do_with_floor_plan4
        self.What_we_do_with_floor_plan5 = What_we_do_with_floor_plan5
        self.florplan_url = florplan_url
        self.floor_covering = floor_covering
        self.doors = doors
        self.sofa = sofa
        self.chairs = chairs
        self.lighting_fixtures = lighting_fixtures
        self.plumbing = plumbing
        self.link_to_the_moodboard = link_to_the_moodboard
        self.the_last_header = the_last_header
        self.the_last_text = the_last_text
        self.main_picture = main_picture

        self.text = f'''
 <head>
  <meta charset="utf-8">
  <title>Заготовка статьи для сайта</title>
 </head>
<a href="https://www.pinterest.com/pin/create/button/" data-pin-do="buttonBookmark"></a>

<h2>О проекте:</h2>
<b>Место:</b>{self.adress_of_object}<br>
<b>Размер:</b> {self.how_mutch_rooms}-х комнатная квартира площадью {self.area} м.кв. Высота потолка {self.ceiling_height} м.
<br>
<b>Стиль:</b>{self.style}<br>
<b>Автор проекта:</b>{self.authors}<br>
<i><a target="_blank" href="{self.link_to_blueprints}">Ссылка на рабочий проект:</a></i>
    <h2>О заказчике:</h2>{self.about_customer}
    <br>
    <h2>Ситуация:</h2>{self.situation}
    <br>
    <br>
    
        <div class="twentytwenty-container" style="width: 600px">
        <img src="{self.picture_before_url}"> <img
            src="{self.picture_after_url}">
         </div>
    
    <br>
    <a href="{self.illustration1_url}"></a>
    <span style="font-size: 9pt">{self.podpis_1}</span><br>
    <h3>Особенности планировки:</h3>
    <ul>
        <li>{self.features_of_the_layout1}</li>
        <li>{self.features_of_the_layout2}</li>
        <li>{self.features_of_the_layout2}</li>
    </ul>
    <h2>Бюджет:</h2>
    {self.budget}
    <h2>Что хотел заказчик:</h2>
    <h3>{self.Wish_1_title}</h3>
        {self.Wish_1_text}
    <a href="{self.Wish_1_picture_url}"><img width="800" class="img-responsive"></a>
    <h3>{self.Wish_2_title}</h3>
    {self.Wish_2_text}
    <a href="{self.Wish_2_picture_url}"><img width="800" alt="9.jpg" height="436" title="9.jpg" class="img-responsive"></a><br>
    <h3>{self.Wish_3_title}</h3>
    {self.Wish_3_text}
    <h3>{self.Wish_4_title}</h3>
    {self.Wish_4_text}
    <h3>{self.Wish_5_title}</h3>
    {self.Wish_5_text}
    <a href="{self.Wish_5_picture_url}"><img width="800" alt="4.jpg" height="436" title="4.jpg" class="img-responsive"></a><br>
    <h3>{self.Wish_6_title}</h3>
    {self.Wish_6_text}
    <a href="{self.Wish_6_picture_url}"><img width="800" alt="4.jpg" height="436" title="4.jpg" class="img-responsive"></a><br>
    <h2>Планировка:</h2>
    Что мы сделали полезного в планировке:
    <ul>

            <li>{self.What_we_do_with_floor_plan1}</li>
            <li>{self.What_we_do_with_floor_plan2}</li>
            <li>{self.What_we_do_with_floor_plan3}</li>
            <li>{self.What_we_do_with_floor_plan4}</li>
            <li>{self.What_we_do_with_floor_plan5}</li>

    </ul>
    <a href="{self.florplan_url}"><img width="800" alt="план.JPG" height="574" title="план.JPG" class="img-responsive"></a>
    <br>
    <h2>Детали:</h2>
    
    <b>Напольная плитка:</b>&nbsp; &nbsp; {self.floor_covering}<br>
    <b>Двери</b>:&nbsp; &nbsp; {self.doors}<br>
    <b>Диван:</b>&nbsp; &nbsp; {self.sofa}<br>
    <b>Стулья:</b>&nbsp; &nbsp; {self.chairs}<br>
    <b>Светильники:&nbsp; &nbsp;</b>{lighting_fixtures}br>
    <b>Сантехника:</b>&nbsp; &nbsp;{self.plumbing}<br>
    

    <a href="{self.link_to_the_moodboard}"><img width="599" alt="price.jpg" height="600" title="price.jpg"
                                                class="img-responsive"></a><br>
    <h3>{self.the_last_header}</h3>
    <{self.the_last_text}<br>
    <p>
    </p>
    <p>
        Смотреть еще: <a href="/catalog/9/" title="дизайн проект офиса цена">цена дизайн-проекта офиса</a>, <a
            href="/articles/34/razrabotka_proekta_pereplanirovki/" title="разработка проекта перепланировки">разработка
        проекта перепланировки</a>, <a href="/articles/34/uslugi_dizainera_interera_krasnodar/"
                                       title="услуга дизайнера интерьера цена">цена услуг дизайнера интерьера</a>.
    </p>
        '''

