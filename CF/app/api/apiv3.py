import sqlite3
import pandas as pd
from flask import render_template, request, Blueprint, current_app
from .depends import session
from ..models import *


v3 = Blueprint("v3", __name__, template_folder="templates")


@v3.route("/", methods=["GET"])
def index():
    """
    Runs when GET requested on '/'.
    Returns: render_template (flask): index.html
    """
    current_app.logger.info("@ index()")

    df1 = pd.read_sql(session.query(Data).statement, session.bind)
    df2 = pd.read_sql(session.query(Records).statement, session.bind)

    # df1.to_pickle("df_Data.pkl")
    # df2.to_pickle("df_Records.pkl")

    print(df1.head())
    print(df2.head())

    print(df1.shape)
    print(df2.shape)

    conn = sqlite3.connect("database.db")

    df1.to_sql("data", conn, if_exists="replace", index=False)
    df2.to_sql("records", conn, if_exists="replace", index=False)

    return "ok"
