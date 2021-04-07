#=================================EACT BANK==============================================
#This program is designed an internet bank page. It has ten pages: The main page is opened
# automatically when the program runs. This page presents two alternatives; one is bank officer processes
# and the other one customer processes. Bank Officer Page is for opening an account for a new customer.
# The Bank Officer can enter the informations of a customer and bank gives 1000 EUR to the new customer as a gift.
# Also it appoints a default password. Customer page encounters the customer with a user id and a password.
# After entering these informations correctly, the customer can insert money to his/her account,
#  transfer and withdraw. In addition, he/she can display his/her informations and account activities.
# The EACT BANK Program includes also an update information page. The program uses three data bases,
# prepared in .txt format. One is for customer database, second one is for to hold the information of current
# customer temporarily. The third one is account activities of customers or banking process logs.

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from datetime import datetime
import string
from PyQt5.QtWidgets import QMessageBox
global Capital
Capital = string.ascii_uppercase+"Ç"+"Ğ"+"İ"+"Ö"+"Ş"+" "+"Ü"

class Ilksayfa(QDialog):    #bank officer or customer
    def __init__(self):
        super(Ilksayfa, self).__init__()
        loadUi("ilkekran.ui", self)
        self.bank_op_btn.clicked.connect(self.go_bank_op)
        self.mainpagecutomeroperationbutton.clicked.connect(self.go_cust_op)
    def go_bank_op(self):
        ikincisayfa = Ikincisayfa()
        widget.addWidget(ikincisayfa)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def go_cust_op(self):
        ucuncusayfa = Ucuncusayfa()
        widget.addWidget(ucuncusayfa)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Ikincisayfa(QDialog): # bank officer screen

    def __init__(self):
        super(Ikincisayfa, self).__init__()
        loadUi("ikinciekran.ui", self)

        self.exit.clicked.connect(self.exit_func1)
        self.save_customer.clicked.connect(self.save_info)
        self.textEdit.setText(" Enter the Information of the Customer")
    def exit_func1(self):
        ilksayfa = Ilksayfa()
        widget.addWidget(ilksayfa)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def save_info(self):
        self.space = " "
        self.password = "123"
        self.account = "1000"
        self.id = self.bankoperationid.text()
        self.name = self.bankoperationname.text().upper()
        self.surname = self.bankoperationsurname.text().upper()
        self.tel = self.bankoperationtelephone.text()
        self.process="account_opening"

        if self.name == "" or self.surname == "" or self.id == "" or self.tel == "":
            self.textEdit.setText("You have left empty at least one information!")
        else:
            from datetime import datetime
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            self.dt_object = datetime.fromtimestamp(timestamp)
            with open("userss.txt", "a", encoding="utf-8") as file:
                file.write(f"{self.name}{self.space}{self.surname}{self.space}{self.id}{self.space}"
                           f"{self.tel}{self.space}{self.password}{self.space}{self.account}{self.space}{self.process}{self.space}{self.dt_object}{self.space}")
                self.textEdit.setText("Saved!")
            with open("records.txt", "a", encoding="utf-8") as dosya:
                dosya.write(f"{self.name} {self.surname} {self.process} {self.dt_object} ")

class Ucuncusayfa(QDialog): # customer password screen
    def __init__(self):
        super(Ucuncusayfa, self).__init__()
        loadUi("ucuncuekran.ui", self)
        self.entypagelinebuttonexit.clicked.connect(self.exit_func2)
        self.entypagelinebuttonentry.clicked.connect(self.go_cust_page)

        self.textEdit_pass.setText("Enter Your Id and Password ")
    def go_cust_page(self):
        self.id_cust= self.entypagelineEditid.text()  # customer  ıd bundan sonraki islemlerde kullanılacak
        self.pass_cust=self.entypagelineEditpassword.text()
        with open ("userss.txt", encoding="utf-8") as file:
            readfiles = file.readline()
            readfiles = readfiles.split(" ")
            for i in range(len(readfiles)):
                if readfiles[i] == self.id_cust and readfiles[i+2] ==self.pass_cust:
                    temp=readfiles[i-2:i+4]  #current customer information
                    with open("temporary.txt", "w", encoding="utf-8") as dos:
                        dos.write(f"{temp[0]} {temp[1]} {temp[2]} {temp[3]} {temp[4]} {temp[5]}")  # record temporary file

                    bessayfa_ = Bessayfa()
                    widget.addWidget(bessayfa_)
                    widget.setCurrentIndex(widget.currentIndex() + 1)
                else:
                    self.textEdit_pass.setText("Your Id or Password is Incorret!")

        with open("temporary.txt", encoding="utf-8") as dos:  # read the info of current customer from temporary.txt
            readfiles = dos.readline()
            temp = readfiles.split(" ")

        self.process = "log_in"

        from datetime import datetime  # put time stamp
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        self.dt_object = datetime.fromtimestamp(timestamp)
        with open("records.txt", "a", encoding="utf-8") as file:  # record the process
            file.write(f"{temp[0]} {temp[1]} {self.process} {self.dt_object} ")

    def exit_func2(self):
        ilksayfa = Ilksayfa()
        widget.addWidget(ilksayfa)
        widget.setCurrentIndex(widget.currentIndex() + 1)

#class Dorduncusayfa(QDialog): # update customer information (not designed yet)

class Bessayfa(QDialog): #customer banking operation main page
    def __init__(self):
        super(Bessayfa, self).__init__()
        loadUi("besekran.ui", self)
        self.displayacccount.clicked.connect(self.display_account_func)
        self.withdrawmoney.clicked.connect(self.withdrawmoney_func)
        self.depositmoney.clicked.connect(self.depositmoney_func)
        self.moneytransfer.clicked.connect(self.moneytransfer_func)
        self.accountstatement.clicked.connect(self.accountstatement_func)
        self.changeinformation.clicked.connect(self.changeinformation_func)
        self.logoutcustomer.clicked.connect(self.logoutcustomer_func)

    def display_account_func(self):
        altisayfa = Altisayfa()
        widget.addWidget(altisayfa)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def logoutcustomer_func(self):
        ilksayfa = Ilksayfa()
        widget.addWidget(ilksayfa)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def withdrawmoney_func(self):
        yedisayfa = Yedisayfa()
        widget.addWidget(yedisayfa)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def depositmoney_func(self):
        sekizsayfa = Sekizsayfa()
        widget.addWidget(sekizsayfa)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def moneytransfer_func(self):
        dokuzsayfa = Dokuzsayfa()
        widget.addWidget(dokuzsayfa)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def changeinformation_func(self):
        onsayfa=Onsayfa()
        widget.addWidget(onsayfa)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def accountstatement_func(self):
        onbirsayfa = Onbirsayfa()
        widget.addWidget(onbirsayfa)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Altisayfa(QDialog): # displays the informations of customer
    def __init__(self):
        super(Altisayfa, self).__init__()
        loadUi("altiekran.ui", self)
        self.previousscreenacccount.clicked.connect(self.go_cust_page2)

        with open("temporary.txt", encoding="utf-8") as dos: #read the info of current customer from temporary.txt
            readfiles = dos.readline()
            temp = readfiles.split(" ")

        self.process = "display_the_amount"

        self.displayaacountscreen.setText(f"Mr/Mrs {temp[0]} {temp[1]}: \nYou have {temp[5]} EUR \n in your account")

        from datetime import datetime  # put time stamp
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        self.dt_object = datetime.fromtimestamp(timestamp)
        with open("records.txt", "a", encoding="utf-8") as file:  # record the process
            file.write(f"{temp[0]} {temp[1]} {self.process} {self.dt_object} ")

    def go_cust_page2(self):
        bessayfa_ = Bessayfa()
        widget.addWidget(bessayfa_)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Yedisayfa(QDialog): # withdraw screen
    def __init__(self):
        super(Yedisayfa, self).__init__()
        loadUi("yediekran.ui", self)
        self.returntopreviouspage.clicked.connect(self.go_cust_page3)
        self.pushentry.clicked.connect(self.entry_func2)
        with open("temporary.txt", encoding="utf-8") as dos: #read the info of current customer from temporary.txt
            readfiles = dos.readline()
            self.temp = readfiles.split(" ")
    def entry_func2(self):
        self.money=(self.enty.text())  # amount of money to draw manuel

        if int(self.temp[5])>=int(self.money):
            self.kalan=int(self.temp[5])-int(self.money)

        # --------------------update the account in temporary file----------------------------
            with open("temporary.txt", "r", encoding="utf-8") as dos:
                readfiles = dos.readline()
                self.temp = readfiles.split(" ")
                self.temp[5] = self.kalan
            with open("temporary.txt", "w", encoding="utf-8") as dos:
                dos.write(f"{self.temp[0]} {self.temp[1]} {self.temp[2]} {self.temp[3]} {self.temp[4]} {self.temp[5]}")
            self.textEdit_pass.setText(f" You have drawn enough {self.money} EUR. Your current account is {self.kalan} EUR")

        #------------------------------recording----------------------------
            with open("temporary.txt", encoding="utf-8") as dos:  # read the info of current customer from temporary.txt
                readfiles = dos.readline()
                temp = readfiles.split(" ")
            self.process = "withdrawal"
            from datetime import datetime  # put time stamp
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            self.dt_object = datetime.fromtimestamp(timestamp)
            with open("records.txt", "a", encoding="utf-8") as file:  # record the process
                file.write(f"{temp[0]} {temp[1]} {self.process} {self.dt_object} ")
        #---------------------------update the main customer file------------------------------------------
        else:
            self.textEdit_pass.setText(" You dont have enough money for this withdrawal!")
    def go_cust_page3(self):
        bessayfa_ = Bessayfa()
        widget.addWidget(bessayfa_)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Sekizsayfa(QDialog): #insert maney screen
    def __init__(self):
        super(Sekizsayfa, self).__init__()
        loadUi("sekizekran.ui", self)
        #global draw_money

        self.returntopreviouspage.clicked.connect(self.go_cust_page4)
        self.pushentry.clicked.connect(self.entrry_func2)
        with open("temporary.txt", encoding="utf-8") as dos: #read the info of current customer from temporary.txt
            readfiles = dos.readline()
            self.temp = readfiles.split(" ")
            print(self.temp[5])
    def entrry_func2(self):

        self.money = self.enty.text()  # amount of money to draw manuel
        self.new = int((self.temp[5])) + int((self.money))

        # --------------------update the account in temporary file----------------------------
        with open("temporary.txt", "r", encoding="utf-8") as dos:
            readfiles = dos.readline()
            self.temp = readfiles.split(" ")
            self.temp[5] = self.new
        with open("temporary.txt", "w", encoding="utf-8") as dos:
            dos.write(f"{self.temp[0]} {self.temp[1]} {self.temp[2]} {self.temp[3]} {self.temp[4]} {self.temp[5]}")
        self.textEdit_pas.setText(f" You have inserted {self.money} EUR. Your current account is {self.new} EUR")
        # ------------------------------recording----------------------------
        with open("temporary.txt", encoding="utf-8") as dos:  # read the info of current customer from temporary.txt
            readfiles = dos.readline()
            temp = readfiles.split(" ")
        self.process = "deposit_money"
        from datetime import datetime  # put time stamp
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        self.dt_object = datetime.fromtimestamp(timestamp)
        with open("records.txt", "a", encoding="utf-8") as file:  # record the process
            file.write(f"{temp[0]} {temp[1]} {self.process} {self.dt_object} ")

    def go_cust_page4(self):
        bessayfa_ = Bessayfa()
        widget.addWidget(bessayfa_)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        """        
        """

class Dokuzsayfa(QDialog): # money transfer screen (not completed yet)
    def __init__(self):
        super(Dokuzsayfa, self).__init__()
        loadUi("dokuzekran.ui", self)

        self.returntopr.clicked.connect(self.go_cust_page5)

    def go_cust_page5(self):
        bessayfa_ = Bessayfa()
        widget.addWidget(bessayfa_)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        #self.pushButtonentry_2.clicked.connect(self.entry_func2)
        with open("temporary.txt", encoding="utf-8") as dos:  # read the info of current customer from temporary.txt
            readfiles = dos.readline()
            self.temp = readfiles.split(" ")

class Onsayfa(QDialog):
    def __init__(self):
        super(Onsayfa, self).__init__()
        loadUi("onekran.ui", self)
        self.saveButton.clicked.connect(self.go_cust_page6)
        self.removetheaccount.clicked.connect(self.go_cust_page7)
        """self.pushButtonentry.clicked.connect(self.entry_func2)
        #self.transfer_money = self.transferamountofmoney.text() #amount of money to draw manuel
    def entry_func2(self):
        self.transfer_money = self.transferamountofmoney.text()  # amount of money to transfer manuel"""

    def go_cust_page6(self):
        #telefon ve passwor blgilerini burada guncelle
        #self.new_password = self.newpaswordedit.text()
        #self.new_telephonenumber = self.newtelephoneedit.text()
        bessayfa_ = Bessayfa()
        widget.addWidget(bessayfa_)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_cust_page7(self):
        # tum hesap bilgilerini buradan sil
        ilksayfa = Ilksayfa()
        widget.addWidget(ilksayfa)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Onbirsayfa(QDialog):  # logs of baning processses
    def __init__(self):
        super(Onbirsayfa, self).__init__()
        loadUi("onbirekran.ui", self)
        self.returntopreviouspage2.clicked.connect(self.go_cust_page8)
        self.islemdisplay.setText("Your account activities are listed below:")
        self.button_get.clicked.connect(self.get_info)

    def get_info(self):
        with open("temporary.txt", encoding="utf-8") as dos:  # read the info of current customer from temporary.txt
            readfiles = dos.readline()
            self.temp1 = readfiles.split(" ")
            print(self.temp1)

        with open("records.txt", encoding="utf-8") as dos:  # read the info of current customer from temporary.txt
            readfiles = dos.readline()
            self.temp2 = readfiles.split(" ")
            print(self.temp2)
        self.islemdisplay.setText(f"Your account activities are listed below:\n{self.temp2[:]}")
        #for i in self.temp2:
        #    if self.temp1[0]==self.temp2[i]:
        # file.write(f"{self.temp2[i]} {self.temp2[i+1]} {self.temp2[i+2]} {self.temp2[i+3]} {self.temp2[i+4]}")
        #print(a)
        #self.textBrowser_islemdisplay.setText(a)

    def go_cust_page8(self):
        bessayfa_ = Bessayfa()
        widget.addWidget(bessayfa_)
        widget.setCurrentIndex(widget.currentIndex() + 1)

#====================================================================
app = QApplication(sys.argv)
mainwindow = Ilksayfa()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setWindowTitle("EACT BANK")
widget.setFixedHeight(500)
widget.setFixedWidth(400)
widget.show()
app.exec_()
#=======================================END OF THE PROGRAM==================================================