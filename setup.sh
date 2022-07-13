docker image build ML_projet2_api/ -t ml-api-sentiment-analysis:latest
docker image build projet2_test_image/ -t ml-api-sentiments-analysis-tests:latest
docker volume create --name my_volume_for_project2
docker-compose up
