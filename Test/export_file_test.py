# -*- coding: utf-8 -*-
"""
Export streams are closed even when writing a report fails.

Retain the stream outside the export call so garbage collection cannot hide
a missing explicit close. No real files or operating-system errors are used.

>>> import io
>>> from unittest.mock import patch
>>> from pycm import ConfusionMatrix
>>> cm = ConfusionMatrix(matrix={0: {0: 2, 1: 1}, 1: {0: 1, 1: 2}})
>>> class FailingStream(io.StringIO):
...     write_called = False
...     def write(self, text):
...         self.write_called = True
...         raise OSError("simulated write failure")
>>> for method in (cm.save_stat, cm.save_html, cm.save_csv, cm.save_obj):
...     stream = FailingStream()
...     with patch("builtins.open", return_value=stream):
...         result = method("report", address=False)
...     assert result == {"Status": False, "Message": "simulated write failure"}
...     assert stream.write_called
...     assert stream.closed

A failure in the second CSV file must also leave both streams closed.

>>> statistics_stream = io.StringIO()
>>> matrix_stream = FailingStream()
>>> with patch("builtins.open", side_effect=[statistics_stream, matrix_stream]):
...     result = cm.save_csv("report", address=False)
>>> result == {"Status": False, "Message": "simulated write failure"}
True
>>> statistics_stream.closed and matrix_stream.closed
True
>>> matrix_stream.write_called
True

Successful CSV exports close both files before returning, without relying on
object finalization. Disabling matrix output opens only the statistics file.

>>> for matrix_save in (False, True):
...     streams = [io.StringIO() for _ in range(1 + matrix_save)]
...     with patch("builtins.open", side_effect=streams) as opener:
...         result = cm.save_csv("report", address=False, matrix_save=matrix_save)
...     assert result == {"Status": True, "Message": None}
...     assert opener.call_count == len(streams)
...     assert all(stream.closed for stream in streams)
"""
