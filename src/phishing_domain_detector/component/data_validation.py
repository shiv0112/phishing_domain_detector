import os
import pandas  as pd
from phishing_domain_detector.entity import DataValidationConfig
from phishing_domain_detector import logger
from phishing_domain_detector.utils import *
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab
import json

class DataValidation:
    def __init__(self,config = DataValidationConfig):
        self.config = config

    def get_train_test_file(self):
        logger.info("Fetching dataset")
        train_file = os.path.join(self.config.data_dir, self.config.train_file_name)
        test_file = os.path.join(self.config.data_dir, self.config.test_file_name)
        train_df = pd.read_csv(train_file)
        test_df = pd.read_csv(test_file)
        return train_df, test_df

    def is_train_test_file_exists(self):
        is_train_file_exist = False
        is_test_file_exist = False

        train_file = os.path.join(self.config.data_dir, self.config.train_file_name)
        test_file = os.path.join(self.config.data_dir, self.config.test_file_name)

        is_train_file_exist = os.path.exists(train_file)
        is_test_file_exist = os.path.exists(test_file)

        is_available =  is_train_file_exist and is_test_file_exist

        logger.info(f"Is train and test file exists?-> {is_available}")

        if not is_available:
            training_file = self.data_ingestion_artifact.train_file_path
            testing_file = self.data_ingestion_artifact.test_file_path
            message=f"Training file: {training_file} or Testing file: {testing_file}" \
                "is not present"
            raise Exception(message)

        return is_available

    def validate_dataset_schema(self):
        v_status = False
        #
        #
        #
        #
        logger.info("Validating dataset schema")
        v_status = True
        logger.info(f"Validation complete? -> {v_status}")
        return v_status

    def get_and_save_data_report(self):
        logger.info("Trying to get json report of data")
        profile = Profile(sections=[DataDriftProfileSection()])
        
        train_df,test_df = self.get_train_test_file()

        logger.info("Calculating data report... this may take a while")

        profile.calculate(train_df,test_df)

        report = json.loads(profile.json())

        report_file = os.path.join(self.config.root_dir, self.config.report_file_path)

        with open(report_file,"w") as report_file:
            json.dump(report, report_file, indent=6)

        logger.info("Data report successfully created.")

        return report
    
    def save_data_drift_report_page(self):
        logger.info("Trying to save a html report of data")
        dashboard = Dashboard(tabs=[DataDriftTab()])
        train_df,test_df = self.get_train_test_file()
        logger.info("Saving data report as HTML... this may take a while")
        dashboard.calculate(train_df,test_df)

        report_page_file_path =  os.path.join(self.config.root_dir, self.config.report_page_file_path)
        logger.info("Data report saved as HTML")
        dashboard.save(report_page_file_path)
        


