import time


class PseudoRandom:
   def generate_seed(self) -> int:
       # Get the current time as a seed
       seed = int(time.time() * 1000)
       return seed


   def pseudo_random_generator(self, end_range) -> int:
       seed = self.generate_seed() # Gets a seed from the generate_seed function
    
       random_number = ((seed * 6364136223846793005) % 2**64) % end_range
       # Xn = ((Xn * a) % 2**64) % m


       return random_number


# Generate and print a “random” number
random_num = PseudoRandom().pseudo_random_generator(end_range = 100)
print("Random number:", random_num)
