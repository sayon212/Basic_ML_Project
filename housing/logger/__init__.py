# import libraries
import logging
import os
from datetime import datetime

# set log directory
log_dir = "housing_logs"

# set current timestamp
current_timestamp = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

# create logfile for each run
log_file = f"log_{current_timestamp}.log"

# create file path
file_path = os.path.join(log_dir,log_file)

# if directory doesnot exist the create
os.makedirs(log_dir , exist_ok=True)

logging.basicConfig(
    filename=file_path , 
    filemode='w' , 
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s' ,
    level=logging.INFO
    )