# access_control.py

def compute_access_level(control):
    """
    Computes access level based on the formula:
    (CONTROL_NUM * 3) + length of FAVORITE_ARTIST
    """
    # Note: Define FAVORITE_ARTIST locally or pass it as an argument
    FAVORITE_ARTIST = "LINKIN PARK" 
    return (control * 3) + len(FAVORITE_ARTIST)