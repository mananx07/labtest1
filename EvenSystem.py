import numpy as np
import matplotlib.pyplot as plt
emp = np.array([[0,1000,"manager","a1",80],[1,5671,"TL","a2",70],[2,2671,"founder","a3",67],[3,6711,"support","a4",51],[4,1071,"clerk","a5",49]])
print(emp)
empcodes = np.arange(0,5,1)
print(empcodes)
attendence = np.array([10,20,30,11,57]) # attendence in number out of 100 working days 
def takeattendence(attd):
    for i in range(len(attd)):
        a = input("Enter 1 if present 0 otherwise")
        #attd[i] += 1
        if a == 1:
            attd[i] += 1

    return attd

newatt = takeattendence(attendence)
print(newatt)
def changeperformance(id,emp):
    newperf = input("enter new performance of the employee")
    emp[id,4] = newperf
    print(emp)

changeperformance(3,emp)
sal = np.arange(0,len(emp))
avg = 0
for i in range(len(emp)):
    sal[i] = emp[i,0]
    avg += sal[i]

print(avg/len(sal))
HP = -89889999
LP = 9912739
for i in range(len(emp)):
    a = emp[i,1]
    if a > HP: 
        HP = emp[i,1]
    if a < LP: 
        LP = emp[i,1]
    

print(HP,LP)
xpts = np.array([0,1,2,3,4])
ypts = np.array([80,70,67,51,49])
plt.scatter(xpts,ypts)
plt.show()
