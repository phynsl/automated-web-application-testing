from testcontainers.postgres import PostgresContainer

class PostgresTestContainer:
    def __init__(self, version="15"):
        self.container = PostgresContainer("postgres:" + version)

    def start(self):
        self.container.start()
        return {
            "host": self.container.get_container_host_ip(),
            "port": self.container.get_exposed_port(5432),
            "user": self.container.POSTGRES_USER,
            "password": self.container.POSTGRES_PASSWORD,
            "database": self.container.POSTGRES_DB,
        }

    def stop(self):
        self.container.stop()
