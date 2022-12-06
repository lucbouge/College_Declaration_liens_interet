import os
import pickle
from typing import NamedTuple, Literal

import pandas as pd


# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
# - “openpyxl” supports newer Excel file formats.

DEFAULT_XLSX_ENGINE = "openpyxl"

PKL_DIRNAME = "PKL"
XLSX_DIRNAME = "XLSX"


class triple(NamedTuple):
    path: str
    dirname: str
    filename: str


##################################################################


def make_full_dataname(*, tag=None):
    assert tag is not None
    return tag + "_original"


def load_df_from_pkl(*, tag=None):
    dataname = make_full_dataname(tag=tag)
    df = load_file_to_data(dataname=dataname, dirname=tag)
    return df


def dump_df_to_pkl(*, df, tag=None):
    dataname = make_full_dataname(tag=tag)
    dump_data_to_file(df, dataname=dataname, dirname=tag)


##################################################################


def load_file_to_data(*, dataname, dirname=None):
    tmp = PKL_dataname_to_path(dataname=dataname, dirname=dirname)
    dirname = tmp.dirname
    path = tmp.path
    assert os.path.exists(path), path
    with open(path, "rb") as cin:
        print(f"Loading {dataname} from: {path}", end="... ", flush=True)
        data = pickle.load(cin)
    print("Done!")
    return data


def dump_data_to_file(data, *, dataname, dirname=None):
    tmp = PKL_dataname_to_path(dataname=dataname, dirname=dirname)
    dirname = tmp.dirname
    path = tmp.path
    os.makedirs(dirname, exist_ok=True)
    assert os.path.exists(dirname)
    with open(path, "wb") as cout:
        print(f"Dumping {dataname} to: {path}", end="... ", flush=True)
        pickle.dump(data, cout)
    print("Done!")
    assert os.path.exists(path), path


def PKL_dataname_to_path(*, dataname, dirname=None):
    return dataname_to_path(
        dataname=dataname, dirname=dirname, default_dirpath=PKL_DIRNAME, suffix=".pkl"
    )


##################################################################


def load_xlsx_to_df(
    *,
    dataname,
    dirname,
    sheetname,
    engine=DEFAULT_XLSX_ENGINE,
    no_default_dirpath=False,
):
    tmp = XLSX_dataname_to_path(
        dataname=dataname, dirname=dirname, no_default_dirpath=no_default_dirpath
    )
    dirname = tmp.dirname
    path = tmp.path
    os.makedirs(dirname, exist_ok=True)
    assert os.path.exists(path), path
    df = read_xlsx(xlsx=path, sheetname=sheetname, engine=engine)
    # print(df)
    return df


def dump_df_to_xlsx(
    df,
    *,
    dataname,
    dirname,
    sheetname,
    columns,
    engine=DEFAULT_XLSX_ENGINE,
):
    tmp = XLSX_dataname_to_path(dataname=dataname, dirname=dirname)
    dirname = tmp.dirname
    path = tmp.path
    ##
    os.makedirs(dirname, exist_ok=True)
    assert os.path.exists(dirname), dirname
    print(f"Dumping dataframe to {path}")
    if columns is not None:
        df = df[list(columns)]
    if sheetname is None:
        df.to_excel(path, index=False, engine=engine)
    else:
        df.to_excel(path, index=False, sheet_name=sheetname, engine=engine)


def XLSX_dataname_to_path(*, dataname, dirname, no_default_dirpath=False):
    default_dirpath = XLSX_DIRNAME
    if no_default_dirpath:
        default_dirpath = ""
    return dataname_to_path(
        dataname=dataname,
        dirname=dirname,
        default_dirpath=default_dirpath,
        suffix=".xlsx",
    )


# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html


def read_xlsx(*, xlsx, sheetname, engine=DEFAULT_XLSX_ENGINE):
    assert xlsx is not None
    assert sheetname is not None
    ##
    print("Reading from:", sheetname, end="... ")
    assert engine in ("xlrd", "openpyxl", "odf", "pyxlsb")
    df = pd.read_excel(xlsx, sheetname, engine=engine)
    print("Done!")
    return df


##################################################################


def remove_file(*, dataname, dirname=None):
    (path, _, _) = PKL_dataname_to_path(dataname=dataname, dirname=dirname)
    assert test_file_exists(dataname=dataname, dirname=dirname), dataname
    print(f"Deleting {path}")
    os.remove(path)


def test_file_exists(*, dataname, dirname=None):
    (path, _, _) = PKL_dataname_to_path(dataname=dataname, dirname=dirname)
    return os.path.exists(path)


##################################################################


def dataname_to_path(dataname, dirname, default_dirpath, suffix=None):
    assert dataname is not None
    assert default_dirpath is not None
    ##
    dirpath = default_dirpath
    if dirname is not None:
        dirpath = os.path.join(dirpath, dirname)
    filename = dataname
    if not filename.lower().endswith(suffix):
        filename = filename + suffix
    path = os.path.join(dirpath, filename)
    return triple(path=path, dirname=dirpath, filename=filename)
