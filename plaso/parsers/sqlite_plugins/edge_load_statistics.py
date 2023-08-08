# -*- coding: utf-8 -*-
"""Parser for edge load statistics database.

SQLite database path: test_data/load_statistics.db
SQLite database Name: load_statistics.db
"""

from __future__ import unicode_literals

from dfdatetime import posix_time as dfdatetime_posix_time

from plaso.containers import time_events
from plaso.lib import eventdata
from plaso.parsers import sqlite
from plaso.parsers.sqlite_plugins import interface


class EdgeLoadStatisticsResourceEventData(events.EventData):
  """edge load statistics resource event data.

  Attributes:
    top_level_hostname: <ADD DESCRIPTION HERE>
    resource_hostname: <ADD DESCRIPTION HERE>
    resource_url_hash: <ADD DESCRIPTION HERE>
    resource_type: <ADD DESCRIPTION HERE>
    last_update: <ADD DESCRIPTION HERE>

  """

  DATA_TYPE = 'edge:load:statistics:resource'

  def __init__(self):
    """Initializes event data."""
    super(EdgeLoadStatisticsResourceEventData,
          self).__init__(data_type=self.DATA_TYPE)
    self.last_update = None
    self.resource_hostname = None
    self.resource_type = None
    self.resource_url_hash = None
    self.top_level_hostname = None


class EdgeLoadStatisticsPlugin(interface.SQLitePlugin):
  """Parser for EdgeLoadStatistics"""

  NAME = 'edge_load_statistics'
  DESCRIPTION = 'Parser for EdgeLoadStatistics'

  QUERIES = [((
      'SELECT'
      'top_level_hostname,resource_hostname,resource_url_hash,resource_type,last_update'
      'from load_statistics'), 'ParseResourceRow')]

  REQUIRED_TABLES = frozenset(['load_statistics'])

  SCHEMAS = [{
      'load_statistics': (
          'CREATE TABLE load_statistics(top_level_hostname TEXT,'
          'resource_hostname TEXT, resource_url_hash TEXT, resource_type'
          'INTEGER, last_update INTEGER NOT NULL,'
          'UNIQUE(top_level_hostname,resource_url_hash))'),
      'meta': (
          'CREATE TABLE meta(key LONGVARCHAR NOT NULL UNIQUE PRIMARY KEY,'
          'value LONGVARCHAR)'),
      'redirect_statistics': (
          'CREATE TABLE redirect_statistics(source_hostname TEXT,'
          'destination_hostname TEXT, is_top_level_document INTEGER NOT'
          'NULL, last_update INTEGER NOT NULL, UNIQUE(source_hostname,desti'
          'nation_hostname,is_top_level_document))')
  }]

  def ParseResourceRow(self, parser_mediator, query, row, **unused_kwargs):
    """Parses a row from the database.

    Args:
      parser_mediator (ParserMediator): mediates interactions between parsers
          and other components, such as storage and dfvfs.
      query (str): query that created the row.
      row (sqlite3.Row): row resulting from query.
    """
    # Note that pysqlite does not accept a Unicode string in row['string'] and
    # will raise "IndexError: Index must be int or string".

    event_data = EdgeLoadStatisticsResourceEventData()
    event_data.last_update = row['last_update']
    event_data.resource_hostname = row['resource_hostname']
    event_data.resource_type = row['resource_type']
    event_data.resource_url_hash = row['resource_url_hash']
    event_data.top_level_hostname = row['top_level_hostname']


sqlite.SQLiteParser.RegisterPlugin(EdgeLoadStatisticsPlugin)
