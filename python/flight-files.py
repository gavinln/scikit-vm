#!/usr/bin/python
# vim: set sts=4 sw=4 ts=4:

'''
Serial:
gzip elapsed = 38.7517540455
feather elapsed = 10.9021530151
total elapsed = 228.851939917

Parallel:
gzip elapsed = 143.551666975
feather elapsed = 8.11894202232
total elapsed = 215.440063953

conda create -n flight-files python=3
activate flight-files
conda install feather-format -c conda-forge
conda env export -f flight-files.yml
deactivate flight-files

conda env create -f flight-files.yml
conda install cython
conda install feather-format --channel conda-forge
conda install dask
conda install distributed
conda env export --file flight-files2.yml
'''

import subprocess
import glob
import feather
import logging
import dask.dataframe as dd
from collections import Counter

import os
import sys
import subprocess
import pandas as pd
import time
import dask.dataframe as dd

from distributed import Client
from distributed import LocalCluster
from functools import reduce
from dask.delayed import delayed


logging.basicConfig(level=logging.WARNING)


def get_file_names():
    start = 1988
    end = 1997
    files = []
    filename = '{}.csv.bz2'
    for year in range(start, end + 1):
        files.append(filename.format(year))
    return files


def download_file(filename):
    files = glob.glob(filename)
    if filename not in files:
        url = 'http://stat-computing.org/dataexpo/2009/' + filename
        cmd = 'curl -O {}'.format(url)
        print(cmd)
        subprocess.check_call(cmd.split(' '))
    return filename


def convert_gzip(filename):
    print('about to convert {}'.format(filename))
    new_filename = filename.replace('bz2', 'gz')
    files = glob.glob(new_filename)
    print('searching {} in {}'.format(new_filename, files))
    if new_filename not in files:
        cmd = 'bunzip2 -c {0} | gzip > {1}'.format(
            filename, new_filename)
        print(cmd)
        subprocess.check_call(cmd, shell=True)
    return new_filename


def convert_feather(filename):
    new_filename = filename.replace('.bz2', '.feather')
    files = glob.glob(new_filename)
    if new_filename not in files:
        df = pd.read_csv(
            filename, compression='bz2', header=0, sep=',')
        feather.write_dataframe(df, new_filename)
        print(new_filename)
    return new_filename


def combine_gzip_files():
    ' not used '
    files = os.listdir('.')
    data_files = []
    for filename in files:
        if filename.startswith('19') and filename.endswith('.csv.gz'):
            data_files.append(filename)

    data_files.sort()

    df_files = []
    for filename in data_files:
        df = pd.read_csv(
            filename, compression='gzip', header=0, sep=',')
        print(df.shape)
        df_files.append(df)

    df = pd.concat(df_files)
    del df_files

    print(df.shape)
    df2 = df.to_csv('all-1900.csv.gz', compression='gzip', sep=',')


def gzip_count(column):
    def pandas_time():
        df = pd.read_csv(
            'all-1900.csv.gz', compression='gzip', header=0, sep=',')
        print(df.shape)

    def gzip_time():
        df = dd.read_csv(
            '1*.csv.gz', compression='gzip', header=0, sep=',',
            dtype='object')
        # res = df.reduction(lambda r: r.Year.count(),
        #                    aggregate=lambda x: x.sum())
        res = df.groupby(column)[column].count()
        print(res.compute())


    print('gzip started')
    start = time.time()
    gzip_time()
    elapsed = time.time() - start
    print('gzip elapsed = {}'.format(elapsed))



def feather_count(files, column):
    def read_from_feather(filename):
        print('reading {}'.format(filename))
        return delayed(feather.read_dataframe)(filename, columns=[column])

    print('feather started')
    start = time.time()
    dfs = list(map(read_from_feather, files))
    df = dd.from_delayed(dfs)
    print(df.columns)
    result = df.groupby(column)[column].count()
    print(result.compute())
    elapsed = time.time() - start
    print('feather elapsed = {}'.format(elapsed))

    # Check this http://dask.pydata.org/en/latest/delayed-collections.html

def process_file(filename):
    return convert_feather(download_file(filename))


def main():
    names = ['Year', 'Month', 'DayofMonth', 'DayOfWeek', 'DepTime',
        'CRSDepTime', 'ArrTime', 'CRSArrTime', 'UniqueCarrier',
        'FlightNum', 'TailNum', 'ActualElapsedTime', 'CRSElapsedTime',
        'AirTime', 'ArrDelay', 'DepDelay', 'Origin', 'Dest', 'Distance',
        'TaxiIn', 'TaxiOut', 'Cancelled', 'CancellationCode', 'Diverted',
        'CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay',
        'LateAircraftDelay']

    if len(sys.argv) == 1:
        sys.exit('please enter column name')

    column_name = sys.argv[1]
    if column_name not in names:
        col_name_str = ', '.join(names)
        sys.exit('Invalid column name {}. Should be one of:\n{}'.format(
            column_name, col_name_str))

    start = time.time()
    files = get_file_names()
    files2 = list(map(download_file, files))
    # files3 = list(map(convert_gzip, files2))
    files4 = list(map(convert_feather, files2))

    # client = Client()
    # items1 = client.map(download_file, files)
    # items2 = client.map(convert_feather, items1)
    # files4 = client.gather(items2)
    # del client

    # gzip_count('DayOfWeek')
    feather_count(files4, column_name)
    elapsed = time.time() - start
    print('total elapsed = {}'.format(elapsed))


if __name__ == "__main__":
    main()
