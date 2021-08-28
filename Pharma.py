from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

def main():
    win=Tk()
    app=LoginSystem(win)
    win.mainloop()

#=========================================================== class 1 ===================================================================================

class LoginSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")
    
        lbltitle = Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=10,relief=RIDGE
                                ,bg='white',fg="darkgreen",font=("times new roaman",30,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\Logo.png")
        img1=img1.resize((45,45),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=18)

        # ===============================Data Frame=================================== 
        DataFrame=Frame(self.root,bd=1,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=90,width=1530,height=800)

        DataFrameLeft=LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=20,text="LOGIN INFORMATION",
                                    fg="darkgreen",font=("arial",12,"bold"))

        DataFrameLeft.place(x=210,y=100,width=800,height=350)

        lblusername=Label(DataFrame,font=("arial",18,"bold"),text="UserId",padx=2,pady=4)
        lblusername.place(x=290,y=200)
        txtusername=Entry(DataFrame,font=("arial",18,"bold"),bg="White",bd=2,relief=RIDGE,width=20)
        txtusername.place(x=480,y=200)

        lblpassword=Label(DataFrame,font=("arial",18,"bold"),text="Password",padx=2,pady=4)
        lblpassword.place(x=290,y=250)
        txtpassword=Entry(DataFrame,font=("arial",18,"bold"),bg="White",textvariable="password",bd=2,relief=RIDGE,width=20)
        txtpassword.place(x=480,y=250)

        btnLogin=Button(DataFrame,text="Login",bg="lime",font=("arial",10,"bold"),width=20,fg="Black",pady=4,command=self.window )
        btnLogin.grid(row=0,column=0)
        btnLogin.place(x=480,y=320)

    def window(self):
        self.new_window=Toplevel(self.root)
        self.app=pageSystem(self.new_window)

#=========================================================== class 2 ===================================================================================

class pageSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")
    
        lbltitle = Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=10,relief=RIDGE
                                ,bg='white',fg="darkgreen",font=("times new roaman",30,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\Logo.png")
        img1=img1.resize((45,45),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=18)

        # ===============================Data Frame=================================== 
        DataFrame=Frame(self.root,bd=1,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=90,width=1530,height=800)

        DataFrameLeft=LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=20,text="LOGIN INFORMATION",
                                    fg="darkgreen",font=("arial",12,"bold"))

        DataFrameLeft.place(x=210,y=100,width=1000,height=350)

        btnstaff=Button(DataFrame,text="Staff ",bg="lime",font=("arial",10,"bold"),width=20,fg="Black",pady=4,command=self.window1 )
        btnstaff.grid(row=0,column=0)
        btnstaff.place(x=350,y=200)

        btndrug=Button(DataFrame,text="Drug",bg="lime",font=("arial",10,"bold"),width=20,fg="Black",pady=4,command=self.window2 )
        btndrug.grid(row=0,column=0)
        btndrug.place(x=560,y=200)

        btnmfg=Button(DataFrame,text="Manufacture",bg="lime",font=("arial",10,"bold"),width=20,fg="Black",pady=4,command=self.window3 )
        btnmfg.grid(row=0,column=0)
        btnmfg.place(x=760,y=200)

        btnpurchasemaster=Button(DataFrame,text="Purchase Order Master",bg="lime",font=("arial",10,"bold"),width=20,fg="Black",pady=4,command=self.window4 )
        btnpurchasemaster.grid(row=0,column=0)
        btnpurchasemaster.place(x=960,y=200)

        btnpurchasedetails=Button(DataFrame,text="Purchase Details",bg="lime",font=("arial",10,"bold"),width=20,fg="Black",pady=4,command=self.window5 )
        btnpurchasedetails.grid(row=0,column=0)
        btnpurchasedetails.place(x=350,y=280)

        btncust=Button(DataFrame,text="Customer",bg="lime",font=("arial",10,"bold"),width=20,fg="Black",pady=4,command=self.window6 )
        btncust.grid(row=0,column=0)
        btncust.place(x=560,y=280)

        btnsellsmaster=Button(DataFrame,text="sells Order Master",bg="lime",font=("arial",10,"bold"),width=20,fg="Black",pady=4,command=self.window7 )
        btnsellsmaster.grid(row=0,column=0)
        btnsellsmaster.place(x=760,y=280)

        btnsellsdetails=Button(DataFrame,text="Sells order Details",bg="lime",font=("arial",10,"bold"),width=20,fg="Black",pady=4,command=self.window8 )
        btnsellsdetails.grid(row=0,column=0)
        btnsellsdetails.place(x=960,y=280)


    def window1(self):
        self.new_window=Toplevel(self.root)
        self.app=staffManagementSystem(self.new_window)

    def window2(self):
        self.new_window=Toplevel(self.root)
        self.app=PharmacyManagementSystem(self.new_window)

    def window3(self):
        self.new_window=Toplevel(self.root)
        self.app=ManufacturingSystem(self.new_window)
    
    def window4(self):
        self.new_window=Toplevel(self.root)
        self.app=purchaseSystem(self.new_window)
    
    def window5(self):
        self.new_window=Toplevel(self.root)
        self.app=purchaseorder(self.new_window)

    def window6(self):
        self.new_window=Toplevel(self.root)
        self.app=customer(self.new_window)

    def window7(self):
        self.new_window=Toplevel(self.root)
        self.app=sellsorder(self.new_window)
    
    def window8(self):
        self.new_window=Toplevel(self.root)
        self.app=sellsdetail(self.new_window)

#=========================================================== class 3 ===================================================================================

class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        # ========================== Main Variable ======================================

        self.ref_var=StringVar()
        self.companyname_var=StringVar()
        self.type_var=StringVar()
        self.tablename_var=StringVar()
        self.lotno_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideeffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.productQt_var=StringVar()

        # ====================================================================================
    
        lbltitle = Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE
                                ,bg='white',fg="darkgreen",font=("times new roaman",30,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\Logo.png")
        img1=img1.resize((45,45),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=18)

        # ===============================Data Frame=================================== 
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=90,width=1520,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
                                    fg="darkgreen",font=("arial",12,"bold"))

        DataFrameLeft.place(x=0,y=5,width=1450,height=350)

        # =========================== Label And Entry ====================================

        lblrefno=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Drug Id :",padx=10)
        lblrefno.grid(row=0,column=0,sticky=W)
        txtrefno=Entry(DataFrameLeft,textvariable=self.ref_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtrefno.grid(row=0,column=1)

        lblCmpName=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Company Name :",padx=2,pady=10)
        lblCmpName.grid(row=1,column=0,sticky=W)
        txtCmpName=Entry(DataFrameLeft,textvariable=self.companyname_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtCmpName.grid(row=1,column=1)

        lblTypeofMedicine=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Type of Drug :",padx=2,pady=10)
        lblTypeofMedicine.grid(row=2,column=0,sticky=W)
        txtTypeofMedicine=Entry(DataFrameLeft,textvariable=self.type_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtTypeofMedicine.grid(row=2,column=1)


        # ============================ Add Medicine =========================================

        lblMedicineName=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Drug Name :",padx=2,pady=10)
        lblMedicineName.grid(row=3,column=0,sticky=W)
        txtMedicineName=Entry(DataFrameLeft,textvariable=self.tablename_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtMedicineName.grid(row=3,column=1)

        lblLotNo=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Batch No :",padx=2,pady=10)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,textvariable=self.lotno_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Production Date :",padx=2,pady=10)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtIssueDate.grid(row=5,column=1)

        lblExDate=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Exp Date :",padx=2,pady=10)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFrameLeft,textvariable=self.expdate_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtExDate.grid(row=6,column=1)

        lblUses=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Uses :",padx=2,pady=10)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtUses.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Side Effect :",padx=2,pady=10)
        lblSideEffect.grid(row=0,column=2,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideeffect_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtSideEffect.grid(row=0,column=3)

        lblPrecWarning=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Prec & Warning :",padx=2,pady=10)
        lblPrecWarning.grid(row=1,column=2,sticky=W)
        txtPrecwarning=Entry(DataFrameLeft,textvariable=self.warning_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtPrecwarning.grid(row=1,column=3)

        lblDosage=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Dosage :",padx=2,pady=10)
        lblDosage.grid(row=2,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,textvariable=self.dosage_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtDosage.grid(row=2,column=3)
        
        lblPrice=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Cost Price :",padx=2,pady=10)
        lblPrice.grid(row=3,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,textvariable=self.price_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtPrice.grid(row=3,column=3)
        
        lblProductQt=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Product QT In Hand :",padx=2,pady=10)
        lblProductQt.grid(row=4,column=2,sticky=W)
        txtProductQt=Entry(DataFrameLeft,textvariable=self.productQt_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtProductQt.grid(row=4,column=3)

        # =====================================Image======================================
        lblhome=Label(DataFrameLeft,font=("arial",8,"bold"),text="STAY HOME STAY SAFE",fg="red",padx=10,pady=4)
        lblhome.place(x=1130,y=280)    

        img2=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\Tablets.jpeg")
        img2=img2.resize((350,250),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=1110,y=150)

        # =============================Medicine Add Button================================
        down_frame=Frame(DataFrameLeft,bd=4,relief=RIDGE,bg="Darkgreen")
        down_frame.place(x=570,y=220,width=240,height=75)

        btnAddmed=Button(down_frame,text="ADD",command=self.add_data,bg="lime",font=("arial",9,"bold"),width=15,fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,text="Update",command=self.update,bg="darkgreen",font=("arial",9,"bold"),width=15,fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,text="Delete",command=self.delete,bg="red",font=("arial",9,"bold"),width=15,fg="white",pady=4)
        btnDeletemed.grid(row=0,column=1)

        btnclearmed=Button(down_frame,text="clear",command=self.clear,bg="darkgreen",font=("arial",9,"bold"),width=15,fg="white",pady=4)
        btnclearmed.grid(row=1,column=1)


        #============================= Frame Details ============================================
        Framedeatils=Frame(self.root,bd=5,relief=RIDGE)
        Framedeatils.place(x=0,y=500,width=1530,height=280)

        # ================================== Main Table & Scrollbar =============================
        Table_frame=Frame(Framedeatils,bd=5,relief=RIDGE,padx=20)
        Table_frame.place(x=0,y=1,width=1520,height=280)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table=ttk.Treeview(Table_frame,columns=("reg","companyname","type","tablename","lotno","issuedate",
                            "expdate","uses","sideeffect","warning","dosage","price","productQt")
                            ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("reg",text="Drug Id")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of Drug")
        self.pharmacy_table.heading("tablename",text="Drug name")
        self.pharmacy_table.heading("lotno",text="Batch no")
        self.pharmacy_table.heading("issuedate",text="Production Date")
        self.pharmacy_table.heading("expdate",text="Expiry Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effects")
        self.pharmacy_table.heading("warning",text="Prec & Warning")
        self.pharmacy_table.heading("dosage",text="Dosage ")
        self.pharmacy_table.heading("price",text="Cost Price ")
        self.pharmacy_table.heading("productQt",text="Product Qts In Hand")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tablename",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productQt",width=100)
        self.fatch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)

        # ================================ Main Table =====================================

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.ref_var.get(),
                                                                                                self.companyname_var.get(),
                                                                                                self.type_var.get(),
                                                                                                self.tablename_var.get(),
                                                                                                self.lotno_var.get(),
                                                                                                self.issuedate_var.get(),
                                                                                                self.expdate_var.get(),
                                                                                                self.uses_var.get(),
                                                                                                self.sideeffect_var.get(),
                                                                                                self.warning_var.get(),
                                                                                                self.dosage_var.get(),
                                                                                                self.price_var.get(),
                                                                                                self.productQt_var.get()
                                                                                                ))
        conn.commit()
        self.fatch_data()
        conn.close()

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy")
        row = my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,values=i) 
                conn.commit()
            conn.close()

    def get_cursor(self,ev=""):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]

        self.ref_var.set(row[0]),
        self.companyname_var.set(row[1]),
        self.type_var.set(row[2]),
        self.tablename_var.set(row[3]),
        self.lotno_var.set(row[4])
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideeffect_var.set(row[8]),
        self.warning_var.set(row[9]),
        self.dosage_var.set(row[10]),
        self.price_var.set(row[11]),
        self.productQt_var.set(row[12])

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update pharmacy set cmpName=%s,type=%s,drug_Name=%s,batchno=%s,productiondate=%s,expdate=%s,uses=%s,sideeffect=%s,warning=%s,dosage=%s,cost_price=%s,productQtInHand=%s Where drug_id=%s",(
                                                                                                                                                                                                                self.companyname_var.get(),
                                                                                                                                                                                                                self.type_var.get(),
                                                                                                                                                                                                                self.tablename_var.get(),
                                                                                                                                                                                                                self.lotno_var.get(),
                                                                                                                                                                                                                self.issuedate_var.get(),
                                                                                                                                                                                                                self.expdate_var.get(),
                                                                                                                                                                                                                self.uses_var.get(),
                                                                                                                                                                                                                self.sideeffect_var.get(),
                                                                                                                                                                                                                self.warning_var.get(),
                                                                                                                                                                                                                self.dosage_var.get(),
                                                                                                                                                                                                                self.price_var.get(),
                                                                                                                                                                                                                self.productQt_var.get(),
                                                                                                                                                                                                                self.ref_var.get()
                                                                                                                                                                                                             ))
        conn.commit()
        self.fatch_data()
        conn.close()


    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()

        sql="delete from pharmacy where drug_id=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fatch_data()
        conn.close()



    def clear(self):
        self.ref_var.set(""),
        self.companyname_var.set(""),
        self.type_var.set(""),
        self.tablename_var.set(""),
        self.lotno_var.set("")
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideeffect_var.set(""),
        self.warning_var.set(""),
        self.dosage_var.set(""),
        self.price_var.set(""),
        self.productQt_var.set("")

#=========================================================== class 4 ===================================================================================
                
class staffManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        # ========================== Main Variable ======================================

        self.staffid_var=StringVar()
        self.fieldtype_var=StringVar()
        self.staffname_var=StringVar()
        self.regno_var=StringVar()
        self.sex_var=StringVar()
        self.date_var=StringVar()
        self.phoneno_var=StringVar()
        self.address_var=StringVar()
        self.email_var=StringVar()
        self.userid_var=StringVar()
    
        lbltitle = Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE
                                ,bg='white',fg="darkgreen",font=("times new roaman",30,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\Logo.png")
        img1=img1.resize((45,45),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=18)

        # ===============================Data Frame=================================== 
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=90,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Staff Information",
                                    fg="darkgreen",font=("arial",12,"bold"))

        DataFrameLeft.place(x=0,y=5,width=1450,height=350)

        # =========================== Label And Entry ====================================

        lblstaffid=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Staff Id :",padx=2,pady=15)
        lblstaffid.grid(row=0,column=0,sticky=W)
        txtstaffid=Entry(DataFrameLeft,textvariable=self.staffid_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtstaffid.grid(row=0,column=1)

        lblfieldtype=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Field Type :",padx=2,pady=15)
        lblfieldtype.grid(row=1,column=0,sticky=W)
        txtfieldtype=Entry(DataFrameLeft,textvariable=self.fieldtype_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtfieldtype.grid(row=1,column=1)

        lblStaff_name=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Staff Name :",padx=2,pady=15)
        lblStaff_name.grid(row=2,column=0,sticky=W)
        txtStaff_name=Entry(DataFrameLeft,textvariable=self.staffname_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtStaff_name.grid(row=2,column=1)

        lblReg_No=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Registation Number :",padx=2,pady=15)
        lblReg_No.grid(row=3,column=0,sticky=W)
        txtReg_No=Entry(DataFrameLeft,textvariable=self.regno_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtReg_No.grid(row=3,column=1)

        lblSex=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Gender",padx=2,pady=15)
        lblSex.grid(row=4,column=0,sticky=W)
        txtSex=Entry(DataFrameLeft,textvariable=self.sex_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtSex.grid(row=4,column=1)

        lblDateofBirth=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Date Of Birth :",padx=2,pady=15)
        lblDateofBirth.grid(row=5,column=0,sticky=W)
        txtDateofBirth=Entry(DataFrameLeft,textvariable=self.date_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtDateofBirth.grid(row=5,column=1)

        lblphoneno=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Phone no :",padx=15,pady=15)
        lblphoneno.grid(row=0,column=2,sticky=W)
        txtphoneno=Entry(DataFrameLeft,textvariable=self.phoneno_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtphoneno.grid(row=0,column=3)

        lblAddress=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Address :",padx=15,pady=15)
        lblAddress.grid(row=1,column=2,sticky=W)
        txtAddress=Entry(DataFrameLeft,textvariable=self.address_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtAddress.grid(row=1,column=3)

        lblemail=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Email_id :",padx=15,pady=15)
        lblemail.grid(row=2,column=2,sticky=W)
        txtemail=Entry(DataFrameLeft,textvariable=self.email_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtemail.grid(row=2,column=3)

        lblUserid=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="User_Id :",padx=15,pady=15)
        lblUserid.grid(row=3,column=2,sticky=W)
        txtUserid=Entry(DataFrameLeft,textvariable=self.userid_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtUserid.grid(row=3,column=3)

        # =====================================Image======================================
        lblhome=Label(DataFrameLeft,font=("arial",8,"bold"),text="STAY HOME STAY SAFE",fg="red",padx=10,pady=4)
        lblhome.place(x=1130,y=280)    

        img4=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\lab.jpg")
        img4=img4.resize((300,250),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=1110,y=150)

        # =============================Medicine Add Button================================
        down_frame=Frame(DataFrameLeft,bd=4,relief=RIDGE,bg="lightBlue")
        down_frame.place(x=570,y=220,width=240,height=75)

        btnAddmed=Button(down_frame,text="ADD",command=self.add_data,bg="lime",font=("arial",9,"bold"),width=15,fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,text="Update",command=self.update,bg="lime",font=("arial",9,"bold"),width=15,fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,text="Delete",command=self.delete,bg="red",font=("arial",9,"bold"),width=15,fg="white",pady=4)
        btnDeletemed.grid(row=0,column=1)

        btnclearmed=Button(down_frame,text="clear",command=self.clear,bg="darkgreen",font=("arial",9,"bold"),width=15,fg="white",pady=4)
        btnclearmed.grid(row=1,column=1)

        #============================= Frame Details ============================================
        Framedeatils=Frame(self.root,bd=5,relief=RIDGE)
        Framedeatils.place(x=0,y=500,width=1530,height=280)

        # ================================== Main Table & Scrollbar =============================
        Table_frame=Frame(Framedeatils,bd=5,relief=RIDGE,padx=20)
        Table_frame.place(x=0,y=1,width=1520,height=280)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.staff_Table=ttk.Treeview(Table_frame,columns=("staff id","Field type","staff name","Reg no","sex","date",
                            "phone no","address","email","user id")
                            ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x.config(command=self.staff_Table.xview)
        scroll_y.config(command=self.staff_Table.yview)

        self.staff_Table["show"]="headings"

        self.staff_Table.heading("staff id",text="staff id")
        self.staff_Table.heading("Field type",text="Field type")
        self.staff_Table.heading("staff name",text="staff name")
        self.staff_Table.heading("Reg no",text="Reg no")
        self.staff_Table.heading("sex",text="gender")
        self.staff_Table.heading("date",text="Date of Birth")
        self.staff_Table.heading("phone no",text="phone no")
        self.staff_Table.heading("address",text="Adress")
        self.staff_Table.heading("email",text="Email id")
        self.staff_Table.heading("user id",text="User id")
        self.staff_Table.pack(fill=BOTH,expand=1)

        self.staff_Table.column("staff id",width=100)
        self.staff_Table.column("Field type",width=100)
        self.staff_Table.column("staff name",width=100)
        self.staff_Table.column("Reg no",width=100)
        self.staff_Table.column("sex",width=100)
        self.staff_Table.column("date",width=100)
        self.staff_Table.column("phone no",width=100)
        self.staff_Table.column("address",width=100)
        self.staff_Table.column("email",width=100)
        self.staff_Table.column("user id",width=100)
        self.fatch_data()
        self.staff_Table.bind("<ButtonRelease-1>",self.get_cursor)

        # ================================ Main Table =====================================

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into staff values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.staffid_var.get(),
                                                                                                self.fieldtype_var.get(),
                                                                                                self.staffname_var.get(),
                                                                                                self.regno_var.get(),
                                                                                                self.sex_var.get(),
                                                                                                self.date_var.get(),
                                                                                                self.phoneno_var.get(),
                                                                                                self.address_var.get(),
                                                                                                self.email_var.get(),
                                                                                                self.userid_var.get(),
                                                                                                ))
        conn.commit()
        self.fatch_data()
        conn.close()


    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from staff")
        row = my_cursor.fetchall()
        if len(row)!=0:
            self.staff_Table.delete(*self.staff_Table.get_children())
            for i in row:
                self.staff_Table.insert("",END,values=i) 
                conn.commit()
            conn.close()

    def get_cursor(self,ev=""):
        cursor_row=self.staff_Table.focus()
        content=self.staff_Table.item(cursor_row)
        row=content["values"]

        self.staffid_var.set(row[0]),
        self.fieldtype_var.set(row[1]),
        self.staffname_var.set(row[2]),
        self.regno_var.set(row[3]),
        self.sex_var.set(row[4]),
        self.date_var.set(row[5]),
        self.phoneno_var.set(row[6]),
        self.address_var.set(row[7]),
        self.email_var.set(row[8]),
        self.userid_var.set(row[9])


    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update staff set fieldtype=%s,staffname=%s,regno=%s,sex=%s,date=%s,phoneno=%s,address=%s,email=%s,userid=%s Where staffid=%s",(
                                                                                                                                                                                                                self.fieldtype_var.get(),
                                                                                                                                                                                                                self.staffname_var.get(),
                                                                                                                                                                                                                self.regno_var.get(),
                                                                                                                                                                                                                self.sex_var.get(),
                                                                                                                                                                                                                self.date_var.get(),
                                                                                                                                                                                                                self.phoneno_var.get(),
                                                                                                                                                                                                                self.address_var.get(),
                                                                                                                                                                                                                self.email_var.get(),
                                                                                                                                                                                                                self.userid_var.get(),
                                                                                                                                                                                                                self.staffid_var.get()
                                                                                                                                                                                                             ))
        conn.commit()
        self.fatch_data()
        conn.close()


    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()

        sql="delete from staff where staffid=%s"
        val=(self.staffid_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fatch_data()
        conn.close()


    def clear(self):
        self.staffid_var.set(""),
        self.fieldtype_var.set(""),
        self.staffname_var.set(""),
        self.regno_var.set(""),
        self.sex_var.set(""),
        self.date_var.set(""),
        self.phoneno_var.set(""),
        self.address_var.set(""),
        self.email_var.set(""),
        self.userid_var.set("")

#=========================================================== class 5 ===================================================================================

class ManufacturingSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        # ========================== Main Variable ======================================

        self.mfgid_var=StringVar()
        self.mfgname_var=StringVar()
        self.phoneno_var=StringVar()
        self.address_var=StringVar()
        self.email_var=StringVar()

        # ==================================================================================
    
        lbltitle = Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE
                                ,bg='white',fg="darkgreen",font=("times new roaman",30,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\Logo.png")
        img1=img1.resize((45,45),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=18)

        # ===============================Data Frame=================================== 
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=90,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Manufacturing Information",
                                    fg="darkgreen",font=("arial",12,"bold"))

        DataFrameLeft.place(x=0,y=5,width=1450,height=350)

        # =========================== Label And Entry ====================================

        lblManfid=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Mfg Id :",padx=2,pady=15)
        lblManfid.grid(row=0,column=0,sticky=W)
        txtManfid=Entry(DataFrameLeft,textvariable=self.mfgid_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtManfid.grid(row=0,column=1)

        lblManf_name=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Mfg Name :",padx=2,pady=15)
        lblManf_name.grid(row=2,column=0,sticky=W)
        txtManf_name=Entry(DataFrameLeft,textvariable=self.mfgname_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtManf_name.grid(row=2,column=1)

        lblphoneno=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Phone no :",padx=15,pady=15)
        lblphoneno.grid(row=3,column=0,sticky=W)
        txtphoneno=Entry(DataFrameLeft,textvariable=self.phoneno_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtphoneno.grid(row=3,column=1)

        lblAddress=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Address :",padx=15,pady=15)
        lblAddress.grid(row=4,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft,textvariable=self.address_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtAddress.grid(row=4,column=1)

        lblemail=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Email_id :",padx=15,pady=15)
        lblemail.grid(row=5,column=0,sticky=W)
        txtemail=Entry(DataFrameLeft,textvariable=self.email_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtemail.grid(row=5,column=1)

        # =====================================Image======================================
        lblhome=Label(DataFrameLeft,font=("arial",8,"bold"),text="STAY HOME STAY SAFE",fg="red",padx=10,pady=4)
        lblhome.place(x=1000,y=280)    

        img4=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\lab1.jpg")
        img4=img4.resize((450,250),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=900,y=150)

        # =============================Medicine Add Button================================
        down_frame=Frame(DataFrameLeft,bd=4,relief=RIDGE,bg="lightBlue")
        down_frame.place(x=570,y=60,width=170,height=165)

        btnAddmed=Button(down_frame,text="ADD",command=self.add_data,bg="lime",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,text="Update",command=self.update,bg="lime",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,text="Delete",command=self.delete,bg="red",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)

        btnclearmed=Button(down_frame,text="clear",command=self.clear,bg="darkgreen",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnclearmed.grid(row=3,column=0)

        #============================= Frame Details ============================================
        Framedeatils=Frame(self.root,bd=5,relief=RIDGE)
        Framedeatils.place(x=0,y=500,width=1530,height=280)

        # ================================== Main Table & Scrollbar =============================
        Table_frame=Frame(Framedeatils,bd=5,relief=RIDGE,padx=20)
        Table_frame.place(x=0,y=1,width=1520,height=280)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.Manufacturing_Table=ttk.Treeview(Table_frame,columns=("mfg id","mfg name",
                            "phone no","address","email")
                            ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x.config(command=self.Manufacturing_Table.xview)
        scroll_y.config(command=self.Manufacturing_Table.yview)

        self.Manufacturing_Table["show"]="headings"

        self.Manufacturing_Table.heading("mfg id",text="staff id")
        self.Manufacturing_Table.heading("mfg name",text="staff name")
        self.Manufacturing_Table.heading("phone no",text="phone no")
        self.Manufacturing_Table.heading("address",text="Adress")
        self.Manufacturing_Table.heading("email",text="Email id")
        self.Manufacturing_Table.pack(fill=BOTH,expand=1)

        self.Manufacturing_Table.column("mfg id",width=100)
        self.Manufacturing_Table.column("mfg name",width=100)
        self.Manufacturing_Table.column("phone no",width=100)
        self.Manufacturing_Table.column("address",width=100)
        self.Manufacturing_Table.column("email",width=100)
        self.fatch_data()
        self.Manufacturing_Table.bind("<ButtonRelease-1>",self.get_cursor)

        # ================================ Main Table =====================================

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into mfg values(%s,%s,%s,%s,%s)",(
                                                                                                self.mfgid_var.get(),
                                                                                                self.mfgname_var.get(),
                                                                                                self.phoneno_var.get(),
                                                                                                self.address_var.get(),
                                                                                                self.email_var.get(),
                                                                                                ))
        conn.commit()
        self.fatch_data()
        conn.close()


    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from mfg")
        row = my_cursor.fetchall()
        if len(row)!=0:
            self.Manufacturing_Table.delete(*self.Manufacturing_Table.get_children())
            for i in row:
                self.Manufacturing_Table.insert("",END,values=i) 
                conn.commit()
            conn.close()

    def get_cursor(self,ev=""):
        cursor_row=self.Manufacturing_Table.focus()
        content=self.Manufacturing_Table.item(cursor_row)
        row=content["values"]

        self.mfgid_var.set(row[0]),
        self.mfgname_var.set(row[1]),
        self.phoneno_var.set(row[2]),
        self.address_var.set(row[3]),
        self.email_var.set(row[4]),



    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update mfg set mfgname=%s,phoneno=%s,address=%s,email=%s Where mfgid=%s",(
                                                                                                                self.mfgname_var.get(),
                                                                                                                self.phoneno_var.get(),
                                                                                                                self.address_var.get(),
                                                                                                                self.email_var.get(),
                                                                                                                self.mfgid_var.get()
                                                                                                               ))
        conn.commit()
        self.fatch_data()
        conn.close()


    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()

        sql="delete from mfg where mfgid=%s"
        val=(self.mfgid_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fatch_data()
        conn.close()


    def clear(self):
        self.mfgid_var.set(""),
        self.mfgname_var.set(""),
        self.phoneno_var.set(""),
        self.address_var.set(""),
        self.email_var.set(""),

#=========================================================== class 6 ===================================================================================

class purchaseSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        # ========================== Main Variable ======================================

        self.mfgid_var=StringVar()
        self.mfgname_var=StringVar()
        self.phoneno_var=StringVar()
        self.address_var=StringVar()


        # ==================================================================================
    
        lbltitle = Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE
                                ,bg='white',fg="darkgreen",font=("times new roaman",30,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\Logo.png")
        img1=img1.resize((45,45),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=18)

        # ===============================Data Frame=================================== 
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=90,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Purchase Master Information",
                                    fg="darkgreen",font=("arial",12,"bold"))

        DataFrameLeft.place(x=0,y=5,width=1450,height=350)

        # =========================== Label And Entry ====================================

        lblManfid=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="product no :",padx=2,pady=15)
        lblManfid.grid(row=0,column=0,sticky=W)
        txtManfid=Entry(DataFrameLeft,textvariable=self.mfgid_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtManfid.grid(row=0,column=1)

        lblManf_name=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="date :",padx=2,pady=15)
        lblManf_name.grid(row=2,column=0,sticky=W)
        txtManf_name=Entry(DataFrameLeft,textvariable=self.mfgname_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtManf_name.grid(row=2,column=1)

        lblphoneno=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Mfg id :",padx=2,pady=15)
        lblphoneno.grid(row=3,column=0,sticky=W)
        txtphoneno=Entry(DataFrameLeft,textvariable=self.phoneno_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtphoneno.grid(row=3,column=1)

        lblAddress=Label(DataFrameLeft,font=("arial",10,"bold"),width=30,text="Date of delivery :",padx=2,pady=15)
        lblAddress.grid(row=4,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft,textvariable=self.address_var,font=("arial",8,"bold"),bg="White",bd=2,relief=RIDGE,width=30)
        txtAddress.grid(row=4,column=1)

        # =====================================Image======================================
        lblhome=Label(DataFrameLeft,font=("arial",8,"bold"),text="STAY HOME STAY SAFE",fg="red",padx=10,pady=4)
        lblhome.place(x=1000,y=280)    

        img4=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\lab1.jpg")
        img4=img4.resize((450,250),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=900,y=150)

        # =============================Medicine Add Button================================
        down_frame=Frame(DataFrameLeft,bd=4,relief=RIDGE,bg="lightBlue")
        down_frame.place(x=570,y=60,width=170,height=165)

        btnAddmed=Button(down_frame,text="ADD",command=self.add_data,bg="lime",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,text="Update",command=self.update,bg="lime",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,text="Delete",command=self.delete,bg="red",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)

        btnclearmed=Button(down_frame,text="clear",command=self.clear,bg="darkgreen",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnclearmed.grid(row=3,column=0)

        #============================= Frame Details ============================================
        Framedeatils=Frame(self.root,bd=5,relief=RIDGE)
        Framedeatils.place(x=0,y=500,width=1530,height=280)

        # ================================== Main Table & Scrollbar =============================
        Table_frame=Frame(Framedeatils,bd=5,relief=RIDGE,padx=20)
        Table_frame.place(x=0,y=1,width=1520,height=280)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.Manufacturing_Table=ttk.Treeview(Table_frame,columns=("mfg id","mfg name",
                            "phone no","address")
                            ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x.config(command=self.Manufacturing_Table.xview)
        scroll_y.config(command=self.Manufacturing_Table.yview)

        self.Manufacturing_Table["show"]="headings"

        self.Manufacturing_Table.heading("mfg id",text="product no")
        self.Manufacturing_Table.heading("mfg name",text="purchase order date")
        self.Manufacturing_Table.heading("phone no",text="mfg id")
        self.Manufacturing_Table.heading("address",text="Date of Delivery")
        self.Manufacturing_Table.pack(fill=BOTH,expand=1)

        self.Manufacturing_Table.column("mfg id",width=100)
        self.Manufacturing_Table.column("mfg name",width=100)
        self.Manufacturing_Table.column("phone no",width=100)
        self.Manufacturing_Table.column("address",width=100)
        self.fatch_data()
        self.Manufacturing_Table.bind("<ButtonRelease-1>",self.get_cursor)

        # ================================ Main Table =====================================

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into purchase values(%s,%s,%s,%s)",(
                                                                                                self.mfgid_var.get(),
                                                                                                self.mfgname_var.get(),
                                                                                                self.phoneno_var.get(),
                                                                                                self.address_var.get(),
                                                                                                ))
        conn.commit()
        self.fatch_data()
        conn.close()


    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from purchase")
        row = my_cursor.fetchall()
        if len(row)!=0:
            self.Manufacturing_Table.delete(*self.Manufacturing_Table.get_children())
            for i in row:
                self.Manufacturing_Table.insert("",END,values=i) 
                conn.commit()
            conn.close()

    def get_cursor(self,ev=""):
        cursor_row=self.Manufacturing_Table.focus()
        content=self.Manufacturing_Table.item(cursor_row)
        row=content["values"]

        self.mfgid_var.set(row[0]),
        self.mfgname_var.set(row[1]),
        self.phoneno_var.set(row[2]),
        self.address_var.set(row[3]),



    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update purchase set purchasedate=%s,mfgid=%s,date=%s Where purchaseno=%s",(
                                                                                                                self.mfgname_var.get(),
                                                                                                                self.phoneno_var.get(),
                                                                                                                self.address_var.get(),
                                                                                                                self.mfgid_var.get()
                                                                                                               ))
        conn.commit()
        self.fatch_data()
        conn.close()


    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()

        sql="delete from purchase where purchaseno=%s"
        val=(self.mfgid_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fatch_data()
        conn.close()


    def clear(self):
        self.mfgid_var.set(""),
        self.mfgname_var.set(""),
        self.phoneno_var.set(""),
        self.address_var.set(""),

#=========================================================== class 7 ===================================================================================

class purchaseorder:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        # ========================== Main Variable ======================================

        self.mfgid_var=StringVar()
        self.mfgname_var=StringVar()
        self.phoneno_var=StringVar()
        self.address_var=StringVar()


        # ==================================================================================
    
        lbltitle = Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE
                                ,bg='white',fg="darkgreen",font=("times new roaman",30,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\Logo.png")
        img1=img1.resize((45,45),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=18)

        # ===============================Data Frame=================================== 
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=90,width=1520,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Purchase Order Details Information",
                                    fg="darkgreen",font=("arial",12,"bold"))

        DataFrameLeft.place(x=0,y=5,width=1450,height=350)

        # =========================== Label And Entry ====================================

        lblManfid=Label(DataFrameLeft,font=("arial",12,"bold"),width=30,text="Purchase Order No :",padx=2,pady=15)
        lblManfid.grid(row=0,column=0,sticky=W)
        txtManfid=Entry(DataFrameLeft,textvariable=self.mfgid_var,font=("arial",12,"bold"),bg="White",bd=2,relief=RIDGE,width=40)
        txtManfid.grid(row=0,column=1)

        lblManf_name=Label(DataFrameLeft,font=("arial",12,"bold"),width=30,text="Drug Id :",padx=2,pady=15)
        lblManf_name.grid(row=2,column=0,sticky=W)
        txtManf_name=Entry(DataFrameLeft,textvariable=self.mfgname_var,font=("arial",12,"bold"),bg="White",bd=2,relief=RIDGE,width=40)
        txtManf_name.grid(row=2,column=1)

        lblphoneno=Label(DataFrameLeft,font=("arial",12,"bold"),width=30,text="Quantity Order :",padx=2,pady=15)
        lblphoneno.grid(row=3,column=0,sticky=W)
        txtphoneno=Entry(DataFrameLeft,textvariable=self.phoneno_var,font=("arial",12,"bold"),bg="White",bd=2,relief=RIDGE,width=40)
        txtphoneno.grid(row=3,column=1)

        lblAddress=Label(DataFrameLeft,font=("arial",12,"bold"),width=30,text="Status :",padx=2,pady=15)
        lblAddress.grid(row=4,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft,textvariable=self.address_var,font=("arial",12,"bold"),bg="White",bd=2,relief=RIDGE,width=40)
        txtAddress.grid(row=4,column=1)

        # =====================================Image======================================
        lblhome=Label(DataFrameLeft,font=("arial",8,"bold"),text="STAY HOME STAY SAFE",fg="red",padx=10,pady=4)
        lblhome.place(x=1130,y=280)    

        img4=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\lab1.jpg")
        img4=img4.resize((350,250),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=1110,y=150)

        # =============================Medicine Add Button================================
        down_frame=Frame(DataFrameLeft,bd=4,relief=RIDGE,bg="lightBlue")
        down_frame.place(x=770,y=60,width=170,height=165)

        btnAddmed=Button(down_frame,text="ADD",command=self.add_data,bg="lime",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,text="Update",command=self.update,bg="lime",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,text="Delete",command=self.delete,bg="red",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)

        btnclearmed=Button(down_frame,text="clear",command=self.clear,bg="darkgreen",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnclearmed.grid(row=3,column=0)

        #============================= Frame Details ============================================
        Framedeatils=Frame(self.root,bd=5,relief=RIDGE)
        Framedeatils.place(x=0,y=500,width=1530,height=280)

        # ================================== Main Table & Scrollbar =============================
        Table_frame=Frame(Framedeatils,bd=5,relief=RIDGE,padx=20)
        Table_frame.place(x=0,y=1,width=1520,height=280)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.Manufacturing_Table=ttk.Treeview(Table_frame,columns=("mfg id","mfg name",
                            "phone no","address")
                            ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x.config(command=self.Manufacturing_Table.xview)
        scroll_y.config(command=self.Manufacturing_Table.yview)

        self.Manufacturing_Table["show"]="headings"

        self.Manufacturing_Table.heading("mfg id",text="Purchase Order no")
        self.Manufacturing_Table.heading("mfg name",text="Drug id")
        self.Manufacturing_Table.heading("phone no",text="Quantity Order")
        self.Manufacturing_Table.heading("address",text="Status")
        self.Manufacturing_Table.pack(fill=BOTH,expand=1)

        self.Manufacturing_Table.column("mfg id",width=100)
        self.Manufacturing_Table.column("mfg name",width=100)
        self.Manufacturing_Table.column("phone no",width=100)
        self.Manufacturing_Table.column("address",width=100)
        self.fatch_data()
        self.Manufacturing_Table.bind("<ButtonRelease-1>",self.get_cursor)

        # ================================ Main Table =====================================

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into purchase_details values(%s,%s,%s,%s)",(
                                                                                                self.mfgid_var.get(),
                                                                                                self.mfgname_var.get(),
                                                                                                self.phoneno_var.get(),
                                                                                                self.address_var.get(),
                                                                                                ))
        conn.commit()
        self.fatch_data()
        conn.close()

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from purchase_details")
        row = my_cursor.fetchall()
        if len(row)!=0:
            self.Manufacturing_Table.delete(*self.Manufacturing_Table.get_children())
            for i in row:
                self.Manufacturing_Table.insert("",END,values=i) 
                conn.commit()
            conn.close()

    def get_cursor(self,ev=""):
        cursor_row=self.Manufacturing_Table.focus()
        content=self.Manufacturing_Table.item(cursor_row)
        row=content["values"]

        self.mfgid_var.set(row[0]),
        self.mfgname_var.set(row[1]),
        self.phoneno_var.set(row[2]),
        self.address_var.set(row[3]),



    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update purchase_details set drug_id=%s,quantity_order=%s,status=%s Where p_o_no=%s",(
                                                                                                                self.mfgname_var.get(),
                                                                                                                self.phoneno_var.get(),
                                                                                                                self.address_var.get(),
                                                                                                                self.mfgid_var.get()
                                                                                                               ))
        conn.commit()
        self.fatch_data()
        conn.close()

    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()

        sql="delete from purchase_details where p_o_no=%s"
        val=(self.mfgid_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fatch_data()
        conn.close()

    def clear(self):
        self.mfgid_var.set(""),
        self.mfgname_var.set(""),
        self.phoneno_var.set(""),
        self.address_var.set(""),

#=========================================================== class 8 ===================================================================================

class customer:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        # ========================== Main Variable ======================================

        self.mfgid_var=StringVar()
        self.mfgname_var=StringVar()
        self.phoneno_var=StringVar()
        self.address_var=StringVar()
        self.email_var=StringVar()


        # ==================================================================================
    
        lbltitle = Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE
                                ,bg='white',fg="darkgreen",font=("times new roaman",30,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\Logo.png")
        img1=img1.resize((45,45),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=18)

        # ===============================Data Frame=================================== 
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=90,width=1520,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Customer Information",
                                    fg="darkgreen",font=("arial",12,"bold"))

        DataFrameLeft.place(x=0,y=5,width=1450,height=350)

        # =========================== Label And Entry ====================================

        lblManfid=Label(DataFrameLeft,font=("arial",12,"bold"),width=30,text="Customer Id :",padx=2,pady=15)
        lblManfid.grid(row=0,column=0,sticky=W)
        txtManfid=Entry(DataFrameLeft,textvariable=self.mfgid_var,font=("arial",12,"bold"),bg="White",bd=2,relief=RIDGE,width=40)
        txtManfid.grid(row=0,column=1)

        lblManf_name=Label(DataFrameLeft,font=("arial",12,"bold"),width=30,text="Customer Name :",padx=2,pady=15)
        lblManf_name.grid(row=1,column=0,sticky=W)
        txtManf_name=Entry(DataFrameLeft,textvariable=self.mfgname_var,font=("arial",12,"bold"),bg="White",bd=2,relief=RIDGE,width=40)
        txtManf_name.grid(row=1,column=1)

        lblphoneno=Label(DataFrameLeft,font=("arial",12,"bold"),width=30,text="Customer Address :",padx=2,pady=15)
        lblphoneno.grid(row=2,column=0,sticky=W)
        txtphoneno=Entry(DataFrameLeft,textvariable=self.phoneno_var,font=("arial",12,"bold"),bg="White",bd=2,relief=RIDGE,width=40)
        txtphoneno.grid(row=2,column=1)

        lblAddress=Label(DataFrameLeft,font=("arial",12,"bold"),width=30,text="Customer Phone No :",padx=2,pady=15)
        lblAddress.grid(row=3,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft,textvariable=self.address_var,font=("arial",12,"bold"),bg="White",bd=2,relief=RIDGE,width=40)
        txtAddress.grid(row=3,column=1)

        lblemail=Label(DataFrameLeft,font=("arial",12,"bold"),width=30,text="Customer Email :",padx=2,pady=15)
        lblemail.grid(row=4,column=0,sticky=W)
        txtemail=Entry(DataFrameLeft,textvariable=self.email_var,font=("arial",12,"bold"),bg="White",bd=2,relief=RIDGE,width=40)
        txtemail.grid(row=4,column=1)


        # =====================================Image======================================
        lblhome=Label(DataFrameLeft,font=("arial",8,"bold"),text="STAY HOME STAY SAFE",fg="red",padx=10,pady=4)
        lblhome.place(x=1130,y=280)    

        img4=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\lab1.jpg")
        img4=img4.resize((350,250),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=1100,y=150)

        # =============================Medicine Add Button================================
        down_frame=Frame(DataFrameLeft,bd=4,relief=RIDGE,bg="lightBlue")
        down_frame.place(x=770,y=60,width=170,height=165)

        btnAddmed=Button(down_frame,text="ADD",command=self.add_data,bg="lime",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,text="Update",command=self.update,bg="lime",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,text="Delete",command=self.delete,bg="red",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)

        btnclearmed=Button(down_frame,text="clear",command=self.clear,bg="darkgreen",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnclearmed.grid(row=3,column=0)

        #============================= Frame Details ============================================
        Framedeatils=Frame(self.root,bd=5,relief=RIDGE)
        Framedeatils.place(x=0,y=500,width=1530,height=400)

        # ================================== Main Table & Scrollbar =============================
        Table_frame=Frame(Framedeatils,bd=5,relief=RIDGE,padx=20)
        Table_frame.place(x=0,y=1,width=1520,height=280)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.Manufacturing_Table=ttk.Treeview(Table_frame,columns=("mfg id","mfg name",
                            "phone no","address","email")
                            ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x.config(command=self.Manufacturing_Table.xview)
        scroll_y.config(command=self.Manufacturing_Table.yview)

        self.Manufacturing_Table["show"]="headings"

        self.Manufacturing_Table.heading("mfg id",text="Customer Id")
        self.Manufacturing_Table.heading("mfg name",text="Customer Name")
        self.Manufacturing_Table.heading("phone no",text="Customer PhoneNo")
        self.Manufacturing_Table.heading("address",text="Customer Address")
        self.Manufacturing_Table.heading("email",text="Customer Email")
        self.Manufacturing_Table.pack(fill=BOTH,expand=1)

        self.Manufacturing_Table.column("mfg id",width=100)
        self.Manufacturing_Table.column("mfg name",width=100)
        self.Manufacturing_Table.column("phone no",width=100)
        self.Manufacturing_Table.column("address",width=100)
        self.Manufacturing_Table.column("email",width=100)
        self.fatch_data()
        self.Manufacturing_Table.bind("<ButtonRelease-1>",self.get_cursor)

        # ================================ Main Table =====================================

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s)",(
                                                                                                self.mfgid_var.get(),
                                                                                                self.mfgname_var.get(),
                                                                                                self.phoneno_var.get(),
                                                                                                self.address_var.get(),
                                                                                                self.email_var.get()
                                                                                                ))
        conn.commit()
        self.fatch_data()
        conn.close()

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        row = my_cursor.fetchall()
        if len(row)!=0:
            self.Manufacturing_Table.delete(*self.Manufacturing_Table.get_children())
            for i in row:
                self.Manufacturing_Table.insert("",END,values=i) 
                conn.commit()
            conn.close()

    def get_cursor(self,ev=""):
        cursor_row=self.Manufacturing_Table.focus()
        content=self.Manufacturing_Table.item(cursor_row)
        row=content["values"]

        self.mfgid_var.set(row[0]),
        self.mfgname_var.set(row[1]),
        self.phoneno_var.set(row[2]),
        self.address_var.set(row[3]),
        self.email_var.set(row[4]),



    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update customer set c_name=%s,c_address=%s,c_phoneno=%s,c_email=%s Where c_id=%s",(
                                                                                                                self.mfgname_var.get(),
                                                                                                                self.phoneno_var.get(),
                                                                                                                self.address_var.get(),
                                                                                                                self.email_var.get(),
                                                                                                                self.mfgid_var.get()
                                                                                                               ))
        conn.commit()
        self.fatch_data()
        conn.close()

    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()

        sql="delete from customer where c_id=%s"
        val=(self.mfgid_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fatch_data()
        conn.close()

    def clear(self):
        self.mfgid_var.set(""),
        self.mfgname_var.set(""),
        self.phoneno_var.set(""),
        self.address_var.set(""),
        self.email_var.set(""),

#=========================================================== class 9 ===================================================================================

class sellsorder:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        # ========================== Main Variable ======================================

        self.mfgid_var=StringVar()
        self.mfgname_var=StringVar()
        self.phoneno_var=StringVar()
        


        # ==================================================================================
    
        lbltitle = Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE
                                ,bg='white',fg="darkgreen",font=("times new roaman",30,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\Logo.png")
        img1=img1.resize((45,45),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=18)

        # ===============================Data Frame=================================== 
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=90,width=1520,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Sells order Information",
                                    fg="darkgreen",font=("arial",12,"bold"))

        DataFrameLeft.place(x=0,y=5,width=1450,height=350)

        # =========================== Label And Entry ====================================

        lblManfid=Label(DataFrameLeft,font=("arial",12,"bold"),width=30,text="Sells Order No :",padx=2,pady=15)
        lblManfid.grid(row=0,column=0,sticky=W)
        txtManfid=Entry(DataFrameLeft,textvariable=self.mfgid_var,font=("arial",12,"bold"),bg="White",bd=2,relief=RIDGE,width=40)
        txtManfid.grid(row=0,column=1)

        lblManf_name=Label(DataFrameLeft,font=("arial",12,"bold"),width=30,text="Sells Order Date :",padx=2,pady=15)
        lblManf_name.grid(row=2,column=0,sticky=W)
        txtManf_name=Entry(DataFrameLeft,textvariable=self.mfgname_var,font=("arial",12,"bold"),bg="White",bd=2,relief=RIDGE,width=40)
        txtManf_name.grid(row=2,column=1)

        lblphoneno=Label(DataFrameLeft,font=("arial",12,"bold"),width=30,text="customer Id :",padx=2,pady=15)
        lblphoneno.grid(row=3,column=0,sticky=W)
        txtphoneno=Entry(DataFrameLeft,textvariable=self.phoneno_var,font=("arial",12,"bold"),bg="White",bd=2,relief=RIDGE,width=40)
        txtphoneno.grid(row=3,column=1)

        
        # =====================================Image======================================
        lblhome=Label(DataFrameLeft,font=("arial",8,"bold"),text="STAY HOME STAY SAFE",fg="red",padx=10,pady=4)
        lblhome.place(x=1130,y=280)    

        img4=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\lab1.jpg")
        img4=img4.resize((350,250),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=1110,y=150)

        # =============================Medicine Add Button================================
        down_frame=Frame(DataFrameLeft,bd=4,relief=RIDGE,bg="lightBlue")
        down_frame.place(x=770,y=60,width=170,height=165)

        btnAddmed=Button(down_frame,text="ADD",command=self.add_data,bg="lime",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,text="Update",command=self.update,bg="lime",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,text="Delete",command=self.delete,bg="red",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)

        btnclearmed=Button(down_frame,text="clear",command=self.clear,bg="darkgreen",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnclearmed.grid(row=3,column=0)

        #============================= Frame Details ============================================
        Framedeatils=Frame(self.root,bd=5,relief=RIDGE)
        Framedeatils.place(x=0,y=500,width=1520,height=280)

        # ================================== Main Table & Scrollbar =============================
        Table_frame=Frame(Framedeatils,bd=5,relief=RIDGE,padx=20)
        Table_frame.place(x=0,y=1,width=1520,height=280)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.Manufacturing_Table=ttk.Treeview(Table_frame,columns=("mfg id","mfg name",
                            "phone no","address")
                            ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x.config(command=self.Manufacturing_Table.xview)
        scroll_y.config(command=self.Manufacturing_Table.yview)

        self.Manufacturing_Table["show"]="headings"

        self.Manufacturing_Table.heading("mfg id",text="Sells Order No")
        self.Manufacturing_Table.heading("mfg name",text="Sells Order Date ")
        self.Manufacturing_Table.heading("phone no",text="customer Id ")
        self.Manufacturing_Table.pack(fill=BOTH,expand=1)

        self.Manufacturing_Table.column("mfg id",width=100)
        self.Manufacturing_Table.column("mfg name",width=100)
        self.Manufacturing_Table.column("phone no",width=100)
        self.fatch_data()
        self.Manufacturing_Table.bind("<ButtonRelease-1>",self.get_cursor)

        # ================================ Main Table =====================================

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into sell_master values(%s,%s,%s)",(
                                                                                                self.mfgid_var.get(),
                                                                                                self.mfgname_var.get(),
                                                                                                self.phoneno_var.get(),
                                                                                        
                                                                                                ))
        conn.commit()
        self.fatch_data()
        conn.close()

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from sell_master")
        row = my_cursor.fetchall()
        if len(row)!=0:
            self.Manufacturing_Table.delete(*self.Manufacturing_Table.get_children())
            for i in row:
                self.Manufacturing_Table.insert("",END,values=i) 
                conn.commit()
            conn.close()

    def get_cursor(self,ev=""):
        cursor_row=self.Manufacturing_Table.focus()
        content=self.Manufacturing_Table.item(cursor_row)
        row=content["values"]

        self.mfgid_var.set(row[0]),
        self.mfgname_var.set(row[1]),
        self.phoneno_var.set(row[2]),
        



    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update sell_master set s_date=%s,c_id=%s Where s_no=%s",(
                                                                                                                self.mfgname_var.get(),
                                                                                                                self.phoneno_var.get(),
                                                                                                                self.mfgid_var.get()
                                                                                                               ))
        conn.commit()
        self.fatch_data()
        conn.close()

    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()

        sql="delete from sell_master where s_no=%s"
        val=(self.mfgid_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fatch_data()
        conn.close()

    def clear(self):
        self.mfgid_var.set(""),
        self.mfgname_var.set(""),
        self.phoneno_var.set(""),

#===========================================================class 10===================================================================================

class sellsdetail:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        # ========================== Main Variable ======================================

        self.mfgid_var=StringVar()
        self.mfgname_var=StringVar()
        self.phoneno_var=StringVar()
        self.address_var=StringVar()


        # ==================================================================================
    
        lbltitle = Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE
                                ,bg='white',fg="darkgreen",font=("times new roaman",30,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\Logo.png")
        img1=img1.resize((45,45),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=18)

        # ===============================Data Frame=================================== 
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=90,width=1520,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Sells Details Information",
                                    fg="darkgreen",font=("arial",12,"bold"))

        DataFrameLeft.place(x=0,y=5,width=1450,height=350)

        # =========================== Label And Entry ====================================

        lblManfid=Label(DataFrameLeft,font=("arial",12,"bold"),width=30,text="Sells Order No :",padx=2,pady=15)
        lblManfid.grid(row=0,column=0,sticky=W)
        txtManfid=Entry(DataFrameLeft,textvariable=self.mfgid_var,font=("arial",12,"bold"),bg="White",bd=2,relief=RIDGE,width=40)
        txtManfid.grid(row=0,column=1)

        lblManf_name=Label(DataFrameLeft,font=("arial",12,"bold"),width=30,text="Drug Id :",padx=2,pady=15)
        lblManf_name.grid(row=2,column=0,sticky=W)
        txtManf_name=Entry(DataFrameLeft,textvariable=self.mfgname_var,font=("arial",12,"bold"),bg="White",bd=2,relief=RIDGE,width=40)
        txtManf_name.grid(row=2,column=1)

        lblphoneno=Label(DataFrameLeft,font=("arial",12,"bold"),width=30,text="Quantity Order :",padx=2,pady=15)
        lblphoneno.grid(row=3,column=0,sticky=W)
        txtphoneno=Entry(DataFrameLeft,textvariable=self.phoneno_var,font=("arial",12,"bold"),bg="White",bd=2,relief=RIDGE,width=40)
        txtphoneno.grid(row=3,column=1)

        lblAddress=Label(DataFrameLeft,font=("arial",12,"bold"),width=30,text="Status :",padx=2,pady=15)
        lblAddress.grid(row=4,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft,textvariable=self.address_var,font=("arial",12,"bold"),bg="White",bd=2,relief=RIDGE,width=40)
        txtAddress.grid(row=4,column=1)

        # =====================================Image======================================
        lblhome=Label(DataFrameLeft,font=("arial",8,"bold"),text="STAY HOME STAY SAFE",fg="red",padx=10,pady=4)
        lblhome.place(x=1130,y=280)    

        img4=Image.open("C:\\Users\Khilesh\Desktop\Project\Pharma_Image\lab1.jpg")
        img4=img4.resize((350,250),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=1110,y=150)

        # =============================Medicine Add Button================================
        down_frame=Frame(DataFrameLeft,bd=4,relief=RIDGE,bg="lightBlue")
        down_frame.place(x=770,y=60,width=170,height=165)

        btnAddmed=Button(down_frame,text="ADD",command=self.add_data,bg="lime",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,text="Update",command=self.update,bg="lime",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,text="Delete",command=self.delete,bg="red",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)

        btnclearmed=Button(down_frame,text="clear",command=self.clear,bg="darkgreen",font=("arial",12,"bold"),width=15,fg="white",pady=4)
        btnclearmed.grid(row=3,column=0)

        #============================= Frame Details ============================================
        Framedeatils=Frame(self.root,bd=5,relief=RIDGE)
        Framedeatils.place(x=0,y=500,width=1530,height=280)

        # ================================== Main Table & Scrollbar =============================
        Table_frame=Frame(Framedeatils,bd=5,relief=RIDGE,padx=20)
        Table_frame.place(x=0,y=1,width=1520,height=280)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.Manufacturing_Table=ttk.Treeview(Table_frame,columns=("mfg id","mfg name",
                            "phone no","address")
                            ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x.config(command=self.Manufacturing_Table.xview)
        scroll_y.config(command=self.Manufacturing_Table.yview)

        self.Manufacturing_Table["show"]="headings"

        self.Manufacturing_Table.heading("mfg id",text="Sells no")
        self.Manufacturing_Table.heading("mfg name",text="Drug id")
        self.Manufacturing_Table.heading("phone no",text="Quantity Order")
        self.Manufacturing_Table.heading("address",text="Status")
        self.Manufacturing_Table.pack(fill=BOTH,expand=1)

        self.Manufacturing_Table.column("mfg id",width=100)
        self.Manufacturing_Table.column("mfg name",width=100)
        self.Manufacturing_Table.column("phone no",width=100)
        self.Manufacturing_Table.column("address",width=100)
        self.fatch_data()
        self.Manufacturing_Table.bind("<ButtonRelease-1>",self.get_cursor)

        # ================================ Main Table =====================================

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into sells_details values(%s,%s,%s,%s)",(
                                                                                                self.mfgid_var.get(),
                                                                                                self.mfgname_var.get(),
                                                                                                self.phoneno_var.get(),
                                                                                                self.address_var.get(),
                                                                                                ))
        conn.commit()
        self.fatch_data()
        conn.close()

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from sells_details")
        row = my_cursor.fetchall()
        if len(row)!=0:
            self.Manufacturing_Table.delete(*self.Manufacturing_Table.get_children())
            for i in row:
                self.Manufacturing_Table.insert("",END,values=i) 
                conn.commit()
            conn.close()

    def get_cursor(self,ev=""):
        cursor_row=self.Manufacturing_Table.focus()
        content=self.Manufacturing_Table.item(cursor_row)
        row=content["values"]

        self.mfgid_var.set(row[0]),
        self.mfgname_var.set(row[1]),
        self.phoneno_var.set(row[2]),
        self.address_var.set(row[3]),



    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update sells_details set drug_id=%s,quantity_order=%s,status=%s Where s_no=%s",(
                                                                                                                self.mfgname_var.get(),
                                                                                                                self.phoneno_var.get(),
                                                                                                                self.address_var.get(),
                                                                                                                self.mfgid_var.get()
                                                                                                               ))
        conn.commit()
        self.fatch_data()
        conn.close()

    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor()

        sql="delete from sells_details where s_no=%s"
        val=(self.mfgid_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fatch_data()
        conn.close()

    def clear(self):
        self.mfgid_var.set(""),
        self.mfgname_var.set(""),
        self.phoneno_var.set(""),
        self.address_var.set(""),


if __name__=="__main__":
    main()
