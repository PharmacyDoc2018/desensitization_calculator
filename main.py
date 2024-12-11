from cyclophosphamide import Cyclophosphamide
from oxaliplatin import Oxaliplatin
from carboplatin import Carboplatin
from bag import Bag
from functions import *

def main():
    print(generate_desensitization_instructions(Carboplatin, 625))

main()
