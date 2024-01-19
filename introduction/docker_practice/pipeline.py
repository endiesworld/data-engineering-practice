import sys
import pandas as pd 

print('The complete command line argument entered: ', sys.argv)
# Some other operations here
# Recall argv collects commandline arguments after 'python' command. argv[0] is the name of the file(pipeline.py)
comand_line_arg = sys.argv[1]
print(f'Pandas version is {pd.__version__}')
print(f'Successfully completed by {comand_line_arg}')
