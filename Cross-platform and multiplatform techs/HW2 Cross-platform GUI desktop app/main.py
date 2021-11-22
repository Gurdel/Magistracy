import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QColor, QBrush

import gui
import solver

class Application(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnOpenFile.clicked.connect(self.solve_file)
        self.btnSaveToFile.clicked.connect(self.save_output)
        
        self.solveNewton.clicked.connect(self.solve_newton)
        self.solveDichotomy.clicked.connect(self.solve_dichotomy)
        self.solveSecant.clicked.connect(self.solve_secant)

        self.actionTask.triggered.connect(self.show_task)
        self.actionDocumentation.triggered.connect(self.show_help)
        self.actionAuthor.triggered.connect(self.show_author)
    

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()


    def drawRectangles(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        qp.setBrush(QColor(160, 160, 160))
        qp.drawRect(5, 25, 270, 85)
        qp.drawRect(10, 130, 245, 80)
        qp.drawRect(10, 230, 245, 100)
        qp.drawRect(10, 350, 245, 100)
        qp.drawRect(290, 47, 110, 60)


    def solve_file(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, "Choose file")
        if path:
            self.textBrowser.setText(solver.SolveFile(path[0]))
    
    def save_output(self):
        path = QtWidgets.QFileDialog.getSaveFileName(self, 
                                                'Save output to file')
        if path:
            text = self.textBrowser.toPlainText()
            with open(path[0], 'w') as sw:
                sw.write(text)
    

    def get_template_number(self, template):
        templates_dict = {
            'A*x + B*cos(x) + C': 1,
            'A*x^2 + B*x + C': 2,
            'A*x * exp(B*x) + C': 3,
        }
        return templates_dict[template]
    
    def get_template_args(self):
        templ = self.get_template_number(self.comboBoxTemplate.currentText())
        a = self.paramA.value()
        b = self.paramB.value()
        c = self.paramC.value()
        e = self.paramE.value()

        return e, templ, [a, b, c]


    def solve_newton(self):
        template_args = self.get_template_args()
        res = solver.Newton(self.paramNewton_x.value(), *template_args)
        self.textBrowser.setText(res[-1])

    def solve_dichotomy(self):
        template_args = self.get_template_args()
        res = solver.Dichotomy(
            self.paramDichotomy_a.value(), 
            self.paramDichotomy_b.value(),
            *template_args
        )
        self.textBrowser.setText(res[-1])

    def solve_secant(self):
        template_args = self.get_template_args()
        res = solver.Secant(
            self.paramSecant_x2.value(), 
            self.paramSecant_x1.value(),
            *template_args
        )
        self.textBrowser.setText(res[-1])
    

    def show_task(self):
        text = '''
Create a program that implements all functionality of 
homework №1. The program should be created using
cross-platform tools (of your choice):
...
- Cross-platform GUI desktop application
...

In each case your application should have a menu with short 
user's guide, info about assignment, and about the author.

Make illustrated report where there are descriptions of technologies
you used and screen shots of working app will be presented.
Send the report into classroom and prepare to defending.
Screen cast video is welcome.
        '''
        self.textBrowser.setText(text)

    def show_help(self):
        text = '''
Application for solving equations by numerical methods

    User's guide:
Choose template, enter template parameters and accuracy e.
Enter numeric method params and click "solve" button.

For getting data from file click "Solve file" button.
For saving output to file click "Save to file" button.

Click "Menu" for seeing additional information.

    Documentation:

Equations templates:
    1. a*x + b*cos(x) + c
    2. a*x^2 + b*x + c
    3. a*x * exp(b*x) + c

Methods:
    1. Newton (tangent) method
    2. Dichotomy method
    3. Secant (chord) method

Common function parameters:
e: accuracy
template: number of equation template
args: list of equation parameters [a, b, c]
Newton( x,  e,  template, [] args)
x: init value
Dichotomy( a,  b,  e,  template, [] args)
a: left value of the erval in which the solution is located
b: right value of the erval in which the solution is located
Secant( x_2,  x_1,  e,  template, [] args)
x_1: previous value of x (Xn-1)
x_2: previous value of x_1 (Xn-2)
        '''
        self.textBrowser.setText(text)

    def show_author(self):
        text = '''
Application created by

     Maksym Shevchenko, AI-1
        '''
        self.textBrowser.setText(text)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()


