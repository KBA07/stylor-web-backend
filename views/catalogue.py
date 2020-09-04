import csv
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint('catalogue', __name__)


@bp.route('/getCategories', methods=['GET'])
def index():
    # Returns all the categories present in excel sheet
    if request.method == 'POST':
        return "the method is post"
    return "the method is get"


@bp.route('/getProducts/<category>', methods=['GET'])
def delete(category):
    # gets product based on category
    return "the method is delete {}".format(id)


@bp.route('/getProductDetails/<productId>', methods=['GET'])
def getProductDetails(productId):
    pass


@bp.route('/getProductInventory/<productId>', methods=['GET'])
def getProductInventory(productId):
    pass