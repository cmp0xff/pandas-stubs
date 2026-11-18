#!/usr/bin/env python3
"""Script entry point; run `python -S scripts/check_ndarray_params.py`."""

import sys

from ndarray_params.check import main

if __name__ == "__main__":
    sys.exit(main())
