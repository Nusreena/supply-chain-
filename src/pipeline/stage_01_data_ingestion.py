from src.config.configuration import ConfiguarationManager
from src.components.data_injection import DataIngestion
from src import logger



STAGE_NAME = " Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def _init_(self):
        pass
    
    def main(self):
        config = ConfiguarationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()