import math


def esat(t: float):
    """Calculate average saturation vapor pressure."""
    return 0.6108 * math.exp((17.27 * t) / (t + 237.3))


def j(m: int, d: int | None = None, leap: bool = False) -> float:
    """Calculate day of the year."""
    if d is not None:
        x = 0 if m <= 2 else -2 + int(leap)
        return 275 * m // 9 - 30 + d + x

    # return the middle day of the month if the day parameter wasn't specified
    days_in_month = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days_in_month[:m - 1]) + days_in_month[m - 1] // 2


def calculate_reference_evapotranspiration(
    j: int,  # day of the year
    z: float,  # elevation (m)
    lat: float,  # latitude (rad)
    tmin: float,  # min & max temperature (°C)
    tmax: float,
    humidity: float,  # (%)
    wind_speed: float,  # wind speed (m/s)
    sun_hours: float,  # sun (hr)
) -> float:
    """
    Calculate reference evapotranspiration (ETo) using the FAO-56 Penman-Monteith equation.
    """
    y = 6.73645e-2 * ((293 - 0.00625 * z) / 293) ** 5.26

    temp = (tmax + tmin) / 2

    slope = (
        4098
        * (0.6108 * math.exp((17.27 * temp) / (temp + 237.3)))
        / pow((temp + 237.3), 2)
    )

    es = (esat(tmax) + esat(tmin)) / 2
    ea = humidity / 100 * (esat(tmin + esat(tmax))) / 2

    # lat = math.pi / 180 * latitude
    dr = 1 + 3.3e-2 * math.cos(2 * math.pi * j / 356)
    d = 0.409 * math.sin(2 * math.pi * j / 356 - 1.39)
    x = max(1 - math.tan(lat) ** 2 * math.tan(d) ** 2, 1e-5)
    ws = math.pi / 2 - math.atan(-math.tan(lat) * math.tan(d) / math.sqrt(x))
    ra = (
        (24 * 60)
        / math.pi
        * 8.2e-2
        * dr
        * (
            ws
            * math.sin(lat)
            * math.sin(d)
            * math.cos(lat)
            * math.cos(d)
            * math.sin(ws)
        )
    )

    # rs = (a + b * npn) * ra
    rs = 0.16 * math.sqrt(tmax - tmin) * ra
    rns = 0.77 * rs
    rso = (0.75 + 2e-5 * z) * ra
    rnl = (
        4.903e-9
        * (tmax**4 + tmin**4)
        / 2
        * (0.34 - 0.14 * math.sqrt(ea))
        * (1.35 * rs / rso - 0.35)
    )
    rn = rns - rnl

    u2 = wind_speed * 4.87 / math.log(67.8 * z - 5.42)
    soilHflux = 0

    etr = (
        0.408 * slope * (rn - soilHflux) + y * (900 / (temp + 273)) * u2 * (es - ea)
    ) / (slope + y * (1 + 0.34 * u2))

    return etr


def main():
    print(
        calculate_reference_evapotranspiration(
            1,
            10,
            0.54,
            8.69,
            18.52,
            82.56,
            2.12,
            10,
        )
    )


if __name__ == "__main__":
    main()
