import sys
import json
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel, QMainWindow, QFrame, QPushButton, QHBoxLayout
from PyQt5 import QtCore, Qt, QtGui
from PyQt5 import uic

from widgets.listBtnAnalyzes import listBtnAnalyzes
from widgets.listBtnMkb import listBtnMkb
from widgets.listBtnMas import listBtnMas
from widgets.listBtnTnm import listBtnTnm
from widgets.listBtnToh import listBtnToh
from widgets.listBtnFed import listBtnFed
from widgets.listBtnKli import listBtnKli
from widgets.listBtnNom import listBtnNom
from widgets.listBtnCod import listBtnCod

class Main_UI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("ui/main.ui", self)
        self.sidebarNum = False
        self.searchShow = False
        self.numberOfFavorites = 0
        self.fontSize = 1
        self.deltaFontSize = 0
        self.indicators = []
        self.favoritesList = {}
        self.favoritesMkbList = {}
        self.favoritesMasList = {}
        self.favoritesTnmList = {}
        self.favoritesTohList = {}
        self.favoritesFedList = {}
        self.favoritesKliList = {}
        self.favoritesNomList = {}
        self.favoritesCodList = {}
        self.favoritesListAnalizWidget = {}
        self.favoritesListMkbWidget = {}
        self.favoritesListMasWidget = {}
        self.favoritesListTnmWidget = {}
        self.favoritesListTohWidget = {}
        self.favoritesListFedWidget = {}
        self.favoritesListKliWidget = {}
        self.favoritesListNomWidget = {}
        self.favoritesListCodWidget = {}

        self.currentIndicator = {}
        self.currentMkbIndex = None
        self.currentMkbSubclassIndex = None
        self.currentMkbDiseaseIndex = None
        self.currentMkbSubdiseaseIndex = None
        self.currentMkbSubdiseaseIndex = None
        self.currentDisease = {}

        self.currentMasIndex = None
        self.currentMasSubclassIndex = None
        self.currentMasDiseaseIndex = None
        self.currentMasSubdiseaseIndex = None
        self.currentMasSubdiseaseIndex = None

        self.currentTnmIndex = None
        self.currentTnmSubclassIndex = None
        self.currentTnmDiseaseIndex = None
        self.currentTnmSubdiseaseIndex = None
        self.currentTnmSubdiseaseIndex = None

        self.currentTohIndex = None
        self.currentTohSubclassIndex = None
        self.currentTohDiseaseIndex = None
        self.currentTohSubdiseaseIndex = None
        self.currentTohSubdiseaseIndex = None

        self.currentFedIndex = None
        self.currentFedSubclassIndex = None
        self.currentFedDiseaseIndex = None
        self.currentFedSubdiseaseIndex = None
        self.currentFedSubdiseaseIndex = None

        self.currentKliIndex = None
        self.currentKliSubclassIndex = None
        self.currentKliDiseaseIndex = None
        self.currentKliSubdiseaseIndex = None
        self.currentKliSubdiseaseIndex = None

        self.currentNomIndex = None
        self.currentNomSubclassIndex = None
        self.currentNomDiseaseIndex = None
        self.currentNomSubdiseaseIndex = None
        self.currentNomSubdiseaseIndex = None

        self.currentCodIndex = None
        self.currentCodSubclassIndex = None
        self.currentCodDiseaseIndex = None
        self.currentCodSubdiseaseIndex = None
        self.currentCodSubdiseaseIndex = None

        self.subclassesMkb = []
        self.diseaseMkb = []

        self.subclassesMas = []
        self.diseaseMas = []

        self.subclassesTnm = []
        self.diseaseTnm = []

        self.subclassesNom = []
        self.diseaseNom= []

        self.subclassesToh = []
        self.diseaseToh = []

        self.subclassesFed = []
        self.diseaseFed = []

        self.subclassesKli = []
        self.diseaseKli= []

        self.subclassesCod = []
        self.diseaseCod= []


        self.mkbListExample = []
        self.mkbListExampleWidgets = []
        self.mkbListExampleMap = QtCore.QSignalMapper(self)

        self.masListExample = []
        self.masListExampleWidgets = []
        self.masListExampleMap = QtCore.QSignalMapper(self)

        self.tnmListExample = []
        self.tnmListExampleWidgets = []
        self.tnmListExampleMap = QtCore.QSignalMapper(self)

        self.tohListExample = []
        self.tohListExampleWidgets = []
        self.tohListExampleMap = QtCore.QSignalMapper(self)

        self.fedListExample = []
        self.fedListExampleWidgets = []
        self.fedListExampleMap = QtCore.QSignalMapper(self)

        self.kliListExample = []
        self.kliListExampleWidgets = []
        self.kliListExampleMap = QtCore.QSignalMapper(self)

        self.nomListExample = []
        self.nomListExampleWidgets = []
        self.nomListExampleMap = QtCore.QSignalMapper(self)

        self.codListExample = []
        self.codListExampleWidgets = []
        self.codListExampleMap = QtCore.QSignalMapper(self)

        self.analizMap = QtCore.QSignalMapper(self)
        self.indicateMap = QtCore.QSignalMapper(self)
        self.favoritesAnalizMap = QtCore.QSignalMapper(self)

        self.mkbMap = QtCore.QSignalMapper(self)
        self.subclassMkbMap = QtCore.QSignalMapper(self)
        self.diseaseMkbMap = QtCore.QSignalMapper(self)
        self.subdiseaseMkbMap = QtCore.QSignalMapper(self)
        self.favoritesMkbMap = QtCore.QSignalMapper(self)

        self.masMap = QtCore.QSignalMapper(self)
        self.subclassMasMap = QtCore.QSignalMapper(self)
        self.diseaseMasMap = QtCore.QSignalMapper(self)
        self.subdiseaseMasMap = QtCore.QSignalMapper(self)
        self.favoritesMasMap = QtCore.QSignalMapper(self)

        self.tnmMap = QtCore.QSignalMapper(self)
        self.subclassTnmMap = QtCore.QSignalMapper(self)
        self.diseaseTnmMap = QtCore.QSignalMapper(self)
        self.subdiseaseTnmMap = QtCore.QSignalMapper(self)
        self.favoritesTnmMap = QtCore.QSignalMapper(self)

        self.tohMap = QtCore.QSignalMapper(self)
        self.subclassTohMap = QtCore.QSignalMapper(self)
        self.diseaseTohMap = QtCore.QSignalMapper(self)
        self.subdiseaseTohMap = QtCore.QSignalMapper(self)
        self.favoritesTohMap = QtCore.QSignalMapper(self)

        self.fedMap = QtCore.QSignalMapper(self)
        self.subclassFedMap = QtCore.QSignalMapper(self)
        self.diseaseFedMap = QtCore.QSignalMapper(self)
        self.subdiseaseFedMap = QtCore.QSignalMapper(self)
        self.favoritesFedMap = QtCore.QSignalMapper(self)

        self.kliMap = QtCore.QSignalMapper(self)
        self.subclassKliMap = QtCore.QSignalMapper(self)
        self.diseaseKliMap = QtCore.QSignalMapper(self)
        self.subdiseaseKliMap = QtCore.QSignalMapper(self)
        self.favoritesKliMap = QtCore.QSignalMapper(self)

        self.nomMap = QtCore.QSignalMapper(self)
        self.subclassNomMap = QtCore.QSignalMapper(self)
        self.diseaseNomMap = QtCore.QSignalMapper(self)
        self.subdiseaseNomMap = QtCore.QSignalMapper(self)
        self.favoritesNomMap = QtCore.QSignalMapper(self)

        self.codMap = QtCore.QSignalMapper(self)
        self.subclassCodMap = QtCore.QSignalMapper(self)
        self.diseaseCodMap = QtCore.QSignalMapper(self)
        self.subdiseaseCodMap = QtCore.QSignalMapper(self)
        self.favoritesCodMap = QtCore.QSignalMapper(self)


        try:
            with open('data/settings.json', encoding='utf-8') as f:
                self.setting = json.load(f)
                deltaFontSize = self.setting['fontSize']
                self.settingFont(deltaFontSize)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.settingFont(1)

        try:
            with open('data/analyzes.json', encoding='utf-8') as f:
                self.analyzes = json.load(f)
        except FileNotFoundError:
            with open('data/analyzes.json', 'w', encoding='utf-8') as f:
                json.dump([
                    {
                        "category": "",
                        "indicators": [
                            {
                                "title": "",
                                "standard": "",
                                "description": []
                            },
                            {
                                "title": "",
                                "standard": "",
                                "description": []
                            }
                        ]
                    }
                ], f)
        self.analyzesWidget = []

        try:
            with open('data/mkb.json', encoding='utf-8') as f:
                self.mkb = json.load(f)
        except FileNotFoundError:
            with open('data/mkb.json', 'w', encoding='utf-8') as f:
                json.dump([
                    {
                        "class": "",
                        "title": "",
                        "subclasses": [
                            {
                                "subclass": "",
                                "subtitle": "",
                                "disease": [
                                    {
                                        "code": "",
                                        "name": "",
                                        "types": [
                                            {
                                                "subcode": "",
                                                "typename": ""
                                            }
                                        ]
                                    }
                                ]
                            }

                        ]
                    },
                ], f)

        for i in range(len(self.mkb)):
            self.subclassesMkb.append(self.mkb[i]['subclasses'])
        self.mkbWidget = []
        self.mkbSubclassesWidget = []
        self.mkbDiseaseWidget = []
        self.mkbSubdiseaseWidget = []

        try:
            with open('data/mas.json', encoding='utf-8') as f:
                self.mas = json.load(f)
        except FileNotFoundError:
            with open('data/mas.json', 'w', encoding='utf-8') as f:
                json.dump([
                    {
                        "class": "",
                        "title": "",
                        "subclasses": [
                            {
                                "subclass": "",
                                "subtitle": "",
                                "disease": [
                                    {
                                        "code": "",
                                        "name": "",
                                        "types": [
                                            {
                                                "subcode": "",
                                                "typename": ""
                                            }
                                        ]
                                    }
                                ]
                            }

                        ]
                    },
                ], f)

        for i in range(len(self.mas)):
            self.subclassesMas.append(self.mas[i]['subclasses'])
        self.masWidget = []
        self.masSubclassesWidget = []
        self.masDiseaseWidget = []
        self.masSubdiseaseWidget = []

        try:
            with open('data/tnm.json', encoding='utf-8') as f:
                self.tnm = json.load(f)
        except FileNotFoundError:
            with open('data/tnm.json', 'w', encoding='utf-8') as f:
                json.dump([
                    {
                        "class": "",
                        "title": "",
                        "subclasses": [
                            {
                                "subclass": "",
                                "subtitle": "",
                                "disease": [
                                    {
                                        "code": "",
                                        "name": "",
                                        "types": [
                                            {
                                                "subcode": "",
                                                "typename": ""
                                            }
                                        ]
                                    }
                                ]
                            }

                        ]
                    },
                ], f)

        for i in range(len(self.tnm)):
            self.subclassesTnm.append(self.tnm[i]['subclasses'])
        self.tnmWidget = []
        self.tnmSubclassesWidget = []
        self.tnmDiseaseWidget = []
        self.tnmSubdiseaseWidget = []

        try:
            with open('data/toh.json', encoding='utf-8') as f:
                self.toh = json.load(f)
        except FileNotFoundError:
            with open('data/toh.json', 'w', encoding='utf-8') as f:
                json.dump([
                    {
                        "class": "",
                        "title": "",
                        "subclasses": [
                            {
                                "subclass": "",
                                "subtitle": "",
                                "disease": [
                                    {
                                        "code": "",
                                        "name": "",
                                        "types": [
                                            {
                                                "subcode": "",
                                                "typename": ""
                                            }
                                        ]
                                    }
                                ]
                            }

                        ]
                    },
                ], f)

        for i in range(len(self.toh)):
            self.subclassesToh.append(self.toh[i]['subclasses'])
        self.tohWidget = []
        self.tohSubclassesWidget = []
        self.tohDiseaseWidget = []
        self.tohSubdiseaseWidget = []

        try:
            with open('data/fed.json', encoding='utf-8') as f:
                self.fed = json.load(f)
        except FileNotFoundError:
            with open('data/fed.json', 'w', encoding='utf-8') as f:
                json.dump([
                    {
                        "class": "",
                        "title": "",
                        "subclasses": [
                            {
                                "subclass": "",
                                "subtitle": "",
                                "disease": [
                                    {
                                        "code": "",
                                        "name": "",
                                        "types": [
                                            {
                                                "subcode": "",
                                                "typename": ""
                                            }
                                        ]
                                    }
                                ]
                            }

                        ]
                    },
                ], f)

        for i in range(len(self.fed)):
            self.subclassesFed.append(self.fed[i]['subclasses'])
        self.fedWidget = []
        self.fedSubclassesWidget = []
        self.fedDiseaseWidget = []
        self.fedSubdiseaseWidget = []

        try:
            with open('data/kli.json', encoding='utf-8') as f:
                self.kli = json.load(f)
        except FileNotFoundError:
            with open('data/kli.json', 'w', encoding='utf-8') as f:
                json.dump([
                    {
                        "class": "",
                        "title": "",
                        "subclasses": [
                            {
                                "subclass": "",
                                "subtitle": "",
                                "disease": [
                                    {
                                        "code": "",
                                        "name": "",
                                        "types": [
                                            {
                                                "subcode": "",
                                                "typename": ""
                                            }
                                        ]
                                    }
                                ]
                            }

                        ]
                    },
                ], f)

        for i in range(len(self.kli)):
            self.subclassesKli.append(self.kli[i]['subclasses'])
        self.kliWidget = []
        self.kliSubclassesWidget = []
        self.kliDiseaseWidget = []
        self.kliSubdiseaseWidget = []

        try:
            with open('data/nom.json', encoding='utf-8') as f:
                self.nom = json.load(f)
        except FileNotFoundError:
            with open('data/nom.json', 'w', encoding='utf-8') as f:
                json.dump([
                    {
                        "class": "",
                        "title": "",
                        "subclasses": [
                            {
                                "subclass": "",
                                "subtitle": "",
                                "disease": [
                                    {
                                        "code": "",
                                        "name": "",
                                        "types": [
                                            {
                                                "subcode": "",
                                                "typename": ""
                                            }
                                        ]
                                    }
                                ]
                            }

                        ]
                    },
                ], f)

        for i in range(len(self.nom)):
            self.subclassesNom.append(self.nom[i]['subclasses'])
        self.nomWidget = []
        self.nomSubclassesWidget = []
        self.nomDiseaseWidget = []
        self.nomSubdiseaseWidget = []

        try:
            with open('data/cod.json', encoding='utf-8') as f:
                self.cod = json.load(f)
        except FileNotFoundError:
            with open('data/cod.json', 'w', encoding='utf-8') as f:
                json.dump([
                    {
                        "class": "",
                        "title": "",
                        "subclasses": [
                            {
                                "subclass": "",
                                "subtitle": "",
                                "disease": [
                                    {
                                        "code": "",
                                        "name": "",
                                        "types": [
                                            {
                                                "subcode": "",
                                                "typename": ""
                                            }
                                        ]
                                    }
                                ]
                            }

                        ]
                    },
                ], f)

        for i in range(len(self.cod)):
            self.subclassesCod.append(self.cod[i]['subclasses'])
        self.codWidget = []
        self.codSubclassesWidget = []
        self.codDiseaseWidget = []
        self.codSubdiseaseWidget = []

        # favorites
        try:
            with open('data/favorites.json', encoding='utf-8') as f:
                self.favorite = json.load(f)
                self.favoriteAnalyzes = self.favorite['analyzes']
                self.favoriteMkb = self.favorite['mkb']
                self.favoriteMas = self.favorite['mas']
                self.favoriteTnm = self.favorite['tnm']
                self.favoriteToh = self.favorite['toh']
                self.favoriteFed = self.favorite['fed']
                self.favoriteKli = self.favorite['kli']
                self.favoriteKli = self.favorite['nom']
                self.favoriteCod = self.favorite['cod']
        except FileNotFoundError:
            with open('data/favorites.json', 'w', encoding='utf-8') as f:
                json.dump({"analyzes": [], "mkb": [],"mas": [],"tnm": [],"toh": [],"fed": [],"kli": [],"nom": [],"cod": []}, f)

        if len(self.favoriteAnalyzes) > 0:
            for favAnaliz in self.favoriteAnalyzes:
                for analiz in self.analyzes:
                    for indicator in analiz['indicators']:
                        if indicator['title'] == favAnaliz:
                            self.favoritesList[self.numberOfFavorites] = indicator
                            self.numberOfFavorites += 1
            self.favContent = True

        for class_ in self.mkb:
            for subclass in class_['subclasses']:
                for code in subclass['disease']:
                    for subcode in code['types']:
                        subcode['subtitle'] = subclass['subtitle']
                        subcode['name'] = code['name']
                        if subcode not in self.mkbListExample:
                            self.mkbListExample.append(subcode)
                        for favMkb in self.favoriteMkb:
                            if subcode['subcode'] == favMkb:
                                self.favoritesMkbList[self.numberOfFavorites] = subcode
                                self.numberOfFavorites += 1

        for class_ in self.nom:
            for subclass in class_['subclasses']:
                for code in subclass['disease']:
                    for subcode in code['types']:
                        subcode['subtitle'] = subclass['subtitle']
                        subcode['name'] = code['name']
                        if subcode not in self.nomListExample:
                            self.nomListExample.append(subcode)
                        for favMkb in self.favoriteNom:
                            if subcode['subcode'] == favNom:
                                self.favoritesNomList[self.numberOfFavorites] = subcode
                                self.numberOfFavorites += 1

        for class_ in self.mas:
            for subclass in class_['subclasses']:
                for code in subclass['disease']:
                    for subcode in code['types']:
                        subcode['subtitle'] = subclass['subtitle']
                        subcode['name'] = code['name']
                        if subcode not in self.masListExample:
                            self.masListExample.append(subcode)
                        for favMas in self.favoriteMas:
                            if subcode['subcode'] == favMas:
                                self.favoritesMasList[self.numberOfFavorites] = subcode
                                self.numberOfFavorites += 1
        for class_ in self.tnm:
            for subclass in class_['subclasses']:
                for code in subclass['disease']:
                    for subcode in code['types']:
                        subcode['subtitle'] = subclass['subtitle']
                        subcode['name'] = code['name']
                        if subcode not in self.tnmListExample:
                            self.tnmListExample.append(subcode)
                        for favTnm in self.favoriteTnm:
                            if subcode['subcode'] == favTnm:
                                self.favoritesTnmList[self.numberOfFavorites] = subcode
                                self.numberOfFavorites += 1
        for class_ in self.fed:
            for subclass in class_['subclasses']:
                for code in subclass['disease']:
                    for subcode in code['types']:
                        subcode['subtitle'] = subclass['subtitle']
                        subcode['name'] = code['name']
                        if subcode not in self.fedListExample:
                            self.fedListExample.append(subcode)
                        for favFed in self.favoriteFed:
                            if subcode['subcode'] == favFed:
                                self.favoritesFedList[self.numberOfFavorites] = subcode
                                self.numberOfFavorites += 1

        for class_ in self.toh:
            for subclass in class_['subclasses']:
                for code in subclass['disease']:
                    for subcode in code['types']:
                        subcode['subtitle'] = subclass['subtitle']
                        subcode['name'] = code['name']
                        if subcode not in self.tohListExample:
                            self.tohListExample.append(subcode)
                        for favToh in self.favoriteToh:
                            if subcode['subcode'] == favToh:
                                self.favoritesTohList[self.numberOfFavorites] = subcode
                                self.numberOfFavorites += 1

        for class_ in self.cod:
            for subclass in class_['subclasses']:
                for code in subclass['disease']:
                    for subcode in code['types']:
                        subcode['subtitle'] = subclass['subtitle']
                        subcode['name'] = code['name']
                        if subcode not in self.codListExample:
                            self.codListExample.append(subcode)
                        for favCod in self.favoriteToh:
                            if subcode['subcode'] == favCod:
                                self.favoritesCodList[self.numberOfFavorites] = subcode
                                self.numberOfFavorites += 1

        for class_ in self.kli:
            for subclass in class_['subclasses']:
                for code in subclass['disease']:
                    for subcode in code['types']:
                        subcode['subtitle'] = subclass['subtitle']
                        subcode['name'] = code['name']
                        if subcode not in self.kliListExample:
                            self.kliListExample.append(subcode)
                        for favKli in self.favoriteKli:
                            if subcode['subcode'] == favToh:
                                self.favoritesKliList[self.numberOfFavorites] = subcode
                                self.numberOfFavorites += 1

        if len(self.favoritesMkbList) > 0:
            self.favContent = True
        else:
            self.favContent = False
        if self.favContent:
            self.initFavorites()


        # change burger menu
        self.Burger.clicked.connect(self.pushSideBar)
        self.stackedWidget.mousePressEvent = self.clickMouse

        self.pushButton_12.clicked.connect(self.openMenu)  # menu
        self.pushButton_18.clicked.connect(self.openFavorites)  # favorite
        self.pushButton_10.clicked.connect(self.openFavorites)
        self.pushButton_20.clicked.connect(self.openSettings)  # setting

        self.pushButton.clicked.connect(self.openMKB)  # МКБ
        self.pushButton_2.clicked.connect(self.openAnalyzes)
        self.pushButton_3.clicked.connect(self.openMAS)   # Анализы
        self.pushButton_4.clicked.connect(self.openTNM)
        self.pushButton_7.clicked.connect(self.openTOH)
        self.pushButton_8.clicked.connect(self.openFED)
        self.pushButton_9.clicked.connect(self.openKLI)
        self.pushButton_5.clicked.connect(self.openNOM)
        self.pushButton_6.clicked.connect(self.openCOD)

        self.lineEdit.textChanged[str].connect(self.filterMkb)  # фильтр мкб
        self.lineEdit_3.textChanged[str].connect(self.filterMkb)
        self.lineEdit_2.textChanged[str].connect(self.filterAnalyzes)  # фильтр анализов
        self.lineEdit_5.textChanged[str].connect(self.filterFavorite)  # фильтр избранного

        self.lineEdit.textChanged[str].connect(self.filterMas)
        self.lineEdit_3.textChanged[str].connect(self.filterMas)

        self.lineEdit.textChanged[str].connect(self.filterTnm)
        self.lineEdit_3.textChanged[str].connect(self.filterTnm)

        self.lineEdit.textChanged[str].connect(self.filterToh)
        self.lineEdit_3.textChanged[str].connect(self.filterToh)

        self.lineEdit.textChanged[str].connect(self.filterFed)
        self.lineEdit_3.textChanged[str].connect(self.filterFed)

        self.lineEdit.textChanged[str].connect(self.filterKli)
        self.lineEdit_3.textChanged[str].connect(self.filterKli)

        self.pushButton_13.clicked.connect(self.changeFavorite)
        self.pushButton_19.clicked.connect(self.changeFavorite)

        self.pushButton_14.clicked.connect(lambda: self.settingFont(1))
        self.pushButton_15.clicked.connect(lambda: self.settingFont(2))
        self.pushButton_16.clicked.connect(lambda: self.settingFont(3))

        self.initMkbExample()
        self.initMasExample()
        self.initTnmExample()
        self.initFedExample()
        self.initKliExample()
        self.initNomExample()

    def settingFont(self, size):
        self.deltaFontSize = self.fontSize - size
        if self.deltaFontSize == -1:
            self.changeFont(1)
        elif self.deltaFontSize == -2:
            self.changeFont(2)
        elif self.deltaFontSize == 1:
            self.changeFont(-1)
        elif self.deltaFontSize == 2:
            self.changeFont(-2)
        self.fontSize -= self.deltaFontSize
        self.pushButton_14.setStyleSheet("background-color: transparent")
        self.pushButton_15.setStyleSheet("background-color: transparent")
        self.pushButton_16.setStyleSheet("background-color: transparent")
        if self.fontSize == 1:
            self.pushButton_14.setStyleSheet("background-color: #ffffff")
            self.deltaFontSize = 0
        elif self.fontSize == 2:
            self.pushButton_15.setStyleSheet("background-color: #ffffff")
            self.deltaFontSize = 3
        elif self.fontSize == 3:
            self.pushButton_16.setStyleSheet("background-color: #ffffff")
            self.deltaFontSize = 6
        with open('data/settings.json', 'w', encoding='utf-8') as f:
            json.dump({'fontSize': self.fontSize}, f)

    def changeFont(self, delta):
        for widget in self.centralwidget.findChildren(QLabel):
            fontSize = widget.font().pointSize()
            font = QtGui.QFont('Open Sans', fontSize + delta)
            widget.setFont(font)
        for widget in self.centralwidget.findChildren(QPushButton):
            fontSize = widget.font().pointSize()
            font = QtGui.QFont('Open Sans', fontSize + delta)
            widget.setFont(font)

    def initMkbExample(self):
        self.clearWidget(self.ScrollAreaFrame_7)
        for ex in self.mkbListExample:
            listItem = listBtnMkb(ex['subcode'], ex['typename'], 18 + self.deltaFontSize)
            self.mkbListExampleWidgets.append(listItem)

            listItem.clicked.connect(self.mkbListExampleMap.map)
            self.mkbListExampleMap.setMapping(listItem, len(self.mkbListExampleWidgets) - 1)

            self.ScrollAreaFrame_7.layout().addWidget(listItem)

        self.mkbListExampleMap.mapped.connect(self.openMkbExampleInfo)

    def initTnmExample(self):
        self.clearWidget(self.ScrollAreaFrame_7)
        for ex in self.tnmListExample:
            listItem = listBtnTnm(ex['subcode'], ex['typename'], 18 + self.deltaFontSize)
            self.tnmListExampleWidgets.append(listItem)

            listItem.clicked.connect(self.tnmListExampleMap.map)
            self.tnmListExampleMap.setMapping(listItem, len(self.tnmListExampleWidgets) - 1)

            self.ScrollAreaFrame_7.layout().addWidget(listItem)

        self.tnmListExampleMap.mapped.connect(self.openTnmExampleInfo)

    def initNomExample(self):
        self.clearWidget(self.ScrollAreaFrame_7)
        for ex in self.nomListExample:
            listItem = listBtnNom(ex['subcode'], ex['typename'], 18 + self.deltaFontSize)
            self.nomListExampleWidgets.append(listItem)

            listItem.clicked.connect(self.nomListExampleMap.map)
            self.nomListExampleMap.setMapping(listItem, len(self.nomListExampleWidgets) - 1)

            self.ScrollAreaFrame_7.layout().addWidget(listItem)

        self.nomListExampleMap.mapped.connect(self.openNomExampleInfo)

    def initTohExample(self):
        self.clearWidget(self.ScrollAreaFrame_7)
        for ex in self.tohListExample:
            listItem = listBtnToh(ex['subcode'], ex['typename'], 18 + self.deltaFontSize)
            self.tohListExampleWidgets.append(listItem)

            listItem.clicked.connect(self.tohListExampleMap.map)
            self.tohListExampleMap.setMapping(listItem, len(self.tohListExampleWidgets) - 1)

            self.ScrollAreaFrame_7.layout().addWidget(listItem)

        self.tohListExampleMap.mapped.connect(self.openTohExampleInfo)

    def initCodExample(self):
        self.clearWidget(self.ScrollAreaFrame_7)
        for ex in self.codListExample:
            listItem = listBtncod(ex['subcode'], ex['typename'], 18 + self.deltaFontSize)
            self.codListExampleWidgets.append(listItem)

            listItem.clicked.connect(self.codListExampleMap.map)
            self.codListExampleMap.setMapping(listItem, len(self.codListExampleWidgets) - 1)

            self.ScrollAreaFrame_7.layout().addWidget(listItem)

        self.codListExampleMap.mapped.connect(self.openCodExampleInfo)

    def initMasExample(self):
        self.clearWidget(self.ScrollAreaFrame_7)
        for ex in self.masListExample:
            listItem = listBtnMas(ex['subcode'], ex['typename'], 18 + self.deltaFontSize)
            self.masListExampleWidgets.append(listItem)

            listItem.clicked.connect(self.masListExampleMap.map)
            self.masListExampleMap.setMapping(listItem, len(self.masListExampleWidgets) - 1)

            self.ScrollAreaFrame_7.layout().addWidget(listItem)

        self.masListExampleMap.mapped.connect(self.openMasExampleInfo)

    def initKliExample(self):
        self.clearWidget(self.ScrollAreaFrame_7)
        for ex in self.kliListExample:
            listItem = listBtnKli(ex['subcode'], ex['typename'], 18 + self.deltaFontSize)
            self.kliListExampleWidgets.append(listItem)

            listItem.clicked.connect(self.kliListExampleMap.map)
            self.kliListExampleMap.setMapping(listItem, len(self.kliListExampleWidgets) - 1)

            self.ScrollAreaFrame_7.layout().addWidget(listItem)

        self.kliListExampleMap.mapped.connect(self.openKliExampleInfo)

    def initFedExample(self):
        self.clearWidget(self.ScrollAreaFrame_7)
        for ex in self.fedListExample:
            listItem = listBtnFed(ex['subcode'], ex['typename'], 18 + self.deltaFontSize)
            self.fedListExampleWidgets.append(listItem)

            listItem.clicked.connect(self.fedListExampleMap.map)
            self.fedListExampleMap.setMapping(listItem, len(self.fedListExampleWidgets) - 1)

            self.ScrollAreaFrame_7.layout().addWidget(listItem)

        self.fedListExampleMap.mapped.connect(self.openFedExampleInfo)

    def filterAnalyzes(self, text):
        for analiz in self.analyzesWidget:
            textLabel = analiz.layout().itemAt(0).widget().layout().itemAt(0).widget().text()
            if text.lower() in textLabel.lower():
                analiz.show()
            else:
                analiz.hide()

    def filterFavorite(self, text):
        for analiz in self.favoritesListAnalizWidget.keys():
            textLabel = self.favoritesListAnalizWidget[analiz].layout().itemAt(0).widget().layout().itemAt(
                0).widget().text()
            if text.lower() in textLabel.lower():
                self.favoritesListAnalizWidget[analiz].show()
            else:
                self.favoritesListAnalizWidget[analiz].hide()

        for mkb in self.favoritesListMkbWidget.keys():
            textLabel = self.favoritesListMkbWidget[mkb].layout().itemAt(0).widget().layout().itemAt(0).widget().text()
            textDescription = self.favoritesListMkbWidget[mkb].layout().itemAt(0).widget().layout().itemAt(
                1).widget().text()
            if text.lower() in textLabel.lower() or text.lower() in textDescription.lower():
                self.favoritesListMkbWidget[mkb].show()
            else:
                self.favoritesListMkbWidget[mkb].hide()


        for mas in self.favoritesListMasWidget.keys():
            textLabel = self.favoritesListMasWidget[mas].layout().itemAt(0).widget().layout().itemAt(0).widget().text()
            textDescription = self.favoritesListMasWidget[mas].layout().itemAt(0).widget().layout().itemAt(
                1).widget().text()
            if text.lower() in textLabel.lower() or text.lower() in textDescription.lower():
                self.favoritesListMasWidget[mas].show()
            else:
                self.favoritesListMasWidget[mas].hide()

        for tnm in self.favoritesListTnmWidget.keys():
            textLabel = self.favoritesListTnmWidget[tnm].layout().itemAt(0).widget().layout().itemAt(0).widget().text()
            textDescription = self.favoritesListTnmWidget[tnm].layout().itemAt(0).widget().layout().itemAt(
                1).widget().text()
            if text.lower() in textLabel.lower() or text.lower() in textDescription.lower():
                self.favoritesListTnmWidget[tnm].show()
            else:
                self.favoritesListTnmWidget[tnm].hide()

        for cod in self.favoritesListCodWidget.keys():
            textLabel = self.favoritesListTCodidget[toh].layout().itemAt(0).widget().layout().itemAt(0).widget().text()
            textDescription = self.favoritesListCodWidget[toh].layout().itemAt(0).widget().layout().itemAt(
                1).widget().text()
            if text.lower() in textLabel.lower() or text.lower() in textDescription.lower():
                self.favoritesListCodWidget[toh].show()
            else:
                self.favoritesListCodWidget[toh].hide()

        for toh in self.favoritesListTohWidget.keys():
            textLabel = self.favoritesListTohWidget[toh].layout().itemAt(0).widget().layout().itemAt(0).widget().text()
            textDescription = self.favoritesListTohWidget[toh].layout().itemAt(0).widget().layout().itemAt(
                1).widget().text()
            if text.lower() in textLabel.lower() or text.lower() in textDescription.lower():
                self.favoritesListTohWidget[toh].show()
            else:
                self.favoritesListTohWidget[toh].hide()

        for fed in self.favoritesListFedWidget.keys():
            textLabel = self.favoritesListFedWidget[fed].layout().itemAt(0).widget().layout().itemAt(0).widget().text()
            textDescription = self.favoritesListFedWidget[fed].layout().itemAt(0).widget().layout().itemAt(
                1).widget().text()
            if text.lower() in textLabel.lower() or text.lower() in textDescription.lower():
                self.favoritesListFedWidget[fed].show()
            else:
                self.favoritesListFedWidget[fed].hide()

        for kli in self.favoritesListKliWidget.keys():
            textLabel = self.favoritesListKliWidget[kli].layout().itemAt(0).widget().layout().itemAt(0).widget().text()
            textDescription = self.favoritesListKliWidget[kli].layout().itemAt(0).widget().layout().itemAt(
                1).widget().text()
            if text.lower() in textLabel.lower() or text.lower() in textDescription.lower():
                self.favoritesListKliWidget[kli].show()
            else:
                self.favoritesListKliWidget[kli].hide()

        for nom in self.favoritesListNomWidget.keys():
            textLabel = self.favoritesListNomWidget[nom].layout().itemAt(0).widget().layout().itemAt(0).widget().text()
            textDescription = self.favoritesListNomWidget[nom].layout().itemAt(0).widget().layout().itemAt(
                1).widget().text()
            if text.lower() in textLabel.lower() or text.lower() in textDescription.lower():
                self.favoritesListNomWidget[nom].show()
            else:
                self.favoritesListNomWidget[nom].hide()

    def filterMkb(self, text):
        if text == '':
            self.InnerStacked.setCurrentIndex(1)
            self.lineEdit.setText(text)
            self.lineEdit_3.setText(text)
        else:
            self.InnerStacked.setCurrentIndex(6)
            self.lineEdit.setText(text)
            self.lineEdit_3.setText(text)

            for mkb in self.mkbListExampleWidgets:
                textLabel = mkb.layout().itemAt(0).widget().layout().itemAt(0).widget().text()
                textDescription = mkb.layout().itemAt(0).widget().layout().itemAt(1).widget().text()
                if text.lower() in textLabel.lower() or text.lower() in textDescription.lower():
                    mkb.show()
                else:
                    mkb.hide()

    def filterMas(self, text):
        if text == '':
            self.InnerStacked.setCurrentIndex(1)
            self.lineEdit.setText(text)
            self.lineEdit_3.setText(text)
        else:
            self.InnerStacked.setCurrentIndex(6)
            self.lineEdit.setText(text)
            self.lineEdit_3.setText(text)
            for mas in self.masListExampleWidgets:
                textLabel = mas.layout().itemAt(0).widget().layout().itemAt(0).widget().text()
                textDescription = mas.layout().itemAt(0).widget().layout().itemAt(1).widget().text()
                if text.lower() in textLabel.lower() or text.lower() in textDescription.lower():
                    mas.show()
                else:
                    mas.hide()

    def filterKli(self, text):
        if text == '':
            self.InnerStacked.setCurrentIndex(1)
            self.lineEdit.setText(text)
            self.lineEdit_3.setText(text)
        else:
            self.InnerStacked.setCurrentIndex(6)
            self.lineEdit.setText(text)
            self.lineEdit_3.setText(text)
            for kli in self.kliListExampleWidgets:
                textLabel = kli.layout().itemAt(0).widget().layout().itemAt(0).widget().text()
                textDescription = kli.layout().itemAt(0).widget().layout().itemAt(1).widget().text()
                if text.lower() in textLabel.lower() or text.lower() in textDescription.lower():
                    kli.show()
                else:
                    kli.hide()


    def filterNom(self, text):
        if text == '':
            self.InnerStacked.setCurrentIndex(1)
            self.lineEdit.setText(text)
            self.lineEdit_3.setText(text)
        else:
            self.InnerStacked.setCurrentIndex(6)
            self.lineEdit.setText(text)
            self.lineEdit_3.setText(text)
            for nom in self.nomListExampleWidgets:
                textLabel = nom.layout().itemAt(0).widget().layout().itemAt(0).widget().text()
                textDescription = nom.layout().itemAt(0).widget().layout().itemAt(1).widget().text()
                if text.lower() in textLabel.lower() or text.lower() in textDescription.lower():
                    nom.show()
                else:
                    nom.hide()


    def filterTnm(self, text):
        if text == '':
            self.InnerStacked.setCurrentIndex(1)
            self.lineEdit.setText(text)
            self.lineEdit_3.setText(text)
        else:
            self.InnerStacked.setCurrentIndex(6)
            self.lineEdit.setText(text)
            self.lineEdit_3.setText(text)
            for tnm in self.tnmListExampleWidgets:
                textLabel = tnm.layout().itemAt(0).widget().layout().itemAt(0).widget().text()
                textDescription = tnm.layout().itemAt(0).widget().layout().itemAt(1).widget().text()
                if text.lower() in textLabel.lower() or text.lower() in textDescription.lower():
                    tnm.show()
                else:
                    tnm.hide()

    def filterToh(self, text):
        if text == '':
            self.InnerStacked.setCurrentIndex(1)
            self.lineEdit.setText(text)
            self.lineEdit_3.setText(text)
        else:
            self.InnerStacked.setCurrentIndex(6)
            self.lineEdit.setText(text)
            self.lineEdit_3.setText(text)
            for toh in self.tohListExampleWidgets:
                textLabel = toh.layout().itemAt(0).widget().layout().itemAt(0).widget().text()
                textDescription = toh.layout().itemAt(0).widget().layout().itemAt(1).widget().text()
                if text.lower() in textLabel.lower() or text.lower() in textDescription.lower():
                    toh.show()
                else:
                    toh.hide()

    def filterCod(self, text):
        if text == '':
            self.InnerStacked.setCurrentIndex(1)
            self.lineEdit.setText(text)
            self.lineEdit_3.setText(text)
        else:
            self.InnerStacked.setCurrentIndex(6)
            self.lineEdit.setText(text)
            self.lineEdit_3.setText(text)
            for cod in self.codListExampleWidgets:
                textLabel = cod.layout().itemAt(0).widget().layout().itemAt(0).widget().text()
                textDescription = cod.layout().itemAt(0).widget().layout().itemAt(1).widget().text()
                if text.lower() in textLabel.lower() or text.lower() in textDescription.lower():
                    cod.show()
                else:
                    cod.hide()

    def filterFed(self, text):
        if text == '':
            self.InnerStacked.setCurrentIndex(1)
            self.lineEdit.setText(text)
            self.lineEdit_3.setText(text)
        else:
            self.InnerStacked.setCurrentIndex(6)
            self.lineEdit.setText(text)
            self.lineEdit_3.setText(text)
            for fed in self.tohListExampleWidgets:
                textLabel = fed.layout().itemAt(0).widget().layout().itemAt(0).widget().text()
                textDescription = fed.layout().itemAt(0).widget().layout().itemAt(1).widget().text()
                if text.lower() in textLabel.lower() or text.lower() in textDescription.lower():
                    fed.show()
                else:
                    fed.hide()
    def saveFavorite(self):
        with open('data/favorites.json', 'w', encoding='utf-8') as f:
            json.dump({"analyzes": self.favoriteAnalyzes, "mkb": self.favoriteMkb, "mas": self.favoriteMas,
            "tnm": self.favoriteTnm,"toh": self.favoriteToh,"fed": self.favoriteFed,"kli": self.favoriteKli,"nom": self.favoriteNom,"cod": self.favoriteCod}, f)

    def changeFavorite(self):
        if self.stackedWidget.currentIndex() == 2:
            if self.currentIndicator['title'] not in self.favoriteAnalyzes:
                self.addAnalizFavorite()
            else:
                self.deleteAnalizFavorite()
        # elif self.stackedWidget.currentIndex() == 6:
        #     if self.currentDisease['subcode'] not in self.favoriteMkb:
        #         self.addMkbFavorite()
        #     else:
        #         self.deleteMkbFavorite()
        # elif self.stackedWidget.currentIndex() == 6:
        #     if self.currentDisease['subcode'] not in self.favoriteMas:
        #         self.addMasFavorite()
        #     else:
        #         self.deleteMasFavorite()
        elif self.stackedWidget.currentIndex() == 6:
            if self.currentDisease['subcode'] not in self.favoriteTnm:
                self.addTnmFavorite()
            else:
                self.deleteTnmFavorite()

    def addMkbFavorite(self):
        self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        if self.currentDisease['subcode'] in self.favoriteMkb:
            return
        self.favoritesMkbList[self.numberOfFavorites] = self.currentDisease
        self.favoriteMkb.append(self.currentDisease['subcode'])

        listItem = listBtnMkb(self.currentDisease['subcode'], self.currentDisease['typename'], 18 + self.deltaFontSize)
        listItem.clicked.connect(self.favoritesMkbMap.map)
        self.favoritesListMkbWidget[self.numberOfFavorites] = listItem
        self.favoritesMkbMap.setMapping(listItem, self.numberOfFavorites)
        self.favoritesMkbMap.mapped.connect(self.openFavMkbDiseaseInfo)
        self.numberOfFavorites += 1

        self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.saveFavorite()
        self.favContent = True

    def addKliFavorite(self):
        self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        if self.currentDisease['subcode'] in self.favoriteKli:
            return
        self.favoritesKliList[self.numberOfFavorites] = self.currentDisease
        self.favoriteKli.append(self.currentDisease['subcode'])

        listItem = listBtnKli(self.currentDisease['subcode'], self.currentDisease['typename'], 18 + self.deltaFontSize)
        listItem.clicked.connect(self.favoritesKliMap.map)
        self.favoritesListKliWidget[self.numberOfFavorites] = listItem
        self.favoritesKliMap.setMapping(listItem, self.numberOfFavorites)
        self.favoritesKliMap.mapped.connect(self.openFavKliDiseaseInfo)
        self.numberOfFavorites += 1

        self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.saveFavorite()
        self.favContent = True

    def addNomFavorite(self):
        self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        if self.currentDisease['subcode'] in self.favoriteNom:
            return
        self.favoritesNomList[self.numberOfFavorites] = self.currentDisease
        self.favoriteNom.append(self.currentDisease['subcode'])

        listItem = listBtnKli(self.currentDisease['subcode'], self.currentDisease['typename'], 18 + self.deltaFontSize)
        listItem.clicked.connect(self.favoritesKliMap.map)
        self.favoritesListNomWidget[self.numberOfFavorites] = listItem
        self.favoritesNomMap.setMapping(listItem, self.numberOfFavorites)
        self.favoritesNomMap.mapped.connect(self.openFavNomDiseaseInfo)
        self.numberOfFavorites += 1

        self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.saveFavorite()
        self.favContent = True

    def addMasFavorite(self):
        self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        if self.currentDisease['subcode'] in self.favoriteMas:
            return
        self.favoritesMasList[self.numberOfFavorites] = self.currentDisease
        self.favoriteMas.append(self.currentDisease['subcode'])

        listItem = listBtnMas(self.currentDisease['subcode'], self.currentDisease['typename'], 18 + self.deltaFontSize)
        listItem.clicked.connect(self.favoritesMasMap.map)
        self.favoritesListMasWidget[self.numberOfFavorites] = listItem
        self.favoritesMasMap.setMapping(listItem, self.numberOfFavorites)
        self.favoritesMasMap.mapped.connect(self.openFavMasDiseaseInfo)
        self.numberOfFavorites += 1

        self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.saveFavorite()
        self.favContent = True

    def addFedFavorite(self):
        self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        if self.currentDisease['subcode'] in self.favoriteFed:
            return
        self.favoritesFedList[self.numberOfFavorites] = self.currentDisease
        self.favoriteFed.append(self.currentDisease['subcode'])

        listItem = listBtnFed(self.currentDisease['subcode'], self.currentDisease['typename'], 18 + self.deltaFontSize)
        listItem.clicked.connect(self.favoritesFedMap.map)
        self.favoritesListFedWidget[self.numberOfFavorites] = listItem
        self.favoritesFedMap.setMapping(listItem, self.numberOfFavorites)
        self.favoritesFedMap.mapped.connect(self.openFavFedDiseaseInfo)
        self.numberOfFavorites += 1

        self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.saveFavorite()
        self.favContent = True

    def addTnmFavorite(self):
        self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        if self.currentDisease['subcode'] in self.favoriteTnm:
            return
        self.favoritesTnmList[self.numberOfFavorites] = self.currentDisease
        self.favoriteTnm.append(self.currentDisease['subcode'])

        listItem = listBtnTnm(self.currentDisease['subcode'], self.currentDisease['typename'], 18 + self.deltaFontSize)
        listItem.clicked.connect(self.favoritesTnmMap.map)
        self.favoritesListTnmWidget[self.numberOfFavorites] = listItem
        self.favoritesTnmMap.setMapping(listItem, self.numberOfFavorites)
        self.favoritesTnmMap.mapped.connect(self.openFavTnmDiseaseInfo)
        self.numberOfFavorites += 1

        self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.saveFavorite()
        self.favContent = True

    def addTohFavorite(self):
        self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        if self.currentDisease['subcode'] in self.favoriteToh:
            return
        self.favoritesTohList[self.numberOfFavorites] = self.currentDisease
        self.favoriteToh.append(self.currentDisease['subcode'])

        listItem = listBtnToh(self.currentDisease['subcode'], self.currentDisease['typename'], 18 + self.deltaFontSize)
        listItem.clicked.connect(self.favoritesTohMap.map)
        self.favoritesListTohWidget[self.numberOfFavorites] = listItem
        self.favoritesTohMap.setMapping(listItem, self.numberOfFavorites)
        self.favoritesTohMap.mapped.connect(self.openFavTohDiseaseInfo)
        self.numberOfFavorites += 1

        self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.saveFavorite()
        self.favContent = True

    def addCodFavorite(self):
        self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        if self.currentDisease['subcode'] in self.favoriteCod:
            return
        self.favoritesCodList[self.numberOfFavorites] = self.currentDisease
        self.favoriteCod.append(self.currentDisease['subcode'])

        listItem = listBtnToh(self.currentDisease['subcode'], self.currentDisease['typename'], 18 + self.deltaFontSize)
        listItem.clicked.connect(self.favoritesCodMap.map)
        self.favoritesListCodWidget[self.numberOfFavorites] = listItem
        self.favoritesCodMap.setMapping(listItem, self.numberOfFavorites)
        self.favoritesCodMap.mapped.connect(self.openFavCodDiseaseInfo)
        self.numberOfFavorites += 1

        self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.saveFavorite()
        self.favContent = True


    def deleteMkbFavorite(self):
        self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))

        curNum = 0
        for num in self.favoritesMkbList.keys():
            if self.favoritesMkbList[num]['subcode'] == self.currentDisease['subcode']:
                curNum = num
                break

        widget = self.favoritesListMkbWidget[curNum]
        self.clearWidget(widget)
        self.ScrollAreaFrame_5.layout().removeWidget(widget)
        widget.hide()

        self.favoriteMkb.remove(self.currentDisease['subcode'])

        self.saveFavorite()
        if len(self.favoriteAnalyzes) or len(self.favoriteTnm) or len(self.favoriteMas) or len(self.favoriteMkb) or len(self.favoriteToh) or len(self.favoriteFed) or len(self.favoriteKli) or len(self.favoriteNom) or len(self.favoriteCod):
            self.favContent = True
        else:
            self.favContent = False
            self.openFavorites()

    def deleteNomFavorite(self):
        self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))

        curNum = 0
        for num in self.favoritesNomList.keys():
            if self.favoritesNomList[num]['subcode'] == self.currentDisease['subcode']:
                curNum = num
                break

        widget = self.favoritesListNomWidget[curNum]
        self.clearWidget(widget)
        self.ScrollAreaFrame_5.layout().removeWidget(widget)
        widget.hide()

        self.favoriteNom.remove(self.currentDisease['subcode'])

        self.saveFavorite()
        if len(self.favoriteAnalyzes) or len(self.favoriteTnm) or len(self.favoriteMas) or len(self.favoriteMkb) or len(self.favoriteToh) or len(self.favoriteFed) or len(self.favoriteKli) or len(self.favoriteNom) or len(self.favoriteCod):
            self.favContent = True
        else:
            self.favContent = False
            self.openFavorites()

    def deleteKliFavorite(self):
        self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))

        curNum = 0
        for num in self.favoritesKliList.keys():
            if self.favoritesKliList[num]['subcode'] == self.currentDisease['subcode']:
                curNum = num
                break

        widget = self.favoritesListKliWidget[curNum]
        self.clearWidget(widget)
        self.ScrollAreaFrame_5.layout().removeWidget(widget)
        widget.hide()

        self.favoriteKli.remove(self.currentDisease['subcode'])

        self.saveFavorite()
        if len(self.favoriteAnalyzes) or len(self.favoriteTnm) or len(self.favoriteMas) or len(self.favoriteMkb) or len(self.favoriteToh) or len(self.favoriteFed) or len(self.favoriteKli) or len(self.favoriteNom) or len(self.favoriteCod):
            self.favContent = True
        else:
            self.favContent = False
            self.openFavorites()

    def deleteTnmFavorite(self):
        self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))

        curNum = 0
        for num in self.favoritesTnmList.keys():
            if self.favoritesTnmList[num]['subcode'] == self.currentDisease['subcode']:
                curNum = num
                break

        widget = self.favoritesListTnmWidget[curNum]
        self.clearWidget(widget)
        self.ScrollAreaFrame_5.layout().removeWidget(widget)
        widget.hide()

        self.favoriteTnm.remove(self.currentDisease['subcode'])

        self.saveFavorite()
        if len(self.favoriteAnalyzes) or len(self.favoriteTnm) or len(self.favoriteMas) or len(self.favoriteMkb) or len(self.favoriteToh) or len(self.favoriteFed) or len(self.favoriteKli) or len(self.favoriteNom) or len(self.favoriteCod):
            self.favContent = True
        else:
            self.favContent = False
            self.openFavorites()

    def deleteFedFavorite(self):
        self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))

        curNum = 0
        for num in self.favoritesFedList.keys():
            if self.favoritesFedList[num]['subcode'] == self.currentDisease['subcode']:
                curNum = num
                break

        widget = self.favoritesListFedWidget[curNum]
        self.clearWidget(widget)
        self.ScrollAreaFrame_5.layout().removeWidget(widget)
        widget.hide()

        self.favoriteFed.remove(self.currentDisease['subcode'])

        self.saveFavorite()
        if len(self.favoriteAnalyzes) or len(self.favoriteTnm) or len(self.favoriteMas) or len(self.favoriteMkb) or len(self.favoriteToh) or len(self.favoriteFed) or len(self.favoriteKli) or len(self.favoriteNom) or len(self.favoriteCod):
            self.favContent = True
        else:
            self.favContent = False
            self.openFavorites()

    def deleteTohFavorite(self):
        self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))

        curNum = 0
        for num in self.favoritesTohList.keys():
            if self.favoritesTohList[num]['subcode'] == self.currentDisease['subcode']:
                curNum = num
                break

        widget = self.favoritesListTohWidget[curNum]
        self.clearWidget(widget)
        self.ScrollAreaFrame_5.layout().removeWidget(widget)
        widget.hide()

        self.favoriteToh.remove(self.currentDisease['subcode'])

        self.saveFavorite()
        if len(self.favoriteAnalyzes) or len(self.favoriteTnm) or len(self.favoriteMas) or len(self.favoriteMkb) or len(self.favoriteToh) or len(self.favoriteFed) or len(self.favoriteKli) or len(self.favoriteNom) or len(self.favoriteCod):
            self.favContent = True
        else:
            self.favContent = False
            self.openFavorites()


    def deleteCodFavorite(self):
        self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))

        curNum = 0
        for num in self.favoritesCodList.keys():
            if self.favoritesCodList[num]['subcode'] == self.currentDisease['subcode']:
                curNum = num
                break

        widget = self.favoritesListCodWidget[curNum]
        self.clearWidget(widget)
        self.ScrollAreaFrame_5.layout().removeWidget(widget)
        widget.hide()

        self.favoriteCod.remove(self.currentDisease['subcode'])

        self.saveFavorite()
        if len(self.favoriteAnalyzes) or len(self.favoriteTnm) or len(self.favoriteMas) or len(self.favoriteMkb) or len(self.favoriteToh) or len(self.favoriteFed) or len(self.favoriteKli) or len(self.favoriteNom) or len(self.favoriteCod):
            self.favContent = True
        else:
            self.favContent = False
            self.openFavorites()

    def deleteMasFavorite(self):
        self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))

        curNum = 0
        for num in self.favoritesMasList.keys():
            if self.favoritesMasList[num]['subcode'] == self.currentDisease['subcode']:
                curNum = num
                break

        widget = self.favoritesListMasWidget[curNum]
        self.clearWidget(widget)
        self.ScrollAreaFrame_5.layout().removeWidget(widget)
        widget.hide()

        self.favoriteMas.remove(self.currentDisease['subcode'])

        self.saveFavorite()
        if len(self.favoriteAnalyzes) or len(self.favoriteMkb) or len(self.favoriteMas) or len(self.favoriteTnm) or len(self.favoriteToh) or len(self.favoriteFed) or len(self.favoriteKli) or len(self.favoriteNom) or len(self.favoriteCod):
            self.favContent = True
        else:
            self.favContent = False
            self.openFavorites()

    def addAnalizFavorite(self):
        self.pushButton_13.setIcon(QtGui.QIcon('images/star-active.png'))
        if self.currentIndicator['title'] in self.favoriteAnalyzes:
            return
        self.favoritesList[self.numberOfFavorites] = self.currentIndicator
        self.favoriteAnalyzes.append(self.currentIndicator['title'])

        listItem = listBtnAnalyzes(self.currentIndicator['title'], 14 + self.deltaFontSize)
        listItem.clicked.connect(self.favoritesAnalizMap.map)
        self.favoritesListAnalizWidget[self.numberOfFavorites] = listItem
        self.favoritesAnalizMap.setMapping(listItem, self.numberOfFavorites)
        self.favoritesAnalizMap.mapped.connect(self.openFavIndicator)
        self.numberOfFavorites += 1

        self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.saveFavorite()
        self.favContent = True

    def deleteAnalizFavorite(self):
        self.pushButton_13.setIcon(QtGui.QIcon('images/star.png'))

        curNum = 0
        for num in self.favoritesList.keys():
            if self.favoritesList[num]['title'] == self.currentIndicator['title']:
                curNum = num
                break

        widget = self.favoritesListAnalizWidget[curNum]
        self.clearWidget(widget)
        self.ScrollAreaFrame_5.layout().removeWidget(widget)
        widget.hide()

        self.favoriteAnalyzes.remove(self.currentIndicator['title'])
        self.favoritesAnalizMap = None

        self.saveFavorite()
        if len(self.favoriteAnalyzes) or len(self.favoriteMkb) or len(self.favoriteMas):
            self.favContent = True
        else:
            self.favContent = False
            self.openFavorites()

    def initFavorites(self):
        self.clearWidget(self.ScrollAreaFrame_5)
        for i in self.favoritesList:
            listItem = listBtnAnalyzes(self.favoritesList[i]['title'], 14 + self.deltaFontSize)
            listItem.clicked.connect(self.favoritesAnalizMap.map)
            self.favoritesListAnalizWidget[i] = listItem
            self.favoritesAnalizMap.setMapping(listItem, i)

            self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.favoritesAnalizMap.mapped.connect(self.openFavIndicator)

        for i in self.favoritesMkbList:
            listItem = listBtnMkb(self.favoritesMkbList[i]['subcode'], self.favoritesMkbList[i]['typename'],
                                  18 + self.deltaFontSize)
            listItem.clicked.connect(self.favoritesMkbMap.map)
            self.favoritesListMkbWidget[i] = listItem
            self.favoritesMkbMap.setMapping(listItem, i)

            self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.favoritesMkbMap.mapped.connect(self.openFavMkbDiseaseInfo)


        for i in self.favoritesMasList:
            listItem = listBtnMas(self.favoritesMasList[i]['subcode'], self.favoritesMasList[i]['typename'],
                                  18 + self.deltaFontSize)
            listItem.clicked.connect(self.favoritesMasMap.map)
            self.favoritesListMasWidget[i] = listItem
            self.favoritesMasMap.setMapping(listItem, i)

            self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.favoritesMasMap.mapped.connect(self.openFavMasDiseaseInfo)

        for i in self.favoritesKliList:
            listItem = listBtnMas(self.favoritesKliList[i]['subcode'], self.favoritesKliList[i]['typename'],
                                  18 + self.deltaFontSize)
            listItem.clicked.connect(self.favoritesKliMap.map)
            self.favoritesListKliWidget[i] = listItem
            self.favoritesKliMap.setMapping(listItem, i)

            self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.favoritesKliMap.mapped.connect(self.openFavKliDiseaseInfo)

        for i in self.favoritesTnmList:
            listItem = listBtnTnm(self.favoritesTnmList[i]['subcode'], self.favoritesTnmList[i]['typename'],
                                  18 + self.deltaFontSize)
            listItem.clicked.connect(self.favoritesTnmMap.map)
            self.favoritesListTnmWidget[i] = listItem
            self.favoritesTnmMap.setMapping(listItem, i)

            self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.favoritesTnmMap.mapped.connect(self.openFavTnmDiseaseInfo)

        for i in self.favoritesTohList:
            listItem = listBtnToh(self.favoritesTohList[i]['subcode'], self.favoritesTohList[i]['typename'],
                                  18 + self.deltaFontSize)
            listItem.clicked.connect(self.favoritesTohMap.map)
            self.favoritesListTohWidget[i] = listItem
            self.favoritesTohMap.setMapping(listItem, i)

            self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.favoritesTohMap.mapped.connect(self.openFavTohDiseaseInfo)

        for i in self.favoritesFedList:
            listItem = listBtnFed(self.favoritesFedList[i]['subcode'], self.favoritesFedList[i]['typename'],
                                  18 + self.deltaFontSize)
            listItem.clicked.connect(self.favoritesFedMap.map)
            self.favoritesListFedWidget[i] = listItem
            self.favoritesFedMap.setMapping(listItem, i)

            self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.favoritesFedMap.mapped.connect(self.openFavFedDiseaseInfo)

        for i in self.favoritesNomList:
            listItem = listBtnFed(self.favoritesNomList[i]['subcode'], self.favoritesNomList[i]['typename'],
                                  18 + self.deltaFontSize)
            listItem.clicked.connect(self.favoritesNomMap.map)
            self.favoritesListNomWidget[i] = listItem
            self.favoritesNomMap.setMapping(listItem, i)

            self.ScrollAreaFrame_5.layout().addWidget(listItem)

        self.favoritesNomMap.mapped.connect(self.openFavNomDiseaseInfo)
    def openAnalyzes(self):
        self.InnerStacked.setCurrentIndex(4)
        self.Header.setStyleSheet("background-color: #6FD3B5; border: none")
        self.Logo.setText("Анализы")
        self.pushButton_10.hide()
        self.closeSidebar()
        self.loadAnalyzes()

    def openMKB(self):
        self.InnerStacked.setCurrentIndex(1)
        self.Header.setStyleSheet("background-color: #6FD3B5; border: none")
        self.Logo.setText("МКБ")
        self.pushButton_10.hide()
        self.closeSidebar()
        self.loadMkb()


    def openCOD(self):
        self.InnerStacked.setCurrentIndex(1)
        self.Header.setStyleSheet("background-color: #6FD3B5; border: none")
        self.Logo.setText("Коды хирургических операций")
        self.pushButton_10.hide()
        self.closeSidebar()
        self.loadCod()

    def openMAS(self):
        self.InnerStacked.setCurrentIndex(1)
        self.Header.setStyleSheet("background-color: #6FD3B5; border: none")
        self.Logo.setText("МЭС")
        self.pushButton_10.hide()
        self.closeSidebar()
        self.loadMas()

    def openTNM(self):
        self.InnerStacked.setCurrentIndex(1)
        self.Header.setStyleSheet("background-color: #6FD3B5; border: none")
        self.Logo.setText("TNM")
        self.pushButton_10.hide()
        self.closeSidebar()
        self.loadTnm()

    def openTOH(self):
        self.InnerStacked.setCurrentIndex(1)
        self.Header.setStyleSheet("background-color: #6FD3B5; border: none")
        self.Logo.setText("Сроки лечения")
        self.pushButton_10.hide()
        self.closeSidebar()
        self.loadToh()

    def openFED(self):
        self.InnerStacked.setCurrentIndex(1)
        self.Header.setStyleSheet("background-color: #6FD3B5; border: none")
        self.Logo.setText("Федеральные стандарты")
        self.pushButton_10.hide()
        self.closeSidebar()
        self.loadFed()

    def openKLI(self):
        self.InnerStacked.setCurrentIndex(1)
        self.Header.setStyleSheet("background-color: #6FD3B5; border: none")
        self.Logo.setText("Клинические рекомендации")
        self.pushButton_10.hide()
        self.closeSidebar()
        self.loadKli()

    def openNOM(self):
        self.InnerStacked.setCurrentIndex(1)
        self.Header.setStyleSheet("background-color: #6FD3B5; border: none")
        self.Logo.setText("Номенклатура медицинских услуг")
        self.pushButton_10.hide()
        self.closeSidebar()
        self.loadNom()


    def openMenu(self):
        self.InnerStacked.setCurrentIndex(0)
        self.Header.setStyleSheet("background-color: #74DCBD; border: none")
        self.Logo.setText("MedHealth")
        self.pushButton_10.show()
        self.pushButton_10.setIcon(QtGui.QIcon('images/favorites.png'))
        self.closeSidebar()
        self.analizMap = QtCore.QSignalMapper(self)
        self.indicateMap = QtCore.QSignalMapper(self)

    def openFavorites(self):
        self.Header.setStyleSheet("background-color: #6FD3B5; border: none")
        self.Logo.setText("Избранное")
        self.closeSidebar()
        self.analizMap = QtCore.QSignalMapper(self)
        self.indicateMap = QtCore.QSignalMapper(self)
        self.frame_72.hide()
        if self.favContent:
            self.pushButton_10.show()
            self.pushButton_10.setIcon(QtGui.QIcon('images/favorites-search.png'))
            self.pushButton_10.clicked.connect(self.showSearchFavorite)
            self.InnerStacked.setCurrentIndex(5)
        else:
            self.pushButton_10.hide()
            self.InnerStacked.setCurrentIndex(3)

    def showSearchFavorite(self):
        self.lineEdit_5.setText('')
        if self.searchShow:
            self.frame_72.hide()
            self.searchShow = not self.searchShow
        else:
            self.frame_72.show()
            self.searchShow = not self.searchShow

    def openSettings(self):
        self.InnerStacked.setCurrentIndex(2)
        self.Header.setStyleSheet("background-color: #6FD3B5; border: none")
        self.Logo.setText("Настройки")
        self.pushButton_10.hide()
        self.closeSidebar()
        self.analizMap = QtCore.QSignalMapper(self)
        self.indicateMap = QtCore.QSignalMapper(self)

    def pushSideBar(self):
        animationSidebar = QtCore.QPropertyAnimation(self.Sidebar, b"geometry")
        animationSidebar.setDuration(1000)

        animationWindow = QtCore.QPropertyAnimation(self.stackedWidget, b"geometry")
        animationWindow.setDuration(1000)
        if self.sidebarNum:
            animationWindow.setStartValue(Qt.QRect(0, 0, 1920, 1080))
            animationWindow.setEndValue(Qt.QRect(730, 0, 1920, 1080))

            animationSidebar.setStartValue(Qt.QRect(0, 0, 0, 1080))
            animationSidebar.setEndValue(Qt.QRect(0, 0, 730, 1080))
            self.sidebarNum = False
        else:
            animationWindow.setStartValue(Qt.QRect(730, 0, 1920, 1080))
            animationWindow.setEndValue(Qt.QRect(0, 0, 1920, 1080))

            animationSidebar.setStartValue(Qt.QRect(0, 0, 730, 1080))
            animationSidebar.setEndValue(Qt.QRect(0, 0, 0, 1080))
            self.sidebarNum = True
        animationSidebar.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        animationWindow.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        animationSidebar.start()
        animationWindow.start()

    def clickMouse(self, e):
        if e.button() == Qt.QMouseEvent.button(e) and self.sidebarNum:
            self.closeSidebar()

    def closeSidebar(self):
        if self.sidebarNum:
            animationSidebar = QtCore.QPropertyAnimation(self.Sidebar, b"geometry")
            animationSidebar.setDuration(1000)

            animationWindow = QtCore.QPropertyAnimation(self.stackedWidget, b"geometry")
            animationWindow.setDuration(1000)
            animationWindow.setStartValue(Qt.QRect(0, 0, 1920, 1080))
            animationWindow.setEndValue(Qt.QRect(730, 0, 1920, 1080))

            animationSidebar.setStartValue(Qt.QRect(0, 0, 0, 1080))
            animationSidebar.setEndValue(Qt.QRect(0, 0, 730, 1080))
            self.sidebarNum = False
            animationSidebar.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            animationWindow.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            animationSidebar.start()
            animationWindow.start()

    def closeIndicators(self):
        self.stackedWidget.setCurrentIndex(0)

    def closeIndicator(self):
        self.stackedWidget.setCurrentIndex(1)

    def closeFavIndicator(self):
        self.stackedWidget.setCurrentIndex(0)

    def closeClasses(self):
        self.stackedWidget.setCurrentIndex(0)

    def closeDisease(self):
        self.stackedWidget.setCurrentIndex(3)

    def closeSubdisease(self):
        self.stackedWidget.setCurrentIndex(4)

    def closeDiseaseInfo(self):
        self.stackedWidget.setCurrentIndex(5)

    def closeDiseaseExampleInfo(self):
        self.stackedWidget.setCurrentIndex(0)

    @QtCore.pyqtSlot(int)
    def openAnalyzesIndicators(self, index):
        self.stackedWidget.setCurrentIndex(1)
        self.pushButton_10.hide()
        self.Burger_3.clicked.connect(self.closeIndicators)
        self.Logo_3.setText(self.analyzes[index]['category'])
        self.loadIndicators(index)

    @QtCore.pyqtSlot(int)
    def openIndicator(self, index):
        self.stackedWidget.setCurrentIndex(2)
        self.pushButton_10.hide()
        if self.indicators[index]['title'] in self.favoriteAnalyzes:
            self.pushButton_13.setIcon(QtGui.QIcon('images/star-active.png'))
        else:
            self.pushButton_13.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_4.clicked.connect(self.closeIndicator)
        self.Logo_4.setText(self.indicators[index]['title'])
        self.loadIndicatorInfo(self.indicators[index])

    @QtCore.pyqtSlot(int)
    def openFavIndicator(self, index):
        self.stackedWidget.setCurrentIndex(2)
        self.pushButton_10.hide()
        self.pushButton_13.setIcon(QtGui.QIcon('images/star-active.png'))
        self.Burger_4.clicked.connect(self.closeFavIndicator)
        self.Logo_4.setText(self.favoritesList[index]['title'])
        self.loadIndicatorInfo(self.favoritesList[index])



    @QtCore.pyqtSlot(int)
    def openMkbSubclass(self, index):
        self.currentMkbIndex = index
        self.stackedWidget.setCurrentIndex(3)
        self.pushButton_10.hide()
        self.Burger_2.clicked.connect(self.closeClasses)
        self.Logo_2.setText(self.mkb[index]['class'].split('(')[0])

        self.loadMkbSubclasses(index)

    @QtCore.pyqtSlot(int)
    def openFedSubclass(self, index):
        self.currentFedIndex = index
        self.stackedWidget.setCurrentIndex(3)
        self.pushButton_10.hide()
        self.Burger_2.clicked.connect(self.closeClasses)
        self.Logo_2.setText(self.fed[index]['class'].split('(')[0])
        print(self.fed[index]['class'].split('(')[0])


    @QtCore.pyqtSlot(int)
    def openCodSubclass(self, index):
        self.currentCodIndex = index
        self.stackedWidget.setCurrentIndex(3)
        self.pushButton_10.hide()
        self.Burger_2.clicked.connect(self.closeClasses)
        self.Logo_2.setText(self.cod[index]['class'].split('(')[0])
        print(self.cod[index]['class'].split('(')[0])

    @QtCore.pyqtSlot(int)
    def openKliSubclass(self, index):
        self.currentKliIndex = index
        self.stackedWidget.setCurrentIndex(3)
        self.pushButton_10.hide()
        self.Burger_2.clicked.connect(self.closeClasses)
        self.Logo_2.setText(self.kli[index]['class'].split('(')[0])
        self.loadKliSubclasses(index)

    @QtCore.pyqtSlot(int)
    def openNomSubclass(self, index):
        self.currentNomKliIndex = index
        self.stackedWidget.setCurrentIndex(3)
        self.pushButton_10.hide()
        self.Burger_2.clicked.connect(self.closeClasses)
        self.Logo_2.setText(self.nom[index]['class'].split('(')[0])
        self.loadNomKliSubclasses(index)

    @QtCore.pyqtSlot(int)
    def openTnmSubclass(self, index):
        self.currentTnmIndex = index
        self.stackedWidget.setCurrentIndex(3)
        self.pushButton_10.hide()
        self.Burger_2.clicked.connect(self.closeClasses)
        self.Logo_2.setText(self.tnm[index]['class'].split('(')[0])
        self.loadTnmSubclasses(index)

    @QtCore.pyqtSlot(int)
    def openTohSubclass(self, index):
        self.currentTohIndex = index
        self.stackedWidget.setCurrentIndex(3)
        self.pushButton_10.hide()
        self.Burger_2.clicked.connect(self.closeClasses)
        self.Logo_2.setText(self.toh[index]['class'].split('(')[0])

        self.loadTohSubclasses(index)

    @QtCore.pyqtSlot(int)
    def openMasSubclass(self, index):
        self.currentMasIndex = index
        self.stackedWidget.setCurrentIndex(3)
        self.pushButton_10.hide()
        self.Burger_2.clicked.connect(self.closeClasses)
        self.Logo_2.setText(self.mas[index]['class'].split('(')[0])
        self.loadMasSubclasses(index)

    @QtCore.pyqtSlot(int)
    def openMkbDisease(self, index):
        self.currentMkbSubclassIndex = index
        self.stackedWidget.setCurrentIndex(4)
        self.pushButton_17.hide()
        self.Burger_5.clicked.connect(self.closeDisease)
        self.Logo_8.setText(self.subclassesMkb[self.currentMkbIndex][self.currentMkbSubclassIndex]['subtitle'])
        self.loadMkbDisease(index)

    @QtCore.pyqtSlot(int)
    def openCodDisease(self, index):
        self.currentCodSubclassIndex = index
        self.stackedWidget.setCurrentIndex(4)
        self.pushButton_17.hide()
        self.Burger_5.clicked.connect(self.closeDisease)
        self.Logo_8.setText(self.subclassesCod[self.currentCodIndex][self.currentCodSubclassIndex]['subtitle'])
        self.loadCodDisease(index)

    @QtCore.pyqtSlot(int)
    def openKliDisease(self, index):
        self.currentKliSubclassIndex = index
        self.stackedWidget.setCurrentIndex(4)
        self.pushButton_17.hide()
        self.Burger_5.clicked.connect(self.closeDisease)
        self.Logo_8.setText(self.subclassesKli[self.currentKliIndex][self.currentKliSubclassIndex]['subtitle'])
        self.loadKliDisease(index)

    @QtCore.pyqtSlot(int)
    def openNomDisease(self, index):
        self.currentNomSubclassIndex = index
        self.stackedWidget.setCurrentIndex(4)
        self.pushButton_17.hide()
        self.Burger_5.clicked.connect(self.closeDisease)
        self.Logo_8.setText(self.subclassesNom[self.currentNomIndex][self.currentNomSubclassIndex]['subtitle'])
        self.loadNomDisease(index)

    @QtCore.pyqtSlot(int)
    def openFedDisease(self, index):
        self.currentFedSubclassIndex = index
        self.stackedWidget.setCurrentIndex(4)
        self.pushButton_17.hide()
        self.Burger_5.clicked.connect(self.closeDisease)
        self.Logo_8.setText(self.subclassesFed[self.currentFedIndex][self.currentFedSubclassIndex]['subtitle'])
        self.loadFedDisease(index)

    @QtCore.pyqtSlot(int)
    def openTnmDisease(self, index):
        self.currentTnmSubclassIndex = index
        self.stackedWidget.setCurrentIndex(4)
        self.pushButton_17.hide()
        self.Burger_5.clicked.connect(self.closeDisease)
        self.Logo_8.setText(self.subclassesTnm[self.currentTnmIndex][self.currentTnmSubclassIndex]['subtitle'])
        self.loadTnmDisease(index)

    @QtCore.pyqtSlot(int)
    def openTohDisease(self, index):
        self.currentTohSubclassIndex = index
        self.stackedWidget.setCurrentIndex(4)
        self.pushButton_17.hide()
        self.Burger_5.clicked.connect(self.closeDisease)
        self.Logo_8.setText(self.subclassesToh[self.currentTohIndex][self.currentTohSubclassIndex]['subtitle'])
        self.loadTohDisease(index)

    @QtCore.pyqtSlot(int)
    def openMasDisease(self, index):
        self.currentMasSubclassIndex = index
        self.stackedWidget.setCurrentIndex(4)
        self.pushButton_17.hide()
        self.Burger_5.clicked.connect(self.closeDisease)
        self.Logo_8.setText(self.subclassesMas[self.currentMasIndex][self.currentMasSubclassIndex]['subtitle'])
        self.loadMasDisease(index)

    @QtCore.pyqtSlot(int)
    def openMkbSubdiaseDisease(self, index):
        self.currentMkbDiseaseIndex = index
        self.stackedWidget.setCurrentIndex(5)
        self.pushButton_22.hide()
        self.Burger_8.clicked.connect(self.closeSubdisease)
        title = self.subclassesMkb[self.currentMkbIndex][self.currentMkbSubclassIndex]['disease'][
                                self.currentMkbDiseaseIndex]['name']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_8.setText(title)
        self.loadMkbSubdisease(index)

    @QtCore.pyqtSlot(int)
    def openNomSubdiaseDisease(self, index):
        self.currentNomDiseaseIndex = index
        self.stackedWidget.setCurrentIndex(5)
        self.pushButton_22.hide()
        self.Burger_8.clicked.connect(self.closeSubdisease)
        title = self.subclassesNom[self.currentNomIndex][self.currentNomSubclassIndex]['disease'][
                                self.currentNomDiseaseIndex]['name']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_8.setText(title)
        self.loadNomSubdisease(index)

    @QtCore.pyqtSlot(int)
    def openKliSubdiaseDisease(self, index):
        self.currentKliDiseaseIndex = index
        self.stackedWidget.setCurrentIndex(5)
        self.pushButton_22.hide()
        self.Burger_8.clicked.connect(self.closeSubdisease)
        title = self.subclassesKli[self.currentKliIndex][self.currentKliSubclassIndex]['disease'][
                                self.currentKliDiseaseIndex]['name']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_8.setText(title)
        self.loadKliSubdisease(index)

    @QtCore.pyqtSlot(int)
    def openCodSubdiaseDisease(self, index):
        self.currentCodDiseaseIndex = index
        self.stackedWidget.setCurrentIndex(5)
        self.pushButton_22.hide()
        self.Burger_8.clicked.connect(self.closeSubdisease)
        title = self.subclassesCod[self.currentCodIndex][self.currentCodSubclassIndex]['disease'][
                                self.currentCodDiseaseIndex]['name']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_8.setText(title)
        self.loadCodSubdisease(index)

    @QtCore.pyqtSlot(int)
    def openFedSubdiaseDisease(self, index):
        self.currentFedDiseaseIndex = index
        self.stackedWidget.setCurrentIndex(5)
        self.pushButton_22.hide()
        self.Burger_8.clicked.connect(self.closeSubdisease)
        title = self.subclassesFed[self.currentFedIndex][self.currentFedSubclassIndex]['disease'][
                                self.currentFedDiseaseIndex]['name']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_8.setText(title)
        self.loadFedSubdisease(index)

    @QtCore.pyqtSlot(int)
    def openTnmSubdiaseDisease(self, index):
        self.currentTnmDiseaseIndex = index
        self.stackedWidget.setCurrentIndex(5)
        self.pushButton_22.hide()
        self.Burger_8.clicked.connect(self.closeSubdisease)
        title = self.subclassesTnm[self.currentTnmIndex][self.currentTnmSubclassIndex]['disease'][
                                self.currentTnmDiseaseIndex]['name']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_8.setText(title)
        self.loadTnmSubdisease(index)

    @QtCore.pyqtSlot(int)
    def openTohSubdiaseDisease(self, index):
        self.currentTohDiseaseIndex = index
        self.stackedWidget.setCurrentIndex(5)
        self.pushButton_22.hide()
        self.Burger_8.clicked.connect(self.closeSubdisease)
        title = self.subclassesToh[self.currentTohIndex][self.currentTohSubclassIndex]['disease'][
                                self.currentTohDiseaseIndex]['name']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_8.setText(title)
        self.loadTohSubdisease(index)

    @QtCore.pyqtSlot(int)
    def openMasSubdiaseDisease(self, index):
        self.currentMasDiseaseIndex = index
        self.stackedWidget.setCurrentIndex(5)
        self.pushButton_22.hide()
        self.Burger_8.clicked.connect(self.closeSubdisease)
        title = self.subclassesMas[self.currentMasIndex][self.currentMasSubclassIndex]['disease'][
                                self.currentMasDiseaseIndex]['name']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_8.setText(title)
        self.loadMasSubdisease(index)

    @QtCore.pyqtSlot(int)
    def openMkbDiseaseInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        if \
                self.subclassesMkb[self.currentMkbIndex][self.currentMkbSubclassIndex]['disease'][
                    self.currentMkbDiseaseIndex][
                    'types'][index]['typename'] in self.favoritesMkbList:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        else:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_7.clicked.connect(self.closeDiseaseInfo)
        title = \
            self.subclassesMkb[self.currentMkbIndex][self.currentMkbSubclassIndex]['disease'][
                self.currentMkbDiseaseIndex][
                'types'][index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)

        self.loadDiseasesInfo(self.subclassesMkb[self.currentMkbIndex][self.currentMkbSubclassIndex]['disease'][
                                  self.currentMkbDiseaseIndex]['types'][index])

    @QtCore.pyqtSlot(int)
    def openKliDiseaseInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        if \
                self.subclassesKli[self.currentKliIndex][self.currentKliSubclassIndex]['disease'][
                    self.currentKliDiseaseIndex][
                    'types'][index]['typename'] in self.favoritesKliList:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        else:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_7.clicked.connect(self.closeDiseaseInfo)
        title = \
            self.subclassesKli[self.currentKliIndex][self.currentKliSubclassIndex]['disease'][
                self.currentKliDiseaseIndex][
                'types'][index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo(self.subclassesKli[self.currentKliIndex][self.currentKliSubclassIndex]['disease'][
                                  self.currentKliDiseaseIndex]['types'][index])



    @QtCore.pyqtSlot(int)
    def openNomDiseaseInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        if \
                self.subclassesNom[self.currentNomIndex][self.currentNomSubclassIndex]['disease'][
                    self.currentNomDiseaseIndex][
                    'types'][index]['typename'] in self.favoritesNomList:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        else:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_7.clicked.connect(self.closeDiseaseInfo)
        title = \
            self.subclassesNom[self.currentNomIndex][self.currentNomSubclassIndex]['disease'][
                self.currentNomDiseaseIndex][
                'types'][index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo(self.subclassesNom[self.currentNomIndex][self.currentNomSubclassIndex]['disease'][
                                  self.currentNomDiseaseIndex]['types'][index])

    @QtCore.pyqtSlot(int)
    def openFedDiseaseInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        if \
                self.subclassesFed[self.currentFedIndex][self.currentFedSubclassIndex]['disease'][
                    self.currentFedDiseaseIndex][
                    'types'][index]['typename'] in self.favoritesFedList:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        else:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_7.clicked.connect(self.closeDiseaseInfo)
        title = \
            self.subclassesFed[self.currentFedIndex][self.currentFedSubclassIndex]['disease'][
                self.currentFedDiseaseIndex][
                'types'][index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo4(self.subclassesFed[self.currentFedIndex][self.currentFedSubclassIndex]['disease'][
                                  self.currentFedDiseaseIndex]['types'][index])

    @QtCore.pyqtSlot(int)
    def openMasDiseaseInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        if \
                self.subclassesMas[self.currentMasIndex][self.currentMasSubclassIndex]['disease'][
                    self.currentMasDiseaseIndex][
                    'types'][index]['typename'] in self.favoritesMasList:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        else:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_7.clicked.connect(self.closeDiseaseInfo)
        title = \
            self.subclassesMas[self.currentMasIndex][self.currentMasSubclassIndex]['disease'][
                self.currentMasDiseaseIndex][
                'types'][index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo1(self.subclassesMas[self.currentMasIndex][self.currentMasSubclassIndex]['disease'][
                                  self.currentMasDiseaseIndex]['types'][index])

    @QtCore.pyqtSlot(int)
    def openTnmDiseaseInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        if \
                self.subclassesTnm[self.currentTnmIndex][self.currentTnmSubclassIndex]['disease'][
                    self.currentTnmDiseaseIndex][
                    'types'][index]['typename'] in self.favoritesTnmList:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        else:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_7.clicked.connect(self.closeDiseaseInfo)
        title = \
            self.subclassesTnm[self.currentTnmIndex][self.currentTnmSubclassIndex]['disease'][
                self.currentTnmDiseaseIndex][
                'types'][index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo2(self.subclassesTnm[self.currentTnmIndex][self.currentTnmSubclassIndex]['disease'][
                                  self.currentTnmDiseaseIndex]['types'][index])

    @QtCore.pyqtSlot(int)
    def openTohDiseaseInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        if \
                self.subclassesToh[self.currentTohIndex][self.currentTohSubclassIndex]['disease'][
                    self.currentTohDiseaseIndex][
                    'types'][index]['typename'] in self.favoritesTohList:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        else:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_7.clicked.connect(self.closeDiseaseInfo)
        title = \
            self.subclassesToh[self.currentTohIndex][self.currentTohSubclassIndex]['disease'][
                self.currentTohDiseaseIndex][
                'types'][index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo3(self.subclassesToh[self.currentTohIndex][self.currentTohSubclassIndex]['disease'][
                                  self.currentTohDiseaseIndex]['types'][index])

    @QtCore.pyqtSlot(int)
    def openCodDiseaseInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        if \
                self.subclassesCod[self.currentCodIndex][self.currentCodSubclassIndex]['disease'][
                    self.currentCodDiseaseIndex][
                    'types'][index]['typename'] in self.favoritesTohList:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        else:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_7.clicked.connect(self.closeDiseaseInfo)
        title = \
            self.subclassesCod[self.currentCodIndex][self.currentCodSubclassIndex]['disease'][
                self.currentCodDiseaseIndex][
                'types'][index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo3(self.subclassesToh[self.currentCodIndex][self.currentCodSubclassIndex]['disease'][
                                  self.currentCodDiseaseIndex]['types'][index])

    @QtCore.pyqtSlot(int)
    def openFavMkbDiseaseInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        self.Burger_7.clicked.connect(self.closeFavIndicator)
        title = self.favoritesMkbList[index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo(self.favoritesMkbList[index])

    @QtCore.pyqtSlot(int)
    def openFavFedDiseaseInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        self.Burger_7.clicked.connect(self.closeFavIndicator)
        title = self.favoritesFedList[index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo4(self.favoritesFedList[index])

    @QtCore.pyqtSlot(int)
    def openFavMasDiseaseInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        self.Burger_7.clicked.connect(self.closeFavIndicator)
        title = self.favoritesMasList[index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo1(self.favoritesMasList[index])

    @QtCore.pyqtSlot(int)
    def openFavTnmDiseaseInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        self.Burger_7.clicked.connect(self.closeFavIndicator)
        title = self.favoritesTnmList[index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo2(self.favoritesTnmList[index])

    @QtCore.pyqtSlot(int)
    def openFavNomDiseaseInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        self.Burger_7.clicked.connect(self.closeFavIndicator)
        title = self.favoritesNomList[index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo2(self.favoritesNomList[index])

    @QtCore.pyqtSlot(int)
    def openFavTohDiseaseInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        self.Burger_7.clicked.connect(self.closeFavIndicator)
        title = self.favoritesTohList[index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo3(self.favoritesTohList[index])

    @QtCore.pyqtSlot(int)
    def openFavCodDiseaseInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        self.Burger_7.clicked.connect(self.closeFavIndicator)
        title = self.favoritesCodList[index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo3(self.favoritesCodList[index])

    @QtCore.pyqtSlot(int)
    def openFavKliDiseaseInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        self.Burger_7.clicked.connect(self.closeFavIndicator)
        title = self.favoritesKliList[index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo5(self.favoritesKliList[index])

    @QtCore.pyqtSlot(int)
    def openMkbExampleInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        try:
            if self.mkbListExample[index]['subcode'] == self.favoritesMkbList[index]['subcode']:
                self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        except KeyError as e:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_7.clicked.connect(self.closeDiseaseExampleInfo)
        title = self.mkbListExample[index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo(self.mkbListExample[index])

    @QtCore.pyqtSlot(int)
    def openTnmExampleInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        try:
            if self.tnmListExample[index]['subcode'] == self.favoritesTnmList[index]['subcode']:
                self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        except KeyError as e:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_7.clicked.connect(self.closeDiseaseExampleInfo)
        title = self.tnmListExample[index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo2(self.tnmListExample[index])

    @QtCore.pyqtSlot(int)
    def openTohExampleInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        try:
            if self.tohListExample[index]['subcode'] == self.favoritesTohList[index]['subcode']:
                self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        except KeyError as e:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_7.clicked.connect(self.closeDiseaseExampleInfo)
        title = self.tohListExample[index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo3(self.tohListExample[index])

    @QtCore.pyqtSlot(int)
    def openCodExampleInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        try:
            if self.codListExample[index]['subcode'] == self.favoritesCodList[index]['subcode']:
                self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        except KeyError as e:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_7.clicked.connect(self.closeDiseaseExampleInfo)
        title = self.codListExample[index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo3(self.codListExample[index])

    @QtCore.pyqtSlot(int)
    def openNomExampleInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        try:
            if self.nomListExample[index]['subcode'] == self.favoritesNomList[index]['subcode']:
                self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        except KeyError as e:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_7.clicked.connect(self.closeDiseaseExampleInfo)
        title = self.nomListExample[index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo6(self.nomListExample[index])

    @QtCore.pyqtSlot(int)
    def openFedExampleInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        try:
            if self.tohListExample[index]['subcode'] == self.favoritesTohList[index]['subcode']:
                self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        except KeyError as e:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_7.clicked.connect(self.closeDiseaseExampleInfo)
        title = self.fedListExample[index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo4(self.fedListExample[index])

    @QtCore.pyqtSlot(int)
    def openMasExampleInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        try:
            if self.masListExample[index]['subcode'] == self.favoritesMasList[index]['subcode']:
                self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        except KeyError as e:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_7.clicked.connect(self.closeDiseaseExampleInfo)
        title = self.masListExample[index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo1(self.masListExample[index])

    @QtCore.pyqtSlot(int)
    def openKliExampleInfo(self, index):
        self.stackedWidget.setCurrentIndex(6)
        self.pushButton_10.hide()
        try:
            if self.kliListExample[index]['subcode'] == self.favoritesKliList[index]['subcode']:
                self.pushButton_19.setIcon(QtGui.QIcon('images/star-active.png'))
        except KeyError as e:
            self.pushButton_19.setIcon(QtGui.QIcon('images/star.png'))
        self.Burger_7.clicked.connect(self.closeDiseaseExampleInfo)
        title = self.kliListExample[index]['typename']
        if len(title) > 32:
            title = title[:31] + '...'
        self.Logo_7.setText(title)
        self.loadDiseasesInfo5(self.kliListExample[index])


    def loadIndicators(self, index):
        self.clearWidget(self.ScrollAreaFrame_4)
        for i in range(len(self.analyzes[index]['indicators'])):
            listItem = listBtnAnalyzes(self.analyzes[index]['indicators'][i]['title'], 14 + self.deltaFontSize)
            if self.analyzes[index]['indicators'][i]['title'] not in self.indicators:
                self.indicators.append(self.analyzes[index]['indicators'][i])
                listItem.clicked.connect(self.indicateMap.map)
                self.indicateMap.setMapping(listItem, len(self.indicators) - 1)
            else:
                listItem.clicked.connect(self.indicateMap.map)
                self.indicateMap.setMapping(listItem,
                                            self.indicators.index(self.analyzes[index]['indicators'][i]['title']))

            listItem.clicked.connect(self.indicateMap.map)
            self.indicateMap.setMapping(listItem, len(self.indicators) - 1)

            self.ScrollAreaFrame_4.layout().addWidget(listItem)

        self.indicateMap.mapped.connect(self.openIndicator)

    def loadAnalyzes(self):
        self.clearWidget(self.ScrollAreaFrame_2)
        self.analyzesWidget.clear()
        for index in range(len(self.analyzes)):
            listItem = listBtnAnalyzes(self.analyzes[index]['category'], 14 + self.deltaFontSize)

            listItem.clicked.connect(self.analizMap.map)
            self.analizMap.setMapping(listItem, index)

            self.ScrollAreaFrame_2.layout().addWidget(listItem)
            self.analyzesWidget.append(listItem)

        self.analizMap.mapped.connect(self.openAnalyzesIndicators)

    def loadMkbSubdisease(self, index):
        self.clearWidget(self.ScrollAreaFrame_8)
        self.mkbSubdiseaseWidget.clear()
        self.subdiseaseMkbMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesMkb[self.currentMkbIndex][self.currentMkbSubclassIndex]['disease'][
                               self.currentMkbDiseaseIndex]['types'])):
            listItem = listBtnMkb(self.subclassesMkb[self.currentMkbIndex][self.currentMkbSubclassIndex]['disease'][
                                      self.currentMkbDiseaseIndex]['types'][i]['subcode'],
                                  self.subclassesMkb[self.currentMkbIndex][self.currentMkbSubclassIndex]['disease'][
                                      self.currentMkbDiseaseIndex]['types'][i]['typename'],
                                  18 + self.deltaFontSize)

            listItem.clicked.connect(self.subdiseaseMkbMap.map)
            self.subdiseaseMkbMap.setMapping(listItem, i)

            self.ScrollAreaFrame_8.layout().addWidget(listItem)
            self.mkbSubclassesWidget.append(listItem)

        self.subdiseaseMkbMap.mapped.connect(self.openMkbDiseaseInfo)

    def loadFedSubdisease(self, index):
        self.clearWidget(self.ScrollAreaFrame_8)
        self.fedSubdiseaseWidget.clear()
        self.subdiseaseFedMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesFed[self.currentFedIndex][self.currentFedSubclassIndex]['disease'][
                               self.currentFedDiseaseIndex]['types'])):
            listItem = listBtnMkb(self.subclassesFed[self.currentFedIndex][self.currentFedSubclassIndex]['disease'][
                                      self.currentFedDiseaseIndex]['types'][i]['subcode'],
                                  self.subclassesFed[self.currentFedIndex][self.currentFedSubclassIndex]['disease'][
                                      self.currentFedDiseaseIndex]['types'][i]['typename'],
                                  18 + self.deltaFontSize)

            listItem.clicked.connect(self.subdiseaseFedMap.map)
            self.subdiseaseFedMap.setMapping(listItem, i)

            self.ScrollAreaFrame_8.layout().addWidget(listItem)
            self.fedSubclassesWidget.append(listItem)

        self.subdiseaseFedMap.mapped.connect(self.openFedDiseaseInfo)

    def loadMasSubdisease(self, index):
        self.clearWidget(self.ScrollAreaFrame_8)
        self.masSubdiseaseWidget.clear()
        self.subdiseaseMasMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesMas[self.currentMasIndex][self.currentMasSubclassIndex]['disease'][
                               self.currentMasDiseaseIndex]['types'])):
            listItem = listBtnMas(self.subclassesMas[self.currentMasIndex][self.currentMasSubclassIndex]['disease'][
                                      self.currentMasDiseaseIndex]['types'][i]['subcode'],
                                  self.subclassesMas[self.currentMasIndex][self.currentMasSubclassIndex]['disease'][
                                      self.currentMasDiseaseIndex]['types'][i]['typename'],
                                  18 + self.deltaFontSize)

            listItem.clicked.connect(self.subdiseaseMasMap.map)
            self.subdiseaseMasMap.setMapping(listItem, i)

            self.ScrollAreaFrame_8.layout().addWidget(listItem)
            self.masSubclassesWidget.append(listItem)

        self.subdiseaseMasMap.mapped.connect(self.openMasDiseaseInfo)

    def loadNomSubdisease(self, index):
        self.clearWidget(self.ScrollAreaFrame_8)
        self.nomSubdiseaseWidget.clear()
        self.subdiseaseNomMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesNom[self.currentNomIndex][self.currentNomSubclassIndex]['disease'][
                               self.currentNomDiseaseIndex]['types'])):
            listItem = listBtnMas(self.subclassesNom[self.currentNomIndex][self.currentNomSubclassIndex]['disease'][
                                      self.currentNomDiseaseIndex]['types'][i]['subcode'],
                                  self.subclassesMas[self.currentMasIndex][self.currentNomSubclassIndex]['disease'][
                                      self.currentNomDiseaseIndex]['types'][i]['typename'],
                                  18 + self.deltaFontSize)

            listItem.clicked.connect(self.subdiseaseNomMap.map)
            self.subdiseaseNomMap.setMapping(listItem, i)

            self.ScrollAreaFrame_8.layout().addWidget(listItem)
            self.nomSubclassesWidget.append(listItem)

        self.subdiseaseNomMap.mapped.connect(self.openNomDiseaseInfo)

    def loadTnmSubdisease(self, index):
        self.clearWidget(self.ScrollAreaFrame_8)
        self.tnmSubdiseaseWidget.clear()
        self.subdiseaseTnmMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesTnm[self.currentTnmIndex][self.currentTnmSubclassIndex]['disease'][
                               self.currentTnmDiseaseIndex]['types'])):
            listItem = listBtnTnm(self.subclassesTnm[self.currentTnmIndex][self.currentTnmSubclassIndex]['disease'][
                                      self.currentTnmDiseaseIndex]['types'][i]['subcode'],
                                  self.subclassesTnm[self.currentTnmIndex][self.currentTnmSubclassIndex]['disease'][
                                      self.currentTnmDiseaseIndex]['types'][i]['typename'],
                                  18 + self.deltaFontSize)

            listItem.clicked.connect(self.subdiseaseTnmMap.map)
            self.subdiseaseTnmMap.setMapping(listItem, i)

            self.ScrollAreaFrame_8.layout().addWidget(listItem)
            self.tnmSubclassesWidget.append(listItem)

        self.subdiseaseTnmMap.mapped.connect(self.openTnmDiseaseInfo)

    def loadKliSubdisease(self, index):
        self.clearWidget(self.ScrollAreaFrame_8)
        self.kliSubdiseaseWidget.clear()
        self.subdiseaseKliMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesKli[self.currentKliIndex][self.currentKliSubclassIndex]['disease'][
                               self.currentKliDiseaseIndex]['types'])):
            listItem = listBtnKli(self.subclassesKli[self.currentKliIndex][self.currentKliSubclassIndex]['disease'][
                                      self.currentKliDiseaseIndex]['types'][i]['subcode'],
                                  self.subclassesKli[self.currentKliIndex][self.currentKliSubclassIndex]['disease'][
                                      self.currentKliDiseaseIndex]['types'][i]['typename'],
                                  18 + self.deltaFontSize)

            listItem.clicked.connect(self.subdiseaseKliMap.map)
            self.subdiseaseKliMap.setMapping(listItem, i)

            self.ScrollAreaFrame_8.layout().addWidget(listItem)
            self.kliSubclassesWidget.append(listItem)

        self.subdiseaseKliMap.mapped.connect(self.openKliDiseaseInfo)

    def loadTohSubdisease(self, index):
        self.clearWidget(self.ScrollAreaFrame_8)
        self.tohSubdiseaseWidget.clear()
        self.subdiseaseTohMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesToh[self.currentTohIndex][self.currentTohSubclassIndex]['disease'][
                               self.currentTohDiseaseIndex]['types'])):
            listItem = listBtnTnm(self.subclassesToh[self.currentTohIndex][self.currentTohSubclassIndex]['disease'][
                                      self.currentTohDiseaseIndex]['types'][i]['subcode'],
                                  self.subclassesToh[self.currentTohIndex][self.currentTohSubclassIndex]['disease'][
                                      self.currentTohDiseaseIndex]['types'][i]['typename'],
                                  18 + self.deltaFontSize)

            listItem.clicked.connect(self.subdiseaseTohMap.map)
            self.subdiseaseTohMap.setMapping(listItem, i)

            self.ScrollAreaFrame_8.layout().addWidget(listItem)
            self.tohSubclassesWidget.append(listItem)

        self.subdiseaseTohMap.mapped.connect(self.openTohDiseaseInfo)

    def loadCodSubdisease(self, index):
        self.clearWidget(self.ScrollAreaFrame_8)
        self.codSubdiseaseWidget.clear()
        self.subdiseaseCodMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesToh[self.currentTohIndex][self.currentCodSubclassIndex]['disease'][
                               self.currentCodDiseaseIndex]['types'])):
            listItem = listBtnTnm(self.subclassesCod[self.currentCodIndex][self.currentCodSubclassIndex]['disease'][
                                      self.currentTohDiseaseIndex]['types'][i]['subcode'],
                                  self.subclassesCod[self.currentCodIndex][self.currentCodSubclassIndex]['disease'][
                                      self.currentTohDiseaseIndex]['types'][i]['typename'],
                                  18 + self.deltaFontSize)

            listItem.clicked.connect(self.subdiseaseCodMap.map)
            self.subdiseaseCodMap.setMapping(listItem, i)

            self.ScrollAreaFrame_8.layout().addWidget(listItem)
            self.codSubclassesWidget.append(listItem)

        self.subdiseaseCodMap.mapped.connect(self.openCodDiseaseInfo)

    def loadMkbDisease(self, index):
        self.clearWidget(self.ScrollAreaFrame_6)
        self.mkbDiseaseWidget.clear()
        self.diseaseMkbMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesMkb[self.currentMkbIndex][self.currentMkbSubclassIndex]['disease'])):
            listItem = listBtnMkb(
                self.subclassesMkb[self.currentMkbIndex][self.currentMkbSubclassIndex]['disease'][i]['code'],
                self.subclassesMkb[self.currentMkbIndex][self.currentMkbSubclassIndex]['disease'][i]['name'],
                18 + self.deltaFontSize)

            listItem.clicked.connect(self.diseaseMkbMap.map)
            self.diseaseMkbMap.setMapping(listItem, i)

            self.ScrollAreaFrame_6.layout().addWidget(listItem)
            self.mkbSubclassesWidget.append(listItem)

        self.diseaseMkbMap.mapped.connect(self.openMkbSubdiaseDisease)

    def loadFedDisease(self, index):
        self.clearWidget(self.ScrollAreaFrame_6)
        self.fedDiseaseWidget.clear()
        self.diseaseFedMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesFed[self.currentFedIndex][self.currentFedSubclassIndex]['disease'])):
            listItem = listBtnFed(
                self.subclassesFed[self.currentFedIndex][self.currentFedSubclassIndex]['disease'][i]['code'],
                self.subclassesFed[self.currentFedIndex][self.currentFedSubclassIndex]['disease'][i]['name'],
                18 + self.deltaFontSize)

            listItem.clicked.connect(self.diseaseFedMap.map)
            self.diseaseFedMap.setMapping(listItem, i)

            self.ScrollAreaFrame_6.layout().addWidget(listItem)
            self.fedSubclassesWidget.append(listItem)

        self.diseaseFedMap.mapped.connect(self.openFedSubdiaseDisease)

    def loadMasDisease(self, index):
        self.clearWidget(self.ScrollAreaFrame_6)
        self.masDiseaseWidget.clear()
        self.diseaseMasMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesMas[self.currentMasIndex][self.currentMasSubclassIndex]['disease'])):
            listItem = listBtnMas(
                self.subclassesMas[self.currentMasIndex][self.currentMasSubclassIndex]['disease'][i]['code'],
                self.subclassesMas[self.currentMasIndex][self.currentMasSubclassIndex]['disease'][i]['name'],
                18 + self.deltaFontSize)

            listItem.clicked.connect(self.diseaseMasMap.map)
            self.diseaseMasMap.setMapping(listItem, i)

            self.ScrollAreaFrame_6.layout().addWidget(listItem)
            self.masSubclassesWidget.append(listItem)

        self.diseaseMasMap.mapped.connect(self.openMasSubdiaseDisease)

    def loadKliDisease(self, index):
        self.clearWidget(self.ScrollAreaFrame_6)
        self.kliDiseaseWidget.clear()
        self.diseaseKliMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesKli[self.currentKliIndex][self.currentKliSubclassIndex]['disease'])):
            listItem = listBtnKli(
                self.subclassesKli[self.currentKliIndex][self.currentKliSubclassIndex]['disease'][i]['code'],
                self.subclassesKli[self.currentKliIndex][self.currentKliSubclassIndex]['disease'][i]['name'],
                18 + self.deltaFontSize)

            listItem.clicked.connect(self.diseaseKliMap.map)
            self.diseaseKliMap.setMapping(listItem, i)

            self.ScrollAreaFrame_6.layout().addWidget(listItem)
            self.kliSubclassesWidget.append(listItem)

        self.diseaseKliMap.mapped.connect(self.openKliSubdiaseDisease)

    def loadTnmDisease(self, index):
        self.clearWidget(self.ScrollAreaFrame_6)
        self.tnmDiseaseWidget.clear()
        self.diseaseTnmMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesTnm[self.currentTnmIndex][self.currentTnmSubclassIndex]['disease'])):
            listItem = listBtnTnm(
                self.subclassesTnm[self.currentTnmIndex][self.currentTnmSubclassIndex]['disease'][i]['code'],
                self.subclassesTnm[self.currentTnmIndex][self.currentTnmSubclassIndex]['disease'][i]['name'],
                18 + self.deltaFontSize)

            listItem.clicked.connect(self.diseaseTnmMap.map)
            self.diseaseTnmMap.setMapping(listItem, i)

            self.ScrollAreaFrame_6.layout().addWidget(listItem)
            self.tnmSubclassesWidget.append(listItem)

        self.diseaseTnmMap.mapped.connect(self.openTnmSubdiaseDisease)

    def loadTohDisease(self, index):
        self.clearWidget(self.ScrollAreaFrame_6)
        self.tohDiseaseWidget.clear()
        self.diseaseTohMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesToh[self.currentTohIndex][self.currentTohSubclassIndex]['disease'])):
            listItem = listBtnToh(
                self.subclassesToh[self.currentTohIndex][self.currentTohSubclassIndex]['disease'][i]['code'],
                self.subclassesToh[self.currentTohIndex][self.currentTohSubclassIndex]['disease'][i]['name'],
                18 + self.deltaFontSize)

            listItem.clicked.connect(self.diseaseTohMap.map)
            self.diseaseTohMap.setMapping(listItem, i)

            self.ScrollAreaFrame_6.layout().addWidget(listItem)
            self.tohSubclassesWidget.append(listItem)

        self.diseaseTohMap.mapped.connect(self.openTohSubdiaseDisease)

    def loadCodDisease(self, index):
        self.clearWidget(self.ScrollAreaFrame_6)
        self.codDiseaseWidget.clear()
        self.diseaseCodMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesCod[self.currentCodIndex][self.currentCodSubclassIndex]['disease'])):
            listItem = listBtnToh(
                self.subclassesCod[self.currentCodIndex][self.currentCodSubclassIndex]['disease'][i]['code'],
                self.subclassesCod[self.currentCodIndex][self.currentCodSubclassIndex]['disease'][i]['name'],
                18 + self.deltaFontSize)

            listItem.clicked.connect(self.diseaseCodMap.map)
            self.diseaseCodMap.setMapping(listItem, i)

            self.ScrollAreaFrame_6.layout().addWidget(listItem)
            self.codSubclassesWidget.append(listItem)

        self.diseaseCodMap.mapped.connect(self.openCodSubdiaseDisease)

    def loadNomDisease(self, index):
        self.clearWidget(self.ScrollAreaFrame_6)
        self.nomDiseaseWidget.clear()
        self.diseaseNomMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesNom[self.currentNomIndex][self.currentNomSubclassIndex]['disease'])):
            listItem = listBtnToh(
                self.subclassesNom[self.currentNomIndex][self.currentNomSubclassIndex]['disease'][i]['code'],
                self.subclassesNom[self.currentNomIndex][self.currentNomSubclassIndex]['disease'][i]['name'],
                18 + self.deltaFontSize)

            listItem.clicked.connect(self.diseaseNomMap.map)
            self.diseaseNomMap.setMapping(listItem, i)

            self.ScrollAreaFrame_6.layout().addWidget(listItem)
            self.nomSubclassesWidget.append(listItem)

        self.diseaseNomMap.mapped.connect(self.openNomSubdiaseDisease)

        def loadCodDisease(self, index):
            self.clearWidget(self.ScrollAreaFrame_6)
            self.codDiseaseWidget.clear()
            self.diseaseCodMap = QtCore.QSignalMapper(self)
            for i in range(len(self.subclassesCod[self.currentCodIndex][self.currentCodSubclassIndex]['disease'])):
                listItem = listBtnToh(
                    self.subclassesCod[self.currentCodIndex][self.currentCodSubclassIndex]['disease'][i]['code'],
                    self.subclassesCod[self.currentCodIndex][self.currentCodSubclassIndex]['disease'][i]['name'],
                    18 + self.deltaFontSize)

                listItem.clicked.connect(self.diseaseCodMap.map)
                self.diseaseCodMap.setMapping(listItem, i)

                self.ScrollAreaFrame_6.layout().addWidget(listItem)
                self.nomSubclassesWidget.append(listItem)

            self.diseaseCodMap.mapped.connect(self.openCodSubdiaseDisease)

    def loadMkbSubclasses(self, index):
        self.clearWidget(self.ScrollAreaFrame_3)
        self.mkbSubclassesWidget.clear()
        self.subclassMkbMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesMkb[index])):
            listItem = listBtnMkb(self.subclassesMkb[index][i]['subclass'], self.subclassesMkb[index][i]['subtitle'],
                                  18 + self.deltaFontSize)

            listItem.clicked.connect(self.subclassMkbMap.map)
            self.subclassMkbMap.setMapping(listItem, i)

            self.ScrollAreaFrame_3.layout().addWidget(listItem)
            self.mkbSubclassesWidget.append(listItem)

        self.subclassMkbMap.mapped.connect(self.openMkbDisease)

    def loadKliSubclasses(self, index):
        self.clearWidget(self.ScrollAreaFrame_3)
        self.kliSubclassesWidget.clear()
        self.subclassKliMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesKli[index])):
            listItem = listBtnKli(self.subclassesKli[index][i]['subclass'], self.subclassesKli[index][i]['subtitle'],
                                  18 + self.deltaFontSize)

            listItem.clicked.connect(self.subclassKliMap.map)
            self.subclassKliMap.setMapping(listItem, i)

            self.ScrollAreaFrame_3.layout().addWidget(listItem)
            self.kliSubclassesWidget.append(listItem)

        self.subclassKliMap.mapped.connect(self.openKliDisease)

    def loadCodSubclasses(self, index):
        self.clearWidget(self.ScrollAreaFrame_3)
        self.kliSubclassesWidget.clear()
        self.subclassCodMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesCod[index])):
            listItem = listBtnKli(self.subclassesCod[index][i]['subclass'], self.subclassesCod[index][i]['subtitle'],
                                  18 + self.deltaFontSize)

            listItem.clicked.connect(self.subclassCodMap.map)
            self.subclassCodMap.setMapping(listItem, i)

            self.ScrollAreaFrame_3.layout().addWidget(listItem)
            self.codSubclassesWidget.append(listItem)

        self.subclassCodMap.mapped.connect(self.openCodDisease)

    def loadNomSubclasses(self, index):
        self.clearWidget(self.ScrollAreaFrame_3)
        self.nomSubclassesWidget.clear()
        self.subclassNomMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesNom[index])):
            listItem = listBtnKli(self.subclassesNom[index][i]['subclass'], self.subclassesNom[index][i]['subtitle'],
                                  18 + self.deltaFontSize)

            listItem.clicked.connect(self.subclassNomMap.map)
            self.subclassNomMap.setMapping(listItem, i)

            self.ScrollAreaFrame_3.layout().addWidget(listItem)
            self.nomSubclassesWidget.append(listItem)

        self.subclassNomMap.mapped.connect(self.openNomDisease)

    def loadFedSubclasses(self, index):
        self.clearWidget(self.ScrollAreaFrame_3)
        self.fedSubclassesWidget.clear()
        self.subclassFedMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesFed[index])):
            listItem = listBtnFed(self.subclassesFed[index][i]['subclass'], self.subclassesFed[index][i]['subtitle'],
                                  18 + self.deltaFontSize)

            listItem.clicked.connect(self.subclassFedMap.map)
            self.subclassFedMap.setMapping(listItem, i)

            self.ScrollAreaFrame_3.layout().addWidget(listItem)
            self.fedSubclassesWidget.append(listItem)

        self.subclassFedMap.mapped.connect(self.openFedDisease)

    def loadMasSubclasses(self, index):
        self.clearWidget(self.ScrollAreaFrame_3)
        self.masSubclassesWidget.clear()
        self.subclassMasMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesMas[index])):
            listItem = listBtnMas(self.subclassesMas[index][i]['subclass'], self.subclassesMas[index][i]['subtitle'],
                                  18 + self.deltaFontSize)

            listItem.clicked.connect(self.subclassMasMap.map)
            self.subclassMasMap.setMapping(listItem, i)

            self.ScrollAreaFrame_3.layout().addWidget(listItem)
            self.masSubclassesWidget.append(listItem)

        self.subclassMasMap.mapped.connect(self.openMasDisease)

    def loadTnmSubclasses(self, index):
        self.clearWidget(self.ScrollAreaFrame_3)
        self.tnmSubclassesWidget.clear()
        self.subclassTnmMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesTnm[index])):
            listItem = listBtnTnm(self.subclassesTnm[index][i]['subclass'], self.subclassesTnm[index][i]['subtitle'],
                                  18 + self.deltaFontSize)

            listItem.clicked.connect(self.subclassTnmMap.map)
            self.subclassTnmMap.setMapping(listItem, i)

            self.ScrollAreaFrame_3.layout().addWidget(listItem)
            self.tnmSubclassesWidget.append(listItem)

        self.subclassTnmMap.mapped.connect(self.openTnmDisease)

    def loadTohSubclasses(self, index):
        self.clearWidget(self.ScrollAreaFrame_3)
        self.tohSubclassesWidget.clear()
        self.subclassTohMap = QtCore.QSignalMapper(self)
        for i in range(len(self.subclassesToh[index])):
            listItem = listBtnToh(self.subclassesToh[index][i]['subclass'], self.subclassesToh[index][i]['subtitle'],
                                  18 + self.deltaFontSize)

            listItem.clicked.connect(self.subclassTohMap.map)
            self.subclassTohMap.setMapping(listItem, i)

            self.ScrollAreaFrame_3.layout().addWidget(listItem)
            self.tohSubclassesWidget.append(listItem)

        self.subclassTohMap.mapped.connect(self.openTohDisease)

    def loadMkb(self):
        self.clearWidget(self.ScrollAreaFrame)
        self.mkbWidget.clear()
        for index in range(len(self.mkb)):
            listItem = listBtnMkb(self.mkb[index]['class'], self.mkb[index]['title'], 18 + self.deltaFontSize)

            listItem.clicked.connect(self.mkbMap.map)
            self.mkbMap.setMapping(listItem, index)

            self.ScrollAreaFrame.layout().addWidget(listItem)
            self.mkbWidget.append(listItem)

        self.mkbMap.mapped.connect(self.openMkbSubclass)

    def loadKli(self):
        self.clearWidget(self.ScrollAreaFrame)
        self.kliWidget.clear()
        for index in range(len(self.kli)):
            listItem = listBtnKli(self.kli[index]['class'], self.kli[index]['title'], 18 + self.deltaFontSize)

            listItem.clicked.connect(self.kliMap.map)
            self.kliMap.setMapping(listItem, index)

            self.ScrollAreaFrame.layout().addWidget(listItem)
            self.kliWidget.append(listItem)

        self.kliMap.mapped.connect(self.openKliSubclass)

    def loadMas(self):
        self.clearWidget(self.ScrollAreaFrame)
        self.masWidget.clear()
        for index in range(len(self.mas)):
            listItem = listBtnMas(self.mas[index]['class'], self.mas[index]['title'], 18 + self.deltaFontSize)

            listItem.clicked.connect(self.masMap.map)
            self.masMap.setMapping(listItem, index)

            self.ScrollAreaFrame.layout().addWidget(listItem)
            self.masWidget.append(listItem)

        self.masMap.mapped.connect(self.openMasSubclass)

    def loadCod(self):
        self.clearWidget(self.ScrollAreaFrame)
        self.codWidget.clear()
        for index in range(len(self.cod)):
            listItem = listBtnCod(self.cod[index]['class'], self.cod[index]['title'], 18 + self.deltaFontSize)

            listItem.clicked.connect(self.codMap.map)
            self.codMap.setMapping(listItem, index)

            self.ScrollAreaFrame.layout().addWidget(listItem)
            self.codWidget.append(listItem)

        self.codMap.mapped.connect(self.openCodSubclass)

    def loadFed(self):
        self.clearWidget(self.ScrollAreaFrame)
        self.fedWidget.clear()
        for index in range(len(self.fed)):
            listItem = listBtnFed(self.fed[index]['class'], self.fed[index]['title'], 18 + self.deltaFontSize)

            listItem.clicked.connect(self.fedMap.map)
            self.fedMap.setMapping(listItem, index)

            self.ScrollAreaFrame.layout().addWidget(listItem)
            self.fedWidget.append(listItem)

        self.fedMap.mapped.connect(self.openFedSubclass)

    def loadNom(self):
        self.clearWidget(self.ScrollAreaFrame)
        self.nomWidget.clear()
        for index in range(len(self.nom)):
            listItem = listBtnNom(self.nom[index]['class'], self.nom[index]['title'], 18 + self.deltaFontSize)

            listItem.clicked.connect(self.nomMap.map)
            self.nomMap.setMapping(listItem, index)

            self.ScrollAreaFrame.layout().addWidget(listItem)
            self.nomWidget.append(listItem)

        self.fedMap.mapped.connect(self.openNomSubclass)

    def loadTnm(self):
        self.clearWidget(self.ScrollAreaFrame)
        self.tnmWidget.clear()
        for index in range(len(self.tnm)):
            listItem = listBtnTnm(self.tnm[index]['class'], self.tnm[index]['title'], 18 + self.deltaFontSize)

            listItem.clicked.connect(self.tnmMap.map)
            self.tnmMap.setMapping(listItem, index)

            self.ScrollAreaFrame.layout().addWidget(listItem)
            self.tnmWidget.append(listItem)

        self.tnmMap.mapped.connect(self.openTnmSubclass)

    def loadToh(self):
        self.clearWidget(self.ScrollAreaFrame)
        self.tohWidget.clear()
        for index in range(len(self.toh)):
            listItem = listBtnToh(self.toh[index]['class'], self.toh[index]['title'], 18 + self.deltaFontSize)

            listItem.clicked.connect(self.tohMap.map)
            self.tohMap.setMapping(listItem, index)

            self.ScrollAreaFrame.layout().addWidget(listItem)
            self.tohWidget.append(listItem)

        self.tohMap.mapped.connect(self.openTohSubclass)

    def clearWidget(self, parent):
        widgets = parent.layout().count()
        for i in range(widgets):
            widget = parent.layout().itemAt(0).widget()
            parent.layout().removeWidget(widget)
            widget.hide()

    def loadIndicatorInfo(self, data):
        self.currentIndicator = data
        try:
            self.label_8.setText(data['standard'])
            self.clearWidget(self.frame_37)
            self.createSubtitleIndicator(data['title'])
            for text in data['description']:
                if text[0:3] == 'zZ ':
                    self.createSubtitleIndicator(text[3:])
                else:
                    self.createInfoIndicator(text)
        except KeyError:
            try:
                self.label_8.setText("Анализы")
                self.clearWidget(self.frame_37)
                self.createSubtitleIndicator(data['title'])
            except KeyError:
                self.label_8.setText("Анализы")
                for text in data['description']:
                    if text[0:3] == 'zZ ':
                        self.createSubtitleIndicator(text[3:])
                    else:
                        self.createInfoIndicator(text)
    def loadDiseasesInfo(self, data):
        try:
            self.label_36.setText(data['subtitle'])
            self.label_38.setText(data['name'])
            self.label_44.setText(data['subcode'])
            self.label_42.setText(data['typename'])
        except KeyError as e:
            data['subtitle'] = self.subclassesMkb[self.currentMkbIndex][self.currentMkbSubclassIndex]['subtitle']
            data['name'] = self.subclassesMkb[self.currentMkbIndex][self.currentMkbSubclassIndex]['disease'][
                self.currentMkbDiseaseIndex]['name']
            self.label_44.setText(data['subcode'])
            self.label_42.setText(data['typename'])
        self.currentDisease = data

    def loadDiseasesInfo1(self, data):
        try:
            self.label_36.setText(data['subtitle'])
            self.label_38.setText(data['name'])
            self.label_44.setText(data['subcode'])
            self.label_42.setText(data['typename'])
        except KeyError as e:
            data['subtitle'] = self.subclassesMas[self.currentMasIndex][self.currentMasSubclassIndex]['subtitle']
            data['name'] = self.subclassesMas[self.currentMasIndex][self.currentMasSubclassIndex]['disease'][
                self.currentMasDiseaseIndex]['name']
            self.label_44.setText(data['subcode'])
            self.label_42.setText(data['typename'])
        self.currentDisease = data

    def loadDiseasesInfo2(self, data):
        try:
            self.label_36.setText(data['subtitle'])
            self.label_38.setText(data['name'])
            self.label_44.setText(data['subcode'])
            self.label_42.setText(data['typename'])
        except KeyError as e:
            data['subtitle'] = self.subclassesTnm[self.currentTnmIndex][self.currentTnmSubclassIndex]['subtitle']
            data['name'] = self.subclassesTnm[self.currentTnmIndex][self.currentTnmSubclassIndex]['disease'][
                self.currentTnmDiseaseIndex]['name']
            self.label_44.setText(data['subcode'])
            self.label_42.setText(data['typename'])
        self.currentDisease = data

    def loadDiseasesInfo3(self, data):
        try:
            self.label_36.setText(data['subtitle'])
            self.label_38.setText(data['name'])
            self.label_44.setText(data['subcode'])
            self.label_42.setText(data['typename'])
        except KeyError as e:
            data['subtitle'] = self.subclassesToh[self.currentTohIndex][self.currentTohSubclassIndex]['subtitle']
            data['name'] = self.subclassesToh[self.currentTohIndex][self.currentTohSubclassIndex]['disease'][
                self.currentTohDiseaseIndex]['name']
            self.label_44.setText(data['subcode'])
            self.label_42.setText(data['typename'])
        self.currentDisease = data

    def loadDiseasesInfo4(self, data):
        try:
            self.label_36.setText(data['subtitle'])
            self.label_38.setText(data['name'])
            self.label_44.setText(data['subcode'])
            self.label_42.setText(data['typename'])
        except KeyError as e:
            data['subtitle'] = self.subclassesFed[self.currentFedIndex][self.currentFedSubclassIndex]['subtitle']
            data['name'] = self.subclassesFed[self.currentFedIndex][self.currentFedSubclassIndex]['disease'][
                self.currentFedDiseaseIndex]['name']
            self.label_44.setText(data['subcode'])
            self.label_42.setText(data['typename'])
        self.currentDisease = data

    def loadDiseasesInfo5(self, data):
        try:
            self.label_36.setText(data['subtitle'])
            self.label_38.setText(data['name'])
            self.label_44.setText(data['subcode'])
            self.label_42.setText(data['typename'])
        except KeyError as e:
            data['subtitle'] = self.subclassesKli[self.currentKliIndex][self.currentKliSubclassIndex]['subtitle']
            data['name'] = self.subclassesKli[self.currentKliIndex][self.currentKliSubclassIndex]['disease'][
                self.currentKliDiseaseIndex]['name']
            self.label_44.setText(data['subcode'])
            self.label_42.setText(data['typename'])
        self.currentDisease = data

    def loadDiseasesInfo5(self, data):
        try:
            self.label_36.setText(data['subtitle'])
            self.label_38.setText(data['name'])
            self.label_44.setText(data['subcode'])
            self.label_42.setText(data['typename'])
        except KeyError as e:
            data['subtitle'] = self.subclassesNom[self.currentNomIndex][self.currentNomSubclassIndex]['subtitle']
            data['name'] = self.subclassesKli[self.currentNomIndex][self.currentNomSubclassIndex]['disease'][
                self.currentNomDiseaseIndex]['name']
            self.label_44.setText(data['subcode'])
            self.label_42.setText(data['typename'])
        self.currentDisease = data

    def createSubtitleIndicator(self, subtitle):
        frame_42 = QFrame()
        frame_42.setFrameShape(QFrame.StyledPanel)
        frame_42.setFrameShadow(QFrame.Raised)
        horizontalLayout_38 = QHBoxLayout(frame_42)
        horizontalLayout_38.setContentsMargins(65, 25, 0, 0)
        horizontalLayout_38.setSpacing(0)
        horizontalLayout_38.setObjectName("horizontalLayout_38")
        label_7 = QLabel(frame_42)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        label_7.setFont(font)
        horizontalLayout_38.addWidget(label_7)
        label_7.setText("subtitle")

        self.frame_37.layout().addWidget(frame_42)

    def createInfoIndicator(self, text):
        frame_45 = QFrame()
        frame_45.setFrameShape(QFrame.StyledPanel)
        frame_45.setFrameShadow(QFrame.Raised)
        horizontalLayout_43 = QHBoxLayout(frame_45)
        horizontalLayout_43.setContentsMargins(15, 0, 15, 0)
        horizontalLayout_43.setSpacing(0)
        horizontalLayout_43.setObjectName("horizontalLayout_43")
        label_11 = QLabel(frame_45)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        label_11.setFont(font)
        label_11.setAlignment(QtCore.Qt.AlignCenter)
        label_11.setWordWrap(True)
        horizontalLayout_43.addWidget(label_11)
        label_11.setText(text)

        self.frame_37.layout().addWidget(frame_45)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main_UI()
    # window.show()
    window.showMaximized()
    sys.exit(app.exec_())
