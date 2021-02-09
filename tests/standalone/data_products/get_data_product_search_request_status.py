import aurorax
import datetime
import time
import pprint


def main():
    # start search
    print("Executing request ...")
    s = aurorax.data_products.Search(datetime.datetime(2020, 1, 1, 0, 0, 0),
                                     datetime.datetime(2020, 1, 1, 23, 59, 59),
                                     programs=["themis-asi"],
                                     platforms=["gillam"],
                                     instrument_types=["panchromatic ASI"])
    s.execute()

    # get status
    print("Getting request status ...")
    status = aurorax.data_products.get_request_status(s.request_id)
    pprint.pprint(status)
    print("----------------------------\n")

    # if the request isn't done, wait continuously
    print("Waiting for request to complete ...")
    while (status["request_status"]["completed"] is False):
        time.sleep(1)
        status = aurorax.data_products.get_request_status(s.request_id)

    # print status
    pprint.pprint(status)


# ----------
if (__name__ == "__main__"):
    main()