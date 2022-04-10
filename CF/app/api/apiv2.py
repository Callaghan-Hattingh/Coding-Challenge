import time
from flask import render_template, request, Blueprint, current_app
from sqlalchemy import select
from .depends import session
from ..models import *
import json

v2 = Blueprint("v2", __name__, template_folder="templates")


@v2.route("/", methods=["GET"])
def index():
    """
    Runs when GET requested on '/'.
    Returns: render_template (flask): index.html
    """
    current_app.logger.info("@ index()")
    return render_template("at-index.html")


@v2.route("/test/<int:item_count>", methods=["GET"])
def at_test(item_count=None):
    """
    Runs when GET requested on '/login/<user_id>'.
    The main endpoint to test the time it takes to process the items in the database.
    Args:
        item_count=None (str): sets the number of items to count after the '/test/' path
    Return:
        render_template (flask): html template based on logic from this app"""
    current_app.logger.info("@ at_test(item_count=None): %s", item_count)
    if item_count > 100:
        return render_template(
            "at-error.html",
            message="More then 100 items selected, too many. Item Count: ",
            error=item_count,
        )
    #  ˅This is the script that measures the performance, not allowed to edit this section.˅
    hit_time = time.time()
    #  ˄This is the script that measures the performance, not allowed to edit this section.˄
    person_query = request.args.get("person", type=str)
    type_query = request.args.get("type", type=str)

    query = (
        session.query(Data, Records)
        .join(Records)
        .filter(Records.person == person_query)
        .limit(item_count)
        .all()
    )

    if type_query == "text":
        info = [i.Data.text for i in query]
    else:
        info = [i.Data.json for i in query]
        type_query = "json"

    json_records = {
        "person": query[0].Records.person,
        "type": type_query.upper(),
        "json_text": info,
        "id": [i.Data.id for i in query],
    }

    # json_records = json.loads(json.dumps(json_records))

    response = render_template(
        "at-json.html", data=json_records, item_count=item_count, hit=hit_time
    )
    return response
