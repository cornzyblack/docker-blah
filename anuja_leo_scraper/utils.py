from pathlib import Path
from typing import Union
from datetime import datetime


def save_html(html_str: str, filepath: Union[Path | str]):
    """
    Save the raw html to a html location

    Parameters
    ----------
    html_str : str
        The html string
    filepath : Path
        The filepath to save the html file
    """
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_str)


def get_current_date(date_format: str = "%Y-%m-%d"):
    """
    Get the current date

    Parameters
    ----------
    date_format : str
        The date format, by default "%Y-%m-%d"

    Returns
    -------
    str
        The current date in with the given time format
    """
    return datetime.now().strftime(date_format)


# def get_
