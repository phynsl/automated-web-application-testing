from framework.metrics.navigation_timing import get_navigation_timings

def test_page_performance(driver):
    driver.get("http://localhost/selfconcept/index.html")
    metrics = get_navigation_timings(driver)

    assert metrics["page_load_time"] < 3000, "Страница грузится слишком медленно"

