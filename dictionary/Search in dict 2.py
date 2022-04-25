dept = {
    'Mohamed':['accountant',35,10000],
    'Ibrahim':['Sales',36,9000],
    'Mahmoud':['Marketing',27,12000],
    'Ahmed':['IT',30,11000],
    'Omer':['purchases',32,10500]
}
name = input('Enter Name of employee : ')
for x,y in dept.items():
    if(name == x):
        print('sallary of ',x,'is :',y[2])
