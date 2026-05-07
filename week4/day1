class DataAnalyzer:
    def __init__(self, data):
        # data = list of dictionaries
        self.data = data

    # get column values
    def get_column(self, column):
        return [row[column] for row in self.data if column in row]

    # basic stats
    def mean(self, column):
        values = self.get_column(column)
        return sum(values) / len(values) if values else 0

    def max(self, column):
        values = self.get_column(column)
        return max(values) if values else None

    def min(self, column):
        values = self.get_column(column)
        return min(values) if values else None

    # filter data
    def filter(self, column, condition):
        return [row for row in self.data if column in row and condition(row[column])]

    # sort data
    def sort(self, column):
        return sorted(self.data, key=lambda x: x.get(column, 0))

    # property (like pandas shape)
    @property
    def shape(self):
        rows = len(self.data)
        cols = len(self.data[0]) if self.data else 0
        return (rows, cols)

    # nice print
    def __str__(self):
        return f"DataAnalyzer(rows={len(self.data)})"

data = [
    {"name": "Aman", "marks": 80},
    {"name": "Riya", "marks": 95},
    {"name": "John", "marks": 70},
    {"name": "Sara", "marks": 85}
]

analyzer = DataAnalyzer(data)

# basic stats
print("Mean:", analyzer.mean("marks"))
print("Max:", analyzer.max("marks"))
print("Min:", analyzer.min("marks"))

# shape
print("Shape:", analyzer.shape)

# filtering
top_students = analyzer.filter("marks", lambda x: x > 80)
print("Top Students:", top_students)

# sorting
sorted_data = analyzer.sort("marks")
print("Sorted:", sorted_data)
