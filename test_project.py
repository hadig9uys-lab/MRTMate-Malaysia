from project import (
    normalize_station_name,
    calculate_station_count,
    create_mrt_system
)


def test_normalize_station_name():
    assert normalize_station_name("  serdang raya utara  ") == "Serdang Raya Utara"
    assert normalize_station_name("trx") == "Tun Razak Exchange (TRX)"


def test_calculate_station_count():
    route = ["A", "B", "C", "D"]

    assert calculate_station_count(route) == 3


def test_create_mrt_system():
    mrt = create_mrt_system()

    assert "Serdang Raya Utara" in mrt.stations
    assert "Tun Razak Exchange (TRX)" in mrt.stations
    assert "Putrajaya Sentral" in mrt.stations

