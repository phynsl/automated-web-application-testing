from framework.metrics.navigation_timing import get_navigation_timings

def test_page_performance(driver):
    driver.get("http://localhost/selfconcept/index.html")
    metrics = get_navigation_timings(driver)

    assert metrics["page_load_time"] < 3000, "Страница грузится слишком медленно"

def test_ttfb_below_threshold(driver):
    driver.get("http://localhost/selfconcept/index.html")
    metrics = get_navigation_timings(driver)
    assert metrics["time_to_first_byte"] < 500, "TTFB слишком большой"

def test_dom_content_loaded_below_threshold(driver):
    driver.get("http://localhost/selfconcept/index.html")
    metrics = get_navigation_timings(driver)
    assert metrics["dom_content_loaded"] < 2000, "DOMContentLoaded слишком долгий"

def test_dom_interactive_below_threshold(driver):
    driver.get("http://localhost/selfconcept/index.html")
    metrics = get_navigation_timings(driver)
    assert metrics["dom_interactive"] < 2500, "DOM стал интерактивным слишком поздно"
