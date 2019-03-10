stop:
	docker-compose stop

cleanup: stop
	docker-compose rm -f -v

run:
	docker-compose up

check:
	docker-compose run --entrypoint "coverage run number_to_text/number_to_text_tests.py" webapp

shell:
	docker-compose run --entrypoint sh webapp
