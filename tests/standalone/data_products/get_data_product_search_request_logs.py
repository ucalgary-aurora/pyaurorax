import aurorax
import datetime
import time
import pprint


def main():
    # start search
    print("Executing search ...")
    s = aurorax.data_products.Search(datetime.datetime(2020, 1, 1, 0, 0, 0),
                                     datetime.datetime(2020, 1, 1, 23, 59, 59),
                                     programs=["themis-asi"],
                                     platforms=["gillam"],
                                     instrument_types=["panchromatic ASI"])
    s.execute()

    # if the request isn't done, wait continuously
    print("Waiting for request to complete ...")
    status = aurorax.data_products.get_request_status(s.request_id)
    while (status["request_status"]["completed"] is False):
        time.sleep(1)
        status = aurorax.data_products.get_request_status(s.request_id)

    # get request logs
    print("Retrieving logs ...")
    logs = aurorax.data_products.get_request_logs(s.request_id)

    # print logs
    print()
    pprint.pprint(logs)


# ----------
if (__name__ == "__main__"):
    main()