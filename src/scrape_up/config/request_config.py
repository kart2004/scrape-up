from typing import Dict
import requests


class RequestConfig:
    """
    A class used to configure requests.

    Args
    ----
    timeout: int
        The timeout in seconds.
    redirect: bool
        Whether to follow redirects.
    """

    def __init__(
        self,
        timeout: int = 20,
        redirect: bool = False,
        headers: Dict[str, str] = {},
    ):
        self._timeout = timeout
        self._redirect = redirect
        self._headers = headers

    def set_timeout(self, timeout: int):
        self._timeout = timeout

    def set_redirect(self, redirect: bool):
        self._redirect = redirect

    def set_headers(self, headers: Dict[str, str]):
        self._headers = headers

    @property
    def timeout(self):
        return self._timeout

    @property
    def redirect(self):
        return self._redirect

    @property
    def headers(self):
        return self._headers


def get(url: str, config: RequestConfig):
    r = requests.get(
        url=url,
        headers=config.headers,
        timeout=config.timeout,
        allow_redirects=config.redirect,
    )
    return r
