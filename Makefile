run:
	docker-compose up

check:
	docker-compose run --entrypoint "coverage run number_to_text/number_to_text_tests.py" challenge-webapp

shell:
	docker-compose run --entrypoint sh webapp
