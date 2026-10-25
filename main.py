import pandas as pd
from src.reporter import DataFrameReporter 

def main():
    df = pd.read_csv('data/payments.csv')
    
    reporter = DataFrameReporter()
    reporter.show_report(df)


if __name__ == '__main__': 
    main() 