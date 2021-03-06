# -*- coding: utf-8 -*-
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException

__author__ = 'Apple'

class BaseForm(Form):
    def __init__(self):
        # data = request.json
        data = request.get_json(slient=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # form errors
            raise ParameterException(msg=self.errors)
        return self