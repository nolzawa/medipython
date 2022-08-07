from tkinter import *
import tkinter.scrolledtext as st
class RecommendedDosage(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Recommended Dosage Calculator -Sabina Safarudin")
        #self.master.geometry("650x350") #width by height dimension
        self._memList = []
        self._memPos = len(self._memList) - 1
        #create the components
        #create RadioButtons
        self._option = StringVar() #common variable for Radio buttons
        self._maxDose = StringVar() #for maxDosage
        self._doseLimit = StringVar() #dosageLimit
        self._weight = StringVar() # for weight
        self._rb1 = Radiobutton(self,text="12 years and under",variable=self._option,value="child")
        self._rb2 = Radiobutton(self,text="above 12 years old",variable=self._option,value="adult")
        self._option.set("adult") #value of radiobutton, this is to set default selection
        #create other components
        self._lb1 = Label(self, text="Maximum Dosage Allowed Per KG in mg:")
        self._lb2 = Label(self, text= "Dosage Limit in mg:")
        self._lb3 = Label(self, text= "Patient Weight:")
        self._tb1 = Entry(self, width=50, textvariable = self._maxDose)
        self._tb2 = Entry(self, width=50, textvariable = self._doseLimit)
        self._tb3 = Entry(self, width=50, textvariable = self._weight)
        self._bt1 = Button(self, text="Get Recommended Dosage", command=self.getDosage)
        self._bt2 = Button(self, text="Add to Memory", command = self.addMemory)
        self._bt3 = Button(self, text="Clear Input/Output", command = self.clearAll)
        self._bt4 = Button(self, text="Next", command = self.nextButton)
        self._bt5 = Button(self, text="Previous", command = self.previousButton)
        self._output1 = st.ScrolledText(self,width = 75, height = 10)
        #place onto the window use grid layout
        
        self._lb1.grid(row=0, column=0, sticky = W, padx = 5)
        self._tb1.grid(row=0, column=1, columnspan=5, sticky = W)
        self._lb2.grid(row=1, column=0, sticky = W, padx = 5)
        self._tb2.grid(row=1, column=1, columnspan=5, sticky = W)
        self._lb3.grid(row=2, column=0, sticky = W, padx = 5)
        self._tb3.grid(row=2, column=1, columnspan=5, sticky = W)
        #radio buttons
        self._rb1.grid(row=3, column=1, sticky = W)
        self._rb2.grid(row=3, column=2, sticky = W)
        #buttons
        self._bt1.grid(row=4, column=0, sticky = W+E)
        self._bt2.grid(row=4, column=1, sticky = W+E)
        self._bt3.grid(row=4, column=2, sticky = W+E)
        self._bt4.grid(row=4, column=3, sticky = W+E)
        self._bt5.grid(row=4, column=4, sticky = W+E)
        self._output1.grid(row=5, column=0, columnspan=6)

        
        self.grid()
    
    def getDosage(self):
        maxDose = float(self._maxDose.get())
        doseLimit = float(self._doseLimit.get())
        opt = self._option.get()
        wt = float(self._weight.get())
        recDose = wt * maxDose
        if self._option.get() == 'child':
            recDose = recDose / 2
        msg = f'\nDosage Recommendation for {opt}\nMaximum Dosage Allowed Per KG in mg = {maxDose}\nDosage Limit in mg = {doseLimit}\nRecommended Dosage in mg = {recDose}'
        self._output1.insert(END, msg)
    
    def addMemory(self):
        maxDose = float(self._maxDose.get())
        doseLimit = float(self._doseLimit.get())
        opt = self._option.get()
        wt = float(self._weight.get())
        
        self._memList.append([maxDose, doseLimit, opt, wt])
        self._memPos = len(self._memList) - 1
        
        #print(self._memList)
            
        msg = f'\nAdded to Memory\nMaximum Dosage Allowed Per KG in mg = {maxDose}\nDosage Limit in mg = {doseLimit}\nWeight in kg = {wt}\nPatient type = {opt}'
        self._output1.insert(END, msg)
        self._maxDose.set("")
        self._doseLimit.set("")
        self._weight.set("")
        self._option.set("adult")
        
    def clearAll(self):
        self._tb1.delete(0, END)
        self._tb2.delete(0, END)
        self._tb3.delete(0, END)
        self._option.set("adult")
        self._output1.delete(1.0, END)
        
    def nextButton(self):
        #set into variables
        if len(self._memList) == 0:
            msg = f'\nMemory is Empty'
        elif len(self._memList) == 1:
            #set fields as per
            maxDose = str(self._memList[0][0])
            doseLimit = str(self._memList[0][1])
            weight = str(self._memList[0][3])
            opt = str(self._memList[0][2])
            self._maxDose.set(maxDose)
            self._doseLimit.set(doseLimit)
            self._weight.set(weight)
            self._option.set(opt)
            msg = f'\nMaximum Dosage Allowed Per KG in mg = {maxDose}\nDosage Limit in mg = {doseLimit}\nWeight in kg = {weight}\nPatient type = {opt}\nMemory has only one set of values.\n'
        elif self._memPos == len(self._memList)-1:
            msg = f'\nEnd of memory, Try PREVIOUS button\n'
        else:
            self._memPos +=1 #iterate through the memList
            maxDose = str(self._memList[self._memPos][0])
            doseLimit = str(self._memList[self._memPos][1])
            weight = str(self._memList[self._memPos][3])
            opt = str(self._memList[0][2])
            self._maxDose.set(maxDose)
            self._doseLimit.set(doseLimit)
            self._weight.set(weight)
            self._option.set(opt)
            msg = f'\nMaximum Dosage Allowed Per KG in mg = {maxDose}\nDosage Limit in mg = {doseLimit}\nWeight in kg = {weight}\nPatient type = {opt}'
            
        self._output1.insert(END, msg)
    
    def previousButton(self):
        if len(self._memList) == 0:
            msg = f'\nMemory is Empty'
        elif len(self._memList) == 1:
            #set fields as per
            maxDose = str(self._memList[0][0])
            doseLimit = str(self._memList[0][1])
            weight = str(self._memList[0][3])
            opt = str(self._memList[0][2])
            self._maxDose.set(maxDose)
            self._doseLimit.set(doseLimit)
            self._weight.set(weight)
            self._option.set(opt)
            msg = f'\nMaximum Dosage Allowed Per KG in mg = {maxDose}\nDosage Limit in mg = {doseLimit}\nWeight in kg = {weight}\nPatient type = {opt}\nMemory has only one set of values.\n'
        elif self._memPos == 0:
            msg = f'\nStart of memory, Try NEXT button'
        else:
            self._memPos -=1 #iterate through the memList backwards
            maxDose = str(self._memList[self._memPos][0])
            doseLimit = str(self._memList[self._memPos][1])
            weight = str(self._memList[self._memPos][3])
            opt = str(self._memList[0][2])
            self._maxDose.set(maxDose)
            self._doseLimit.set(doseLimit)
            self._weight.set(weight)
            self._option.set(opt)
            msg = f'\nMaximum Dosage Allowed Per KG in mg = {maxDose}\nDosage Limit in mg = {doseLimit}\nWeight in kg = {weight}\nPatient type = {opt}'
        
        self._output1.insert(END, msg)
                
   
def main():
    app = RecommendedDosage()
    app.mainloop()

main()