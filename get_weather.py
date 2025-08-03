import requests

def get_weather(location: str) -> str:
    """
    Fetches the current weather for a given city or country using wttr.in.
    Args:
        location (str): The name of the city or country (e.g., 'Paris',
        'Singapore').
    Returns:
        str: A plain-text summary of the current weather, or an error message.
    """
    try:
        url = f"https://wttr.in/{location}?format=3"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return (
                f"Error: Unable to fetch weather data "
                f"(status code {response.status_code})"
            )
    except Exception as e:
        return f"Error: {e}"

# Example usage:
if __name__ == "__main__":
    location = input("Enter a city or country: ")
    print(get_weather(location))
