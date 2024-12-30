# Define the Python interpreter
PYTHON := python3

# Default target
.PHONY: all
all: update-readme

# Target to update the README file
.PHONY: update-readme
update-readme:
	@echo "Updating README.md..."
	$(PYTHON) update_readme.py

# Clean target (optional: for cleaning temporary files, if any)
.PHONY: clean
clean:
	@echo "Cleaning temporary files..."
	@rm -f *.pyc
	@rm -rf __pycache__

# Help target
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  all              - Default target, runs update-readme."
	@echo "  update-readme    - Updates the README.md with the folder list."
	@echo "  clean            - Removes temporary files."
	@echo "  help             - Shows this help message."
