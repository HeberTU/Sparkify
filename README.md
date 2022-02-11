Sparkify
==============================
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Code for project: Sparkify, Udacity

- Origin: (https://github.com/HeberTU/Sparkify)
- Author: Heber Trujillo <heber.trj.urt@gmail.com>
- Date of last README.md update: 11.02.2022

Project Overview
-
This project aims to show Python capabilities for data modeling and ETL pipelines design using Postgres.

Mainly, this project will focus on:

* Define fact and dimension tables under the star schema optimized for OLAP.
* ETL pipeline design to transfer data from two local directories to a Postgres Data Base.

Dependencies Installation 
-

1. Poetry is the tool used for dependency management. To install poetry, run from a terminal:
    ```bash
    pip install poetry
    ```
    Make sure that version 1.1.8 is installed (1.1.7 is buggy).
2. Create and activate a virtual environment for the project. For example:
    ```bash
    python3 -m venv ./.venv
    ./.venv/Scripts/activate
    ```
3. From the virtual environment, install the required dependencies with
    ```bash
    poetry update
    ```
