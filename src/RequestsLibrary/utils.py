import json

from requests.status_codes import codes
from requests.structures import CaseInsensitiveDict


class UnknownStatusError(Exception):
    pass


class InvalidResponse(Exception):
    pass


def parse_named_status(status_code):
    """
    Converts named status from human readable to integer
    """
    code = status_code.lower().replace(' ', '_')
    code = codes.get(code)
    if not code:
        raise UnknownStatusError(status_code)
    return code


def merge_headers(session, headers):
    if headers is None:
        headers = {}
    if session.headers is None:
        merged_headers = {}
    else:
        # Session headers are the default but local headers
        # have priority and can override values
        merged_headers = session.headers.copy()

    # Make sure merged_headers are CaseIsensitiveDict
    if not isinstance(merged_headers, CaseInsensitiveDict):
        merged_headers = CaseInsensitiveDict(merged_headers)

    merged_headers.update(headers)
    return merged_headers


def json_pretty_print(content):
    """
    Pretty print a JSON object

    ``content``  JSON object to pretty print
    """
    temp = json.loads(content)
    return json.dumps(
        temp,
        sort_keys=True,
        indent=4,
        separators=(
            ',',
            ': '))
