import pdb
def calculate_sum(a,b):
    result = a+ b
    # pdb.set_trace() #set a breakpoint here 
    print("hello")
    return result

def multiply_by_two(num):
    result = num*2
    return result

def main():
    x =10
    y =5
    z = calculate_sum(x, y)
    w = multiply_by_two(z)
    print(f"The sum of {x} and {y} is {z}")

evens = [x for x in range(10) if x % 2 ==0]
print(evens)

if __name__ =="__main__":
    calculate_sum(2,3)