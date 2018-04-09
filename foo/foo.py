#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import base64


def encode(id_num, format="empty=true&id={0}"):
    d = format.format(str(id_num))
    e = base64.b64encode(d.encode('utf-8'))
    r = e[::-1]
    return base64.b64encode(r).decode('utf-8')
