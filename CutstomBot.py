import time
from itertools import count
import pyautogui
import keyboard as keyb
from pynput.keyboard import Listener, KeyCode

from pyautogui import SECONDARY, sleep

while True:
    time.sleep(5)  # Задержка 5 сек
    pyautogui.moveTo(520,542)  # выбор иконки главы
    time.sleep(1)
    pyautogui.click(520,542)  # выбор иконки главы
    time.sleep(1)
    pyautogui.moveTo(788,787)  # Наводится на кнопку "подтвердить"
    time.sleep(2)  # Задержка 2 сек
    pyautogui.click(788,787)  # кнопка "подтвердить" главу
    time.sleep(4)
    pyautogui.moveTo(481,532)  # Наводится на Выбор сложности
    time.sleep(0.5)
    pyautogui.click(481,532)  # Выбор сложности
    time.sleep(0.5)
    pyautogui.moveTo(783,783)  # Наводится на "подтвердить"
    time.sleep(0.5)
    pyautogui.click(783,783)  # кнопка "подтвердить" сложность
    time.sleep(6)
    keyb.press('m')  # Зажимает кнопку m
    keyb.release('m')
    time.sleep(1)
    keyb.press('o')  # Зажимает кнопку О
    keyb.release('o')  # Отжимает кнопку О
    pyautogui.moveTo(763,320)  # Наводится поверхность
    time.sleep(1)
    pyautogui.doubleClick(763,320, button="SECONDARY")  # Перемещение юнита
    time.sleep(1)
    pyautogui.moveTo(937,880)  # Наводится на Улучшение казармы на 2 ЛВЛ
    time.sleep(2)
    pyautogui.click(937,880)  # Улучшение казармы на 2 ЛВЛ
    time.sleep(1)
    pyautogui.click(937,880)  # Улучшение казармы на 2 ЛВЛ
    time.sleep(1)
    pyautogui.moveTo(763,858)  # Наводится на Покупка фиол магазина
    pyautogui.click(763,858)  # Покупка фиол магазина
    time.sleep(1)
    pyautogui.moveTo(539,668)  # ; автопокупка
    time.sleep(1)
    pyautogui.click(539,668)  # автопокупка
    time.sleep(1)
    keyb.press('Tab')  # Зажимает кнопку x
    keyb.release('Tab')  # Отжимает кнопку x
    time.sleep(1)
    keyb.press('m')  # Зажимает кнопку m
    keyb.release('m')
    time.sleep(1)
    keyb.press('o')  # Зажимает кнопку О
    keyb.release('o')  # Отжимает кнопку О
    pyautogui.moveTo(759,436)  # Наводится на Открытие сундука S
    time.sleep(1)
    pyautogui.click(759,436, button="SECONDARY")  # Открытие сундука S
    time.sleep(1)
    pyautogui.moveTo(913,362)  # Наводится на Выбор Лиона
    pyautogui.click(913,362)  # Выбор Лиона
    time.sleep(1)
    keyb.press('m')  # Зажимает кнопку m
    keyb.release('m')
    time.sleep(1)
    keyb.press('o')  # Зажимает кнопку О
    keyb.release('o')  # Отжимает кнопку О
    time.sleep(1)
    pyautogui.moveTo(1355,668)  # Наводится на карту лиона
    time.sleep(1)
    pyautogui.dragTo(995,436)  # Перетаскивает лиона на поле битвы
    pyautogui.click(995,436)  # Ставит лиона
    time.sleep(22)
    keyb.press('f1')  # Зажимает кнопку О
    keyb.release('f1')  # Отжимает кнопку О
    time.sleep(1)
    pyautogui.moveTo(489,565)
    time.sleep(1)
    pyautogui.click(489,565, button="SECONDARY")  #Перемещение
    time.sleep(1)
    pyautogui.moveTo(1118,498)  #  Наводится на Место где забрать аганимы
    time.sleep(1)
    keyb.press('b')  # Зажимает кнопку b
    keyb.release('b')  # Отжимает кнопку b
    time.sleep(1)
    pyautogui.click(1118,498)  # Открывает ящики
    time.sleep(1)
    pyautogui.moveTo(799,375)  # Наводится на аганим выбор
    pyautogui.click(799,375)  # Выбирает аганимы 1й
    time.sleep(1)
    pyautogui.click(799,375)  # Выбирает аганимы 2й
    time.sleep(1)
    pyautogui.moveTo(489,565)  # Наводится на место где упали аганимы
    keyb.press('b')  # Зажимает кнопку b
    keyb.release('b')  # Отжимает кнопку b
    time.sleep(1)
    pyautogui.click(489,565)  # Подбирает аганимы
    time.sleep(1)
    keyb.press('x')  # Зажимает кнопку x
    keyb.release('x')  # Отжимает кнопку x
    time.sleep(1)
    pyautogui.moveTo(1352,662)  # Наводится в инвентарь на первый аганим
    time.sleep(1)
    pyautogui.mouseDown(1352,662, button='Left')  # зажимает в инвентае первый аганим
    time.sleep(1)
    pyautogui.moveTo(575,753)  # # Наводится на слот лиона 1 аганим
    time.sleep(1)
    pyautogui.mouseUp(575,753, button='Left')  # отпускает первый аганим в инвентарь
    time.sleep(1)
    pyautogui.moveTo(1397,666)  # Наводится в инвентарь на второй аганим
    time.sleep(1)
    pyautogui.mouseDown(1397,666, button='Left')  # зажимает в инвентае первый аганим
    time.sleep(1)
    pyautogui.moveTo(626,746)  # # Наводится на слот лиона второй аганим
    time.sleep(1)
    pyautogui.mouseUp(626,746, button='Left')  # отпускает второй аганим в инвентарь
    time.sleep(3)
    time.sleep(3)
    keyb.press('x')  # Зажимает кнопку x
    keyb.release('x')  # Отжимает кнопку x
    time.sleep(1)
    pyautogui.moveTo(551,76)  # Наводит на перегрузку
    time.sleep(1)
    pyautogui.click(551,76)  # Открытие перегрузки
    time.sleep(1)
    pyautogui.moveTo(169,419)  # Наводит на уровень перегрузке
    time.sleep(1)
    pyautogui.doubleClick(169,419)  # Нажатие 2 уровня перегрузки
    time.sleep(0.5)
    pyautogui.moveTo(583,420)  # Наводит на уровень перегрузке
    time.sleep(1)
    pyautogui.doubleClick(583,420)  # Нажатие 2 уровня перегрузки
    time.sleep(0.5)
    pyautogui.moveTo(202,478)  # Наводит на "подтвердить"
    time.sleep(1)
    pyautogui.click(202,478)  # Клик на подтвердить
    time.sleep(1)
    # Поменять звездных героев  (DOOM/Venga)
    pyautogui.moveTo(438,46) #Открываем комбинации
    time.sleep(1)
    pyautogui.click(438,46)
    time.sleep(1)
    pyautogui.moveTo(534,836)  # наводимся 2 слот
    time.sleep(1)
    pyautogui.click(534,836)  #
    time.sleep(1)
    pyautogui.moveTo(438,46)  # закрываем комбинации
    time.sleep(1)
    pyautogui.click(438,46)
    time.sleep(255)
    pyautogui.moveTo(992,160)  # Наводится на мусор
    time.sleep(1)
    keyb.press('b')  # Зажимает кнопку b
    keyb.release('b')  # Отжимает кнопку b
    time.sleep(1)
    pyautogui.click(992,160)  # Нажимает на мусор
    time.sleep(1)
    pyautogui.moveTo(1357,669)  # Наводится на мусор
    time.sleep(1)
    pyautogui.mouseDown(1347,664, button='Left')  # зажимает мусор в инвентарн
    time.sleep(1)
    pyautogui.moveTo(1486,234)  # # Наводится на пустое место чтобы выкинуть
    time.sleep(1)
    pyautogui.mouseUp(1486,234, button='Left')  # отпускает мусор
    time.sleep(3)
    time,sleep(160)
    keyb.press('m')  # Зажимает кнопку m
    keyb.release('m')
    time.sleep(1)
    keyb.press('o')  # Зажимает кнопку О
    keyb.release('o')  # Отжимает кнопку О
    time.sleep(1)
    pyautogui.moveTo(988,156)  # Наводится на яйцо
    time.sleep(1)
    keyb.press('b')  # Зажимает кнопку b
    keyb.release('b')  # Отжимает кнопку b
    time.sleep(1)
    pyautogui.click(988,156)  # Подбирает яйцо
    time.sleep(1)
    pyautogui.moveTo(1355,668)  # Наводится на яйцо в инвентаре
    time.sleep(1)
    pyautogui.click(1355,668)  # Нажимает на яйцо в инвентаре
    time.sleep(1)
    pyautogui.moveTo(685,529)  # Наводится на поле
    time.sleep(1)
    pyautogui.click(685,529)  # ставит на поле яйцо
    time.sleep(1)
    pyautogui.moveTo(940,866)  # Наводится на Улучшение казармы на 2 ЛВЛ
    time.sleep(1)
    pyautogui.click(940,866)  # Улучшение казармы на 2 ЛВЛ
    time.sleep(1)
    pyautogui.click(940,866)  # Улучшение казармы на 2 ЛВЛ
    time.sleep(1)
    pyautogui.moveTo(844,872)  # Наводится на Покупка жёлт магазина
    time.sleep(1)
    pyautogui.click(844,872)  # Покупка жёлт магазина
    time.sleep(1)
    keyb.press('Tab')  # Зажимает кнопку Tab
    keyb.release('Tab')  # Отжимает кнопку Tab
    time.sleep(1)
    keyb.press('m')  # Зажимает кнопку m
    keyb.release('m')
    time.sleep(1)
    keyb.press('o')  # Зажимает кнопку О
    keyb.release('o')  # Отжимает кнопку О
    time.sleep(1)
    pyautogui.moveTo(761,435)  # Наводится на Открытие сундука S
    time.sleep(1)
    pyautogui.click(761,435, button="SECONDARY")  # Открытие сундука S
    time.sleep(1)
    pyautogui.moveTo(923,627)  # свернуть
    time.sleep(1)
    pyautogui.click(923,627)  # свернуть
    time.sleep(0.5)
    pyautogui.moveTo(761,435)  # Наводится на Открытие сундука S
    time.sleep(1)
    pyautogui.click(761,435, button="SECONDARY")  # Открытие сундука S
    time.sleep(1)
    pyautogui.moveTo(913,362)  # Наводится на Выбор Лиона
    pyautogui.click(913,362)  # Выбор Лиона
    time.sleep(1)
    pyautogui.moveTo(1355,668)  # Наводится на карту лиона
    time.sleep(1)
    pyautogui.click(1354,666)  # Ставит лиона
    time.sleep(0.5)
    pyautogui.click(1354,666)  # Ставит лиона
    time.sleep(429)
    keyb.press('m')  # Зажимает кнопку m
    keyb.release('m')
    time.sleep(1)
    keyb.press('o')  # Зажимает кнопку О
    keyb.release('o')  # Отжимает кнопку О
    time.sleep(1)
    pyautogui.moveTo(1347,664)
    time.sleep(1)
    pyautogui.mouseDown(1347,664, button='Left')  # зажимает мусор в инвентарн
    time.sleep(1)
    pyautogui.moveTo(1486,234)  # # Наводится на пустое место чтобы выкинуть
    time.sleep(1)
    pyautogui.mouseUp(1486,234, button='Left')  # отпускает мусор
    time.sleep(1)
    pyautogui.moveTo(1397,666)
    time.sleep(1)
    pyautogui.mouseDown(1397,666, button='Left')  # зажимает мусор в инвентарн
    time.sleep(1)
    pyautogui.moveTo(1486,234)  # # Наводится на пустое место чтобы выкинуть
    time.sleep(1)
    pyautogui.mouseUp(1486,234, button='Left')  # отпускает мусор
    time.sleep(180)
    pyautogui.moveTo(923,627)  # свернуть
    time.sleep(1)
    pyautogui.click(923,627)  # свернуть
    time.sleep(0.5)
    pyautogui.moveTo(797,689)  # свернуть
    time.sleep(1)
    pyautogui.click(797,689)  # свернуть
    time.sleep(1)
    pyautogui.moveTo(1561,863)  # продать инвент
    time.sleep(1)
    pyautogui.click(1561,863)  # продать инвент
    time.sleep(1)
    pyautogui.moveTo(733,552)  # продать инвент
    time.sleep(1)
    pyautogui.click(733,552)  # продать инвент
    time.sleep(20)
    keyb.press('m')  # Зажимает кнопку m
    keyb.release('m')
    time.sleep(1)
    keyb.press('o')  # Зажимает кнопку О
    keyb.release('o')  # Отжимает кнопку О
    time.sleep(1)
    keyb.press('f1')  # Зажимает кнопку О
    keyb.release('f1')  # Отжимает кнопку О
    time.sleep(1)
    pyautogui.moveTo(685,529)  # Наводит на дроп яйца
    time.sleep(1)
    keyb.press('f')  # Зажимает кнопку f
    keyb.release('f')  # Отжимает кнопку f
    time.sleep(3)
    pyautogui.click(685,529)  # кликает, разбивая дроп яйца
    time.sleep(1)
    pyautogui.moveTo(685,529)  # Наводит на дроп яйца
    time.sleep(1)
    keyb.press('b')  # Зажимает кнопку b
    keyb.release('b')  # Отжимает кнопку b
    time.sleep(1)
    pyautogui.click(685,529)  # кликает, забирая дроп яйца
    time.sleep(1)
    for i in range(4):
        pyautogui.moveTo(1553,640)  # Наводит на сортировку
        time.sleep(0.2)
        pyautogui.doubleClick(1553,640)  # Кликает на сортировку
        time.sleep(0.2)
        pyautogui.moveTo(1350,664)  # Наводит на 1й слот
        time.sleep(0.2)
        pyautogui.doubleClick(1350,664)  # Кликает на 1й слот
        time.sleep(0.2)
        pyautogui.moveTo(969,430)  # Наводит на лиона
        time.sleep(0.2)
        pyautogui.doubleClick(969,430)  # Кликает на лиона ( апая его уровень )
        time.sleep(0.2)
        pyautogui.doubleClick(1398,665)  # Наводит на 2й слот
        time.sleep(0.2)
        pyautogui.doubleClick(1398,665)  # Кликает на 2й слот
        time.sleep(0.2)
        pyautogui.moveTo(969,430)  # Наводит на лиона
        time.sleep(0.2)
        pyautogui.doubleClick(969,430)  # Кликает на лиона ( апая его уровень )
        time.sleep(0.2)
        pyautogui.moveTo(893,400)  # выбирает первое
        time.sleep(0.2)
        pyautogui.doubleClick(893,400)  # выбирает первое
        time.sleep(0.2)
        pyautogui.moveTo(1436,665)  # Наводит на 3 слот рюкзака
        time.sleep(0.2)
        pyautogui.doubleClick(1436,665)  # Кликает на 3 слот рюкзака
        time.sleep(0.2)
        pyautogui.moveTo(1478,665)  # Наводит на 4 слот рюкзака
        time.sleep(0.2)
        pyautogui.doubleClick(1478,665)  # Кликает на 4 слот рюкзака
        time.sleep(0.2)
        pyautogui.moveTo(1519,666)  # Наводит на 5 слот рюкзака
        time.sleep(0.2)
        pyautogui.doubleClick(1519,666)  # Кликает на 5 слот рюкзака
        time.sleep(0.2)
        pyautogui.moveTo(1558,666)  # Наводит на 6 слот рюкзака
        time.sleep(0.2)
        pyautogui.doubleClick(1558,666)  # Кликает на 6 слот рюкзака
        time.sleep(0.2)
        pyautogui.moveTo(1358,700)  # Наводит на 7 слот рюкзака
        time.sleep(0.2)
        pyautogui.doubleClick(1358,700)  # Кликает на 7 слот рюкзака
        time.sleep(0.2)
        pyautogui.moveTo(1398,702)  # Наводит на 8 слот рюкзака
        time.sleep(0.2)
        pyautogui.doubleClick(1398,702)  # Кликает на 8 слот рюкзака
        time.sleep(0.2)
        pyautogui.moveTo(1439,700)  # Наводит на 9 слот рюкзака
        time.sleep(0.2)
        pyautogui.doubleClick(1439,700)  # Кликает на 9 слот рюкзака
        time.sleep(0.2)
    time.sleep(1)
    keyb.press('f1')  # Зажимает кнопку b
    keyb.release('f1')  # Отжимает кнопку b
    time.sleep(1)
    for a in range(1, 15):
        pyautogui.moveTo(844,872)  # ; жёлт магаз
        time.sleep(0.5)
        pyautogui.click(844,872)  # Покупка жёлт магазина
        time.sleep(0.5)
    pyautogui.moveTo(901,374)  # Наводит возможный эффект
    time.sleep(0.5)
    pyautogui.click(901,374)  # Наводит возможный эффект
    time.sleep(1)
    keyb.press('x')  # Зажимает кнопку b
    keyb.release('x')  # Отжимает кнопку b
    time.sleep(1)
    for a in range(1, 6):
        pyautogui.moveTo(574,746)  # аганим 1
        time.sleep(0.5)
        pyautogui.click(574,746)  # аганим 1
        time.sleep(0.5)
        pyautogui.moveTo(628,748)  # аганим 2
        pyautogui.click(628,748)  # аганим 2
        time.sleep(0.5)
    time.sleep(1)
    keyb.press('x')  # Зажимает кнопку x
    keyb.release('x')  # Отжимает кнопку x
    time.sleep(1)
    pyautogui.moveTo(1561,863)  # продать инвент
    time.sleep(1)
    pyautogui.click(1561,863)  # продать инвент
    time.sleep(1)
    pyautogui.moveTo(733,552)  # продать инвент
    time.sleep(1)
    pyautogui.click(733,552)  # продать инвент
    time.sleep(1)
    #--------------------------------------
    pyautogui.moveTo(1554,641)  # сортировка
    time.sleep(1)
    pyautogui.click(1554,641)  # сортировка
    time.sleep(1)
    #-----------------------------------
    pyautogui.mouseDown(1347,664, button='Left')  # зажимает мусор в инвентарн
    time.sleep(1)
    pyautogui.moveTo(1486,234)  # # Наводится на пустое место чтобы выкинуть
    time.sleep(1)
    pyautogui.mouseUp(1486,234, button='Left')  # отпускает мусор
    time.sleep(1)
    pyautogui.moveTo(1397,666)
    time.sleep(1)
    pyautogui.mouseDown(1397,666, button='Left')  # зажимает мусор в инвентарн
    time.sleep(1)
    pyautogui.moveTo(1486,234)  # # Наводится на пустое место чтобы выкинуть
    time.sleep(1)
    pyautogui.mouseUp(1486,234, button='Left')  # отпускает мусор
    time.sleep(1)
    pyautogui.mouseDown(1434,664, button='Left')  # зажимает мусор в инвентарн
    time.sleep(1)
    pyautogui.moveTo(1486,234)  # # Наводится на пустое место чтобы выкинуть
    time.sleep(1)
    pyautogui.mouseUp(1486,234, button='Left')  # отпускает мусор
    time.sleep(1)
    pyautogui.mouseDown(1483,665, button='Left')  # зажимает мусор в инвентарн
    time.sleep(1)
    pyautogui.moveTo(1486,234)  # # Наводится на пустое место чтобы выкинуть
    time.sleep(1)
    pyautogui.mouseUp(1486,234, button='Left')  # отпускает мусор
    time.sleep(1)
    pyautogui.moveTo(438,46) #Открываем комбинации
    time.sleep(1)
    pyautogui.click(438,46)
    time.sleep(1)
    pyautogui.moveTo(437,834)  # наводимся 1 слот
    time.sleep(1)
    pyautogui.click(437,834)  #
    time.sleep(1)
    pyautogui.moveTo(438,46) #закрываем комбинации
    time.sleep(1)
    pyautogui.click(438,46)
    time.sleep(1)
    pyautogui.moveTo(844,872,)  # ; жёлт магаз
    time.sleep(0.5)
    pyautogui.click(844,872, button="SECONDARY")  # Покупка жёлт магазина
    time.sleep(10)
    pyautogui.moveTo(844,872,)  # ; жёлт магаз
    time.sleep(0.5)
    pyautogui.click(844,872, button="SECONDARY")  # Покупка жёлт магазина
    time.sleep(1)
    pyautogui.moveTo(1350,663) #Наводится на вингу
    time.sleep(0.5)
    pyautogui.click(1350,663)  #ставит вингу
    time.sleep(1)
    pyautogui.moveTo(970,430) #Наводится на место
    time.sleep(0.5)
    pyautogui.click(970,430)  #ставит вингу
    time.sleep(1)
    pyautogui.moveTo(1397,665) #Наводится на дума
    time.sleep(0.5)
    pyautogui.click(1397,665)  #жмёт дума
    time.sleep(0.5)
    pyautogui.moveTo(998,633) #Наводится на место
    time.sleep(0.5)
    pyautogui.click(998,633)  #ставит вингу
    time.sleep(1)
    for a in range(1, 6):
        pyautogui.moveTo(1353,666)  # 1 слот
        time.sleep(0.5)
        pyautogui.click(1353,666)  # 1 слот
        time.sleep(0.5)
        pyautogui.moveTo(1397, 666)  # 2 слот
        time.sleep(0.5)
        pyautogui.click(1397, 666)  # 2 слот
        time.sleep(0.5)
    pyautogui.moveTo(901, 374)  # Наводит возможный эффект
    time.sleep(0.5)
    pyautogui.click(901, 374)  #  возможные эффекты
    keyb.press('m')  # Зажимает кнопку m
    keyb.release('m')
    time.sleep(1)
    keyb.press('o')  # Зажимает кнопку О
    keyb.release('o')  # Отжимает кнопку О
    time.sleep(1)
    pyautogui.moveTo(1104,522)  # подходит к подземке
    time.sleep(0.5)
    pyautogui.click(1104,522, button="SECONDARY")  # подходит к подземке
    time.sleep(1)
    pyautogui.moveTo(758,433)  # Наводит на сундук
    time.sleep(0.5)
    pyautogui.click(758,433)  # Наводит на сундук
    time.sleep(1)
    pyautogui.moveTo(1196,836)  # открыть 1 вариант
    time.sleep(0.5)
    pyautogui.click(1196,836)  # открыть 1 вариант
    time.sleep(1)
    pyautogui.moveTo(1200,799)  # открыть 2 вариант
    time.sleep(0.5)
    pyautogui.click(1200,799)  # открыть 2 вариант
    time.sleep(1)
    pyautogui.moveTo(1213,767)  # открыть 3 вариант
    time.sleep(0.5)
    pyautogui.click(1213,767)  # открыть 3 вариант
    time.sleep(1)
    pyautogui.moveTo(1209,739)  # открыть 4 вариант
    time.sleep(0.5)
    pyautogui.click(1209,739)  # открыть 4 вариант
    time.sleep(1)
    pyautogui.moveTo(1200,713)  # открыть 5 вариант
    time.sleep(0.5)
    pyautogui.click(1200,713)  # открыть 5 вариант
    time.sleep(0.5)
    pyautogui.moveTo(1055,831)  # бесконечность
    time.sleep(0.5)
    pyautogui.click(1055,831)  # бесконечность
    time.sleep(310)
    pyautogui.moveTo(670,838)  # рестарт
    time.sleep(0.5)
    pyautogui.click(670,838)  # рестар
    time.sleep(11)





