from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    report_file_path: Path
    report_page_file_path: Path
    data_dir: Path
    train_file_name: str
    test_file_name: str

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_dir: Path
    train_file_name: str
    test_file_name: str
    train_trans: str
    test_trans: str

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    report_file_path: Path
    report_page_file_path: Path
    data_dir: Path
    train_file_name: str
    test_file_name: str

@dataclass(frozen=True)
class ModelTrainerConfig:
    trained_model_dir: Path
    data_dir: Path
    train_file: str
    test_file: str
    model_file_name: str
    best_model_name: str
    rand_state: str



    

