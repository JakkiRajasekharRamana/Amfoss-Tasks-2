import pyinputplus as pyip
wheat=100
white=100
sourdough=120
chicken=turkey=ham=100
tofu=80
chesse=20
mayo=mustard=lettuce=tomato=20
cheddar=swiss=mozzarella=20
bread_type=pyip.inputMenu(['wheat','white','sourdough'])
#print(bread_type)
protein_type=pyip.inputMenu(['chicken','turkey','ham','tofu'])
#print(protein_type)
prompt_1 = 'Do you want any cheese?\n'
cheese=pyip.inputYesNo(prompt_1)
if(cheese=='yes'):
    cheese_type=pyip.inputMenu(['cheddar','swiss','mozzarella'])
else:
    chesse=0
prompt_2='Do you want mayo or mustard or letttuce or tomamto?(btw this is free :D)\n'
extras=pyip.inputYesNo(prompt_2)
if(extras=='Yes'):
    prompt="Please enter your desired choise?"
    while True:
        if(prompt!=('mayo' or 'mustard' or 'lettuce' or 'tomato')):
            print("We do not have that sorry! Please select again :D")
        else:
            break
prompt_3='How many would you want?\n'
quantity=pyip.inputInt(prompt_3,min=1)
sum=0
if(bread_type=='wheat' or 'white'):
    sum=sum+wheat
else:
    sum=sum+sourdough
if(protein_type=='chicken' or 'turkey' or 'ham'):
    sum=sum+chicken
else:
    sum=sum+tofu
print('Your total cost will be =',quantity*(sum+chesse),'rupees')
