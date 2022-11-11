import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets, QtSql
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QMovie)
from PySide2.QtWidgets import *

# IMPORT APP MODULES
from app_modules import *

# GLOBALS
counter = counter1 = 0
jumper = 10
GLOBAL_STATE = 0

# CHECKED STATE LOGIN FORM
checked = False

# YOUR APPLICATION
class MainWindow(QMainWindow): 
    GLOBAL_STATE = 0

    # diffie hellman variables
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = MainWindowUI()
        self.ui.initUI(self)
        self.oldPos = self.pos()

        # algorithm variables
        self.mode = ""
        self.algorithm = "Diffie_Hellman"   #default algorithm 
 
        # Display welcome message
        dataBase.query1.exec_("SELECT user FROM userdata;")
        dataBase.query1.first()
        self.ui.label_welcome.setText(f"Welcome, {dataBase.query1.value(0)}!")

        self.centerScreen()

        # REMOVE TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) 

        # checkbox
        self.ui.checkBox.stateChanged.connect(self.checkState)
        self.ui.checkBox_2.stateChanged.connect(self.checkState)


        # provide a list of algorithms
        algorithmList = ["RSA", "ElGamal"]
        for algorithm in algorithmList:
            self.ui.algorithm_list.addItem(algorithm)
        self.ui.algorithm_list.currentIndexChanged.connect(self.algorithm_selected)

        self.ui.pushButton.clicked.connect(self.startTranscoding)

        # Disable maximize if wanted (uncomment the line)
        self.enableMaximumSize(1015, 720)

        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.btn_maximize_restore.clicked.connect(lambda: self.maximize_restore())

        # CLOSE APPLICATION
        self.ui.btn_close.clicked.connect(lambda: self.close())

        ## Functions to drag the window around
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    # show the window in the screen center
    def centerScreen(self):
        qtRectangle = self.frameGeometry()  
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    # MAXIMIZE/RESTORE Window
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")

    # ENABLE MAXIMUM SIZE
    def enableMaximumSize(self, width, height):
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.btn_maximize_restore.hide()

    # UNCHECK METHOD - CHECK ONE CHECKBOX AT A TIME
    def checkState(self, state):
        # checking if state is checked
        if state == Qt.Checked:
  
            # if first check box is selected
            if self.sender() == self.ui.checkBox:
                self.mode = "e"
                self.ui.lineEdit_output.setText("")
                self.ui.lineEdit_memory.setText("")
                self.ui.lineEdit_time.setText("")
                # making other check box to uncheck
                self.ui.checkBox_2.setChecked(False)
  
            # if second check box is selected
            elif self.sender() == self.ui.checkBox_2:
                self.mode = "d"
                self.ui.lineEdit_output.setText("")
                self.ui.lineEdit_memory.setText("")
                self.ui.lineEdit_time.setText("")
                # making other check box to uncheck
                self.ui.checkBox.setChecked(False)
            else: 
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)


    def resetText(self):
        self.ui.lineEdit_key.setText("")
        self.ui.lineEdit_key_2.setText("")
        self.ui.lineEdit_time.setText("")
        self.ui.lineEdit_memory.setText("")

    def algorithm_selected(self):
        self.algorithm = self.ui.algorithm_list.currentText()
        self.resetText()

        if self.algorithm == "Diffie_Hellman":
            self.ui.key_label.show()
            self.ui.key_label_2.show()
            self.ui.lineEdit_key.show()
            self.ui.lineEdit_key_2.show()
        
        if self.algorithm != "Diffie_Hellman":
            self.ui.key_label.hide()
            self.ui.key_label_2.hide()
            self.ui.lineEdit_key.hide()
            self.ui.lineEdit_key_2.hide()

        print(f"The selected algorithm is {self.algorithm}.")


    def startTranscoding(self):
        global a, algorithm, message, output, encrypted_message_list, temp

        output = ""
        temp = 0
        encrypted_message_list = []
        aKey = self.ui.lineEdit_key.text()
        bKey = self.ui.lineEdit_key_2.text()
        message = self.ui.lineEdit_mes.text()
        
    # ALGORITHM PROCESSING
        # Diffie_Hellman algorithm

        if self.algorithm == "Diffie_Hellman":
            temp = 0
            if len(aKey) == 0 or len(message) == 0 or len(bKey) == 0:

                self.ui.err.setText("Please input all the fields.")
                QtCore.QTimer.singleShot(3500, lambda: self.ui.err.setText(""))
                self.ui.lineEdit_output.setText('')

            else:
                print("Button clicked!")
                self.ui.err.setText("")
                aKey = int(aKey)
                bKey = int(bKey)
                # Timing a section of python code
                start_time = perf_counter()

                self.diffie_hellman = Diffie_Hellman(aKey, bKey)
                if self.mode.strip() == "e":  

                    output = self.diffie_hellman.encrypt(message.split(" "), self.diffie_hellman.astar, self.diffie_hellman.BobKey)

                    # End time once the code has finished       
                    end_time = perf_counter()

                    # Total time
                    final_time = end_time - start_time
                    self.ui.lineEdit_output.setText(' '.join([str(i) for i in output]))
                    self.ui.lineEdit_time.setText(str(final_time))
                    self.ui.lineEdit_memory.setText(str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))

                elif self.mode.strip() == "d":
                    myList = message.split(" ")
                    # print("my list is", myList)
                    for item in myList:
                        for i in item:
                            temp = temp * 10 + int(i) 
                        encrypted_message_list.append(temp)
                        temp = 0
                    # print("encrypted list is", encrypted_message_list)            
                    output = self.diffie_hellman.decrypt(encrypted_message_list, self.diffie_hellman.bstar, self.diffie_hellman.AliceKey).rstrip()
                    end_time = perf_counter()
                    # Total time
                    final_time = end_time - start_time
                    self.ui.lineEdit_output.setText(output)
                    self.ui.lineEdit_time.setText(str(final_time))
                    self.ui.lineEdit_memory.setText(str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))

        # Elgamal algorithm
        elif self.algorithm == "ElGamal":
            temp = 0
            if len(message) == 0:

                self.ui.err.setText("Please input the missing field.")
                QtCore.QTimer.singleShot(3500, lambda: self.ui.err.setText(""))
                self.ui.lineEdit_output.setText('')

            else:
                print("Button clicked!")
                self.ui.err.setText("")
                  
                # Timing a section of python code
                start_time = time.time()

                self.elgamal = ElGamal(0, 0)
                q = random.randint(pow(10,20),pow(10,50))
                self.elgamal.setK(q)
                g = random.randint(2,q)
                key = self.elgamal.gen_key(q)
                h = self.elgamal.power(g,key,q)

                if self.mode.strip() == "e":
                    output = self.elgamal.encryption(message, q, h)
                    print(output)

                    # End time once the code has finished       
                    end_time = perf_counter()

                    # Total time
                    final_time = end_time - start_time
                    self.ui.lineEdit_output.setText(' '.join([str(i) for i in output]))
                    self.ui.lineEdit_time.setText(str(final_time))
                    self.ui.lineEdit_memory.setText(str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))

                elif self.mode.strip() == "d":
                    myList = message.split(" ")
                    # print("my list is", myList)
                    for item in myList:
                        for i in item:
                            temp = temp * 10 + int(i) 
                        encrypted_message_list.append(temp)
                        temp = 0

                    print("encrypted list is", encrypted_message_list)

                    res = self.elgamal.decryption(encrypted_message_list, key, q, g)
                    print(res)
                    d_msg = ''.join(res)
                    print(d_msg)

                    output = unicodedata.normalize('NFKD', d_msg).encode('ASCII', 'ignore').decode("utf-8")
                    end_time = perf_counter()
                    # Total time
                    final_time = end_time - start_time
                    self.ui.lineEdit_output.setText(output)
                    self.ui.lineEdit_time.setText(str(final_time))
                    self.ui.lineEdit_memory.setText(str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))
                    
        # RSA algorithm

        if self.algorithm == "RSA":
            temp = 0
            if len(message) == 0:

                self.ui.err.setText("Please input all the fields.")
                QtCore.QTimer.singleShot(3500, lambda: self.ui.err.setText(""))
                self.ui.lineEdit_output.setText('')

            else:
                print("Button clicked!")
                self.ui.err.setText("")

                # Timing a section of python code
                start_time = perf_counter()
                self.rsa = RSA()
                if self.mode.strip() == "e":  

                    output = self.rsa.rsa_encryption(message.split(" "), self.rsa.e, self.rsa.p, self.rsa.q)

                    # End time once the code has finished       
                    end_time = perf_counter()

                    # Total time
                    final_time = end_time - start_time
                    self.ui.lineEdit_output.setText(' '.join([str(i) for i in output]))
                    self.ui.lineEdit_time.setText(str(final_time))
                    self.ui.lineEdit_memory.setText(str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))

                elif self.mode.strip() == "d":
                    myList = message.split(" ")
                    # print("my list is", myList)
                    for item in myList:
                        for i in item:
                            temp = temp * 10 + int(i) 
                        encrypted_message_list.append(temp)
                        temp = 0
                    # print("encrypted list is", encrypted_message_list)            
                    output = self.rsa.rsa_decryption(self.rsa.p,self.rsa.q,self.rsa.e, encrypted_message_list)
                    end_time = perf_counter()
                    # Total time
                    final_time = end_time - start_time
                    self.ui.lineEdit_output.setText(output)
                    self.ui.lineEdit_time.setText(str(final_time))
                    self.ui.lineEdit_memory.setText(str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))        



# LOADING SCREEN
class LoadingScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = LoadingScreenUI()
        self.ui.initUI(self)
        self.oldPos = self.pos()

        # SET INITIAL PROGRESS BAR TO ZERO
        self.progressBarValue(0)

        # REMOVE TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) 

        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        # START TIMER
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        ## TIMER IN MILLISECONDS
        self.timer.start(30)

        # SHOW MAIN WINDOW
        self.show()

    # Functions to drag the window around
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def progress (self):
        global counter1
        global jumper
        value = counter1

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if(value > jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(newHtml)
            jumper += 10

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100: value = 1.000
        self.progressBarValue(value)

        # CLOSE LOADING SCREEN AND OPEN APP
        if counter1 > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE LOADING SCREEN
            self.close()

        # INCREASE COUNTER
        counter1 += 0.5

    # PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(254, 121, 199, 255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        self.ui.circularProgress.setStyleSheet(newStylesheet)


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = SplashScreenUI()
        self.ui.initUI(self)
        self.oldPos = self.pos()

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(40)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO OUR APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(2000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(4000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))
        QtCore.QTimer.singleShot(6000, lambda: self.ui.label_description.setText("<strong>GET</strong> READY"))

        self.show()


    ## Functions to drag the window around
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def progress(self):

        global counter

        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREEN AND OPEN APP
        if counter > 150:
            self.timer.stop()

            self.login = Login()
            self.login.show()

            self.close()

        counter += 1

# LOGIN WINDOW
class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = LogIn_Form()
        self.ui.initUI(self)
        self.oldPos = self.pos()

        # Remember me
        self.ui.checkBox.stateChanged.connect(lambda:self.checkState(self.ui.checkBox))

        # Remember login data when reopened
        dataBase.query1.exec("UPDATE userdata SET id = 1")
        dataBase.query1.exec_("SELECT id, user, password FROM userdata;")
        dataBase.query1.first()
        self.ui.lineEdit.setText(dataBase.query1.value(1))
        self.ui.lineEdit_2.setText(dataBase.query1.value(2))

        # Connect to signUp
        self.ui.signUpButton.clicked.connect(self.gotoReg)

        # Database
        self.ui.logInButton.clicked.connect(self.checkUser)

    # Remember me functions
    def checkState(self, checkBox):
        global checked
        if checkBox.isChecked() == True:
            checked = True

        else:
            checked = False

    # Functions to drag the window around
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def gotoReg(self):

        self.reg = Registration()
        self.reg.show()
        self.close()

    def checkUser(self):
        
        user = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if len(user) == 0 or len(password) == 0:
            self.ui.error.setText("Please input all the fields.")
            QtCore.QTimer.singleShot(3500, lambda: self.ui.error.setText(""))
        else:
            
            dataBase.query.exec_("select username, email, password from userdata;")
            while (dataBase.query.next()):
                if (user == dataBase.query.value(0) or user == dataBase.query.value(1)):
        
                    if dataBase.query.value(2) == password:
                        print("Successfully logged in.") 
                        self.ui.error.setText("")

                        # Open loading Screen
                        self.loadingScreen = LoadingScreen()
                        self.loadingScreen.show()
                        self.close()
                        break

                    else:
                        self.ui.error.setText("Invalid username or password!")
                        QtCore.QTimer.singleShot(3500, lambda: self.ui.error.setText(""))     
                else:
                    self.ui.error.setText("Invalid username or password!")
                    QtCore.QTimer.singleShot(3500, lambda: self.ui.error.setText(""))
        
            if checked and self.ui.error.text() == "":                
                print("checked")
                dataBase.query1.exec_("DELETE FROM userdata WHERE id = 1")
                dataBase.query1.exec_(f"INSERT INTO userdata (user, password) VALUES ('{user}', '{password}')")

# REGISTRATION WINDOW
class Registration(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Reg_Form()
        self.ui.initUI(self)
        self.oldPos = self.pos()

        # Go back to logIn
        self.ui.signInButton.clicked.connect(self.gotoLogIn)

        #Database
        self.ui.pushButton.clicked.connect(self.checkUser)

    def gotoLogIn(self):
        self.login = Login()
        self.login.show()
        self.close()

    # Functions to drag the window around
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def checkUser(self):
        duplicate = False
        username = self.ui.lineEdit_2.text()
        email = self.ui.lineEdit_3.text()
        password = self.ui.lineEdit_4.text()
        confirmPass = self.ui.lineEdit_5.text()

        if len(username) == 0 or len(password) == 0 or len(email) == 0 or len(confirmPass) == 0:
            self.ui.err.setText("Please input all the fields.")
            QtCore.QTimer.singleShot(3500, lambda: self.ui.err.setText(""))

        elif '@' not in email:
            self.ui.err.setText("Invalid email address.")
            QtCore.QTimer.singleShot(3500, lambda: self.ui.err.setText(""))

        else:
            dataBase.query.exec_("SELECT username, email FROM userdata")
            while (dataBase.query.next()):
                if (username == dataBase.query.value(0)):
                    self.ui.err.setText("This username has already been taken.")
                    QtCore.QTimer.singleShot(3500, lambda: self.ui.err.setText(""))
                    duplicate = True
                if (email == dataBase.query.value(1)):
                    self.ui.err.setText("This email has already been taken.")
                    QtCore.QTimer.singleShot(3500, lambda: self.ui.err.setText(""))
                    duplicate = True

            if not duplicate:
                if password != confirmPass:
                    self.ui.err.setText("Passwords do not match!")
                    QtCore.QTimer.singleShot(3500, lambda: self.ui.err.setText(""))
                else:
                    dataBase.query.exec_(f"""INSERT INTO userdata (username, email, password)
                                    VALUES ('{username}', '{email}', '{password}')""")
                    self.ui.err.setText("")

                    # Open loading Screen
                    self.loadingScreen = LoadingScreen()
                    self.loadingScreen.show()
                    self.close() 
                    print("You have successfully signed up!")
        
# RUNNING
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window = SplashScreen()

#     login = Login()
#     login.show()

#     loadingScreen = LoadingScreen()
#     loadingScreen.show()

#     main = MainWindow()
#     main.show()
    sys.exit(app.exec_())
