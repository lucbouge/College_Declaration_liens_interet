import os
import re
import glob
import pandas as pd
import pprint as pp
from unidecode import unidecode
import datetime
from typing import (
    NamedTuple,
    Optional,
    List,
    Dict,
    cast,
    Type,
    no_type_check,
    Optional,
    Sequence,
    Any,
    Iterable,
    Tuple,
    Union,
    Callable,
    TypeAlias,
    Literal,
    Set,
    NoReturn,
)
import time
import pathlib
from bs4 import BeautifulSoup
from docx import Document


from functools import wraps
from enum import Enum, auto, unique
from attrs import define, frozen, field, fields, validators, asdict
import more_itertools

from Libraries.Utilities.file import (
    load_file_to_data,
    dump_data_to_file,
    test_file_exists,
)
from Libraries.Utilities.utilities import *


