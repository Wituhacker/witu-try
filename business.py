import re
import kivymd
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
import mysql.connector
from kivy.core.text import LabelBase
from kivy.core.window import Window
#Window.size = (310, 580)




class businessApp(MDApp):
    def build(self):
        screen_manager =ScreenManager()
        screen_manager.add_widget(Builder.load_file('main.kv'))
        screen_manager.add_widget(Builder.load_file('login.kv'))
        screen_manager.add_widget(Builder.load_file('singup.kv'))
        return screen_manager
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 
    database = mysql.connector.connect(
       host= "localhost",
       user="root",
       password="chikwa",
       database="users"
  )
 

    cursor = database.cursor()
    cursor.execute('SELECT * FROM user_login')
    # result = mycursor.fetchall()
    for i in cursor.fetchall():
        print(i[0], i[1])

    def send_data(self,userfield,emails, pwds,pwdsc):
        if re.fullmatch(self.regex, emails.text):
            self.cursor.execute(f"insert into user_singup values('{userfield.text}','{emails.text}', '{pwds.text}','{pwdsc}')")  
            self.database.commit() 
            userfield.text=""
            emails.text=""
            pwds.text=""
            pwdsc.text=""


    def data_receive(self, email,password ):
        self.cursor.execute("select * from user_login")
        email_list= []
        for i in self.cursor.fetchall():
            email_list.append(i[0])
        if email.text in email_list and email.text !="":
            self.cursor.execute (f"select password from user_login where email='{email.text}'")
            for j in self.cursor:
                if password.text == j[0]:
                    print("login done")
                else:
                    print("incorrect")
        else:
            print("acha ujanja")

if __name__ == '__main__':
    app=businessApp()
    app.run() 