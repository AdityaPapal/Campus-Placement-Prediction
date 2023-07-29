import os 
import sys
import pandas as pd 
import numpy as np
from dataclasses import dataclass
from logger import logging
from exception import CustomException

from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet,LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC

from utils import save_object
from utils import evaluate_models


@dataclass
class ModelTraningConfig:
    train_model_file_obj = os.path.join("artifcats","model.pkl")


class ModelTraning:
    def __init__(self):
        self.model_traner_config = ModelTraningConfig()


    def initatied_model_traning(self,train_array,test_array):
        try:
            logging.info("Split Dependent And Independent Features")
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models = {
                "Random Forest": RandomForestClassifier(random_state=42),
                "Decision Tree": DecisionTreeClassifier(random_state=42),
                "Logastic":LogisticRegression(random_state=42),
                "LinearSVC":LinearSVC(random_state=42)

            }
            params = {
                "Random Forest":{
                    "class_weight":["balanced"],
                    "n_estimators":[400],
                    "criterion":["gini","entropy"],
                    'max_depth': [8,20],
                    'min_samples_split': [2, 3,5,8, 10],
                },
                "Decision Tree":{
                    "class_weight":["balanced"],
                    "criterion":['gini',"entropy","log_loss"],
                    "splitter":['best','random'],
                    "max_depth":[3,4,5,6],
                    "min_samples_split":[2,3,4,5],
                    "min_samples_leaf":[1,2,3],
                    "max_features":["auto","sqrt","log2"]
                },
                "Logastic":{
                    "penalty":["l1", "l2", "elasticnet", None],
                    "class_weight":["balanced"],
                    'C': [0.001, 0.01, 0.1, 1, 10],
                    "solver":["lbfgs", "liblinear", "sag", "saga"]
                },
                "LinearSVC":{
                    'C': [0.1, 1, 10],
                    "penalty":["l1", "l2",],
                    "loss":["hinge", "squared_hinge"],
                    "class_weight":["balanced"],
                }
            }

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                                models=models,param=params)

                ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            print(f"Best Model Found, Model Name is: {best_model_name},Accuracy_Score: {best_model_score}")
            print("\n***************************************************************************************\n")
            logging.info(f"Best Model Found, Model Name is: {best_model_name},Accuracy_Score: {best_model_score}")

            save_object(file_path=self.model_traner_config.train_model_file_obj,
                obj = best_model
                )

        except Exception as e:
            logging.info("Error Occured in Model Traning")
            raise CustomException(e,sys)