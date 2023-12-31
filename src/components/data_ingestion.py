import os
import sys
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split
from data_transformation import DataTransformation, DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv")
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"raw.csv")

class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Initiating data ingestion")
        try:
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Reading dataset as dataframe")
            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)
            df.to_csv(self.config.raw_data_path, index=False, header=True)
            logging.info("Train test split")
            df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
            df_train.to_csv(self.config.train_data_path, index=False)
            df_test.to_csv(self.config.test_data_path, index=False)
            logging.info("Data ingestion completed")
            return (self.config.train_data_path, self.config.test_data_path)
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    di = DataIngestion()
    train_data, test_data = di.initiate_data_ingestion()

    dt = DataTransformation()
    train_arr, test_arr, _ = dt.initiate_data_transformation(train_data, test_data)

    mt = ModelTrainer()
    print(mt.initiate_model_trainer(train_arr, test_arr))
    
