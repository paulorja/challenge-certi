build:
	docker build -t webapp .

run:
	docker-compose up

check:
	docker-compose run --entrypoint "coverage run tests/http_server_tests.py" webapp

shell:
	docker-compose run --entrypoint sh webapp
