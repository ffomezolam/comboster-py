# taken from The Hitchhiker's Guide To Python

import os
import sys

# add root path to search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import used modules
import comboster
