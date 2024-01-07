import kaggle

# Provide the dataset name
dataset_name = 'ylchang/coffee-shop-sample-data-1113'
# Specify the download directory
download_path = 'G:/Data Science Job and Internship/Personal Projects/DW-Analytics-Personal-Project/Flat-files'
# Download the dataset to the specified directory
kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=True)