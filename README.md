# My MCP Server

A Python-based Model Context Protocol (MCP) server that provides various utility tools including greeting functionality, file system operations, and weather information.

## Features

This MCP server provides the following tools:

### 🌟 **say_hello**
- **Description**: A friendly greeting function
- **Parameters**: `name` (string) - The name of the person to greet
- **Returns**: A personalized welcome message
- **Example**: `say_hello("Max")` → `"Hello, Max! Welcome to MCP."`

### 📁 **list_directory**
- **Description**: Lists the contents of a specified directory
- **Parameters**: `directory_path` (string) - Path to the directory
- **Returns**: List of file and folder names
- **Error Handling**: Returns appropriate messages for missing directories or permission issues

### 📋 **list_details**
- **Description**: Provides detailed information about directory contents
- **Parameters**: `directory_path` (string) - Path to the directory
- **Returns**: Detailed list with:
  - File/folder name
  - Size in bytes
  - Type (file or directory)
  - Last modified timestamp
- **Error Handling**: Validates path existence and directory type

### 🌤️ **get_weather**
- **Description**: Fetches current weather information for any city or country
- **Parameters**: `location` (string) - City or country name (e.g., 'Sydney', 'Paris')
- **Returns**: Current weather summary with temperature and conditions
- **Data Source**: Uses wttr.in weather service
- **Example**: `get_weather("Sydney")` → `"Sydney: ⛅️ +12°C"`

## Requirements

- Python 3.7+
- Required packages:
  - `mcp` - Model Context Protocol library
  - `requests` - For HTTP requests (weather functionality)
  - `pathlib` - For modern file path handling (built-in)
  - `datetime` - For timestamp formatting (built-in)

## Installation

1. **Clone or download this project**
   ```bash
   git clone <repository-url>
   cd mcp-exercise
   ```

2. **Install required dependencies**
   ```bash
   pip install mcp requests
   ```

3. **Verify installation**
   ```bash
   python my_mcp_server.py
   ```

## Usage

### Running the Server

To start the MCP server:

```bash
python my_mcp_server.py
```

The server will start and listen for connections via stdio (standard input/output).

### Testing Individual Functions

You can test the functions directly by importing them:

```python
from my_mcp_server import say_hello, list_directory, list_details, get_weather

# Test greeting
print(say_hello("World"))

# Test directory listing
print(list_directory("C:\\Users"))

# Test detailed directory listing
details = list_details("C:\\Users")
for item in details:
    print(f"{item['name']} - {item['type']} - {item['size']} bytes")

# Test weather
print(get_weather("London"))
```

### Example Test Scripts

The project includes several test scripts:

- `test_hello.py` - Tests the greeting functionality
- `test_list_dir.py` - Tests directory listing
- `test_list_details.py` - Tests detailed directory information
- `test_weather.py` - Tests weather functionality

## MCP Configuration

This server is configured to work with the Model Context Protocol. To use it with an MCP client:

1. Start the server: `python my_mcp_server.py`
2. Configure your MCP client to connect via stdio
3. The server will expose all four tools for use

## Error Handling

The server includes robust error handling:

- **File System Operations**: Handles missing directories, permission errors
- **Weather Service**: Manages network errors, invalid locations, API failures
- **General**: Catches and reports unexpected exceptions

## Project Structure

```
mcp-exercise/
├── my_mcp_server.py      # Main MCP server implementation
├── mcp.json              # MCP configuration
├── test_*.py             # Test scripts
├── README.md             # This documentation
└── __pycache__/          # Python cache directory
```

## API Reference

### Tool Signatures

```python
def say_hello(name: str) -> str
def list_directory(directory_path: str) -> list
def list_details(directory_path: str) -> list
def get_weather(location: str) -> str
```

## Contributing

To add new tools to this MCP server:

1. Create a new function with the `@server.tool()` decorator
2. Add proper type hints and docstrings
3. Include error handling as appropriate
4. Test the new functionality

## License

This project is open source and available under the MIT License.

## Changelog

- **v1.0** - Initial release with basic greeting functionality
- **v1.1** - Added file system operations (list_directory, list_details)
- **v1.2** - Added weather functionality using wttr.in service

## Support

For issues or questions about this MCP server, please check the documentation or create an issue in the project repository.
