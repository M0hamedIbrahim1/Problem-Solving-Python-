dept = {
    'Mohamed':'accountant',
    'Ibrahim':'Sales',
    'Mahmoud':'Marketing',
    'Ahmed':'IT',
    'Omer':'purchases'
}
job = input('Enter Job : ')
for x,y in dept.items():
    if(job == y):
        print(x,'work in this position')
