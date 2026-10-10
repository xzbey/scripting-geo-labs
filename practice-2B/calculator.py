from PyQt5.QtWidgets import QWidget, QLabel, QDoubleSpinBox, QPushButton, QComboBox

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label_units = QLabel("Единицы измерения:", self)
        label_units.move(50, 0)

        self.comboBox_units = QComboBox(self)
        self.comboBox_units.addItems(["Сантиметры", "Метры", "Километры"])
        self.comboBox_units.setCurrentIndex(1)
        self.comboBox_units.move(90, 30)

        label_l = QLabel("Длина", self)
        label_w = QLabel("Ширина", self)
        label_h = QLabel("Высота", self)

        label_l.move(50, 90)
        label_w.move(150, 90)
        label_h.move(250, 90)

        self.spinBox_l = QDoubleSpinBox(self)
        self.spinBox_w = QDoubleSpinBox(self)
        self.spinBox_h = QDoubleSpinBox(self)

        self.spinBox_l.move(50, 120)
        self.spinBox_w.move(150, 120)
        self.spinBox_h.move(250, 120)

        self.btn_s = QPushButton("Посчитать площадь", self)
        self.btn_v = QPushButton("Посчитать объем", self)

        self.btn_s.move(50, 190)
        self.btn_v.move(50, 240)      

        self.btn_s.clicked.connect(self.onPushBtnS_clicked)
        self.btn_v.clicked.connect(self.onPushBtnV_clicked)                     

        self.label_result = QLabel("Результат", self)
        self.label_result.move(50, 300)
        self.label_result.resize(300, 50)
        self.label_result.setWordWrap(True)

        self.resize(400, 350)
        self.setWindowTitle('Калькулятор площади и объёма')
        self.show()

        self.test()

    def test(self):
        self.spinBox_l.setValue(1.34)
        self.spinBox_h.setValue(5.81)
        self.spinBox_w.setValue(3.58)

    def getUnits(self) -> str:
        match self.comboBox_units.currentText():
            case "Сантиметры":
                return "см"
            case "Метры":
                return "м"
            case "Километры":
                return "км"
            case _:
                return ""

    def onPushBtnS_clicked(self):
        self.label_result.setText("Площадь: " + 
                                  str(round(self.spinBox_l.value() * self.spinBox_w.value(), 2))
                                  + " кв." + self.getUnits())
        
    def onPushBtnV_clicked(self):
        self.label_result.setText("Объем: " + 
                                  str(round(self.spinBox_l.value() * self.spinBox_w.value() * self.spinBox_h.value(), 2))
                                  + " куб." + self.getUnits())

