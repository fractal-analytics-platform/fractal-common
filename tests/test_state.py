from datetime import datetime

from devtools import debug

from schemas import _StateBase


def test_state():
    s = _StateBase(data={"some": "thing"}, timestamp=datetime.now())
    debug(s)
    debug(s.sanitised_dict())
    assert isinstance(s.sanitised_dict()["timestamp"], str)
