"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    coordinate = record[-1]
    return coordinate


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    
    individual_components = tuple(coordinate)
    return individual_components


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    if tuple(azara_record[1]) == tuple(rui_record[1]):
        return True
    else:
        return False


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    new_list = (azara_record) + (rui_record)
    
    if tuple(azara_record[1]) == tuple(rui_record[1]):
        return new_list
    else:
        return 'not a match'

def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """

    cleaned_records = []

    for record in combined_record_group:
        name = record[0]
        location = record[2]
        coordinates = record[3]
        color = record[4]

        cleaned_record = f"('{name}', '{location}', {coordinates}, '{color}')"
        cleaned_records.append(cleaned_record)

    return "\n".join(cleaned_records) + "\n"


