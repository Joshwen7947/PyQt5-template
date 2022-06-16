from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel,QVBoxLayout,QPushButton, QWidget

app = QApplication([])
window =  QWidget()
window.setWindowTitle('Test')
window.move(800,400)
window.setGeometry(100,100,500,500)
# 
text = QLabel("Hello World!")
layout = QVBoxLayout()
layout.addWidget(text, alignment=Qt.AlignCenter)
# 
button1  = QPushButton('Click Me!')
button2 = QPushButton('Button 2')
layout.addWidget(button1, alignment=Qt.AlignCenter)
layout.addWidget(button2, alignment=Qt.AlignCenter)

# Class with functions for buttons
class Buttons:
    def test_btn():
        fun_title = QLabel('This button is working!')
        layout.addWidget(fun_title, alignment = Qt.AlignCenter)
        window.setLayout(layout)

    def btn_click():
        warn = QLabel("Warning! 1...2...3...")
        layout.addWidget(warn,alignment=Qt.AlignCenter)
        window.setLayout(layout)

# Var to store class
btn = Buttons
# We connect the button to the class and method
button1.clicked.connect(btn.test_btn)
button2.clicked.connect(btn.btn_click)


# Ususally set towards bottom of our code
window.show()
window.setLayout(layout)
app.exec()