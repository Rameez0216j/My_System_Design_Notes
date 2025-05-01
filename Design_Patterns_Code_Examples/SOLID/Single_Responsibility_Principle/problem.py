class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate_report(self):
        return f"Report Title: {self.title}\nContent: {self.content}"

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write(self.generate_report())
        print("Report saved to file.")

# Issue:
# - The `Report` class has two responsibilities:
#   1. Generating the report content.
#   2. Handling file operations for saving the report.
# - Any change in file handling logic (e.g., saving to a database or cloud) will require modifying the `Report` class, violating SRP.
