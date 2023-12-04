import time

class MersenneTwister:
    def __init__(self):
        # Initialize Mersenne Twister with a seed and state
        self.seed = self.generate_seed()
        self.state = [0] * 624
        self.index = 0

    def generate_seed(self):
        # Generate a seed based on the current time
        temp = int(str(time.time())[-1])
        seed = int(time.time() * 1000)

        # Manipulate seed based on the last digit of the current time
        if temp % 2 == 0:
            seed *= temp
        else:
            seed //= temp

        # Ensure seed is within the 32-bit range
        seed %= 2**32
        return seed

    def seed_mt(self, seed):
        # Seed the Mersenne Twister with a given seed
        self.state[0] = seed & 0xFFFFFFFF
        for i in range(1, 624):
            temp = (self.state[i - 1] ^ (self.state[i - 1] >> 30))
            self.state[i] = (1812433253 * temp + i) & 0xFFFFFFFF

    def generate_mt(self):
        # Generate the next batch of Mersenne Twister numbers
        for i in range(624):
            y = (self.state[i] & 0x80000000)
            y += (self.state[(i + 1) % 624] & 0x7FFFFFFF)
            self.state[i] = self.state[(i + 397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                self.state[i] ^= 0x9908B0DF

    def extract_random(self, end_range):
        # Extract a random number within the specified range
        if self.index == 0:
            self.generate_mt()
        y = self.state[self.index]
        y ^= (y >> 11)
        y ^= ((y << 7) & 0x9D2C5680)
        y ^= ((y << 15) & 0xEFC60000)
        y ^= (y >> 18)
        self.index = (self.index + 1) % 624
        return y % end_range

    def main(self):
        # Main function to demonstrate the Mersenne Twister
        self.seed_mt(self.seed)
        random_number = self.extract_random(100)
        print("Seed:", self.seed)
        print("Random Number:", random_number)

# Create an instance of MersenneTwister and run the main function
MersenneTwister().main()
