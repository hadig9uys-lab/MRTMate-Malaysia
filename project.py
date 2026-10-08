import networkx as nx
import pyfiglet
from rich.console import Console
from rich.table import Table

console = Console()

class Station:
    def __init__(self, name, line, facilities=None):
        self.name = name
        self.line = line
        self.facilities = facilities or []

    def __str__(self):
        return f"{self.name} - {self.line} Line"

class Journey:
    def __init__(self, start, destination, route):
        self.start = start
        self.destination = destination
        self.route = route

    @property
    def station_count(self):
        return len(self.route) - 1

class MRTSystem:
    def __init__(self):
        self.graph = nx.Graph()
        self.stations = {}

    def add_station(self, station):
        self.stations[station.name] = station
        self.graph.add_node(station.name)

    def connect(self, station1, station2):
        self.graph.add_edge(station1, station2)

    def find_route(self, start, destination):
        return nx.shortest_path(
            self.graph,
            source = start,
            target = destination
        )

def normalize_station_name(name):
    name = name.strip()

    if name.lower() == "trx":
        return "Tun Razak Exchange (TRX)"

    return name.title()


def calculate_station_count(route):
    return len(route) - 1

def create_mrt_system():
    mrt = MRTSystem()

    station_names = [
        "Kwasa Damansara",
        "Kampung Selamat",
        "Sungai Buloh",
        "Damansara Damai",
        "Sri Damansara Barat",
        "Sri Damansara Sentral",
        "Sri Damansara Timur",
        "Metro Prima",
        "Kepong Baru",
        "Jinjang",
        "Sri Delima",
        "Kampung Batu",
        "Kentonmen",
        "Jalan Ipoh",
        "Sentul Barat",
        "Titiwangsa",
        "Hospital Kuala Lumpur",
        "Raja Uda",
        "Ampang Park",
        "Persiaran KLCC",
        "Conlay",
        "Tun Razak Exchange (TRX)",
        "Chan Sow Lin",
        "Bandar Malaysia Utara",
        "Bandar Malaysia Selatan",
        "Kuchai",
        "Taman Naga Emas",
        "Sungai Besi",
        "Serdang Raya Utara",
        "Serdang Raya Selatan",
        "Serdang Jaya",
        "UPM",
        "Taman Equine",
        "Putra Permai",
        "16 Sierra",
        "Cyberjaya Utara",
        "Cyberjaya City Centre",
        "Putrajaya Sentral"
    ]

    for name in station_names:
        facilities = []

        if name == "Serdang Raya Utara":
            facilities = [
                "Public Toilets",
                "Surau",
                "Ticket Vending Machine",
                "Customer Service Office",
                "Park & Ride"
            ]

        station = Station(
            name,
            "Putrajaya",
            facilities
        )

        mrt.add_station(station)

    for i in range(len(station_names) - 1):
        mrt.connect(
            station_names[i],
            station_names[i + 1]
        )

    return mrt

def main():
    mrt = create_mrt_system()

    title = pyfiglet.figlet_format("MRTMate")
    console.print(title)

    while True:
        console.print("\n[bold]MRT Malaysia Smart Journey Planner[/bold]")
        console.print("1. Plan Journey")
        console.print("2. Search Station")
        console.print("3. Exit")

        choice = input("Choice: ")
        if choice == "1":
            start = normalize_station_name(
                input("Starting station: ")
            )

            destination = normalize_station_name(
                input("Destination: ")
            )

            if start not in mrt.stations or destination not in mrt.stations:
                console.print("Station not found.")
                continue

            route = mrt.find_route(
                start,
                destination
            )

            journey = Journey(
                start,
                destination,
                route
            )

            table = Table(
                title = "Your MRT Journey"
            )

            table.add_column("No.")
            table.add_column("Station")

            for number, station in enumerate(
                route,
                start=1
            ):
                table.add_row(
                    str(number),
                    station
                )

            console.print(table)

            console.print(
                f"Station travelled: {journey.station_count}"
            )

        elif choice == "2":
            name = normalize_station_name(
                input("Station name: ")
            )

            if name not in mrt.stations:
                console.print("Station not found.")
                continue

            station = mrt.stations[name]

            console.print(
                f"\n[bold]{station.name}[/bold]"
            )

            console.print(
                f"Line {station.line}"
            )

            if station.facilities:
                console.print("Facilities: ")

                for facility in station.facilities:
                    console.print(
                        f"- {facility}"
                    )

            else:
                console.print(
                    "No detailed facilities stored yet."
                )

        elif choice == "3":
            console.print("Goodbye!")
            break

        else:
            console.print("Invalid choice.")

if __name__ == "__main__":
    main()

