from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint('task_list', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        return "the method is post"
    return "the method is get"

@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    return "the method is delete {}".format(id)