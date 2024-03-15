"""Methods to calculate kinematics."""

from typing import Optional, Union

from physics_sims.calculations.exceptions import (
    TimeInputError
)


def calc_average_velocity(disp, ts_) -> Union[float, int]:
    """Calculate the average velocity.
    
    Parameters
    ----------
    dis : float or int
        displacement of object in meters, this value can be postive or negative.
    ts_ : float or int
        time in seconds

    Returns
    -------
    float or int
        the average velocity of the object
    """
    if ts_ < 0 or not isinstance(ts_, int, float):
        raise TimeInputError
    
    return dist / ts_

def calc_velocity_final(
        vo_: Union[float, int],
        acc: Union[float, int],
        ts: Union[float, int]
    ) -> Union[float, int]:
    """Calculate the velocity final, assuming constant acceleration.
    
    Parameters
    ----------
    vo_ : float or int
        initial velocity in m/s
    acc : float or int
        acceleration in m/s^2
    ts_ : float or int
        time in seconds
    
    Raises
    ------
    TimeInputError
        if the time inputed is a non valid input

    Returns
    -------
    float
        the final velocity of the object
    """
    if ts_ < 0 or not isinstance(ts_, int, float):
        raise TimeInputError

    return vo_ + (acc * ts_)

calc_average_velocity(1,1)