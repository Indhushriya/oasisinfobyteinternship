import requests
from rich.console import Console
from rich.tree import Tree

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }

    console = Console()

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']

            
            
            
            # Create a tree structure with styles
            weather_tree = Tree("🌡️  Weather Information🌧️", style="bold green ", guide_style="bold #fff50a")

            # Coordinates
            coord_tree = weather_tree.add("Coordinates", style="bold #51fff8")
            coord_tree.add(f"Location: {data['name']}", style="bold #516dff")
            coord_tree.add(f"Longitude: {data['coord']['lon']}", style="bold #516dff")
            coord_tree.add(f"Latitude: {data['coord']['lat']}", style="bold #516dff")

            # Weather
            weatherdesc_tree = weather_tree.add("Weather", style="bold #51fff8")
            weatherdesc_tree.add(f"Description: {weather_description}", style="bold #516dff")
            

            # Main
            main_tree = weather_tree.add("Main", style="bold #51fff8")
            main_tree.add(f"Temperature: {data['main']['temp']}°C", style="bold #516dff")
            main_tree.add(f"Feels Like: {data['main']['feels_like']}°C", style="bold #516dff")
            main_tree.add(f"Min Temperature: {data['main']['temp_min']}°C", style="bold #516dff")
            main_tree.add(f"Max Temperature: {data['main']['temp_max']}°C", style="bold #516dff")
            main_tree.add(f"Pressure: {data['main']['pressure']} hPa", style="bold #516dff")
            main_tree.add(f"Humidity: {data['main']['humidity']}%", style="bold #516dff")

            # Wind
            wind_tree = weather_tree.add("Wind", style="bold #51fff8")
            wind_tree.add(f"Speed: {data['wind']['speed']} m/s", style="bold #516dff")
            wind_tree.add(f"Direction: {data['wind']['deg']}°", style="bold #516dff")
            wind_tree.add(f"Gust: {data['wind']['gust']} m/s", style="bold #516dff")

            # Clouds
            clouds_tree = weather_tree.add("Clouds", style="bold #51fff8")
            clouds_tree.add(f"Cloudiness: {data['clouds']['all']}%", style="bold #516dff")

            # Visibility
            visibility_tree = weather_tree.add("Visibility", style="bold #51fff8")
            visibility_tree.add(f"Visibility: {data.get('visibility', 'N/A')} meters", style="bold #516dff")

            

            # Display the tree
            console.print(weather_tree)
            print(":-----------------------------------------------------------:")
        else:
            console.print(f"[bold red]Error:[/bold red] {data['message']}")

    except requests.RequestException as e:
        console.print(f"[bold red]Error fetching data:[/bold red] {e}")


api_key = ""   #api key

print("               🆂 🅺 🆈  🅸 🅽 🆂 🅸 🅶 🅷 🆃")
print(":-----------------------------------------------------------:")
location = input("Enter city or ZIP code: ")
print(":-----------------------------------------------------------:")
get_weather(api_key, location)
