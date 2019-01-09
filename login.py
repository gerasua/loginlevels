from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from PyQt5.QtWidgets import (QApplication, QMessageBox)
from PyQt5.QtCore import Qt
import sys
import imagesqt_rc

class MainWindowExample(QMainWindow):

    def __init__(self):
        super(MainWindowExample, self).__init__()
        loadUi('login.ui', self)
        self.ButtonLogin.clicked.connect(self.selectLevel)

#
#Authenticate Module
#
    def selectLevel(self):
        username = self.user.text()
        password = self.password.text()

        try:
            dbconfig = read_db_config()
            conn = MySQLConnection(**dbconfig)
            cursor = conn.cursor()
            cursor1 = conn.cursor()
            cursor1.execute("SELECT * FROM users WHERE authenticate='1'")
            rows = cursor1.fetchall()
            print('Total Row(s):', cursor1.rowcount)
            if cursor1.rowcount >= 1:
                print("The user is alredy logged in")
                Q = QMessageBox()
                Q = QMessageBox.information(Q, 'Error',
                                            'The system is already being used.',
                                            QMessageBox.Ok)
                for row in rows:
                    print(row)
            else:

                cursor.execute("SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'")
                row = cursor.fetchone()

                if row is not None:
                    print(row)
                    print("\nUser Levelo: ", row[3])

                    def nivel1():
                        print("Hi level 1")
                        if row[4] == 1:
                            print("The user is alredy logged in", row[1])
                            Q = QMessageBox()
                            Q = QMessageBox.information(Q, 'Error',
                                                        'The system is already being used.',
                                                        QMessageBox.Ok)
                        else:
                            query = """ UPDATE users SET authenticate = %s WHERE id = %s """
                            data = (1, row[0])
                            try:
                                # update usuario
                                cursor = conn.cursor()
                                cursor.execute(query, data)
                                # Realizar el cambio
                                conn.commit()
                            except Error as error:
                                print(error)
                            finally:
                                cursor.close()
                                conn.close()

                            print("Hi again lelvel 1", row)
                            self.hide()
                            otraventana = ventana_Nivel1(self)
                            otraventana.show()

                    def nivel2():
                        print("Hi level 2")

                        if row[4] == 1:
                            print("The user is alredy logged in", row[1])
                            Q = QMessageBox()
                            Q = QMessageBox.information(Q, 'Error',
                                                        'The system is already being used.',
                                                        QMessageBox.Ok)
                        else:
                            query = """ UPDATE users SET authenticate = %s WHERE id = %s """
                            data = (1, row[0])
                            try:
                                # update usuario
                                cursor = conn.cursor()
                                cursor.execute(query, data)
                                # Realizar el cambio
                                conn.commit()
                            except Error as error:
                                print(error)
                            finally:
                                cursor.close()
                                conn.close()

                            print("Hi again level 2", row)
                            self.hide()
                            otraventana = ventana_Nivel2(self)
                            otraventana.show()

                    def nivel3():

                        if row[4] == 1:
                            print("The user is alredy logged in", row[1])
                            Q = QMessageBox()
                            Q = QMessageBox.information(Q, 'Error',
                                                        'The system is already being used.',
                                                        QMessageBox.Ok)
                        else:
                            query = """ UPDATE users SET authenticate = %s WHERE id = %s """
                            data = (1, row[0])
                            try:
                                # update usuario
                                cursor = conn.cursor()
                                cursor.execute(query, data)
                                # Realizar el cambio
                                conn.commit()
                            except Error as error:
                                print(error)
                            finally:
                                cursor.close()
                                conn.close()

                            print("Hi level 3", row)
                            self.hide()
                            otraventana = ventana_Nivel3(self)
                            otraventana.show()

                    nivel = row[3]
                    options = {1: nivel1,
                               2: nivel2,
                               3: nivel3,
                               }
                    options[nivel]()

                else:
                    print("User or password incorrect/empty")
                    Q = QMessageBox()
                    Q = QMessageBox.information(Q, 'Error',
                                                'User or password incorrect/empty.',
                                                QMessageBox.Ok)

        except Error as e:
            print(e)

        finally:
            cursor.close()
            conn.close()

#
#Fin Módulo de Autenticación
#

#
# Modulo Pesador
#
class ventana_Nivel1(QMainWindow):

    def __init__(self, parent=None):
        super(ventana_Nivel1, self).__init__(parent)
        loadUi('level1.ui', self)
        self.btn_salir.clicked.connect(self.salida)

    def salida(self):
        self.close()

    def closeEvent(self, event):
        """Generate 'question' dialog on clicking 'X' button in title bar.

        Reimplement the closeEvent() event handler to include a 'Question'
        dialog with options on how to proceed - Save, Close, Cancel buttons
        """
        reply = QMessageBox.question(
            self, "Message",
            "¿Estás completamente seguro de salir del sistema?",
            QMessageBox.Close | QMessageBox.Cancel)

        if reply == QMessageBox.Close:
            print("Salida If? Close")
            #Update de autenticado aqui
            dbconfig = read_db_config()
            conn = MySQLConnection(**dbconfig)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE authenticate='1'")
            row = cursor.fetchone()
            query = """ UPDATE users SET authenticate = %s WHERE id = %s """
            data = (0, row[0])
            try:
                # update usuario
                cursor = conn.cursor()
                cursor.execute(query, data)
                # Realizar el cambio
                conn.commit()
                app.quit()
            except Error as error:
                print(error)
            finally:
                cursor.close()
                conn.close()
        else:
            print("Salida Else? Cancel")
            event.ignore()


    def keyPressEvent(self, event):
        """Close application from escape key.

        results in QMessageBox dialog from closeEvent, good but how/why?
        """
        if event.key() == Qt.Key_Escape:
            print("Key Scape?")
            self.close()
#
#
#End level 1
#
#

#
#
#Level 2
#
class ventana_Nivel2(QMainWindow):

    def __init__(self, parent=None):
        super(ventana_Nivel2, self).__init__(parent)
        loadUi('level2.ui', self)
        self.btn_salir.clicked.connect(self.salida)

    def salida(self):
        self.close()

    def closeEvent(self, event):
        """Generate 'question' dialog on clicking 'X' button in title bar.

        Reimplement the closeEvent() event handler to include a 'Question'
        dialog with options on how to proceed - Save, Close, Cancel buttons
        """
        reply = QMessageBox.question(
            self, "Message",
            "¿Estás completamente seguro de salir del sistema?",
            QMessageBox.Close | QMessageBox.Cancel)

        if reply == QMessageBox.Close:
            print("Salida If? Close")
            #Update de autenticado aqui
            dbconfig = read_db_config()
            conn = MySQLConnection(**dbconfig)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE authenticate='1'")
            row = cursor.fetchone()
            query = """ UPDATE users SET authenticate = %s WHERE id = %s """
            data = (0, row[0])
            try:
                # update usuario
                cursor = conn.cursor()
                cursor.execute(query, data)
                # Realizar el cambio
                conn.commit()
                app.quit()
            except Error as error:
                print(error)
            finally:
                cursor.close()
                conn.close()
        else:
            print("Salida Else? Cancel")
            event.ignore()


    def keyPressEvent(self, event):
        """Close application from escape key.

        results in QMessageBox dialog from closeEvent, good but how/why?
        """
        if event.key() == Qt.Key_Escape:
            print("Key Scape?")
            self.close()
#
#
#Fin Módulo Supervisor
#

#
# Modulo Admiistracion
#
class ventana_Nivel3(QMainWindow):

    def __init__(self, parent=None):
        super(ventana_Nivel3, self).__init__(parent)
        loadUi('level3.ui', self)
        self.btn_salir.clicked.connect(self.salida)

    def salida(self):
        self.close()

    def closeEvent(self, event):
        """Generate 'question' dialog on clicking 'X' button in title bar.

        Reimplement the closeEvent() event handler to include a 'Question'
        dialog with options on how to proceed - Save, Close, Cancel buttons
        """
        reply = QMessageBox.question(
            self, "Message",
            "¿Estás completamente seguro de salir del sistema?",
            QMessageBox.Close | QMessageBox.Cancel)

        if reply == QMessageBox.Close:
            print("Salida If? Close")
            #Update de autenticado aqui
            dbconfig = read_db_config()
            conn = MySQLConnection(**dbconfig)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE authenticate='1'")
            row = cursor.fetchone()
            query = """ UPDATE users SET authenticate = %s WHERE id = %s """
            data = (0, row[0])
            try:
                # update usuario
                cursor = conn.cursor()
                cursor.execute(query, data)
                # Realizar el cambio
                conn.commit()
                app.quit()
            except Error as error:
                print(error)
            finally:
                cursor.close()
                conn.close()
        else:
            print("Salida Else? Cancel")
            event.ignore()


    def keyPressEvent(self, event):
        """Close application from escape key.

        results in QMessageBox dialog from closeEvent, good but how/why?
        """
        if event.key() == Qt.Key_Escape:
            print("Key Scape?")
            self.close()

#
# End level 3
#

app = QApplication(sys.argv)
main = MainWindowExample()
main.show()
sys.exit(app.exec_())