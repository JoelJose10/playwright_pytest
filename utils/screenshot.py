import os


RESULTS_DIR = "results"


def take_screenshot(page, test_name):
    """Take a screenshot and save it to the results folder."""
    filename = f"{test_name}.png"
    filepath = os.path.join(RESULTS_DIR, filename)
    page.screenshot(path=filepath)
    print(f"Screenshot saved: {filepath}")
    return filepath
