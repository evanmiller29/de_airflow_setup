sudo apt install unzip
sudo snap install docker

mkdir -p airflow-materials
unzip /home/evanmiller/airflow-materials.zip

cd airflow-materials/airflow-section-3
sudo sh start.sh