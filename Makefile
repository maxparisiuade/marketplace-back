install:
	poetry install

update:
	poetry update
	
serve:
	poetry run uvicorn main:app --host 0.0.0.0 --port 5000 --reload
zip:
	poetry export -f requirements.txt --output requirements.txt
	pip3 install --target .\libs -r requirements.txt
	copy main.py .\libs
	xcopy /s /e /i /y app .\libs\app
	cd .\libs && 7z a -r ..\lambda.zip .
	rd /s /q .\libs

.PHONY: \
	install \
	update \
	serve \
	zip