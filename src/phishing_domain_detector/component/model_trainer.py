import os
import pandas  as pd
import numpy as np
from sklearn.metrics import accuracy_score,confusion_matrix,roc_auc_score,classification_report
from sklearn.metrics import precision_recall_fscore_support

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import GradientBoostingClassifier

from phishing_domain_detector.entity import ModelTrainerConfig
from phishing_domain_detector import logger
from phishing_domain_detector.utils import *
import joblib



class ModelTrainer:
    def __init__(self,config = ModelTrainerConfig):
        self.config = config
        self.models = []

    def get_train_test_file(self):
        logger.info("Fetching dataset")
        train_file = os.path.join(self.config.data_dir, self.config.train_file)
        test_file = os.path.join(self.config.data_dir, self.config.test_file)
        train_df = pd.read_csv(train_file)
        test_df = pd.read_csv(test_file)
        return train_df, test_df

    def train_model(self):
        train_df, _ = self.get_train_test_file()
        
        X_train = train_df.iloc[:,:-1]
        y_train = train_df.iloc[:,-1]

        logger.info("Training data on Logistic Regression")
        
        lr_model = LogisticRegression()
        lr_model.fit(X_train,y_train)
        self.models.append(lr_model)

        logger.info("Training data on Random Forest Classifier") 

        rf_model = RandomForestClassifier(random_state=self.config.rand_state)
        rf_model.fit(X_train,y_train)
        self.models.append(rf_model)
        
        logger.info("Training data on Gradient Boosting Classifier")

        gb_model = GradientBoostingClassifier(random_state=self.config.rand_state)
        gb_model.fit(X_train, y_train)
        self.models.append(gb_model)

        logger.info("Training data on XG-Boost Classifier")

        xgb_model = XGBClassifier(random_state=self.config.rand_state)
        xgb_model.fit(X_train, y_train)
        self.models.append(xgb_model)

        logger.info("Model trained on all models")

    def evaluater(self, actual, predicted):
        print(confusion_matrix(actual, predicted))
        print()
        print(classification_report(actual, predicted))
        print()
        print('roc_auc_score: ', roc_auc_score(actual, predicted))
        logger.info(f"roc_auc_score: {roc_auc_score(actual, predicted)}")
        print()
        print("test set accuracy score :",  accuracy_score(actual, predicted))
        logger.info(f"test set accuracy score : {accuracy_score(actual, predicted)}")
        print()
        p, r, f, _ = precision_recall_fscore_support(actual, predicted, average='binary')
        print('test set precision: ', p)
        logger.info(f"test set precision: {p}")
        print()
        print('test set recall: ', r)
        logger.info(f"test set recall: {r}")
        print()
        print('test set f1-score: ', f)
        logger.info(f"test set f1-score: {f}")
        print()
        print()
    
    def model_eval(self):
        train_df , test_df = self.get_train_test_file()

        X_train = train_df.iloc[:,:-1]
        y_train = train_df.iloc[:,-1]
        
        X_test = test_df.iloc[:,:-1]
        y_test = test_df.iloc[:,-1]

        best_score = 0.0

        for model in self.models:
            score = accuracy_score(y_test, model.predict(X_test))
            model_save_path = os.path.join(self.config.trained_model_dir, f"{type(model).__name__}_"+self.config.model_file_name)
            if score > best_score:
                best_score = score
                best_model = model
            best_score = max(score, best_score)
            print(f"{type(model).__name__} test accuracy: {score}")
            logger.info(f"{type(model).__name__} metrics: ")
            self.evaluater(y_test, model.predict(X_test))
            joblib.dump(model, model_save_path)
        
        print(f"The best model is {type(best_model).__name__} with test accuracy: {best_score}")
        logger.info(f"The best model is {type(best_model).__name__} with train accuracy: {accuracy_score(y_train, best_model.predict(X_train))}")
        logger.info(f"The best model is {type(best_model).__name__} with test accuracy: {best_score}")
        best_model_save_path = os.path.join(self.config.trained_model_dir, self.config.best_model_name)
        joblib.dump(best_model, best_model_save_path)
        logger.info("best model serialized")


    
        


