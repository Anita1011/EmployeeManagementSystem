from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import requests 
from sqlite3 import *
import csv
import pandas as pd 
import matplotlib.pyplot as plt 

#Add
def f1(): 
	root.withdraw()
	aw.deiconify()

#Add_Save
def f2(): 
	con=None
	try:
		con = connect("memory.db")
		cursor = con.cursor()
		sql ="insert into employee values('%d','%s','%d')"
		id =(aw_ent_id.get())
		name =aw_ent_name.get()
		salary =(aw_ent_salary.get())
		
		if id.isalpha() :
			showerror('Failure','Id cannot be Alphabets, Enter Only Non zero Positive Integer')
		elif len(id)==0:
			showerror('Failure','Id Cannot be Empty')
		elif '-' in id:
			showerror('Failure','Id cannot be Negative, Enter only Positive Integer')
		elif id.isdigit():
			id1=int(id)
			if id1==0:
				showerror('failed','id Cannot be  0')
			else:
				if name.isdigit():
					showerror('Failure','Name has Numbers, Enter only Alphabets')
				elif len(name)==0:
					showerror('Failure','Name Cannot be Empty')
				elif name.isalpha and len(name)<2:
					showerror('Failure','name is too short, minimum length must be 2')
				elif name.isalpha() and len(name)>=2:
					if salary.isalpha() :
						showerror('Failure','Salary Should not be in alphabets')
					elif len(salary)==0:
						showerror('Failure','Salary Cannot be Empty')
					elif salary.isdigit():
						salary1=int(salary)
						if salary1<8000:
							showerror('Failure','Salary Should not be less than 8000')
						elif salary1>=8000:
							cursor.execute(sql%(id1,name,salary1))
							con.commit()
							showinfo("success", str(id1)+" is succesfully added")
					else:
						showerror('Failure','salary is alphabets num, Enter Only non zero Positive Integer')
				else:
					showerror('Failure','Name Cannot be Alphanum, enter only Alphabet')  
		elif id.isalnum():
			showerror('Failure','id cannot be alphabets num') 
		else:
			showerror('Failure','id is not valid')
	#except Exception as e :
		#showerror("failed", str(id1)+ " already exist")
	except IntegrityError :
		showerror("issue"," Id Already Exists" )	
	except Exception as e:
		con.rollback()
		showerror("issue", e)
	finally:
		if con is not None:
			con.close()
		aw_ent_id.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_salary.delete(0,END)
		aw_ent_id.focus()

	
#Add_Back	
def f3(): 
	aw.withdraw()
	root.deiconify()

 #View
def f4(): #View
	root.withdraw()
	vw.deiconify()
	vw_st_data.delete(1.0,END)
	try:
		con=connect("memory.db")
		cursor=con.cursor()
		sql="select * from employee order by id"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for d in data:
			info= info+"id="+str(d[0])+"  name="+str(d[1])+"  salary="+str(d[2])+"\n"
		vw_st_data.insert(INSERT, info)
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()

 #View_Back
def f5(): 
	vw.withdraw()
	root.deiconify()
 #Update
def f6():
	root.withdraw()
	up.deiconify()

 #Update_save
def f7():
	con=None
	try:
		con=connect("memory.db")
		cursor=con.cursor()
		sql="update employee set name='%s', salary='%s' where id='%s' "
		id=(up_ent_id.get())
		name=up_ent_name.get()
		salary=(up_ent_salary.get())
		cursor.execute(sql%(name,salary,id))

		if id.isalpha():
			showerror('Failure','ID Should only Contain +ve Integer Not Alphabet')
		elif len(id)==0:
			showerror('Failure','ID should not be empty, It should be in +ve integers')

		elif '-' in id:
			showerror('Failure','ID should be in Non Zero +ve integers')
		elif id.isdigit():
			id1=int(id)
			if id==0:
				showerror('Failure','ID should be not zero')
			else:
				if name.isdigit():
					showerror('Failure','Name should contain only alphabets , do not enter integer')
				elif len(name)==0:
					showerror('Failure','Name should not be empty')
				elif  name.isalpha() and len(name)<2 :
					showerror('Failure','Name is too Short \n Minimum Length required must be 2')

				elif name.isalpha() and len(name)>=2:
					if salary.isalpha() :
						showerror('Failure','Salary should  be in integers ')
					elif len(salary)==0:
						showerror('Failure','Salary should not be empty')

					elif salary.isdigit():
						salary1=int(salary)
						if salary1<=7999:
							showerror('Failure','Salary should not be less than 8000')
					elif salary.isalnum():
						showerror('Failure','Salary Should Not contain alphanumeric value, Enter only +ve integers')
				elif name.isalnum():
					showerror('Failure','Name should not be an alphanumeric value, Enter Alphabet with Minimum length 2')
		elif id.isalnum():
			showerror('Failure','ID cannot be an alphanumeric value, it should contain only non zero +ve integers')



		if (id.isalpha() or id.isalnum() or id.isdigit() or (len(id)==0)):
			if (name.isalpha() or name.isalnum() or name.isdigit() or (len(name)==0)):
				if (salary.isalpha() or salary.isalnum() or salary.isdigit() or (len(salary)==0)):
					if (not name.isalnum() ) or name.isalpha():

						if cursor.rowcount==1 and int(id)>0 and len(name)>2 and int(salary)>=8000 :
							con.commit()
							showinfo('updated',str(id)+' is updated')
						elif cursor.rowcount==0 and id.isdigit():
							showerror('Failure',str(id)+' is not exists')
				
				else:
					showerror('Failure','Salary is invalid, It should be in +ve integers')					
			else:
				showerror('Failure','Name is invalid, It should be in alphabets')
		else:
			showerror('Failure','ID is invalid, It should be in +ve integers')


	except ValueError:
		pass		
	except Exception as e:
		con.rollback()	
		showerror('issue',e)
	finally:
		if con is not None:
			con.close()
		up_ent_id.delete(0,END)
		up_ent_name.delete(0,END)
		up_ent_salary.delete(0,END)
		up_ent_id.focus()

 #Update_back
def f8(): 
	up.withdraw()
	root.deiconify()

 #Delete
def f9():
	root.withdraw()
	dt.deiconify()

 #Delete_Save
def f10():
	try:
		con=connect('memory.db')
		cursor=con.cursor()
		sql="delete from employee where id='%s' "
		id=(dt_ent_id.get())
		cursor.execute(sql %(id))
		
		if id.isalpha():
			showerror('Failure','ID Should only Contain +ve Integer Not Alphabet')
		elif len(id)==0:
			showerror('Failure','ID should not be empty, It should be in +ve integers')

		elif id.isdigit():
			id1=int(id)
			if id1==0:
				showerror('Failure','ID should be not zero')
		
			
		if (id.isalpha() or id.isalnum() or id.isdigit() or (len(id)==0)):

			if cursor.rowcount==1:

				con.commit()
				showinfo('updated',str(id)+' is deleted')
			elif cursor.rowcount==0 and id.isdigit():
				showerror('Failure',str(id)+' is not exists')
			else:
					pass
		else:
			showerror('Failure','ID is invalid, It should be in +ve integers')


	except IntegrityError :
		showerror("issue"," Id Already Exists" )
	#except ValueError:
		#showerror("Failed"," Id cannot be Alphanumerical value")	
	except Exception as e:
		con.rollback()	
		showerror('issue',e)
	finally:
		if con is not None:
			con.close()
		dt_ent_id.delete(0,END)
		dt_ent_id.focus()

#Delete_back
def f11(): 
	dt.withdraw()
	root.deiconify()

#Chart
def f13():
	con=connect("memory.db")
	cursor=con.cursor()
	cursor.execute("select * from employee order by salary DESC limit 5 ;")
	with open("out.csv","w",newline = '')as csv_file:
		csv_writer=csv.writer(csv_file)
		csv_writer.writerow([i[0] for i in cursor.description])
		csv_writer.writerows(cursor)
	con.close()

	data=pd.read_csv("out.csv")
	name=data["name"]
	salary=data["salary"]
	plt.bar(name,salary,width=0.30,color="orange")
	plt.xlabel("IDs")
	plt.ylabel("Salaries")
	plt.title("TOP 5 EMPLOYEES SCORE")
	
	plt.show()


	


root=Tk()
root.title("Employee Management System")
root.geometry("600x650+400+50")
root.configure(bg='Azure')
f= ("Arial", 25, "bold")

btn_add=Button(root, text="Add",font=f, width=10,bg='chocolate1',bd=5,command=f1)
btn_add.pack(pady=20)

btn_view=Button(root, text="Views",font=f,width=10,bg='chocolate1',bd=5,command=f4)
btn_view.pack(pady=10)

btn_update=Button(root, text="Update",font=f,width=10,bg='chocolate1',bd=5,command=f6)
btn_update.pack(pady=10)

btn_delete=Button(root, text="Delete",font=f,width=10,bg='chocolate1',bd=5,command=f9)
btn_delete.pack(pady=10)

btn_chart=Button(root, text="Chart",font=f,width=10,bg='chocolate1',bd=5,command=f13)
btn_chart.pack(pady=10)


def message():
	try:
		wa="https://ipinfo.io/"
		res= requests.get(wa)
		data= res.json()
		city= data["city"]
		msg=str("Location:- ")+ city
		#lab_msg.configure(text=msg) 
		a1 = "https://api.openweathermap.org/data/2.5/weather"
		a2 = "?q=" + city
		a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
		a4 = "&units=" + "metric"
		wa=a1+a2+a3+a4
		res=requests.get(wa)
		data=res.json()
		temp=data['main']['temp']
		temp1=round(temp,1)
		msg1=str("Location: ")+city+str('    Temp: ')+ str(temp1)+"8\u00b0"+str('C')
		lab_msg1.configure(text=msg1)
		
	except Exception as e :
		print("issue", e)

lab_msg1=Label(root,font=f,bg='SpringGreen2')
lab_msg1.pack(pady=15)

message()

aw=Toplevel(root)
aw.title("Add Employee")
aw.geometry("600x650+400+50")
aw.configure(bg="sky blue")

aw_id=Label(aw,text="Enter Id:", font=f,bg='sky blue',bd=4).pack(pady=10)
aw_ent_id= Entry(aw,font=f)
aw_ent_id.pack(pady=10)

aw_name=Label(aw,text="Enter Name:",font=f,bg='sky blue').pack(pady=10)
aw_ent_name= Entry(aw,font=f)
aw_ent_name.pack(pady=10)

aw_salary=Label(aw,text="Enter Salary:",font=f,bg='sky blue').pack(pady=10)
aw_ent_salary= Entry(aw,font=f)
aw_ent_salary.pack(pady=10)

aw_btn_save=Button(aw,text="Save",font=f,bg='chocolate1',bd=4,command=f2).pack(pady=20)
aw.withdraw()	

aw_btn_back=Button(aw,text="Back",font=f,bg='chocolate1',bd=4,command=f3).pack(pady=10)
aw.withdraw()	


vw=Toplevel(root)
vw.title("View Employee")
vw.geometry("600x650+400+50")
vw.configure(bg="lightgreen")

vw_st_data=ScrolledText(vw,width=35,height=10,font=f)
vw_st_data.pack(pady=10)

vw_btn_back=Button(vw,text="Back", font=f,command=f5,bg='chocolate1',bd=4)
vw_btn_back.pack(pady=10)
vw.withdraw()

up=Toplevel(root)
up.title("Update Employee")
up.geometry("600x650+400+50")
up.configure(bg="salmon")

up_id=Label(up,text="Enter Id:", font=f,bg='salmon',bd=4).pack(pady=10)
up_ent_id= Entry(up,font=f)
up_ent_id.pack(pady=10)

up_name=Label(up,text="Enter Name:",font=f,bg='salmon').pack(pady=10)
up_ent_name= Entry(up,font=f)
up_ent_name.pack(pady=10)

up_salary=Label(up,text="Enter Salary:",font=f,bg='salmon').pack(pady=10)
up_ent_salary= Entry(up,font=f)
up_ent_salary.pack(pady=10)

up_btn_save=Button(up,text="Save",font=f,bg='chocolate1',bd=4,command=f7).pack(pady=20)
up.withdraw()	

up_btn_back=Button(up,text="Back",font=f,bg='chocolate1',bd=4,command=f8).pack(pady=10)
up.withdraw()


dt=Toplevel(root)
dt.title("Delete Employee")
dt.geometry("600x650+400+50")
dt.configure(bg="light slate blue")

dt_id=Label(dt,text="Enter Id:", font=f,bg='light slate blue',bd=4).pack(pady=10)
dt_ent_id= Entry(dt,font=f)
dt_ent_id.pack(pady=10)

dt_btn_save=Button(dt,text="Save",font=f,bg='chocolate1',bd=4,command=f10).pack(pady=20)
dt.withdraw()	

dt_back_btn=Button(dt,text="Back",font=f,bg='chocolate1',bd=4,command=f11).pack(pady=10)
dt.withdraw()

def f12():
	answer= askyesno(title = 'confirmation', message=' Do You want to exit ?')
	if answer:
		answer= askyesno(title = 'confirmation', message='Thank You !')
		if answer:
			root.destroy()
			
root.protocol("WM_DELETE_WINDOW", f12)

root.mainloop()