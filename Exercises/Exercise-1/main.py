import requests
from logger import logger
from os.path import join,exists
from os import mkdir
from zipfile import ZipFile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def download_files(uri:str,dest_folder:str) -> str | None:
    logger.info("Starting the download...")
    logger.info(f"URI : {uri}")
    file_name = uri.split("/")[-1]
    file_path = join(dest_folder, file_name) # os path join 
    try:
        with requests.get(uri,stream=True,timeout=10) as response:
            response.raise_for_status() # Checks for status codes
            logger.info("Download Completed")
            with open(file_name, 'wb') as file:
                for text in response.iter_content(chunk_size=4096):
                    file.write(text)
        logger.info(f"File Created: {file}")
        return file_name
    except Exception as e:
        logger.error(f"Error: {e}")
        return None
    
def unzip(file_name:str , dest_folder:str) -> None:
    try:
        with ZipFile(file_name) as zip_file:
            logger.info(f"Unzipping {file_name}")
            zip_file.extractall(dest_folder)
        logger.info("Extracted.")
    except Exception as e:
        logger.error(f"Error: {e}")

    except:...
def downloader(uri_list:list,dest_folder:str) -> None:
    if not exists(dest_folder):
        mkdir(dest_folder)

    for uri in uri_list:
        download_files(uri,dest_folder)




def main():
    downloader(download_uris,'./downloads')

if __name__ == "__main__":
    main()
