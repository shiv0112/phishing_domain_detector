from phishing_domain_detector.config import ConfigurationManager
from phishing_domain_detector.component import DataTransformation
from phishing_domain_detector import logger 


STAGE_NAME ="Data Transformation"


def main():
    config = ConfigurationManager()
    data_transformation_config = config.get_data_transformation_config()
    data_transformation = DataTransformation(config=data_transformation_config)
    data_transformation.feature_selection()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> Stage: {STAGE_NAME} ended <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e