from testcontainers.core.container import DockerContainer

class MockApiContainer:
    def __init__(self, port=8080):
        self.container = DockerContainer("wiremock/wiremock:2.35.0").with_exposed_ports(port)

    def start(self):
        self.container.start()
        return f"http://{self.container.get_container_host_ip()}:{self.container.get_exposed_port(8080)}"

    def stop(self):
        self.container.stop()
