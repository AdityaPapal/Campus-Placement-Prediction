import os 
import sys
import pandas as pd 
import numpy as np
from dataclasses import dataclass
from logger import logging
from exception import CustomException

from utils import load_object


class PredictPipline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            ## Load pickel File
            ## This Code Work in /any system
            preprocessor_path = os.path.join("artifcats","preprocessor.pkl")
            model_path = os.path.join("artifcats","model.pkl")

            ## Load Pickel File
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)

            pred = model.predict(data_scaled)

            return pred

        except Exception as e:
            logging.info("Error Occure in Prediction Pipline")
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
            ssc_p:float,
            hsc_p:float,
            hsc_s:int,
            degree_p:float,
            degree_t:int,
            workex:int,
            etest_p:float,
            specialisation:int,
            mba_p:float):


        self.ssc_p = ssc_p
        self.hsc_p= hsc_p
        self.hsc_s = hsc_s
        self.degree_p = degree_p
        self.degree_t = degree_t
        self.workex = workex
        self.etest_p = etest_p
        self.specialisation = specialisation
        self.mba_p = mba_p


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "ssc_p":[self.ssc_p], 
                "hsc_p":[self.hsc_p],
                "hsc_s":[self.hsc_s],
                "degree_p":[self.degree_p],
                "degree_t":[self.degree_t],
                "workex":[self.workex],
                "etest_p":[self.etest_p],
                "specialisation":[self.specialisation],
                "mba_p":[self.mba_p],       
            }

            data = pd.DataFrame(custom_data_input_dict)
            logging.info("Data Frame Gathered")
            return data

        except Exception as e:
            logging.info("Error Occured In Predict Pipline")
            raise CustomException(e, sys)

        