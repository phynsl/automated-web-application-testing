from testcontainers.selenium import BrowserWebDriverContainer

class ChromeContainer:
    def __init__(self, version="latest"):
        self.container = BrowserWebDriverContainer("selenium/standalone-chrome", version=version)

    def start(self):
        self.container.start()
        return self.container.get_driver()

    def stop(self):
        self.container.stop()
