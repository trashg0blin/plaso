# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for Edge Load Statistics event formatter."""

import unittest

from plaso.formatters import edge_load_statistics
from tests.formatters import test_lib


class EdgeLoadStatisticsResourceFormatterTest(test_lib.EventFormatterTestCase):
  """Tests the Edge Load Statistics resource event formatter."""

  def testInitialization(self):
    """Tests the initialization."""
    event_formatter = edge_load_statistics.EdgeLoadStatisticsResourceFormatter()
    self.assertIsNotNone(event_formatter)

  def testGetFormatStringAttributeNames(self):
    """Tests the GetFormatStringAttributeNames function."""
    event_formatter = edge_load_statistics.EdgeLoadStatisticsResourceFormatter()

    expected_attribute_names = [
        'last_update', 'resource_hostname', 'resource_type',
        'resource_url_hash', 'top_level_hostname'
    ]

    self._TestGetFormatStringAttributeNames(
        event_formatter, expected_attribute_names)


if __name__ == '__main__':
  unittest.main()
