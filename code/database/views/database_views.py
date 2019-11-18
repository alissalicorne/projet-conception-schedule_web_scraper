from typing import Optional

import bson
import bson.json_util
import json
from flask import render_template, Blueprint, redirect, session, jsonify

from database.models.users import User
from database.models.courses import Course


blueprint = Blueprint('account', __name__, template_folder='templates')


@blueprint.route('/database/<name>', methods=['GET'])
def get_name(name):
    result = User.objects().all()
    print(result)

    print(bson.json_util.dumps(result))
    return (bson.json_util.dumps(result))
