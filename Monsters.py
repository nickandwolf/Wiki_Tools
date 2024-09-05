import tkinter as tk
from tkinter import ttk

# Creating tkinter window 
window = tk.Tk() 
window.title('Monster Wiki Maker') 
window.geometry('320x580') 
  
# Name
name_v = tk.StringVar()
ttk.Label(window, text = "Name:").grid(row = 0, column = 0,sticky="e")
name_e = tk.Entry(window, width=25, textvariable=name_v).grid(row=0,column=1,sticky="w")

# Type
ttk.Label(window, text = "Type:").grid(row = 1, column = 0,sticky="e")
type_v = tk.StringVar() 
typeCB = ttk.Combobox(window, width = 20, textvariable = type_v)
typeCB['values'] = ('Aberration','Beast','Celestial','Construct','Dragon',
                    'Elemental','Fey','Fiend','Giant','Humanoid','Lowlife',
                    'Magical Beast','Monster','Planar','Plant','Undead')
  
typeCB.grid(row = 1, column = 1,sticky="w") 
typeCB.current()

# Terrain
ttk.Label(window, text = "Terrain:").grid(row = 2, column = 0,sticky="e")
type_v = tk.StringVar() 
terrainCB = ttk.Combobox(window, width = 20, textvariable = type_v)
terrainCB['values'] = ('Anywhere','Desert','Extra-Planar','Forest','Hills ','Jungle',
                        'Mountains','Plains','Swamp','Tundra','Underground','Wetlands')
terrainCB.grid(row = 2, column = 1,sticky="w")
terrainCB.current()

# Rarity
ttk.Label(window, text = "Rarity:").grid(row = 3, column = 0,sticky="e")
rare_v = tk.StringVar() 
rareCB = ttk.Combobox(window, width = 20, textvariable = rare_v)
rareCB['values'] = ('Common','Uncommon','Rare','Very Rare','Unique')
rareCB.grid(row = 3, column = 1,sticky="w")
rareCB.current()

# No. Appear
noApp_v = tk.StringVar()
ttk.Label(window, text = "No. Appear:").grid(row = 4, column = 0,sticky="e")
noApp_e = tk.Entry(window, width=25, textvariable=noApp_v).grid(row=4,column=1,sticky="w")

#HD
HD_v = tk.StringVar()
ttk.Label(window, text = "HD:").grid(row = 5, column = 0,sticky="e")
HD_e = tk.Entry(window, width=25, textvariable=HD_v).grid(row=5,column=1,sticky="w")

#AC
AC_v = tk.StringVar()
ttk.Label(window, text = "AC:").grid(row = 6, column = 0,sticky="e")
AC_e = tk.Entry(window, width=25, textvariable=AC_v).grid(row=6,column=1,sticky="w")

#Move
MV_v = tk.StringVar()
ttk.Label(window, text = "Move:").grid(row = 7, column = 0,sticky="e")
MV_e = tk.Entry(window, width=25, textvariable=MV_v).grid(row=7,column=1,sticky="w")

#THAC0 Box
BX_v = tk.IntVar()
ADD_v = tk.IntVar()
BX_cb = tk.Checkbutton(window, text="B/X", variable=BX_v, onvalue=1, offvalue=0).grid(row=8,column=1,sticky="e")
ADD_cb = tk.Checkbutton(window, text="ADV", variable=ADD_v, onvalue=1, offvalue=0).grid(row=9,column=1,sticky="e")

#Attack
attack_v = tk.StringVar()
ttk.Label(window, text = "Attack:").grid(row = 8, column = 0,sticky="e")
attack_e = tk.Entry(window, width=25, textvariable=attack_v).grid(row=8,column=1,sticky="w")

#Damage
damage_v = tk.StringVar()
ttk.Label(window, text = "Damage:").grid(row = 9, column = 0,sticky="e")
damage_e = tk.Entry(window, width=25, textvariable=damage_v).grid(row=9,column=1,sticky="w")

#Special Atk
spec_attack_v = tk.StringVar()
ttk.Label(window, text = "Special Attack:").grid(row = 10, column = 0,sticky="e")
spec_attack_e = tk.Entry(window, width=25, textvariable=spec_attack_v).grid(row=10,column=1,sticky="w")

#Special Def
spec_def_v = tk.StringVar()
ttk.Label(window, text = "Special Defense:").grid(row = 11, column = 0,sticky="e")
spec_def_e = tk.Entry(window, width=25, textvariable=spec_def_v).grid(row=11,column=1,sticky="w")

#Saving Throw
saving_throw_v = tk.StringVar()
ttk.Label(window, text = "Saving Throw:").grid(row = 12, column = 0,sticky="e")
saving_throw_e = tk.Entry(window, width=25, textvariable=saving_throw_v).grid(row=12,column=1,sticky="w")

#Morale
morale_v = tk.StringVar()
ttk.Label(window, text = "Morale:").grid(row = 13, column = 0,sticky="e")
morale_e = tk.Entry(window, width=25, textvariable=morale_v).grid(row=13,column=1,sticky="w")

#Treasure
treasure_v = tk.StringVar()
ttk.Label(window, text = "Treasure:").grid(row = 14, column = 0,sticky="e")
treasure_e = tk.Entry(window, width=25, textvariable=treasure_v).grid(row=14,column=1,sticky="w")

#Alignment
alignment_v = tk.StringVar()
ttk.Label(window, text = "Alignment:").grid(row = 15, column = 0,sticky="e")
alignment_e = tk.Entry(window, width=25, textvariable=alignment_v).grid(row=15,column=1,sticky="w")

#Desc
ttk.Label(window, text = "Description:").grid(row = 16, column = 0,sticky="e")
desc_e = tk.Text(window, width=25, height=5)
desc_e.grid(row=16,column=1,sticky="w")

#color
color_v = tk.StringVar()
color_v.set("d8e9d2")
color_e = ttk.Entry(window,textvariable=color_v, width=7).grid(row=17,column=0,sticky="w")

#OUTPUT
output_e = tk.Text(window, width=36, height=8)
output_e.grid(row=18,column=0, columnspan=2)

table_v = tk.StringVar()
table_e = ttk.Entry(window,width=36,textvariable=table_v).grid(row=19,column=0,columnspan=2)

#button
def crunch():
    blam = "====== " + name_v.get() + " ======\n"
    blam += "| @#" + color_v.get() + ": **Type:** " + typeCB.get() + "\\\\ "
    blam += "**Terrain:** " + terrainCB.get() + "\\\\ "
    blam += "**Rarity:** " + rareCB.get() + "\\\\ "
    blam += "**No. Appear:** " + noApp_v.get() + "\\\\ "
    blam += "**Hit Die:** " + HD_v.get() + "\\\\ "
    
    defense = int(AC_v.get())
    if BX_v.get() == 1:
        defense = 19 - defense
    elif ADD_v.get() == 1:
        defense = 20 - defense
    blam += "**Armor Class:** " + str(defense) + "\\\\ "
    
    blam += "**Move:** " + MV_v.get() + "\\\\ "
    
    attack = int(attack_v.get().split(" ")[0])
    if BX_v.get() == 1:
        attack = 19 - attack
    elif ADD_v.get() == 1:
        attack = 20 - attack
    blam += "**Attack:** +" + str(attack) + attack_v.get().split(" ")[1] + "\\\\ "
    
    blam += "**Damage:** " + damage_v.get() + "\\\\ "
    if spec_attack_v.get() != "":
        blam += "**Special Attack:** " + spec_attack_v.get() + "\\\\ "
    if spec_def_v.get() != "":
        blam += "**Special Defense:** " + spec_def_v.get() + "\\\\ "
    
    saves = saving_throw_v.get().split(" ")
    saveD = saves[0]
    saveR = saves[1]
    saveH = saves[2]
    saveB = saves[3]
    saveS = saves[4]
    
    blam += "**Saving Throw:** D" + saveD + " R" + saveR + " H" + saveH + " B" + saveB + " S" + saveS + "\\\\ "
    
    blam += "**Morale:** " + morale_v.get() + "\\\\ "
    blam += "**Treasure:** [[ttrpg:treasure:" + treasure_v.get() + "]]\\\\ "
    blam += "**Alignment:** " + alignment_v.get() + "  |\n"
    blam += "===== Description =====\n" + desc_e.get("1.0", tk.END)
    
    output_e.delete(1.0, tk.END)
    output_e.insert(1.0, blam)
    
    slam = "|  @#" + color_v.get() + ": [[.monsters:" + name_v.get() + "]]  |  " + HD_v.get() + "  |  " + typeCB.get() + "  |  " + rareCB.get() + "  |  " + terrainCB.get() + "  |\n"
    table_v.set("")
    table_v.set(slam)
    
    name_v.set("")
    noApp_v.set("")
    HD_v.set("")
    AC_v.set("")
    MV_v.set("")
    attack_v.set("")
    damage_v.set("")
    spec_attack_v.set("")
    spec_def_v.set("")
    saving_throw_v.set("")
    morale_v.set("")
    treasure_v.set("")
    alignment_v.set("")
    
    desc_e.delete(1.0, tk.END)
    
ttk.Button(window, text="BLAM!", command=crunch).grid(row=17,column=1)
window.mainloop()