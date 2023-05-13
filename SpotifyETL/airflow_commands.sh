# Install Dependencies in ec2 server:
sudo apt-get update
sudo apt install python3-pip
sudo pip install apache-airflow
sudo pip install pandas
sudo pip install boto3
sudo pip install spotipy

#Start Airflow:
airflow standalone
