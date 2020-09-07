from .api import URL_EPHEMERIS_SOURCES
from .api import AuroraXRequest


def get_sources(program=None, platform=None, instrument_type=None, source_type=None, owner=None, format="basic_info"):
    """
    Returns a list of dictionaries representing all ephemeris sources

    :param program: program name to filter sources by, optional
    :param platform: platform name to filter sources by, optional
    :param instrument_type: instrument type to filter sources by, optional
    :param source_type: source type to filter sources by (e.g. "heo"), optional
    :param owner: owner ID to filter sources by, optional
    :param format: the format of the ephemeris source returned Available values: "identifier_only", "basic_info",
                   "full_record". Default is "basic_info"

    :return: a dictionary of all ephemeris sources
    """
    params = {
        "program": program,
        "platform": platform,
        "instrument_type": instrument_type,
        "source_type": source_type,
        "owner": owner,
        "format": format
    }
    req = AuroraXRequest(URL_EPHEMERIS_SOURCES, params=params)
    res = req.execute()
    return res


def add_source(api_key, program, platform, instrument_type, source_type, metadata_schema={}, maintainers=[]):
    pass


def remove_source(api_key, program, platform, instrument_type, source_type, metadata_schema={}, maintainers=[]):
    pass
