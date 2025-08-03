from my_mcp_server import list_directory
import os

# Get the current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Test the list_directory function with the current directory
result = list_directory(current_dir)
print(f"Contents: {result}")
