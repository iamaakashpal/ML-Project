import yaml
from housing.exception import HousingException
import os,sys

def read_yaml_file(file_path:str)->dict:
    """
    Description : This function is going to read yaml file and return a dictionary
    """
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(os,sys) from e