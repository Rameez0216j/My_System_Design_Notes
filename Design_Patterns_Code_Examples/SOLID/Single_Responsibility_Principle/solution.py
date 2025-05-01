"""
    Definition: A class should have only one reason to change, meaning it should have only one responsibility.
    Explanation: If a class is responsible for more than one thing, changes in one responsibility can affect the functionality of the other, making the code more fragile and harder to maintain.
"""

class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate_report(self):
        return f"Report Title: {self.title}\nContent: {self.content}"

class FileManager:
    @staticmethod
    def save_to_file(file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)
        print("Report saved to file.")

# Usage
report = Report("Monthly Sales", "The sales increased by 20% this month.")
file_manager = FileManager()
content = report.generate_report()
file_manager.save_to_file("report.txt", content)

# Fix:
# - The `Report` class is now responsible only for generating the report.
# - The `FileManager` class handles file operations, adhering to the Single Responsibility Principle.
