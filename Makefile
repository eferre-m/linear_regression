RED 		= \033[0;91m
GREEN 		= \033[0;92m
YELLOW		= \033[0;93m
BLUE		= \033[0;94m
NC			= \033[0m

VENV_DIR	:= .venv
PYTHON		:= python3
VENV_PY		:= $(VENV_DIR)/bin/python
VENV_PIP	:= $(VENV_DIR)/bin/pip
STAMP		:= $(VENV_DIR)/.installed

help:
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# Create the virtual environment
venv: 
	@echo "$(BLUE)Creating virtual environment in $(VENV_DIR)...$(NC)"
	@$(PYTHON) -m venv $(VENV_DIR)

# activate venv: "source .venv/bin/activate"

$(STAMP): requirements.txt | venv
	@echo "$(BLUE)Installing dependencies...$(NC)"
	@$(VENV_PIP) install --upgrade pip -q
	@$(VENV_PIP) install -r requirements.txt -q
	@touch $(STAMP)
	@echo "$(GREEN)Dependencies installed.$(NC)"
install: $(STAMP)

train: install
	@echo "$(YELLOW)Training the model...$(NC)"
	@$(VENV_PY) src/train.py
	@echo "$(GREEN)Training done.$(NC)"

predict: install
	@echo "$(YELLOW)Enter a mileage to get a price estimate:$(NC)"
	@$(VENV_PY) src/predict.py

plot: install ## Bonus: plot the dataset and the regression line
	@echo "$(YELLOW)Generating plot...$(NC)"
	@$(VENV_PY) src/plot.py
	@echo "$(GREEN)Plot saved to plot.png$(NC)"

precision: install ## Bonus: compute MAE, RMSE and R^2 of the model
	@echo "$(YELLOW)Computing precision metrics...$(NC)"
	@$(VENV_PY) src/precision.py

flake: install
	@echo "$(YELLOW)Running flake8 linter...$(NC)"
	@$(VENV_PY) -m flake8 src

clean:
	@echo "$(RED)Removing generated artifacts...$(NC)"
	@rm -f theta.json plot.png

.PHONY: help venv install train predict plot precision flake clean fclean re