import os
from pathlib import Path

from flask import Request


def save_file_from_request(request_reference: Request) -> str:
    """
    Save a file from a HTTP request.

    Parameters:
    request_reference (Request): The HTTP request object.

    Returns:
    str: The filename of the saved file.

    Raises:
    None

    Example usage:
    request = get_http_request()
    filename = save_file_from_request(request)
    """
    file = request_reference.files.get('file')
    filename = file.filename
    file.save(filename)
    return filename

def delete_file_after_use(filename: str, cwd: str = Path.cwd().absolute()) -> None:
    """Deletes a file after it has been used.

    Parameters:
        filename (str): The name of the file to be deleted.
        cwd (str, optional): The current working directory. Defaults to the absolute path of the current directory.

    Returns:
        str: A message indicating that the file has been successfully deleted.

    Example usage:
        delete_file_after_use("example.txt")
    """
    os.remove(f"{cwd}/{filename}")
