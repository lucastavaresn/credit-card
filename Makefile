run:
	uvicorn credit_card.main:app --port 8000 --reload

test:
	pytest -vv

format:
	@echo "Start isort execution:"
	@poetry run isort ./credit_card ./tests
	@echo ""

	@echo "Start black execution:"
	@poetry run black ./credit_card ./tests --target-version py310
	@echo "Finished black execution."
	@echo ""

clean:
	@echo "Cleaning cache..."
	@find . | egrep '.pyc|.pyo|pycache' | xargs rm -rf
	@find . | egrep '.pyc|.pyo|pycache|pytest_cache' | xargs rm -rf
	@rm -rf ./pycache
	@rm -rf ./.pytest_cache
	@rm -rf ./.mypy_cache