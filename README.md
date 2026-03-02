# Sauce Demo Playwright Tests

Automated tests for [Sauce Demo](https://www.saucedemo.com) using Playwright and pytest.

## Setup

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install pytest playwright pytest-playwright

# Install browsers
playwright install
```

## Run Commands

### Basic run (headless)
```bash
pytest main.py
```

### Run with browser visible
```bash
pytest main.py --headed
```

### Run with verbose output (shows PASSED/FAILED)
```bash
pytest main.py --headed -v
```

### Run a specific test
```bash
pytest main.py::test_login_flow --headed -v
pytest main.py::test_add_fleece_jacket_to_cart --headed -v
pytest main.py::test_product_sorting --headed -v
```

