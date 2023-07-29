import os 
import sys
import pandas as pd 
import numpy as np
from dataclasses import dataclass
from logger import logging
from exception import CustomException
from sklearn.model_selection import train_test_split

from data_transformation import DataTransformation


## initalising Data Ingestion
@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join("artifcats","train.csv")
    test_data_path:str = os.path.join("artifcats","test.csv")
    raw_data_path:str = os.path.join("artifcats","raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    ## Data Ingestion Method
    def initated_data_ingestion(self):
        logging.info("Data Ingestion Method Started")
        try:
            data = pd.read_csv(os.path.join("Dataset/","Clean Campus Placment.csv"))
            logging.info("Data Reading As Panda DataFraom")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("Train Test Split")
            train_set,test_set = train_test_split(data,test_size=0.20,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("data ingestion Complites")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info("Error Occured in Data Ingestion Stage")
            raise CustomException(e, sys)


## Run
if __name__=="__main__":
    obj = DataIngestion()
    train_data_path,test_data_path = obj.initated_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.inited_data_transformation(train_data_path, test_data_path)