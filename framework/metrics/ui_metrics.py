import json
import time

class UIMetricsCollector:
    def __init__(self, driver):
        self.driver = driver

    def collect_performance_metrics(self):
        performance = self.driver.execute_script("return window.performance.timing")
        navigation = self.driver.execute_script("return window.performance.getEntriesByType('navigation')[0]")
        resources = self.driver.execute_script("return window.performance.getEntriesByType('resource')")
        
        metrics = {
            "loadEventEnd": performance["loadEventEnd"],
            "domContentLoadedEventEnd": performance["domContentLoadedEventEnd"],
            "responseStart": performance["responseStart"],
            "responseEnd": performance["responseEnd"],
            "loadTime": navigation["loadEventEnd"] - navigation["startTime"] if navigation else None,
            "resourceCount": len(resources)
        }
        return metrics

    def collect_js_errors(self):
        logs = self.driver.get_log("browser")
        js_errors = [log for log in logs if log["level"] == "SEVERE"]
        return js_errors
