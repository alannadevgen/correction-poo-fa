from datetime import datetime


def timer(function):
    """
    Decorator to measure the execution time of a function.

    Parameters
    ----------
    function : function
        The function to measure the execution time of.

    Returns
    -------
    function
        Wrapped function.
    """
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = function(*args, **kwargs)
        end_time = datetime.now() - start_time
        print(f"Execution time: {end_time}")
        return result
    return wrapper
