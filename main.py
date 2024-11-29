from cyclophosphamide import Cyclophosphamide
from oxaliplatin import Oxaliplatin
from bag import Bag
from functions import *

def main():
    print(generate_desensitization_instructions(Oxaliplatin, 150))

main()
