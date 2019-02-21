"""
This is the sensor module and supports all the ReST actions
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort

# max31865 python module
import max31865

# GIPO 5 - CS sensor1
max1 = max31865.max31865(5,9,10,11)
# GIPO 6 - CS sensor2
max2 = max31865.max31865(6,9,10,11)


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with the API
sensor = {
    "1": {
        "value": max1.readTemp(),
        "name": "1",
        #"fan": fan2.setTemp(),
        "timestamp": get_timestamp(),
    },
    "2": {
        "value": max2.readTemp(),
        "name": "2",
        #"fan": fan2.setTemp(),
        "timestamp": get_timestamp(),
    },
}


def read_all():
    """
    This function responds to a request for /api/temp
    with the complete lists of sensor
    :return:        json string of list of temp
    """
    # Create the list of people from our data
    return [sensor[key] for key in sorted(sensor.keys())]


def read_one(name):
    """
    This function responds to a request for /api/temp/{name}
    with one matching sensor from temp
    :param name:   name of temp to find
    :return:        temp matching name
    """
    # Does the person exist in people?
    if name in sensor:
         = sensor.get(name)

    # otherwise, nope, not found
    else:
        abort(
            404, "Temp with name {name} not found".format(name=name)
        )

    return temp


def create(temp):
    """
    This function creates a new person in the people structure
    based on the passed in sensor data
    :param temp:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    name = temp.get("name", None)
    value = temp.get("value", None)

    # Does the temp exist already?
    if name not in sensor and name is not None:
        sensor[name] = {
            "name": name,
            "value": value,
            "timestamp": get_timestamp(),
        }
        return sensor[name], 201

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Sensor with last name {name} already exists".format(name=name),
        )


def update(name, temp):
    """
    This function updates an existing temp in the temp structure
    :param name:   name of value to update in the temp structure
    :param value:  value to update
    :return:        updated temp structure
    """
    # Does the temp exist in sensors?
    if name in sensor:
        sensor[name]["value"] = temp.get("value")
        sensor[name]["timestamp"] = get_timestamp()

        return sensor[lname]

    # otherwise, nope, that's an error
    else:
        abort(
            404, "Sensor with name {name} not found".format(name=name)
        )


def delete(name):
    """
    This function deletes a temp from the sensor structure
    :param name:   name of sensor to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the person to delete exist?
    if name in sensor:
        del sensor[name]
        return make_response(
            "{name} successfully deleted".format(name=name), 200
        )

    # Otherwise, nope, person to delete not found
    else:
        abort(
            404, "Temp with name {name} not found".format(name=name)
        )