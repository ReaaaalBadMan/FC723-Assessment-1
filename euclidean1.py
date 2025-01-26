class euclideanalgorithm:
    @staticmethod #no self therefor it is a static method
    def get_gcd(a, b): #use Euclidean Algorithm to compute the gcd
        while b != 0: #While b does not equal 0:
            a, b = b, a % b # a will equal b and b will be the remainder of a/b
        return a

if __name__ == "__main__": #only runs if file is main script
    # example usage with random numbers
    gcd_result = euclideanalgorithm.get_gcd(64, 24)
    print("The GCD of 64 and 24 is:", gcd_result)
