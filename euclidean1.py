class euclideanalgorithm:
    @staticmethod #no self therefor it is a static method
    def get_gcd(a, b): #use Euclidean Algorithm to compute the gcd
        while b != 0: #While b does not equal 0:
            a, b = b, a % b # a will equal b and b will be the remainder of a/b
        return a

if __name__ == "__main__": #running the code with user inputs
    try:
        num1 = int(input("Enter the first positive integer: ")) #takes first input
        num2 = int(input("Enter the second positive integer: ")) #takes second input
        if num1<=0 or num2<=0: #makes sure non of the numbers are 0 or less
            raise ValueError("Both inputs must be positive integers")
        else:
            gcd_result = euclideanalgorithm.get_gcd(num1, num2) #applies get_gcd function
            print(f"The GCD of {num1} and {num2} is: {gcd_result}") #print result
    except ValueError: #makes sure that numbers are inputted
        print("Invalid input. Please ensure you enter positive integers.")
