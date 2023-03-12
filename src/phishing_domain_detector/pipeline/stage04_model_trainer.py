from phishing_domain_detector.config import ConfigurationManager
from phishing_domain_detector.component import ModelTrainer
from phishing_domain_detector import logger 


STAGE_NAME ="Model Trainer"


def main():
    config = ConfigurationManager()
    model_trainer_config = config.get_model_trainer_config()
    model_trainer = ModelTrainer(config=model_trainer_config)
    model_trainer.train_model()
    model_trainer.model_eval()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> Stage: {STAGE_NAME} ended <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e