# The dataset contains text and metadata from 244 websites and represents 12,999 posts in total 
# from the past 30 days. The data was pulled using the webhose.io API; because it's coming from 
# their crawler, not all websites identified by the BS Detector are present in this dataset. 
# Each website was labeled according to the BS Detector as documented here. Data sources that were 
# missing a label were simply assigned a label of "bs". There are (ostensibly) no genuine, reliable, 
# or trustworthy news sources represented in this dataset (so far), so don't trust anything you read.

# Input data files are available in the "../datasetsfake-news.csv" directory.
# Data files downloaded from https://www.kaggle.com/mrisdal/fake-news/downloads/fake-news.zip
from subprocess import check_output
print(check_output(["ls", "../datasets"]).decode("utf8"))
