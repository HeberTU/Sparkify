# -*- coding: utf-8 -*-
"""ETL script.

This module contains all the functions needed to perform the ETL
process for Spakify Database.
"""

import os
import glob
from typing import Callable
import psycopg2
import pandas as pd
from sql_queries import *
from psycopg2.extensions import cursor as Cursor
from psycopg2.extensions import connection as Connection


def process_song_file(cur: Cursor, filepath: str) -> None:
    """This function reads, transforms, and load song from a JSON file.

    Args:
        cur: DataBase Cursor.
        filepath: Path to the JSON file.

    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert artist record
    artist_data = df[
        ['artist_id', 'artist_name', 'artist_location',
         'artist_latitude', 'artist_longitude']]. \
        values. \
        tolist()[0]
    cur.execute(artist_table_insert, artist_data)

    # insert song record
    song_data = df[
        ['song_id', 'title', 'artist_id', 'year', 'duration']]. \
        values. \
        tolist()[0]
    cur.execute(song_table_insert, song_data)


def process_log_file(cur: Cursor, filepath: str) -> None:
    """This function reads, transforms, and loads logs from a JSON file.

    Args:
        cur: DataBase Cursor.
        filepath: Path to the JSON file.

    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df.page == 'NextSong'].copy()

    # convert timestamp column to datetime
    t = pd.to_datetime(df.ts, unit='ms')

    # insert time data records
    time_data = {
        "start_time": t,
        "hour": t.dt.hour,
        "day": t.dt.day,
        "week": t.dt.isocalendar().week,
        "month": t.dt.month,
        "year": t.dt.year,
        "weekday": t.dt.weekday}
    column_labels = None
    time_df = pd.DataFrame(data=time_data).drop_duplicates()

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[
        ['userId', 'firstName', 'lastName', 'gender', 'level']]. \
        drop_duplicates()

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (
            pd.to_datetime(row.ts),
            row.userId,
            row.level,
            songid,
            artistid,
            row.sessionId,
            row.location,
            row.userAgent
        )
        if (not songid is None) and (not artistid is None):
            cur.execute(songplay_table_insert, songplay_data)


def process_data(
        cur: Cursor, conn: Connection, filepath: str, func: Callable
) -> None:
    """This function reads, transforms, and loads all file from data directory.

    Args:
        cur: DataBase Cursor.
        conn: Data Base connection.
        filepath: Path to the JSON file.
        func: ETL function.

    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    # i, filepath = next(enumerate(all_files, 1))
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
