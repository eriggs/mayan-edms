from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

CACHE_PATH = 'document_cache/'
CHECK_DELETE_PERIOD_INTERVAL = 60
CHECK_TRASH_PERIOD_INTERVAL = 60
DELETE_STALE_STUBS_INTERVAL = 60 * 10  # 10 minutes
DEFAULT_DELETE_PERIOD = 30
DEFAULT_DELETE_TIME_UNIT = 'days'
DEFAULT_ZIP_FILENAME = 'document_bundle.zip'
DOCUMENT_IMAGE_TASK_TIMEOUT = 20
STUB_EXPIRATION_INTERVAL = 60 * 60 * 24  # 24 hours
UPDATE_PAGE_COUNT_RETRY_DELAY = 10
UPLOAD_NEW_VERSION_RETRY_DELAY = 10
NEW_DOCUMENT_RETRY_DELAY = 10

PAGE_RANGE_ALL = 'all'
PAGE_RANGE_RANGE = 'range'
PAGE_RANGE_CHOICES = (
    (PAGE_RANGE_ALL, _('All pages')), (PAGE_RANGE_RANGE, _('Page range'))
)

