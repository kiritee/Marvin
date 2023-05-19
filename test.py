import sys, time
def print_response(text):
    for char in text: 
        print(char, end='') 
        sys.stdout.flush() 
        time.sleep(0.2) 

print_response("how was it?")