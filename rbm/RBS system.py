import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
import time
import pyqrcode
from pyqrcode import create
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import png
import pymysql as pym
def Restaurant():
    root=Tk()
    root.resizable(0,0)
    root.geometry("1100x600+0+0")
    root.title("Restaurant Billing System")
    root.configure(background='black')
                                   
#=========================================== Frame ========================================================
    BottomMainFrame = Frame(root, width=1000, height=770, bd=12, bg='silver',relief="raise")
    BottomMainFrame.place(x=0,y=85)
    
    Label(text='Restaurant Billing System',font=('areial',45,'bold')).place(x=300,y=2)

    f1 = Frame(BottomMainFrame, width=500, height=770, bd=12, bg='Blue',relief=SUNKEN)
    f1.pack(side=LEFT)

    f1top = Frame(f1, width=500, height=570, bd=12, relief="raise")
    f1top.pack(side=TOP)
    
    f1bottom = Frame(f1, width=500, height=200, bd=12, relief="raise")
    f1bottom.pack(side=BOTTOM)


    f2 = Frame(BottomMainFrame, width=400, height=770, bd=12, bg='Blue',relief=SUNKEN)
    f2.pack(side=RIGHT)
    
    f2Top = Frame(f2, width=400, height=450, bd=4, relief="raise")
    f2Top.pack(side=TOP)
    
    f2Bottom = Frame(f2, width=400, height=450,bd=4, relief="raise")
    f2Bottom.pack(side=BOTTOM)

    RightMainFrame = Frame(root, width=355, height=855, bd=12, bg='silver',relief="raise")
    RightMainFrame.place(x=1010,y=115)
    
    f3 = Frame(RightMainFrame, width=325, height=600, bd=12, bg='Blue',relief=SUNKEN)
    f3.pack(side=RIGHT)

    f3Top = Frame(f3, width=325, height=600, bd=4, relief="raise")
    f3Top.pack(side=TOP)

    f3bottom = Frame(f3, width=500, height=200, bd=12, relief="raise")
    f3bottom.pack(side=BOTTOM)

# =========================================== VARIABLES =============================================================                 
    Receipt_Ref = StringVar()
    DateofOrder = StringVar()
    DateofOrder.set(time.strftime("%d/%m/%y"))

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()
    var16 = IntVar()
    var17 = IntVar()
    var18 = IntVar()
    var19 = IntVar()
    var20 = IntVar()
    var21 = IntVar()
    var22 = IntVar()
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)

#==================================== BOTTOM FRAME : FRAME 1 VARIABLES ==================================================
    varFries = StringVar()
    varSalad = StringVar()
    varHamburger = StringVar()
    varPizza = StringVar()
    varChickenSalad = StringVar()
    varCheeseSandwich = StringVar()
    varChickenSandwich = StringVar()
    varMushroomSandwich = StringVar()

    varFries.set(0)
    varSalad.set(0)
    varHamburger.set(0)
    varPizza.set(0)
    varChickenSalad.set(0)
    varCheeseSandwich.set(0)
    varChickenSandwich.set(0)
    varMushroomSandwich.set(0)

#==================================== BOTTOM FRAME : FRAME 2 TOP FRAME VARIABLES ==================================================
    varChocoBrownie = StringVar()
    varGulabJamun = StringVar()
    varBlack_Forest = StringVar()
    varRasmalai = StringVar()
    varJalebi = StringVar()

    varChocoBrownie.set(0)
    varGulabJamun.set(0)
    varBlack_Forest.set(0)
    varRasmalai.set(0)
    varJalebi.set(0)

#==================================== BOTTOM FRAME : FRAME 2 BOTTOM FRAME VARIABLES ==================================================
    varTotal = StringVar()
    varCGST = StringVar()
    varSGST = StringVar()
    varServiceCharge = StringVar()
    varPay = StringVar()
    varTotal.set(0)
    varCGST.set(0)
    varSGST.set(0)
    varServiceCharge.set(0)
    varPay.set(0)
    
#====================================BOTTOM FRAME : FRAME 3 VARIABLES==================================================
    varTea = StringVar()
    varCola = StringVar()
    varCoffee = StringVar()
    varOrange = StringVar()
    varWater= StringVar()
    varChocolateShake = StringVar()
    varFruitCocktail = StringVar()
    varVanillaShake = StringVar()
    varOreoKrusher = StringVar()

    varTea.set(0)
    varCoffee.set(0)
    varCola.set(0)
    varOrange.set(0)
    varWater.set(0)
    varChocolateShake.set(0)
    varFruitCocktail.set(0)
    varVanillaShake.set(0)
    varOreoKrusher.set(0)

#==================================== BUTTON FUNCTIONS ============================================
    def iExit():
        qExit = messagebox.askyesno("Restraunt Management","Do you want to quit ?")
        if qExit > 0:
            root.destroy()
            Home()
        
#========================================== RESET FUNCTION ===============================================
    def Reset():
        varFries.set(0)
        varSalad.set(0)
        varHamburger.set(0)
        varPizza.set(0)
        varChickenSalad.set(0)
        varCheeseSandwich.set(0)
        varChickenSandwich.set(0)
        varMushroomSandwich.set(0)
        varChocoBrownie.set(0)
        varGulabJamun.set(0)
        varBlack_Forest.set(0)
        varRasmalai.set(0)
        varJalebi.set(0)
        varTotal.set(0)
        varCGST.set(0)
        varSGST.set(0)
        varServiceCharge.set(0)
        varPay.set(0)
        varTea.set(0)
        varCoffee.set(0)
        varCola.set(0)
        varOrange.set(0)
        varWater.set(0)
        varChocolateShake.set(0)
        varFruitCocktail.set(0)
        varVanillaShake.set(0)
        varOreoKrusher.set(0)

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)
        var17.set(0)
        var18.set(0)
        var19.set(0)
        var20.set(0)
        var21.set(0)
        var22.set(0)

        txtFries.configure(state=DISABLED)
        txtSalad.configure(state=DISABLED)
        txtHamburger.configure(state=DISABLED)
        txtPizza.configure(state=DISABLED)
        txtChickenSalad.configure(state=DISABLED)
        txtCheeseSandwich.configure(state=DISABLED)
        txtChickenSandwich.configure(state=DISABLED)
        txtMushroomSandwich.configure(state=DISABLED)
        txtChocoBrownie.configure(state=DISABLED)
        txtGulabJamun.configure(state=DISABLED)
        txtBlack_Forest.configure(state=DISABLED)
        txtRasmalai.configure(state=DISABLED)
        txtJalebi.configure(state=DISABLED)
        txtTotal.configure(state=DISABLED)
        txtCGST.configure(state=DISABLED)
        txtSGST.configure(state=DISABLED)
        txtServiceCharge.configure(state=DISABLED)
        txtTea.configure(state=DISABLED)
        txtCoffee.configure(state=DISABLED)
        txtCola.configure(state=DISABLED)
        txtOrange.configure(state=DISABLED)
        txtWater.configure(state=DISABLED)
        txtChocolateShake.configure(state=DISABLED)
        txtOreoKrusher.configure(state=DISABLED)
        txtVanillaShake.configure(state=DISABLED)
        txtOreoKrusher.configure(state=DISABLED)

# ================================= RECEIPT FUMCTION ===============================
    def Receipt():
        if varTotal.get()=="0":
            show1 = messagebox.showerror("Restraunt Management","Click On Total")
        else:
            roor = Tk()
            roor.geometry("600x700+0+0")
            roor.resizable(0,0)
            f1 = Frame(roor, width = 1600, height = 700, bd = 12, relief = "raise")
            f1.pack()
            lblReceipt = Label(f1, font=('arial', 12, 'bold'), text="Receipt", bd=2, anchor='w')
            lblReceipt.grid(row=0, column=0, sticky=W)
            txtReceipt = Text(f1, width=64, height=35, bg="white", bd=8, font=('arial', 11, 'bold'))
            txtReceipt.grid(row=1, column=0)
            txtReceipt.delete("1.0", END)
            x = random.randint(1000, 500890)
            randomRef = str(x)
            Receipt_Ref.set("BILL" + randomRef)
            txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+ Receipt_Ref.get() + '\t\t\t' + DateofOrder.get()+"\n")
            txtReceipt.insert(END, 'Items\t\t\t\t' + "No. of Items \n\n")
            txtReceipt.insert(END, 'Fries:\t\t\t\t\t' + varFries.get() + "\n")
            txtReceipt.insert(END, 'Salad: \t\t\t\t\t' + varSalad.get() + "\n")
            txtReceipt.insert(END, 'HamBurger: \t\t\t\t\t' + varHamburger.get() + "\n")
            txtReceipt.insert(END, 'Pizza: \t\t\t\t\t' + varPizza.get() + "\n")
            txtReceipt.insert(END, 'Chicken Salad: \t\t\t\t\t' + varChickenSalad.get() + "\n")
            txtReceipt.insert(END, 'Cheese Sandwhich: \t\t\t\t\t' + varCheeseSandwich.get() + "\n")
            txtReceipt.insert(END, 'Chicken Sandwhich: \t\t\t\t\t' + varChickenSandwich.get() + "\n")
            txtReceipt.insert(END, 'Mushroom Sandwhich: \t\t\t\t\t' + varMushroomSandwich.get() + "\n")
            txtReceipt.insert(END, 'Choco Brownie: \t\t\t\t\t' + varChocoBrownie.get() + "\n")
            txtReceipt.insert(END, 'Gulab Jamun: \t\t\t\t\t' + varGulabJamun.get() + "\n")
            txtReceipt.insert(END, 'Black_Forest: \t\t\t\t\t' + varBlack_Forest.get() + "\n")
            txtReceipt.insert(END, 'RasMalai: \t\t\t\t\t' + varRasmalai.get() + "\n")
            txtReceipt.insert(END, 'Jalebi: \t\t\t\t\t' + varJalebi.get() + "\n")
            txtReceipt.insert(END, 'Tea: \t\t\t\t\t' + varTea.get() + "\n")
            txtReceipt.insert(END, 'Coffee: \t\t\t\t\t' + varCoffee.get() + "\n")
            txtReceipt.insert(END, 'Cola: \t\t\t\t\t' + varCola.get() + "\n")
            txtReceipt.insert(END, 'Orange Juice: \t\t\t\t\t' + varOrange.get() + "\n")
            txtReceipt.insert(END, 'Water: \t\t\t\t\t' + varWater.get() + "\n")
            txtReceipt.insert(END, 'Chocolate Shake: \t\t\t\t\t' + varChocolateShake.get() + "\n")
            txtReceipt.insert(END, 'Fruit Cocktail: \t\t\t\t\t' + varFruitCocktail.get() + "\n")
            txtReceipt.insert(END, 'Vanilla Shake: \t\t\t\t\t' + varVanillaShake.get() + "\n")
            txtReceipt.insert(END, 'Oreo Krusher: \t\t\t\t\t' + varOreoKrusher.get() + "\n")
            txtReceipt.insert(END, '\nTotal Cost of Food: \t\t' + varTotal.get() + "\nCGST:\t\t" +
                              varCGST.get() + "\nSGST:\t\t" +varSGST.get() + "\nService Charge:\t\t" +
                              varServiceCharge.get() + "\nTotal Payble amount:\t\t" + varPay.get())
            text_file=open("Reciept.txt",'w')
            text_file.write(txtReceipt.get(1.0,END))
            text_file.close
            roor.mainloop()
        
#================================================ PRICE LIST =======================================
    def price_list():
        roo = Tk()
        roo.geometry("600x700+0+0")
        roo.title("Price List")

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
        lblinfo.grid(row=0, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="white", anchor=W)
        lblinfo.grid(row=0, column=2)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
        lblinfo.grid(row=0, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries", fg="steel blue", anchor=W)
        lblinfo.grid(row=1, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="105", fg="steel blue", anchor=W)
        lblinfo.grid(row=1, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Salad", fg="steel blue", anchor=W)
        lblinfo.grid(row=2, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="120", fg="steel blue", anchor=W)
        lblinfo.grid(row=2, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Hamburger", fg="steel blue", anchor=W)
        lblinfo.grid(row=3, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="100", fg="steel blue", anchor=W)
        lblinfo.grid(row=3, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza", fg="steel blue", anchor=W)
        lblinfo.grid(row=4, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="190", fg="steel blue", anchor=W)
        lblinfo.grid(row=4, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Salad", fg="steel blue", anchor=W)
        lblinfo.grid(row=5, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="250", fg="steel blue", anchor=W)
        lblinfo.grid(row=5, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Sandwhich", fg="steel blue", anchor=W)
        lblinfo.grid(row=6, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="200", fg="steel blue", anchor=W)
        lblinfo.grid(row=6, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Sandwhich", fg="steel blue", anchor=W)
        lblinfo.grid(row=7, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="180", fg="steel blue", anchor=W)
        lblinfo.grid(row=7, column=3)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Mushroom Sandwich", fg="steel blue", anchor=W)
        lblinfo.grid(row=8, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="150", fg="steel blue", anchor=W)
        lblinfo.grid(row=8, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chocolate Brownie", fg="steel blue", anchor=W)
        lblinfo.grid(row=9, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="139", fg="steel blue", anchor=W)
        lblinfo.grid(row=9, column=3)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Hot Gulab Jamun with Icecream", fg="steel blue",anchor=W)
        lblinfo.grid(row=10, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="250", fg="steel blue", anchor=W)
        lblinfo.grid(row=10, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Black_Forest", fg="steel blue", anchor=W)
        lblinfo.grid(row=11, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="80", fg="steel blue", anchor=W)
        lblinfo.grid(row=11, column=3)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Rasmalai", fg="steel blue", anchor=W)
        lblinfo.grid(row=12, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="120", fg="steel blue", anchor=W)
        lblinfo.grid(row=12, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Jalebi", fg="steel blue", anchor=W)
        lblinfo.grid(row=13, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="90", fg="steel blue", anchor=W)
        lblinfo.grid(row=13, column=3)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Tea", fg="steel blue", anchor=W)
        lblinfo.grid(row=14, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="49", fg="steel blue", anchor=W)
        lblinfo.grid(row=14, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Coffee", fg="steel blue", anchor=W)
        lblinfo.grid(row=15, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="79", fg="steel blue", anchor=W)
        lblinfo.grid(row=15, column=3)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cola", fg="steel blue", anchor=W)
        lblinfo.grid(row=16, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="20", fg="steel blue", anchor=W)
        lblinfo.grid(row=16, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Orange Juice", fg="steel blue", anchor=W)
        lblinfo.grid(row=17, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
        lblinfo.grid(row=17, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Mineral Water", fg="steel blue", anchor=W)
        lblinfo.grid(row=18, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
        lblinfo.grid(row=18, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chocolate Shake", fg="steel blue", anchor=W)
        lblinfo.grid(row=19, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
        lblinfo.grid(row=19, column=3)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fruit Cocktail", fg="steel blue", anchor=W)
        lblinfo.grid(row=20, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="105", fg="steel blue", anchor=W)
        lblinfo.grid(row=20, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Vanilla Shake", fg="steel blue", anchor=W)
        lblinfo.grid(row=21, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="125", fg="steel blue", anchor=W)
        lblinfo.grid(row=21, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Oreo Krusher", fg="steel blue", anchor=W)
        lblinfo.grid(row=22, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
        lblinfo.grid(row=22, column=3)
        roo.mainloop()

# ========================================== TOTAL FUNCTION ============================================
    def TotalCost():
        global iTotal,cgst,sgst,service_charge
        if varFries.get()==""  or varSalad.get()=="" or varHamburger.get()=="" or varPizza.get()=="" or varChickenSalad.get()=="" or varCheeseSandwich.get()=="" or varChickenSandwich.get()=="" or varMushroomSandwich.get()=="" or varChocoBrownie.get()=="" or varGulabJamun.get()=="" or varBlack_Forest.get()=="" or varRasmalai.get()=="" or varJalebi.get()=="" or varTea.get()=="" or varCola.get()=="" or varCoffee.get()=="" or varOrange.get()=="" or varWater.get()=="" or varChocolateShake.get()=="" or varVanillaShake.get()=="" or varFruitCocktail.get()=="" or varOreoKrusher.get()=="" :
            show2 = messagebox.showerror("Restraunt Billing System","Please enter a value ?")
        try:
            m1 = float(varFries.get())
            m2 = float(varSalad.get())
            m3 = float(varHamburger.get())
            m4 = float(varPizza.get())
            m5 = float(varChickenSalad.get())
            m6 = float(varCheeseSandwich.get())
            m7 = float(varChickenSandwich.get())
            m8 = float(varMushroomSandwich.get())
            m9 = float(varChocoBrownie.get())
            m10 = float(varGulabJamun.get())
            m11 = float(varBlack_Forest.get())
            m12 = float(varRasmalai.get())
            m13 = float(varJalebi.get())
            m14 = float(varTea.get())
            m15 = float(varCola.get())
            m16 = float(varCoffee.get())
            m17 = float(varOrange.get())
            m18 = float(varWater.get())
            m19 = float(varChocolateShake.get())
            m20 = float(varVanillaShake.get())
            m21 = float(varFruitCocktail.get())
            m22 = float(varOreoKrusher.get())
            
            iTotal = (m1*105 + m2*120 + m3*100 + m4*190 + m5*250 + m6*200 + m7*180 + m8*150 + m9*139 +
                      m10*250 + m11*80 + m12*120 + m13*90+ m14*49 + m15*79 + m16*20 + m17*50 +
                      m18*25 + m19*50 + m20*105 + m21*125 + m21*50)
            striTotal = str('Rs'+str(iTotal))
            varTotal.set(striTotal)

            cgst = (9/100)*iTotal
            strcgst = 'Rs',str(cgst)
            varCGST.set(strcgst)

            sgst = (9/100)*iTotal
            strsgst = 'Rs',str(sgst)
            varSGST.set(strsgst)

            service_charge = 0.1*iTotal
            strService_charge = "Rs",str(service_charge)
            varServiceCharge.set(strService_charge)

            strPay = 'Rs', str('%.2f'%(iTotal+cgst+sgst+service_charge))
            varPay.set(strPay)
        except ValueError:
            pass
     
#========================================== PAY FUNCTION ==============================================
    def Pay():
        if varTotal.get()=="Rs0.0" or varTotal.get()=="0" :
            show2 = messagebox.showerror("Restraunt Billing System","Please! select the items.")
           
        else:
            try:
                strPay = str('Pay Rs ' + str('%.2f'%(iTotal+cgst+sgst+service_charge)))
                print(strPay)
                qpay = messagebox.askyesno("Restraunt Billing System","Do you want to Pay the Money ?")
                if qpay > 0:
                    root.destroy()
                    qr = tk.Tk()
                    qr.resizable(0,0)
                    qr.geometry("500x500")
                    qr.configure(background='#F25252')
                    qr.title("Qr Code")
                
                    l2=tk.Label(qr,padx=20,pady=1,bd=14,fg="black",bg='#F25252',font=('arial',25,'bold'),
                                text='Pay Using QR Code here,')
                    l2.place(x=35,y=0)
                
                    def back():
                        qpay = messagebox.askyesno("Restraunt Billing System","Do you want to Continue With Your Order ?")
                        if qpay > 0:
                            qr.destroy()
                            Restaurant()
                        else:
                            qr.destroy()
                        
                    def my_generate():
                        global my_img
                        my_qr = pyqrcode.create(strPay) 
                        #my_qr.png('my_qr1.png', module_color=[0, 0, 0, 128], background=[0xff, 0xcc, 0xcc])
                        my_qr = my_qr.xbm(scale=12)
                        my_img=tk.BitmapImage(data=my_qr)
                        l1.config(image=my_img)
                        
                    l1=tk.Label(qr,bg='#F25252')
                    l1.place(x=65,y=55)
                    
                    b1=tk.Button(qr,padx=20,pady=1,bd=14,fg="white",bg='green',font=('arial',16,'bold'),width=4,
                                 text="Pay Now",command=lambda:my_generate())
                    b1.place(x=115,y=425)
                        
                    btnexit=Button(qr,padx=20,pady=1,bd=14,fg="white",bg='red',font=('arial',16,'bold'),width=4,
                                   text="Back",command = back)
                    btnexit.place(x=300,y=425)
                    qr.mainloop()
            except NameError:
                pass
        
# ============================================ CHECKBOX FUNCTION =========================================
    def a():
        if var1.get() == 1:
            txtFries.configure(state=NORMAL)
            varFries.set("")
        elif var1.get() == 0:
            txtFries.configure(state=DISABLED)
            varFries.set("0")

    def b():
        if var2.get() == 1:
            txtSalad.configure(state=NORMAL)
            varSalad.set("")
        elif var2.get() == 0:
            txtSalad.configure(state=DISABLED)
            varSalad.set("0")

    def c():
        if var3.get() == 1:
            txtHamburger.configure(state=NORMAL)
            varHamburger.set("")
        elif var3.get() == 0:
            txtHamburger.configure(state=DISABLED)
            varHamburger.set("0")

    def d():
        if var4.get() == 1:
            txtPizza.configure(state=NORMAL)
            varPizza.set("")
        elif var4.get() == 0:
            txtPizza.configure(state=DISABLED)
            varPizza.set("0")

    def e():
        if var5.get() == 1:
            txtChickenSalad.configure(state=NORMAL)
            varChickenSalad.set("")
        elif var5.get() == 0:
            txtChickenSalad.configure(state=DISABLED)
            varChickenSalad.set("0")

    def f():
        if var6.get() == 1:
            txtCheeseSandwich.configure(state=NORMAL)
            varCheeseSandwich.set("")
        elif var6.get() == 0:
            txtCheeseSandwich.configure(state=DISABLED)
            varCheeseSandwich.set("0")

    def g():
        if var7.get() == 1:
            txtChickenSandwich.configure(state=NORMAL)
            varChickenSandwich.set("")
        elif var7.get() == 0:
            txtChickenSandwich.configure(state=DISABLED)
            varChickenSandwich.set("0")

    def h():
        if var8.get() == 1:
            txtMushroomSandwich.configure(state=NORMAL)
            varMushroomSandwich.set("")
        elif var8.get() == 0:
            txtMushroomSandwich.configure(state=DISABLED)
            varMushroomSandwich.set("0")

    def i():
        if var9.get() == 1:
            txtChocoBrownie.configure(state=NORMAL)
            varChocoBrownie.set("")
        elif var9.get() == 0:
            txtChocoBrownie.configure(state=DISABLED)
            varChocoBrownie.set("0")

    def j():
        if var10.get() == 1:
            txtGulabJamun.configure(state=NORMAL)
            varGulabJamun.set("")
        elif var10.get() == 0:
            txtGulabJamun.configure(state=DISABLED)
            varGulabJamun.set("0")

    def k():
        if var11.get() == 1:
            txtBlack_Forest.configure(state=NORMAL)
            varBlack_Forest.set("")
        elif var11.get() == 0:
            txtBlack_Forest.configure(state=DISABLED)
            varBlack_Forest.set("0")
            
    def l():
        if var12.get() == 1:
            txtRasmalai.configure(state=NORMAL)
            varRasmalai.set("")
        elif var12.get() == 0:
            txtRasmalai.configure(state=DISABLED)
            varRasmalai.set("0")
            
    def m():
        if var13.get() == 1:
            txtJalebi.configure(state=NORMAL)
            varJalebi.set("")
        elif var13.get() == 0:
            txtJalebi.configure(state=DISABLED)
            varJalebi.set("0")
            
    def n():
        if var14.get() == 1:
            txtTea.configure(state=NORMAL)
            varTea.set("")
        elif var14.get() == 0:
            txtTea.configure(state=DISABLED)
            varTea.set("0")
        
    def o():
        if var15.get() == 1:
            txtCola.configure(state=NORMAL)
            varCola.set("")
        elif var15.get() == 0:
            txtCola.configure(state=DISABLED)
            varCola.set("0")
            
    def p():
        if var16.get() == 1:
            txtCoffee.configure(state=NORMAL)
            varCoffee.set("")
        elif var16.get() == 0:
            txtCoffee.configure(state=DISABLED)
            varCoffee.set("0")
            
    def q():
        if var17.get() == 1:
            txtOrange.configure(state=NORMAL)
            varOrange.set("")
        elif var17.get() == 0:
            txtOrange.configure(state=DISABLED)
            varOrange.set("0")
            
    def r():
        if var18.get() == 1:
            txtWater.configure(state=NORMAL)
            varWater.set("")
        elif var18.get() == 0:
            txtWater.configure(state=DISABLED)
            varWater.set("0")

    def s():
        if var19.get() == 1:
            txtChocolateShake.configure(state=NORMAL)
            varChocolateShake.set("")
        elif var19.get() == 0:
            txtChocolateShake.configure(state=DISABLED)
            varChocolateShake.set("0")
            
    def t():
        if var20.get() == 1:
            txtVanillaShake.configure(state=NORMAL)
            varVanillaShake.set("")
        elif var20.get() == 0:
            txtVanillaShake.configure(state=DISABLED)
            varVanillaShake.set("0")
    def u():
        if var21.get() == 1:
            txtFruitCocktail.configure(state=NORMAL)
            varFruitCocktail.set("")
        elif var21.get() == 0:
            txtFruitCocktail.configure(state=DISABLED)
            varFruitCocktail.set("0")
            
    def v():
        if var22.get() == 1:
            txtOreoKrusher.configure(state=NORMAL)
            varOreoKrusher.set("")
        elif var22.get() == 0:
            txtOreoKrusher.configure(state=DISABLED)
            varOreoKrusher.set("0")

# ============================================= FRAME 1 ================================================
    lblMeal = Label(f1top,font=("arial",25,'bold'), text="Fast Meal")
    lblMeal.grid(row=0, column=0)


    Fries = Checkbutton(f1top,text="Fries", variable=var1, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),
                        command=a)
    Fries.grid(row=1, column=0, sticky = W)
    txtFries = Entry(f1top,font=("arial", 18, 'bold'), bd=8,textvariable = varFries, width=4, justify="right",
                     state=DISABLED)
    txtFries.grid(row=1, column=1)
    

    Salad = Checkbutton(f1top, text="Salad", variable=var2, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),
                        command=b)
    Salad.grid(row=2, column=0, sticky = W)
    txtSalad = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varSalad, width=4, justify="right",
                     state=DISABLED)
    txtSalad.grid(row=2, column=1)

    Hamburger = Checkbutton(f1top, text="Hamburger", variable=var3, onvalue=1, offvalue=0,
                            font=("arial", 18, 'bold'),command=c)
    Hamburger.grid(row=3, column=0, sticky = W)
    txtHamburger = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varHamburger, width=4,
                         justify="right",state=DISABLED)
    txtHamburger.grid(row=3, column=1)
    
    Pizza = Checkbutton(f1top, text="Pizza", variable=var4, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),
                              command=d)
    Pizza.grid(row=4, column=0, sticky = W)
    txtPizza = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varPizza, width=4,
                           justify="right",state=DISABLED)
    txtPizza.grid(row=4, column=1)

    ChickenSalad = Checkbutton(f1top, text="Chicken Salad", variable=var5, onvalue=1, offvalue=0,
                               font=("arial",18, 'bold'), command=e)
    ChickenSalad.grid(row=5, column=0, sticky = W)
    txtChickenSalad = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varChickenSalad,
                            width=4, justify="right",state=DISABLED)
    txtChickenSalad.grid(row=5, column=1)

    lblSpace = Label(f1top,text="\n")
    lblSpace.grid(row=6, column=0)
    
    lblSandwich = Label(f1top,font=("arial",25,'bold'), text="Sandwiches")
    lblSandwich.grid(row=7, column=0)

    CheeseSandwich = Checkbutton(f1top, text="Cheese Sandwich", variable=var6, onvalue=1, offvalue=0,
                                 font=("arial", 18, 'bold'), command=f)
    CheeseSandwich.grid(row=8, column=0, sticky = W)
    txtCheeseSandwich = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varCheeseSandwich,
                              width=4, justify="right",state=DISABLED)
    txtCheeseSandwich.grid(row=8, column=1)

    ChickenSandwich = Checkbutton(f1top, text="Chicken Sandwich", variable=var7, onvalue=1, offvalue=0,
                                  font=("arial", 18, 'bold'), command=g)
    ChickenSandwich.grid(row=9, column=0, sticky = W)
    txtChickenSandwich = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varChickenSandwich,
                               width=4, justify="right",state=DISABLED)
    txtChickenSandwich.grid(row=9, column=1)

    MushroomSandwich = Checkbutton(f1top, text="Mushroom Sandwhich", variable=var8, onvalue=1, offvalue=0,
                                   font=("arial", 18, 'bold'), command=h)
    MushroomSandwich.grid(row=10, column=0, sticky = W)
    txtMushroomSandwich = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varMushroomSandwich,
                                width=4, justify="right",state=DISABLED)
    txtMushroomSandwich.grid(row=10, column=1)

#======================================== Receipt Button ===================================================
    btnReceipt=Button(f1bottom,padx=20,pady=2,bd=14,fg="white",bg='red',font=('arial',16,'bold'),
                      width=16,text="GENERATE RECEIPT",command = Receipt)
    btnReceipt.grid(row=0,column=0)
                     
# ====================================== FRAME 2 Top =================================================

    lblMeal = Label(f2Top,font=("arial",25,'bold'), text="Desserts")
    lblMeal.grid(row=0, column=0)

    ChocoBrownie = Checkbutton(f2Top, text="Chocolate Brownie", variable=var9, onvalue=1, offvalue=0,
                               font=("arial", 18, 'bold'), command=i)
    ChocoBrownie.grid(row=1, column=0, sticky = W)
    txtChocoBrownie = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varChocoBrownie, width=4,
                            justify="right",state=DISABLED)
    txtChocoBrownie.grid(row=1, column=1)

    GulabJamun = Checkbutton(f2Top, text="Hot Gulab Jamun with Icecream", variable=var10, onvalue=1, offvalue=0,
                             font=("arial", 18, 'bold'), command=j)
    GulabJamun.grid(row=2, column=0, sticky = W)
    txtGulabJamun = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varGulabJamun, width=4,
                          justify="right",state=DISABLED)
    txtGulabJamun.grid(row=2, column=1)

    Black_Forest = Checkbutton(f2Top, text="Black_Forest", variable=var11, onvalue=1, offvalue=0,
                               font=("arial", 18, 'bold'), command=k)
    Black_Forest.grid(row=3, column=0, sticky = W)
    txtBlack_Forest = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varBlack_Forest, width=4,
                            justify="right",state=DISABLED)
    txtBlack_Forest.grid(row=3, column=1)

    Rasmalai = Checkbutton(f2Top, text="Rasmalai", variable=var12, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),
                           command=l)
    Rasmalai.grid(row=4, column=0, sticky = W)
    txtRasmalai = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varRasmalai, width=4, justify="right",
                        state=DISABLED)
    txtRasmalai.grid(row=4, column=1)

    Jalebi = Checkbutton(f2Top, text="Jalebi", variable=var13, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),
                         command=m)
    Jalebi.grid(row=5, column=0, sticky = W)
    txtJalebi = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varJalebi, width=4, justify="right",
                      state=DISABLED)
    txtJalebi.grid(row=5, column=1)

# ====================================  FRAME 2 BOTTOM ============================================
    lblTotal = Label(f2Bottom, font=("arial", 18, 'bold'), text = "Total", bd=10,fg='green',width=16, anchor='e')
    lblTotal.grid(row=2,column=1)
    txtTotal = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varTotal, width=10, justify="right",
                     state=DISABLED)
    txtTotal.grid(row=2, column=2)

    lblSGST = Label(f2Bottom, font=("arial", 18, 'bold'), text = "SGST @9%", bd=10, width=16, anchor='e')
    lblSGST.grid(row=3,column=1)
    txtSGST = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varSGST, width=10, justify="right",
                    state=DISABLED)
    txtSGST.grid(row=3, column=2)

    lblCGST = Label(f2Bottom, font=("arial", 18, 'bold'), text = "CGST @9%", bd=10, width=16, anchor='e')
    lblCGST.grid(row=4,column=1)
    txtCGST = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varCGST, width=10, justify="right",
                    state=DISABLED)
    txtCGST.grid(row=4, column=2)

    lblServiceCharge = Label(f2Bottom, font=("arial", 18, 'bold'), text = "Service Charge @10%", bd=10, width=16,
                             anchor='e')
    lblServiceCharge.grid(row=5,column=1)
    txtServiceCharge = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varServiceCharge, width=10,
                             justify="right",state=DISABLED)
    txtServiceCharge.grid(row=5, column=2)

#==================================================== BUTTONS ============================================
    btnprice=Button(f2Bottom,padx=20,pady=1, bd=14 ,fg="white",bg='blue',font=('arial' ,16,'bold'),width=5,
                    text="PRICE LIST",command = price_list)
    btnprice.grid(row=2, column=0)

    btnTotal = Button(f2Bottom, padx=20, pady=1, bd=14, fg="white",bg='green',font=("arial", 16, 'bold'), width=5,
                      text="TOTAL", command = TotalCost).grid(row=3, column=0)

    btnReset=Button(f2Bottom,padx=20,pady=1,bd=14,fg="white",bg='brown',font=('arial',16,'bold'),width=5,
                    text="RESET",command=Reset)
    btnReset.grid(row=4,column=0)

    btnExit=Button(f2Bottom,padx=20,pady=1,bd=14,fg="white",bg='red',font=('arial',16,'bold'),width=5,text="EXIT",
                   command = iExit)
    btnExit.grid(row=5,column=0)
         
# =================================================== FRAME 3 ===============================================
    lblDrinks = Label(f3Top,font=("arial",25,'bold'), text="Drinks")
    lblDrinks.grid(row=0, column=0)

    Tea = Checkbutton(f3Top, text="Tea", variable=var14, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),
                      command=n)
    Tea.grid(row=1, column=0, sticky = W)
    txtTea = Entry(f3Top, font=("arial", 18, 'bold'), bd=8, textvariable = varTea, width=4, justify="right",
                   state=DISABLED)
    txtTea.grid(row=1, column=1)
    
    Cola = Checkbutton(f3Top, text="Cola", variable=var15, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),
                       command=o)
    Cola.grid(row=2, column=0, sticky = W)
    txtCola = Entry(f3Top, font=("arial", 18, 'bold'), bd=8, textvariable = varCola, width=4, justify="right",
                    state=DISABLED)
    txtCola.grid(row=2, column=1)
    
    Coffee = Checkbutton(f3Top, text="Coffee", variable=var16, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),
                         command=p)
    Coffee.grid(row=3, column=0, sticky = W)
    txtCoffee = Entry(f3Top, font=("arial", 18, 'bold'), bd=8, textvariable = varCoffee, width=4, justify="right",
                      state=DISABLED)
    txtCoffee.grid(row=3, column=1)
    
    Orange = Checkbutton(f3Top, text="Orange Juice", variable=var17, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),
                         command=q)
    Orange.grid(row=4, column=0, sticky = W)
    txtOrange = Entry(f3Top, font=("arial", 18, 'bold'), bd=8, textvariable = varOrange, width=4, justify="right",
                      state=DISABLED)
    txtOrange.grid(row=4, column=1)
    
    Water = Checkbutton(f3Top, text="Mineral Water", variable=var18, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),
                        command=r)
    Water.grid(row=5, column=0, sticky = W)
    txtWater = Entry(f3Top, font=("arial", 18, 'bold'), bd=8, textvariable = varWater, width=4, justify="right",
                     state=DISABLED)
    txtWater.grid(row=5, column=1)

    ChocolateShake = Checkbutton(f3Top, text="Chocolate Shake", variable=var19, onvalue=1, offvalue=0,
                                 font=("arial", 18, 'bold'), command=s)
    ChocolateShake.grid(row=8, column=0, sticky = W)
    txtChocolateShake = Entry(f3Top, font=("arial", 18, 'bold'), bd=8, textvariable = varChocolateShake, width=4,
                              justify="right",state=DISABLED)
    txtChocolateShake.grid(row=8, column=1)
    
    VanillaShake = Checkbutton(f3Top, text="Vanilla Shake", variable=var20, onvalue=1, offvalue=0,
                               font=("arial", 18, 'bold'), command=t)
    VanillaShake.grid(row=9, column=0, sticky = W)
    txtVanillaShake = Entry(f3Top, font=("arial", 18, 'bold'), bd=8, textvariable = varVanillaShake, width=4,
                            justify="right",state=DISABLED)
    txtVanillaShake.grid(row=9, column=1)
    
    FruitCocktail = Checkbutton(f3Top, text="Fruit Cocktail", variable=var20, onvalue=1, offvalue=0,
                                font=("arial", 18, 'bold'), command=u)
    FruitCocktail.grid(row=10, column=0, sticky = W)
    txtFruitCocktail = Entry(f3Top, font=("arial", 18, 'bold'), bd=8, textvariable = varFruitCocktail,
                             width=4, justify="right",state=DISABLED)
    txtFruitCocktail.grid(row=10, column=1)
    
    OreoKrusher = Checkbutton(f3Top, text="Oreo Krusher", variable=var21, onvalue=1, offvalue=0,
                              font=("arial", 18, 'bold'), command=v)
    OreoKrusher.grid(row=11, column=0, sticky = W)
    txtOreoKrusher = Entry(f3Top, font=("arial", 18, 'bold'), bd=8, textvariable = varOreoKrusher, width=4,
                           justify="right",state=DISABLED)
    txtOreoKrusher.grid(row=11, column=1)
    
    btnPay=Button(f3bottom,padx=20,pady=2,bd=14,fg="white",bg='green',font=('arial',16,'bold'),width=16,text="PAY",
                      command=Pay)
    btnPay.grid(row=0,column=0)  
    root.state('zoomed') 
    root.mainloop()
    
#==================================================== FEED BACK ==================================================================
def feedback():
    global feedback1
    feed = Tk()
    feed.geometry("600x500")
    feed.resizable(0,0)
    feed.config(bg='Blue')
    feed.title("Feedback Form")
    bkg = "#636e72"

    lb1 = Label(feed, font=("Calisto MT", 15, "bold"), text="Thanks for Visiting!", fg="black").pack(side=TOP)
    lbl2 = Label(feed, font=("calisto MT", 15), text="We're glad you chose us ! Please tell us how it was!",
                 fg="black").pack(side=TOP)

    label_firstname = tk.Label(feed, text="Name: ", font=('verdana',12,'bold'), fg="white", bg=bkg)
    entry_firstname = tk.Entry(feed, font=('verdana',12))

    label_email = tk.Label(feed, text="Email: ", font=('verdana',12,'bold'),fg="white",bg=bkg)
    entry_email = tk.Entry(feed, font=('verdana',12))

    label_comment = tk.Label(feed, font=('verdana', 12,'bold'),text="Any comments,questions or suggestions ?",
                                        fg="white",bg=bkg, bd=10, anchor=W)
    entry_comment = tk.Text(feed, font=('verdana',12), width=50, height=4)
    
    ratelbl = tk.Label(feed, font=('vardana', 12,'bold'), text="How would you rate us 0 to 5 ?",
                    fg="white",bg=bkg, bd=10, anchor=W).place(x=10, y=185)
    entry_rate = tk.Entry(feed, font=('verdana',12))
 
    def createtable():
        con = pym.connect(host="localhost", user="root", password="tiger", database="feedback")
        cursor = con.cursor()
        tbl="""CREATE TABLE IF NOT EXISTS FEEDBACK(
                       Name text,
                       Email text,
                       Ratings_from_0_to_5 text,
                       Comments text)"""
        cursor.execute(tbl)
        cursor.close()
        
    def insertData():
        createtable()
        con = pym.connect(host="localhost", user="root", password="tiger", database="feedback")
        cursor = con.cursor()
        
        firstname = entry_firstname.get()
        email = entry_email.get()
        rate= entry_rate.get()
        comment = entry_comment.get('1.0',END)
       
        insert_query="insert into FEEDBACK values(%s,%s,%s,%s)"
        vals = (firstname,email,rate,comment)
        cursor.execute(insert_query,vals)
        con.commit()
        '''cursor.execute("select * from feedback")
        data=cursor.fetchall()
        for i in data :
            print(i)
        con.close()
        print(firstname,email,comment)'''
        messagebox.showinfo("Success","Record has been inserted")
        feed.destroy()
        
    def Exit():
        feed.destroy()
        
    button_insert = tk.Button(feed, text="Submit", font=('verdana',14), bg='green',fg='white',
                              command = insertData)
    button_exit = tk.Button(feed, text="Exit", font=('verdana',14), bg='red',fg='white',
                              command = Exit)

    label_firstname.place(x=10, y=100)
    entry_firstname.place(x=15, y=135)


    label_email.place(x=280, y=100)
    entry_email.place(x=285, y=135)

    label_comment.place(x=10, y=285)
    entry_comment.place(x=15, y=335)

    entry_rate.place(x=10,y=235)

    button_insert.place(x=100, y=440)
    button_exit.place(x=400, y=440)

    feed.mainloop()
    
def About_us():
    home.destroy()
    about=Tk()
    about.geometry("1100x700+0+0")
    about.config(bg='black')
    about.resizable(0,0)
    
    Label(about,text='About Us',font='impack 50 bold',bg= 'black',fg='blue').pack(fill=X)
 
    logo=Image.open("logo.png")
    re_size=logo.resize((200,300))
    img=ImageTk.PhotoImage(re_size)
    Label(about,image=img).place(x=50,y=150)

    Label(about,text="""Our project Restaurant Billing System generates a bill for customer.
    Billing system are an important part of accounting and finance. Our project
    also generates QRcode for easy transactions""",
          font='impack 14 bold',bg= 'black',fg='white').place(x=300,y=155)

    Label(about,text="This project is done by : \n \n M.Guna Ranjana Reddy \n P.Kamalakar \n K.Jaswanth",
          font='impack 18 bold',bg= 'black',fg='white').place(x=700,y=400)
    def about_home():
        about.destroy()
        Home()
        
    button2= Button(about,text='Home',font='airel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',
                      pady=10, width=10, command=about_home,relief="raise").place(x=950,y=600)
    about.mainloop()
    
def Home():
    global home
    home=Tk()
    home.geometry('1150x650+0+0')
    home.title('Restaurant Billing System')
    home.config(bg='#ED7014')
    home.resizable(0,0)
    
    bg1 = PhotoImage(file = "delhi-restaurants.png")

    label1 = Label( home, image = bg1)
    label1.place(x = 0, y = 0)

    Label(text='Restaurant Billing System',font=('areial',45,'bold')).place(x=250,y=20)
    
    localtime=time.asctime(time.localtime(time.time()))
    lblInfo=Label(font=('arial',20,'bold'),text=localtime,bd=10,anchor='w')
    lblInfo.place(x=425,y=150)
    text= Label(home, text= "")
    
    button= Button(home, text="Place Order",font=('areial',45,'bold'),bg='red',fg='white',
                   command=Home_To_Restaurant,cursor='hand2',relief="raise").place(x=410,y=300)

    feedbtn = Button(home, font=('Calibri', 16, 'bold'), text="Feedback Form", fg="white", bg="green",bd=3, padx=10,
                     cursor='hand2',pady=10, width=10, command=feedback,relief="raise").place(x=100,y=450)
    exitbtn = Button(home, font=('Calibri', 16, 'bold'), text="Exit", fg="white", bg="dark red",bd=3, padx=10,
                     cursor='hand2',pady=10, width=10, command=exit_,relief="raise").place(x=950,y=450)
    aboutbtn = Button(home,text='About Us',font='airel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',
                      pady=10, width=10, command=About_us,relief="raise").place(x=550,y=450)
    home.mainloop()

def exit_():
    home.destroy()
    
def Home_To_Restaurant():
    home.destroy()
    Restaurant()
Home()
