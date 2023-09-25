run:
	uvicorn credit_card.main:app --port 8000 --reload

test:
	pytest -vv

format:
	@echo "Start isort execution:"
	@poetry run isort ./credit_card ./tests
	@echo "Finished isort execution."
	@echo ""

	@echo "Start black execution:"
	@poetry run black ./credit_card ./tests --target-version py310
	@echo "Finished black execution."
	@echo ""