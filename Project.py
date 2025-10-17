from datetime import datetime
def divide_numbers():
    try:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        result=a/b
        print("Result:",result)
    except Exception as e:
        with open("error_log.txt","a") as log:
            log.write(f"[{datetime.now()}] Error:{str(e)}\n")
        print("An error occurred! check error_log.txt for details.")
    finally:
        print("program execution completed.")
divide_numbers()    
            