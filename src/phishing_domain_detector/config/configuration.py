import os
from pathlib import Path
from phishing_domain_detector.constants import *
from phishing_domain_detector.utils import read_yaml, create_directories
from phishing_domain_detector.entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)

class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH, schema_filepath = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self):
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL= config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config

    def get_data_validation_config(self):
        config =self.config.data_validation
        
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            data_dir = config.data_dir,
            train_file_name = config.train_file_name,
            test_file_name = config.test_file_name,
            report_file_path = config.report_file_path,
            report_page_file_path = config.report_page_file_path
        )

        return data_validation_config

    def get_data_transformation_config(self):
        config =self.config.data_transformation
        
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_dir = config.data_dir,
            train_file_name = config.train_file_name,
            test_file_name = config.test_file_name,
            train_trans = config.train_trans,
            test_trans = config.test_trans
        )

        return data_transformation_config

    def get_model_trainer_config(self):
        config =self.config.model_trainer
        
        create_directories([config.trained_model_dir])

        model_trainer_config = ModelTrainerConfig(
            trained_model_dir = config.trained_model_dir,
            data_dir= config.data_dir,
            train_file= config.train_file,
            test_file= config.test_file,
            model_file_name= config.model_file_name,
            best_model_name= config.best_model_name,
            rand_state = self.params.RANDOM_STATE
        )

        return model_trainer_config

    