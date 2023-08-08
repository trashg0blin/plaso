# -*- coding: utf-8 -*-
"""Tests for edge load statistics plugin."""
import unittest

from plaso.lib import eventdata
from plaso.lib import timelib
from plaso.parsers.sqlite_plugins import edge_load_statistics

from tests import test_lib as shared_test_lib
from tests.parsers.sqlite_plugins import test_lib


class EdgeLoadStatisticsTest(test_lib.SQLitePluginTestCase):
  """Tests for edge load statistics database plugin."""

  @shared_test_lib.skipUnlessHasTestFile(['load_statistics.db'])
  def testProcess(self):
    """Test the Process function on a Edge Load Statistics file."""
    plugin_object = edge_load_statistics.EdgeLoadStatisticsPlugin()
    storage_writer = self._ParseDatabaseFileWithPlugin(['load_statistics.db'],
                                                       plugin_object)

    # TODO: Replace zero with an actual number.
    self.assertEqual(storage_writer.number_of_events, 0)
    self.assertEqual(storage_writer.number_of_errors, 0)


if __name__ == '__main__':
  unittest.main()
