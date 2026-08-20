import sys
import numpy
import pandas
import scipy
import sklearn
import requests


def main():
    print("Microclimate environment check")
    print(f"Python: {sys.version.split()[0]}")
    print(f"NumPy: {numpy.__version__}")
    print(f"Pandas: {pandas.__version__}")
    print(f"SciPy: {scipy.__version__}")
    print(f"Scikit-learn: {sklearn.__version__}")
    print(f"Requests: {requests.__version__}")
    print("Environment OK")


if __name__ == "__main__":
    main()