from scipy import rand
from sklearn.model_selection import StratifiedShuffleSplit
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataIngestionConfig
import sys , os
from housing.exception import HousingException
from housing.logger import logging
import tarfile
from six.moves import urllib
import pandas as pd
import numpy as np

class DataIngestion:
    def __init__(self , data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Ingestion Log Started.{'='*20} \n\n")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise HousingException(e,sys) from e

    def download_housing_data(self)->str:
        try:
            # url to download the file
            download_url = self.data_ingestion_config.dataset_download_url

            # folder to download the tgz file
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir

            # check if folder exists else create it
            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)
            
            os.makedirs(tgz_download_dir,exist_ok=True)

            # extract filename
            housing_file_name = os.path.basename(download_url)

            # prepare tgz download file path
            tgz_file_path = os.path.join(tgz_download_dir,housing_file_name)
            
            # download the file
            logging.info(f"Downloading file from [{download_url}] into: [{tgz_file_path}]")
            urllib.request.urlretrieve(download_url,tgz_file_path)
            logging.info(f"File: [{tgz_file_path}] downloaded")

            return tgz_file_path

        except Exception as e:
            raise HousingException(e,sys) from e

    def extract_tgz_file(self,tgz_file_path:str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            
            # check if raw folder exists then delete and create new one
            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)
            
            os.makedirs(raw_data_dir,exist_ok=True)
            logging.info(f"Extracting TGZ file [{tgz_file_path}] into folder [{raw_data_dir}]")
            
            # open the tar file and extract the tar file into raw dir
            with tarfile.open(tgz_file_path) as housing_tgz_file_object:
                housing_tgz_file_object.extractall(path=raw_data_dir)
            
            logging.info("Extraction completed")

        except Exception as e:
            raise HousingException(e,sys) from e

    def split_data_as_train_test(self):
        try:
            # fetch raw csv file from raw folder
            # get the folder name
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            
            # get file name
            file_name = os.listdir(raw_data_dir)[0]

            # build complete file path
            housing_file_path = os.path.join(raw_data_dir , file_name)

            # read csv file into pandas dataframe
            logging.info(f"Reading csv file: [{housing_file_path}]")
            housing_df = pd.read_csv(housing_file_path)

            # this is specific to this project
            housing_df["income_cat"] = pd.cut(housing_df["median_income"] , 
                                       bins = [0.0 , 1.5 , 3.0 , 4.5 , 6.0 , np.inf] ,
                                       labels = [1, 2, 3, 4, 5])

            # train test split
            logging.info("Splitting data into train test")
            strat_train_set = None
            strat_test_set = None

            split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
            for train_index, test_index in split.split(housing_df, housing_df["income_cat"]):
                strat_train_set = housing_df.loc[train_index].drop(["income_cat"], axis=1)
                strat_test_set = housing_df.loc[test_index].drop(["income_cat"], axis=1)

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir, file_name)
            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir, file_name)

            # create folder and save the files
            if strat_train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir, exist_ok=True)
                logging.info(f"Exporting training dataset to file: [{train_file_path}]")
                strat_train_set.to_csv(train_file_path, index=False)

            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok=True)
                logging.info(f"Exporting test dataset to file: [{test_file_path}]")
                strat_test_set.to_csv(test_file_path, index=False)
            
            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path ,
                                        test_file_path=test_file_path ,
                                        is_ingested=True ,
                                        message="Data Ingested Completed")
            logging.info(f"Data Ingestion Artifact: [{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise HousingException(e,sys) from e
    
    def inititate_data_ingestion(self)->DataIngestionArtifact:
        try:
            # download the file
            tgz_file_path = self.download_housing_data()

            # extract the file
            self.extract_tgz_file(tgz_file_path=tgz_file_path)

            # do train test split and return named tuple with info
            return self.split_data_as_train_test()

        except Exception as e:
            raise HousingException(e,sys) from e

    def __del__(self):
        logging.info(f"{'='*20}Data Ingestion Completed.{'='*20} \n\n")