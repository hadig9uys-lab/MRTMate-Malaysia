## Description

MRTMate Malaysia is a Python project that I created to make travelling on Malaysia's MRT system a little easier. The program works as a simple journey planner where users can search for MRT stations, plan a trip from one station to another, and view basic information about selected stations.

At the moment, the project focuses on the MRT Putrajaya Line. It includes stations such as Tun Razak Exchange (TRX), Sungai Besi, Serdang Raya Utara, Serdang Raya Selatan, UPM, Cyberjaya, and Putrajaya Sentral.

I chose this project because the MRT is something people use in daily life, so I wanted to create something practical instead of just making a program for practice. At the same time, the project gave me a chance to use many of the topics I learned in CS50’s Introduction to Programming with Python.

## Core Architecture & Classes

The program uses three main classes: Station, Journey, and MRTSystem.

The Station class is used to represent each MRT station. It stores information such as the station name, the MRT line, and available facilities.

The Journey class represents a trip between two stations. It keeps track of the starting station, the destination, the route, and the number of stations travelled.

The MRTSystem class manages the MRT network itself. It stores all the stations and their connections. It also uses the NetworkX library to find a route between the starting station and the destination.

## Functions

I also created several normal functions outside the classes. The normalize_station_name function cleans the user's input so that station names are easier to match. It also handles the abbreviation TRX. The calculate_station_count function calculates how many station-to-station movements are in a route. The create_mrt_system function builds the MRT network by adding the stations and connecting them in the correct order.

## External Libraries

The project uses a few external Python libraries. NetworkX is used to represent the MRT system as a graph and to calculate routes. Rich is used to make the terminal output cleaner and more attractive, especially for tables and formatted text. Pyfiglet is used to display the MRTMate title when the program starts.

## Project Structure

The main file, project.py, contains the classes, functions, station data, route-planning logic, and the main menu.

The test_project.py file contains pytest tests for the custom functions, including normalize_station_name, calculate_station_count, and create_mrt_system.

The requirements.txt file lists the external libraries needed to run the program: networkx, rich, and pyfiglet.

## Design Choices

One of the main design choices I made was to represent the MRT stations as nodes in a graph, while the connections between stations are represented as edges. I chose this approach because it matches how a transport network works and makes it easier to calculate routes using NetworkX.

## Future Improvements

In the future, I would like to expand MRTMate Malaysia by adding more MRT lines, more interchange stations, feeder bus information, estimated travel times, fare estimates, and a trip history feature.

## Conclusion

Overall, MRTMate Malaysia is a practical project that combines classes, functions, libraries, loops, conditionals, data structures, and testing into one real-world application.
