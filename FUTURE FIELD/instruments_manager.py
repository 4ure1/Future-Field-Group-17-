"""
instruments_manager.py

Agricultural Equipment Management System :
- Add equipment 
- Remove equipment
- Update equipment information
- Search for equipment
- List all equipment
"""

from dataclasses import dataclass, asdict
from typing import Dict, List, Optional


@dataclass
class Instrument:
    """
    Represents an agricultural instrument.
    """
    instrument_id: int
    name: str
    category: str
    purchase_year: int
    condition: str
    maintenance_cost: float = 0.0


class InstrumentsManager:
    """
    Agricultural Equipment Management System.
    """

    def __init__(self):
        self._instruments: Dict[int, Instrument] = {}

    def add_instrument(
        self,
        instrument_id: int,
        name: str,
        category: str,
        purchase_year: int,
        condition: str,
        maintenance_cost: float = 0.0
    ) -> bool:
        """
        Add a new instrument.
        """
        if instrument_id in self._instruments:
            return False

        self._instruments[instrument_id] = Instrument(
            instrument_id=instrument_id,
            name=name,
            category=category,
            purchase_year=purchase_year,
            condition=condition,
            maintenance_cost=maintenance_cost
        )
        return True

    def remove_instrument(self, instrument_id: int) -> bool:
        """
        Remove an instrument.
        """
        if instrument_id not in self._instruments:
            return False

        del self._instruments[instrument_id]
        return True

    def update_instrument(
        self,
        instrument_id: int,
        **kwargs
    ) -> bool:
        """
        Update an existing instrument.
        """
        instrument = self._instruments.get(instrument_id)

        if not instrument:
            return False

        for key, value in kwargs.items():
            if hasattr(instrument, key):
                setattr(instrument, key, value)

        return True

    def get_instrument(self, instrument_id: int) -> Optional[dict]:
        """
        Return the information of a specific instrument.
        """
        instrument = self._instruments.get(instrument_id)

        if not instrument:
            return None

        return asdict(instrument)

    def list_instruments(self) -> List[dict]:
        """
        Return the complete list of instruments.
        """
        return [asdict(inst) for inst in self._instruments.values()]

    def get_total_maintenance_cost(self) -> float:
        """
        Calculate the total maintenance cost.
        """
        return sum(
            instrument.maintenance_cost
            for instrument in self._instruments.values()
        )

    def count_instruments(self) -> int:
        """
        Return the total number of instruments.
        """
        return len(self._instruments)


if __name__ == "__main__":

    manager = InstrumentsManager()

    manager.add_instrument(
        1,
        "Tractor John Deere",
        "Tractor",
        2020,
        "Excellent",
        1500.0
    )

    manager.add_instrument(
        2,
        "Sprayer",
        "Treatment",
        2022,
        "Good",
        300.0
    )

    print("\ninstruments list :")
    for item in manager.list_instruments():
        print(item)

    print("\nTotal maintenance cost :")
    print(manager.get_total_maintenance_cost())

    manager.update_instrument(
        2,
        condition="Very Good",
        maintenance_cost=450.0
    )

    print("\nAfter update :")
    print(manager.get_instrument(2))
