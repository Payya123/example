class AwsClass:
    """A simple AWS class template"""
    
    def __init__(self, name):
        """Initialize the class with a name"""
        self.name = name
    
    def display_info(self):
        """Display class information"""
        print(f"AWS Class: {self.name}")
    
    def process_data(self, data):
        """Process input data"""
        return f"Processing {data} in {self.name}"


# Example usage
if __name__ == "__main__":
    aws = AwsClass("MyAwsService")
    aws.display_info()
    result = aws.process_data("test_data")
    print(result)
