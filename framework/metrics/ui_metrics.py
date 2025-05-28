import time

class UIMetrics:
    def __init__(self):
        self.metrics = {}

    def start_timer(self, name):
        self.metrics[name] = {'start': time.time()}

    def stop_timer(self, name):
        if name in self.metrics and 'start' in self.metrics[name]:
            self.metrics[name]['end'] = time.time()
            self.metrics[name]['duration'] = self.metrics[name]['end'] - self.metrics[name]['start']

    def report(self):
        for name, data in self.metrics.items():
            print(f"🕒 {name}: {data.get('duration', 0):.2f} sec")

