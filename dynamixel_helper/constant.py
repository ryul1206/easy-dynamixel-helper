############################################
#              Auto Mode
############################################

_baudrates = [
    9600,
    57600,
    115200,
    1000000,
    2000000,
    3000000,
    4000000,
    4500000]

# protocol_version = [1.0, 2.0]

############################################
#              Verbosity
############################################

_verbose_level = {'quiet': 0, 'minimal': 1, 'detailed': 2}


def assert_verbosity(verbosity):
    """Safety check for verbosity string.

    Args:
        verbosity: 'quiet' or 'minimal' or 'detailed'
    Raises:
        RuntimeError: If the verbosity string is not in verbose_level
    """
    if verbosity not in _verbose_level:
        print("Helper: [ERROR]")
        print("        An undefined verbosity option has been detected.")
        print("        Supported options: {}".format(_verbose_level.keys()))
        raise RuntimeError
