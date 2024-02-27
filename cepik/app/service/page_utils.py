from enum import Enum

class VehicleHistoryInformation(Enum):
    """Enum class to represent vehicle history information.

    Possible values:
    - MOT_STATUS: Represents the MOT status information, its value is css selector used to obtain mot information.
    - INSURANCE_STATUS: Represents the insurance status information, its value is css selector used to obtain mot information.
    """
    MOT_STATUS = '.tech .strong'
    INSURANCE_STATUS = '.oc .strong'


def map_report_result(result: dict[VehicleHistoryInformation, str]) -> dict[VehicleHistoryInformation]:
    """
    Maps the result dictionary containing VehicleHistoryInformation as keys and corresponding str values
    to a new dictionary with mapped keys based on the input values.

    :param result: The input dictionary containing VehicleHistoryInformation as keys and str as values.
    :return: A new dictionary with mapped keys based on the input values.
    """
    mapped_result = {}
    for key, value in result.items():
        match key:
            case VehicleHistoryInformation.MOT_STATUS:
                mapped_result['mot_valid'] = True if value == 'aktualne' else False

            case VehicleHistoryInformation.INSURANCE_STATUS:
                mapped_result['insurance_valid'] = True if value == 'aktualna' else False

    return mapped_result
