import mysql.connector as M
import stdiomask as P
import pygame as D
import pickle as Z
import time as T
def askpassword():
    Tng=dict()
    e=input('\nEnter your email id :- ')
    ce=e.partition('@')
    if ce[1]=='@' and ce[2][-4::1]=='.com':
        print('Fetching account details...')
        print('Press <spacebar> to show the password\nPress <Esc> or CLOSE button to close the window ')
        print("Use the 'Left' or 'Right' arrow key to shift to other accounts") 
        urve=(e,)
        t=("SELECT ACCNAME,ACCPASS FROM keyhole WHERE ACCID=%s")
        kurs.execute(t,urve)
        za=kurs.fetchall()
        for i in range(1,len(za)+1):
            Tng[i]=za[i-1]+('****',)
        if Tng=={}:
            print("\nThe email id doesn't exist")
            print("Press '~' to start the function again")
        else:
            D.init()
            h=1
            surface=D.display.set_mode((468,150))
            D.display.set_caption('Password Viewer')
            Font=D.font.Font('freesansbold.ttf',26)
            Text_Render=Font.render(Tng[h][0],True,(0,255,0))
            Text_rect=Text_Render.get_rect()
            Text_rect.center=(70,26)
            Text_Render_1=Font.render(Tng[h][2],True,(0,255,0))
            Text_rect_1=Text_Render.get_rect()
            Text_rect_1.center=(285,31)
            Text_Render_2=Font.render(str(h),True,(0,255,0))
            Text_rect_2=Text_Render.get_rect()
            Text_rect_2.center=(209,117)
            Text_Render_3=Font.render('/'+str(len(Tng)),True,(0,255,0))
            Text_rect_3=Text_Render.get_rect()
            Text_rect_3.center=(226,118)
            i=0
            Loop=True
            while Loop:
                for event in D.event.get():
                    if event.type == D.QUIT:
                        Loop=False
                keys=D.key.get_pressed()
                if keys[D.K_ESCAPE]:
                    Loop=False
                if keys[D.K_SPACE]:
                    i=1
                if not(keys[D.K_SPACE]):
                    i=0
                if len(Tng) != 1:
                    if keys[D.K_LEFT]:
                        T.sleep(0.25)
                        h-=1
                        if h < 1:
                            h=len(Tng)
                        Text_Render=Font.render(Tng[h][0],True,(0,255,0))
                        Text_Render_2=Font.render(str(h),True,(0,255,0))
                    if keys[D.K_RIGHT]:
                        T.sleep(0.25)
                        h+=1
                        if h > len(Tng):
                            h=1
                        Text_Render=Font.render(Tng[h][0],True,(0,255,0))
                        Text_Render_2=Font.render(str(h),True,(0,255,0))
                if i:  
                    Text_Render_1=Font.render(Tng[h][1],True,(0,255,0))
                else:
                    Text_Render_1=Font.render(Tng[h][2],True,(0,255,0))
                surface.fill((0,0,0))
                surface.blit(Text_Render,Text_rect)
                surface.blit(Text_Render_1,Text_rect_1)
                surface.blit(Text_Render_2,Text_rect_2)
                surface.blit(Text_Render_3,Text_rect_3)
                D.display.update()
            D.quit()
    else:
        print('Invalid email id')
        print("Your email id should contain an '@' and '.com'")
        print("Press '~' to start the function again")
def appendacc():
    s=0
    kurs.execute("SELECT MAX(ACCNO) FROM keyhole")
    for i in kurs:
        if i[0] == None:
            s=1
        else:
            s=i[0]+1
    kurs.execute("SELECT ACCNAME FROM keyhole")
    jkl=kurs.fetchall()
    while True:
        a=input('\nEnter your account name :- ')
        if a in jkl:
            print('The Account Name','\''+a+'\'','already exists in the database')
            print('Try using a different name')
        else:
            break
    b=input('Enter your email id :- ')
    ce=b.partition('@')
    if ce[1]=='@' and ce[2][-4::1]=='.com':
        d=P.getpass('Enter your password :- ')
        e=P.getpass('Re-Enter your password :- ')
        while d != e:
            print('The password doesn\'t  matches with the original password')
            e=P.getpass('Re-Enter your password :- ')
        t="INSERT INTO keyhole VALUES({},'{}','{}','{}')"
        dat=(t.format(s,a,b,e))
        kurs.execute(dat)
        mydb.commit()
        print('Account Details Inserted')
    else:
        print('Invalid email id')
        print('Your email id',b,'is not legal')
        print("Your email id should contain an '@' and '.com'")
        print("Press '@' to start the function again")
def deleteacc():
    a=input('\nEnter your account name :- ')
    jck="SELECT * FROM keyhole WHERE ACCNAME='{}'"
    mat=(jck.format(a))
    kurs.execute(mat)
    ch=kurs.fetchall()
    if len(ch) == 0:
        print("Account name",a,"doesn't exists")
    else:
        while True:
            b=input('R u sure?[y/n] :- ')
            if b == 'y':
                t="DELETE FROM keyhole WHERE ACCNAME='{}'"
                dat=(t.format(a))
                kurs.execute(dat)
                mydb.commit()
                print('Account is deleted')
                break
            elif b == 'n':
                print('Account is not deleted')
                break
            else:
                print("Invalid input, please enter 'y' or 'n'")
def changepassword():
    a=input('\nEnter your account name :- ')
    b=input('Enter your email id :- ')
    ce=b.partition('@')
    qw="SELECT * FROM keyhole WHERE ACCNAME='{}' AND ACCID='{}'"
    nj=qw.format(a,b)
    kurs.execute(nj)
    teg=kurs.fetchall()
    if teg==[] and not(ce[1]=='@' and ce[2][-4::1]=='.com'):
        print("\nThe Account name",a,"and the email id",b,"doesn't exists")
        if not(ce[1]=='@' and ce[2][-4::1]=='.com'):
            print('\nYour email id',b,'is not legal')
            print("\nYour email id should contain an '@' and '.com'")
        print("\nPress '%' to start the function again")
    else:
        d=P.getpass('Enter your new password :- ')
        e=P.getpass('Re-Enter your new password :- ')
        while d != e:
            print('The password doesn\'t  matches with the original password')
            e=P.getpass('Re-Enter your password :- ')
        t="UPDATE keyhole SET ACCPASS='{}' WHERE ACCNAME='{}' AND ACCID='{}'"
        dat=(t.format(e,a,b))
        kurs.execute(dat)
        mydb.commit()
        print('\nPassword Changed')
def listacc():
    kurs.execute("SELECT ACCNO,ACCNAME FROM keyhole ORDER BY ACCNO")
    for i in kurs:
        print(i[0],i[1])
def firsttime():
    try:
        with open('profile_id_steup.dat','rb+') as f:
            g=Z.load(f)
            for i in g:
                if g[i] == 'exwk':
                    return True
    except FileNotFoundError:
        c=dict()
        print('Hello User,\nWelcome to Account recorder')
        print('This app can manage all your internet acounts')
        a=input('\nHave you installed the MySQL app? [y/n] :- ')
        if a == 'y':
            c['MySQL_app']=a
            c['Name_first']=input('Your firstname? :- ')
            c['Name_last']=input('Your lastname? :- ')
            print('\nCreating the database...')
            a=P.getpass('Enter your Password to create your database: ')
            mydb=M.connect(host = "localhost", user = "root",passwd=a)
            kurs=mydb.cursor()
            kurs.execute('CREATE DATABASE padlock')
            kurs.execute('USE padlock')
            kurs.execute('CREATE TABLE keyhole(ACCNO int(30),ACCNAME varchar(50) Primary key,ACCID varchar(50),ACCPASS varchar(50))')
            kurs.close()
            c['Database']='exwk'
            with open('profile_id_steup.dat','wb+') as f:
                d=Z.dump(c,f)
            print('\nDatabase created\n')
            return True
        else:
            print('\nPlease install MySQL app\n')
            T.sleep(5)
            print('Closing program...')
            T.sleep(5)
            return False
t=0
v=firsttime()
if v:
    for i in range(3,-1,-1):
        try:
            a=P.getpass('Enter your Password to connect to your database: ')
            mydb=M.connect(host = "localhost", user = "root",passwd=a,database='padlock')
            t=1
        except:
            print('Access Denied')
            print('You have',i,'chance to enter your password')
            t=0
        if t:
            break
    if not(t):
        print('You have exhausted your chances')
        T.sleep(5)
        print('Restart your program','\nContact your administar')
        T.sleep(5)
    else:
        kurs=mydb.cursor()
        print('\nOn the left hand side = You have the functions in which you can operate the software')
        print('On the right hand side = You have unique character "key" which can enable you to use the function')
        print('You can enter the key in the "Enter command :- " to operate the software')
        print('\nView password =','~')
        print('View account list =','!')
        print('Add account =','@')
        print('Delete account =','#')
        print('Change password =','%')
        print('Exit program =','*')
while True and t:
    v=input('\nEnter command :- ')
    if v == '~':
        askpassword()
    elif v == '!':
        print('')
        listacc()
    elif v == '@':
        appendacc()
    elif v == '#':
        deleteacc()
    elif v == '%':
        changepassword()
    elif v == '*':
        kurs.close()
        print('bye')
        break
    else:
        print('\nInvalid Input')
        print('Please enter these keywords below')
        print('\nView password =','~')
        print('View account list =','!')
        print('Add account =','@')
        print('Delete account =','#')
        print('Change password =','%')
        print('Exit program =','*')
