# ETL/Data Pipelining Project Using AWSservice
In this repository, there are 2 folders: **AmazonDataExtraction** and **SpotifyETL**

## AmazonDataExtraction:
In this project, the goal was to extract data from the amazon website using **BeautifulSoup** library.

1. The rough basic work is shown in:

[Click Here](https://github.com/richardwarepam16/ETL-Data_Pipelining_Project_using_AWSservice/blob/master/AmazonDataExtraction/data_extraction.ipynb)

2. After aggregating all the logic from the basic rough work, I have defined all the functions and extracted data from the website in:

[Click Here](https://github.com/richardwarepam16/ETL-Data_Pipelining_Project_using_AWSservice/blob/master/AmazonDataExtraction/amazon_etl.ipynb)

3. The extra file "amazon_etl.py" is a folder created to define all the functions in a python file and can be later form a pipeline using **AirFlow**.

### Possible Future Improvement in this project are:

1. Loading the extracted data to **S3 storage** using **Airflow**.

2. Then, Modeling the data into **star schema** and finally loading into **Redshift** for further **Analytical Work**

## SpotifyETL:
In this project, the goal was to extract data from a playlist of spotify using **Spotify API** (Spotipy Library)

### Steps of the Project:

1. Build a basic file to explore and extract the data:

[Click Here](https://github.com/richardwarepam16/ETL-Data_Pipelining_Project_using_AWSservice/blob/master/SpotifyETL/DataPipeline.ipynb)

2. Build a python file that connects us to the **spotify api**:

[Click Here](https://github.com/richardwarepam16/ETL-Data_Pipelining_Project_using_AWSservice/blob/master/SpotifyETL/spotify_api_dataExtract.py)

3. Build a python file to define the proper functions of extracting with the help of the above rough work file:

[Click Here](https://github.com/richardwarepam16/ETL-Data_Pipelining_Project_using_AWSservice/blob/master/SpotifyETL/tranform_load_function.py)

4. Now, Create an **EC2 instance** in **AWS Console**.

5. After Connecting to the instance, Install all the dependencies needed for the server:

[Click Here](https://github.com/richardwarepam16/ETL-Data_Pipelining_Project_using_AWSservice/blob/master/SpotifyETL/airflow_commands.sh)

6. Finally, create a DAG file to be used in **Airflow**:

[Click Here](https://github.com/richardwarepam16/ETL-Data_Pipelining_Project_using_AWSservice/blob/master/SpotifyETL/spotify_dag.py)

Then, Perform the functions through **Airflow** and the data will be loaded in **S3 Storage**.

### Possible Future Improvement in this project are:

- Modeling the data into **star schema** and finally loading into **Redshift** for further **Analytical Work**.

## About the Contributer:

My name is **WAREPAM RICHARD SINGH**. In this Project, I have learned:
1. **Data Extraction**
2. **Data Modelling**: (draw.io/ Lucid)
3. **Data Transformation**
4. **Data Loading**
5. **AWS Services**: S3, Apache Airflow, Redshift

## My Social Media Links

For more project Updates, You can find me on:

- [Twitter](https://twitter.com/codeWarepam)
- [Instagram](https://www.instagram.com/warepam10/?next=%2F)
- [LinkedIn](https://www.linkedin.com/in/richard-w-3b817420b/)
