#positional
def full_name(first_name,last_name):
    print(f"Hello, {first_name} {last_name}")
full_name("THARUNIKA","KAMALRAJ")
#default
def  sivaranjani(base,exponent=2):
    print(f"\n The square of {base} is:",(base**exponent))
sivaranjani(8)  
#keyword argument
def student_profile(name,course,year):
    print(f"\nName:",name,"\nCourse:",course,"\nYear:",year)
student_profile(name="Tharunika",course="B.E(AIMl)",year="2nd year")      
#arbitrary arguments
def marks(*marks):
    total=sum(marks)
    average=total/len(marks)
    print("Total:",total)
    print("Average:",average)
marks(80,100,90)    


#1 lambdAfunction
         
square=lambda x:x*x
print("\nSquare=",square(5))



# exercise
add=lambda a,b:a+b
print("\nAdd=",add(9,8))

