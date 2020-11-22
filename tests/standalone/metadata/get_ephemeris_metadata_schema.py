import aurorax
import pprint


def main():
    # set parameters
    program = "swarm"
    platform = "swarma"
    instrument_type = "ssc-web"
    print("Retrieving ephemeris metadata schema with the parameters:")
    print("  Program:\t\t%s" % (program))
    print("  Platform:\t\t%s" % (platform))
    print("  Instrument Type:\t%s\n" % (instrument_type))

    # get idendifier
    data_source = aurorax.sources.get_using_filters(program=program,
                                                    platform=platform,
                                                    instrument_type=instrument_type)

    # get schema
    schema = aurorax.metadata.get_ephemeris_schema(data_source["data"][0]["identifier"])
    pprint.pprint(schema)


# ----------
if (__name__ == "__main__"):
    main()
