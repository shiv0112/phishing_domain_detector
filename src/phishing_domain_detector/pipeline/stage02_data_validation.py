from phishing_domain_detector.config import ConfigurationManager
from phishing_domain_detector.component import DataValidation
from phishing_domain_detector import logger 


STAGE_NAME ="Data Validation"


def main():
    config = ConfigurationManager()
    data_validation_config = config.get_data_validation_config()
    data_validation = DataValidation(config=data_validation_config)
    data_validation.is_train_test_file_exists()
    data_validation.validate_dataset_schema()
    data_validation.get_and_save_data_report()
    data_validation.save_data_drift_report_page()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> Stage: {STAGE_NAME} ended <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e