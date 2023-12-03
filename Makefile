deploy:
	eb init -p python-3.11 --region eu-west-1 docker-csd
	eb create demo-1