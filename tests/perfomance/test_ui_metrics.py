from framework.metrics.navigation_timing import get_navigation_timings
from framework.metrics.resource_metrics import get_resource_count
from framework.metrics.browser_logs import get_js_errors

def test_ui_metrics(browser):
    browser.get("http://localhost/selfconcept/index.html")

    timings = get_navigation_timings(browser)
    resources = get_resource_count(browser)
    js_errors = get_js_errors(browser)

    assert timings["frontend"] < 2.0
    assert resources["images"] < 50
    assert not js_errors
