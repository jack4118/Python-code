import os
import sys

pipPath = f'{os.path.dirname(sys.executable)}\\Scripts'
os.system(f'setx PATH "%PATH%;{pipPath}"')