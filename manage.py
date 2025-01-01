#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server_side_development.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # Django is not installed, try to install it
        raise
    execute_from_command_line(sys.argv)
