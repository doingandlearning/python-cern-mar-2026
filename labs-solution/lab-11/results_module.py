class ResultValue:
    """Simple analysis class for detector results."""

    def __init__(self, detector_name, date):
        self.detector_name = detector_name
        self.date = date
        self.results = []

    def add_result(self, value):
        self.results.append(value)

    def get_average_of_results(self):
        if not self.results:
            return None
        return sum(self.results) / len(self.results)

    def get_maximum_of_results(self):
        return max(self.results) if self.results else None

    def get_range_of_results(self):
        if not self.results:
            return None
        return max(self.results) - min(self.results)

