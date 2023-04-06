
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from forex_python.converter import CurrencyRates
c = CurrencyRates()
app = QApplication([])
win_card = QWidget()
win_card.setWindowTitle('Конвертор валют') 
win_card.resize(400, 200)

app.setStyleSheet("""
        QWidget {
            background: #061c3b;
            border-radius: 11px;    

        }
        
        QPushButton{
            background: #8f7efc;
            color: #ffffff;
            border-radius: 11px;
            min-width: 6em;    
            min-height: 2em;
            font-family: Arial;
            font: bold 18px;      
        }
        
        QLineEdit{
            background-color: #faacfa;
            max-width: 20em;
            max-height: 7em;
            font-family: Arial;
            font: bold 18px;
            border-color: beige;
            color: #031cfc;
            
        }

"""
)

oneline_edit = QLineEdit()
oneline_edit.setPlaceholderText("From which currency")
twoline_edit = QLineEdit()
twoline_edit.setPlaceholderText("In what currency")
fourline_edit = QLineEdit()
fourline_edit.setPlaceholderText("Result")
button = QPushButton("Convert")

ver_line = QVBoxLayout()

ver_line.addWidget(oneline_edit)
ver_line.addWidget(twoline_edit)
ver_line.addWidget(fourline_edit)
ver_line.addWidget(button)

def convert():
    withsomething = oneline_edit.text()
    getrate = twoline_edit.text()
    rate = c.get_rate(withsomething, getrate)
    fourline_edit.setText(str(rate))

button.clicked.connect(convert)
win_card.setLayout(ver_line)
win_card.show()
app.exec_()
