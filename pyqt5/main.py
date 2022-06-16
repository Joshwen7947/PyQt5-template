from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout

app = QApplication([])
window = QWidget()

window.setWindowTitle("Application")
window.move(800,100)
window.resize(400, 200)
# window.setGeometry(100,100,300,150)

window.show()
layout = QHBoxLayout()
text = QLabel('Hello, World!')
layout.addWidget(text, alignment=Qt.AlignCenter)
layout.addWidget(QPushButton('Center'))

window.setLayout(layout)
app.exec_()

