from selenium.webdriver.remote.webdriver import WebDriver

def get_navigation_timings(driver: WebDriver) -> dict:


    timing = driver.execute_script("return window.performance.timing")

    metrics = {
        "navigationStart": timing["navigationStart"],
        "domContentLoadedEventEnd": timing["domContentLoadedEventEnd"],
        "loadEventEnd": timing["loadEventEnd"],
        "responseStart": timing["responseStart"],
        "responseEnd": timing["responseEnd"],
        "domInteractive": timing["domInteractive"],
    }

    results = {
        "time_to_first_byte": timing["responseStart"] - timing["navigationStart"],
        "dom_interactive": timing["domInteractive"] - timing["navigationStart"],
        "dom_content_loaded": timing["domContentLoadedEventEnd"] - timing["navigationStart"],
        "page_load_time": timing["loadEventEnd"] - timing["navigationStart"],
        "backend_response_time": timing["responseEnd"] - timing["requestStart"]
        if "requestStart" in timing and timing["requestStart"] > 0 else None,
    }

    return results
