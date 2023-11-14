person_name=input(' Please enter your name:')
person_age=int(input('Please enter your age:'))
height=float(input('Enter your height in meter(m):'))
weight=float(input('Enter your weight in kilograms(kg):'))
BMI=weight/(height**2)
if(BMI>=16 and BMI<18.5):
  print("is underweight",BMI)
elif(BMI>=18.5 and BMI<25):
  print("is healthy",BMI)
elif(BMI>=25 and BMI<30):
  print("is overweight",BMI)
elif(BMI>=30):
  print("is obese",BMI)
  
  
      