from ..http import dump_header
from ..http import parse_set_header
from ..utils import environ_property
from ..utils import header_property


class RequestCORSMixin(object):
    """A mixin for :class:`BaseRequest` subclasses. Request objects that
    mix this class in will automatically get descriptors for Cross
    Origin Resource Sharing headers.

    .. versionadded:: 1.0
    """

    access_control_origin = environ_property(
        "HTTP_ORIGIN",
        doc="""The origin header field indicates the host that the request
        originated from.""",
    )

    access_control_request_headers = environ_property(
        "HTTP_ACCESS_CONTROL_REQUEST_HEADERS",
        load_func=parse_set_header,
        doc="""The Access-Control-Request-Headers field is set on a preflight
        request to indicate what headers will be sent on the cross
        origin request. This allows the server to reply indicating
        which headers are allowed.""",
    )

    access_control_request_method = environ_property(
        "HTTP_ACCESS_CONTROL_REQUEST_METHOD",
        doc="""The Access-Control-Request-Method field is set on a preflight
        request to indicate which method will be used on the cross
        origin request. This allows the server to reply indicating
        which method is allowed.""",
    )


class ResponseCORSMixin(object):
    """A mixin for :class:`BaseResponse` subclasses. Response objects that
    mix this class in will automatically get descriptors for Cross
    Origin Resource Sharing headers.

    .. versionadded:: 1.0
    """

    allow_credentials = header_property(
        "Access-Control-Allow-Credentials",
        load_func=bool,
        dump_func=str,
        doc="""Indicate whether credentials can be shared by the browser to the
        javascript code. As part of the preflight request it indicates
        whether credentials can be used on the cross origin
        request.""",
    )

    allow_headers = header_property(
        "Access-Control-Allow-Headers",
        load_func=parse_set_header,
        dump_func=dump_header,
        doc="""Indicate which headers can be used on the cross origin request.""",
    )

    allow_methods = header_property(
        "Access-Control-Allow-Methods",
        load_func=parse_set_header,
        dump_func=dump_header,
        doc="""Indicate which methods can be used on the cross origin request.""",
    )

    allow_origin = header_property(
        "Access-Control-Allow-Origin",
        load_func=parse_set_header,
        dump_func=dump_header,
        doc="""Indicate the origins that may make cross origin requests.""",
    )

    expose_headers = header_property(
        "Access-Control-Expose-Headers",
        load_func=parse_set_header,
        dump_func=dump_header,
        doc="""Indicate which headers can be shared by the browser to the
        javascript code.""",
    )

    max_age = header_property(
        "Access-Control-Max-Age",
        load_func=int,
        dump_func=str,
        doc="""Indicate the maximum age in seconds the access control settings can
        be cached for.""",
    )
