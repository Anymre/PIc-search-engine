import pandas as pd

if __name__ == '__main__':
    flight = pd.read_csv("../forward.csv",sep=",")
    flight.hist("price")
    print(flight.head())