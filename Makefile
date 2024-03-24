install:
		pip install --upgrade pip &&\
			pip install -r requirements.txt

# test:
# 	python -m pytest -vv --cov=./scripts/*.py ./scripts/*.py

# format:
# 	black ./Scripts/*.py

# lint:
# 	pylint --disable=R,C ./Scripts/*.py
	
# refactor: format lint

# all: install lint test format

# To test jupyter notebook code
# python -m pytest --nbval notebook.ipynb