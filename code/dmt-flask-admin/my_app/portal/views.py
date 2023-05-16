from flask import Blueprint, request, jsonify

from my_app.service import AttMasterService
from my_app.service import CompStyle
from my_app.service import Feat
from my_app.service import MapTag
from my_app.service import MapXpath
from my_app.service import PcMasterService
from my_app.service import TagMasterService

portal = Blueprint('portal', __name__)


@portal.route("/tag-master", methods=["POST"])
def tag_master():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ct = request.json['ct']
            all_dir = request.json['all-dir'] == "yes"
            prod = request.json['prod'].split(",")
            res = TagMasterService.process_master_tag(loc, ct, all_dir, prod)
            return jsonify({'success': res})
    except Exception as e:
        return {'error': str(e)}


@portal.route("/att-master", methods=["POST"])
def master_att():
    try:
        if request.method == "POST":
            ct = request.json['ct']
            loc = request.json['loc']
            all_dir = request.json['all-dir'] == "yes"
            prod = request.json['prod'].split(",")
            res = AttMasterService.process_master_att(loc, ct, all_dir, prod)
            return jsonify({'success': res})
    except Exception as e:
        return {'error': str(e)}


@portal.route("/pc-master", methods=["POST"])
def master_pc():
    try:
        if request.method == "POST":
            ct = request.json['ct']
            loc = request.json['loc']
            prod = request.json['prod']
            all_dir = request.json['all-dir']
            res = PcMasterService.process_master_pc(loc, ct, all_dir, prod)
            return jsonify({'success': res})
    except Exception as e:
        return {'error': str(e)}


@portal.route("/map-xpath", methods=["POST"])
def map_xpath():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ct = request.json['ct']
            file_name = request.json['file_name']
            sn = request.json['sn']
            res = MapXpath.map_xpath_to_tag(loc, ct, file_name, sn)
            return {'success': res}
    except Exception as e:
        return {'error': str(e)}


@portal.route("/map-tag", methods=["POST"])
def map_tag():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ct = request.json['ct']
            res = MapTag.map_tag(loc, ct)
            return {'success': res}
    except Exception as e:
        return {'error': str(e)}


@portal.route("/feat", methods=["POST"])
def fill_feat():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ct = request.json['ct']
            ls = Feat.fill_feature(loc, ct)
            return {'pat': ls}
    except Exception as e:
        return {'error': str(e)}


@portal.route("/comp-style", methods=["POST"])
def fill_comp_style():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ct = request.json['ct']
            ls = CompStyle.fill_comp_style(loc, ct)
            return {'xpath_left': ls}
    except Exception as e:
        return {'error': str(e)}
