import tkinter as tk
l = []
ll = []
            
wind = tk.Tk()
wind.title('Gestion des Contacts (Rami Ben Hamouda: GLSI1A : Tp3)')
fr = tk.Frame(wind)
vt=tk.StringVar()
vn=tk.StringVar()

imgp = tk.PhotoImage(file='pen.gif')
imgl = tk.PhotoImage(file='loup.gif')

can = tk.Canvas(width=155,height=155)
can.pack()

resnom=tk.StringVar()
restel=tk.StringVar()

tk.Label(fr, text = 'Nom:').pack()
nom = tk.Entry(fr, textvariable = vn).pack()
tk.Label(fr, text = 'Téléphone:').pack()
tel = tk.Entry(fr, textvariable = vt).pack()
curr_display = ''
tk.Label(fr,text='Manuel: Si vous etes satisfait avec les donnees ').pack()
tk.Label(fr,text='que vous avez saisi, Validez les champs ').pack()
tk.Label(fr,text='puis Enregistrez / Recherchez').pack()

def save(nom,tel):
    if(nom == '')or(tel == ''):
        resnom.set('')
        restel.set('Completer les champs, Valider puis Enregistrer')
    elif(len(tel)> 8)or(len(tel)<8):
        resnom.set('')
        restel.set('Le numero de téléphone doit être de longeur 8')
    else:    
        f = open('rptl1.txt','w')        
        f.write(nom)
        f.write('\n')
        f.write(tel)
        f.write('\n')
        f.close()
        resnom.set('')
        restel.set('Enregistré!')
    can.create_image(25,25,image=imgp,anchor='nw')
    
def find(nom):
    f = open('rptl1.txt','rt')
    l = f.readlines()
    for s in l:
        ll.append(s.rstrip('\n'))
    if(nom == ''):
        resnom.set('')
        restel.set('Saisir un nom, Valider puis Rechercher')
    elif(nom in ll):
        resnom.set('Le numero rechérché est : ')
        restel.set(str(ll[ll.index(nom)+1]))
    else:
        resnom.set('Inconnu')
        restel.set('')
    f.close()
    can.create_image(25,25,image=imgl,anchor='nw')
    
def getinto(i):
    vt.set(i)

def sumr():
    resnom.set(vn.get())
    restel.set(vt.get())
    
def num_in(i):
    
    global curr_display
    curr_display = curr_display + str(i)
    vt.set(curr_display)
    display = tk.Label(wind, text=curr_display)

def num_out():
    global curr_display
    curr_display = ''
    vt.set(curr_display)
    
tk.Label(fr, textvariable = resnom).pack()
tk.Label(fr, textvariable = restel).pack()

tk.Button(fr, text='Valider les champs', command = sumr).pack()
tk.Button(wind, text='Enregistrer un contact',command= lambda:save(resnom.get(),restel.get())).pack(side='left')
tk.Button(wind, text='Rchercher un contact',command= lambda:find(resnom.get())).pack(side='right')

for i in range(10):
    tk.Button(fr, text=i, state=tk.NORMAL, command= lambda i=i: num_in(i)).pack(side='left')
    
tk.Button(wind, text='Quitter', command = wind.destroy).pack(side='bottom')
tk.Button(wind, text='<-', command = num_out).pack(side='bottom')

fr.pack()
wind.mainloop()
