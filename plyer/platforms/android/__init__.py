from os import environ
from jnius import autoclass
from kivy import Logger

ANDROID_VERSION = autoclass('android.os.Build$VERSION')
SDK_INT = ANDROID_VERSION.SDK_INT

try:
    from android import config
    ns = config.JAVA_NAMESPACE
except (ImportError, AttributeError) as e:
    Logger.warning("using renpy")
    ns = 'org.renpy.android'

if 'PYTHON_SERVICE_ARGUMENT' in environ:
    PythonService = autoclass(ns + '.PythonService')
    activity = PythonService.mService
else:
    PythonActivity = autoclass(ns + '.PythonActivity')
    activity = PythonActivity.mActivity
