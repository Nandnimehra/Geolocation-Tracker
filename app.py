import requests
import folium
import webbrowser

def get_location():
    url = "http://ip-api.com/json/"

    try:
        response = requests.get(url)
        data = response.json()

        if data["status"] == "success":
            return data
        else:
            return None

    except Exception as e:
        print("Error:", e)
        return None


def create_map(lat, lon, city):
    m = folium.Map(location=[lat, lon], zoom_start=12)

    folium.Marker(
        [lat, lon],
        popup=city,
        tooltip="Your Location"
    ).add_to(m)

    m.save("location.html")
    webbrowser.open("location.html")


def main():

    print("=" * 40)
    print("      GEOLOCATION TRACKER")
    print("=" * 40)

    location = get_location()

    if location:

        print("IP Address :", location["query"])
        print("City       :", location["city"])
        print("State      :", location["regionName"])
        print("Country    :", location["country"])
        print("Latitude   :", location["lat"])
        print("Longitude  :", location["lon"])

        create_map(
            location["lat"],
            location["lon"],
            location["city"]
        )

    else:
        print("Unable to fetch location.")


if __name__ == "__main__":
    main()