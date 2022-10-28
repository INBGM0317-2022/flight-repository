from __future__ import annotations

from dataclasses import field, dataclass
from enum import Enum


@dataclass
class Route:
    """
    Represents a route.
    """
    destination: str = field(hash=True)
    """destination of the route"""
    country: str = field(compare=False)
    """country of the destination"""
    duration: int = field(compare=False)
    """flight time"""
    operator: Airline = field(compare=False)
    """operating airline"""
    flights: list[Flight] = field(compare=False, repr=False, default_factory=lambda: [])
    """flights of the route"""

    class Airline(Enum):
        """
        Represents themes of LEGO sets.

        * CITY = "City"
        * HARRY_POTTER = "Harry Potter"
        * STAR_WARS = "Star Wars"
        * CREATOR_EXPERT = "Creator Expert"
        """
        DLH = "Lufthansa",
        WZZ = "Wizz Air"
        RYR = "Ryanair"
        KLM = "KML"

    @dataclass
    class Flight:
        """
        Represents a flight.
        """
        number: str = field(hash=True)
        """number of the flight"""
        registration: str = field(compare=False)
        """registration of the aircraft"""
        delay: int = field(compare=False)
        """delay of the flight"""
