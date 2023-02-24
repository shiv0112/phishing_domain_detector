import os
import pandas  as pd
import numpy as np
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import AdaBoostClassifier
from phishing_domain_detector.entity import DataTransformationConfig
from phishing_domain_detector import logger
from phishing_domain_detector.utils import *


class DataTransformation:
    def __init__(self,config = DataTransformationConfig):
        self.config = config

    def get_train_test_file(self):
        logger.info("Fetching dataset")
        train_file = os.path.join(self.config.data_dir, self.config.train_file_name)
        test_file = os.path.join(self.config.data_dir, self.config.test_file_name)
        train_df = pd.read_csv(train_file)
        test_df = pd.read_csv(test_file)
        return train_df, test_df

    def feature_selection(self):
        train_df, test_df = self.get_train_test_file()
        
        X_train = train_df.iloc[:,:-1]
        y_train = train_df.iloc[:,-1]

        X_test = test_df.iloc[:,:-1]
        y_test = test_df.iloc[:,-1]

        logger.info("Selecting features using AdaBoost Classifier..")
        
        estimator = AdaBoostClassifier(random_state=0, n_estimators=50)
        selector = SelectFromModel(estimator)
        selector = selector.fit(X_train, y_train) 
        features = np.array(X_train.columns)
        status = selector.get_support()

        logger.info("Saving new features csv")

        X_train=X_train[features[status]]
        X_test=X_test[features[status]]

        logger.info(features[status])

        train_df = pd.concat([X_train, y_train],axis=1)
        test_df = pd.concat([X_test, y_test],axis=1)

        train_path = os.path.join(self.config.root_dir, self.config.train_trans)
        test_path = os.path.join(self.config.root_dir, self.config.test_trans)

        train_df.to_csv(train_path,index=False)
        test_df.to_csv(test_path,index=False)

        logger.info("Selected features successfully saved")


    
        


