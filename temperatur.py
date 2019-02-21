"""
This is the TEMPERATUR module and supports all the ReST actions
"""

# System modules

import max31865

# GIPO 5
max1 = max31865.max31865(5,9,10,11)
# GIPO 6
max2 = max31865.max31865(6,9,10,11)

# 3rd party modules
from flask import make_response, abort


#def get_timestamp():
#    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with the API
TEMPERATUR = {
    "sensor1": {
        "Optitop 1 Temp": max1.readTemp()

    },
    "sensor2": {
        "Optitop 2 Temp": max2.readTemp()
    },
}


def read_all():
    """
    This function responds to a request for /api/TEMPERATUR
    with the complete lists of people

    :return:        json string of list of people
    """
    # Create the list of TEMPERATUR from our data
    return [TEMPERATUR[key] for key in sorted(TEMPERATUR.keys())]


def read_one(Temp):
    """
    This function responds to a request for /api/TEMPERATUR/{Temp}
    with one matching Temp from TEMPERATUR

    :param Temp:   last name of Temp to find
    :return:        Temp matching last name
    """
    # Does the Temp exist in TEMPERATUR?
    if Temp in TEMPERATUR:
        sensor = TEMPERATUR.get(Temp)

    # otherwise, nope, not found
    else:
        abort(
            404, "Temp not found".format(Temp=Temp)
        )

    return Temp

