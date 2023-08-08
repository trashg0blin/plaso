# -*- coding: utf-8 -*-
"""edge load statistics formatter."""

from plaso.formatters import interface
from plaso.formatters import manager
from plaso.lib import errors


class EdgeLoadStatisticsResourceFormatter(interface.ConditionalEventFormatter):
  """edge load statistics resource event formatter."""

  DATA_TYPE = 'edge:load:statistics:resource'
  """Correct Format String Pieces where needed"""

  FORMAT_STRING_PIECES = [
    'top_level_hostname:{top_level_hostname}',
    'resource_hostname:{resource_hostname}',
    'resource_url_hash:{resource_url_hash}',
    'resource_type:{resource_type}',
    'last_update:{last_update}']


  # TODO: Change the default string formatter.
  SOURCE_LONG = 'Edge Load Statistics Resource'
  SOURCE_SHORT = 'Edge Load Statistics'


manager.FormattersManager.RegisterFormatter(
    [EdgeLoadStatisticsResourceFormatter])
