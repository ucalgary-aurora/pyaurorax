from typing import List
import aurorax
import datetime

def test_availability():

    start_date = datetime.datetime(2019, 1, 1)
    end_date = datetime.date(2019, 1, 2)
    program = "swarm"
    platform = "swarma"
    instrument_type = "footprint"

    # get availability
    availability = aurorax.availability.ephemeris(start_date,
                                                  end_date,
                                                  program=program,
                                                  platform=platform,
                                                  instrument_type=instrument_type)

    assert type(availability) is list and len(availability) > 0 and type(availability[0]) is aurorax.availability.AvailabilityResult and availability[0].data_source.program == "swarm"