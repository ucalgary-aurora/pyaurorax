#! /usr/bin/env python

import aurorax
import pprint


def main():
    source = aurorax.get_source_using_identifier(10, format="full_record")
    pprint.pprint(source)


# ----------
if (__name__ == "__main__"):
    main()
