create:
	eb init -p python-3.11 --region eu-west-1 csd
	eb create -c csd-staging env-2

deploy:
	eb init -p python-3.11 --region eu-west-1 csd
	eb deploy -l 1 staging

deploy-1:
	eb init -p python-3.11 --region eu-west-1 csd
	eb deploy -l 1 csd-env-water

clone:
	eb init -p python-3.11 --region eu-west-1 docker-csd
	eb clone -n tmp-dev demo-1

swap:
	eb init -p python-3.11 --region eu-west-1 docker-csd
	eb swap csd-env-earth  -n  csd-env-water

local:
	docker build -t csd .
	docker run -p 80:80 csd