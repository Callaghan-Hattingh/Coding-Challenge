import time
from flask import render_template, request, Blueprint, current_app
import CF.app.test_db.test_gets as gets

v1 = Blueprint("v1", __name__, template_folder="templates")


@v1.route("/", methods=["GET"])
def index():
    """Runs when GET requested on '/'.

    Returns:
        render_template (flask): index.html
    """
    current_app.logger.info("@ index()")

    return render_template("at-index.html")


# this is not in use
@v1.route("/log", methods=["GET"])
def at_log():
    """Runs when GET requested on '/log'.

    When user selects view log from the home page.

    Return:
        render_template (flask): html template based on logic from this app
    """
    current_app.logger.info("@ at_log()")

    response = gets.get_table()
    if isinstance(response, Exception):
        return render_template(
            "at-error.html", message=".error('Error occured')", error=response
        )
    database_log_html = response["data_table"].to_html(index=False)

    return render_template("at-log.html", data=database_log_html)


@v1.route("/test/<int:item_count>", methods=["GET"])
def at_test(item_count=None):
    """Runs when GET requested on '/login/<user_id>'.

    The main endpoint to test the time it takes to process the items in the database.

    Args:
        item_count=None (str): sets the number of items to count after the '/test/' path

    Return:
        render_template (flask): html template based on logic from this app"""
    current_app.logger.info("@ at_test(item_count=None): %s", item_count)

    #  ˅This is the script that measures the performance, not allowed to edit this section.˅
    hit_time = time.time()
    #  ˄This is the script that measures the performance, not allowed to edit this section.˄

    # <- get email query string
    person_query = request.args.get("person", type=str)

    type_query = request.args.get("type", type=str)

    # <- get user info
    response = gets.get_table("records")
    if isinstance(response, Exception):
        return render_template(
            "at-error.html", message="There was an error.", error=response
        )

    records_json = response["records_table"].to_json(orient="records")

    response2 = gets.get_table("data")

    if item_count > 100:

        return render_template(
            "at-error.html",
            message="More then 100 items selected, too many. Item Count: ",
            error=item_count,
        )

    if type_query == "text":

        data_text = response2["data_table"].to_json(orient="records")

        return render_template(
            "at-text.html",
            records=records_json,
            data=data_text,
            item_count=item_count,
            hit=hit_time,
        )

    data_json = response2["data_table"].to_json(orient="records")

    return render_template(
        "at-json.html",
        records=records_json,
        data=data_json,
        item_count=item_count,
        hit=hit_time,
    )
