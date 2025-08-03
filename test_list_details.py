from my_mcp_server import list_details

# Test the list_details function with C:\Users directory
result = list_details("C:\\Users")
print("Details of C:\\Users directory:")
if isinstance(result, list):
    for item in result:
        print(f"Name: {item['name']}")
        print(f"Type: {item['type']}")
        print(f"Size: {item['size']} bytes")
        print(f"Last Modified: {item['last_modified']}")
        print("-" * 40)
else:
    print(result)
