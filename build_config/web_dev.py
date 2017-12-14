#!/usr/bin/env python3

def make_post(path, annotations, fields, **keywords):
    ### TODO: screenshot
    img_path = path.replace(".html", ".png")
    if keywords.get("no_hierarchy", False):
        img_path = img_path.replace("/", "-")
    img="<img src=\"" + str(img_path) + "\">"

    return img


config = {
    "mlc" : "<!--x -->",
    "generator": {
        "post": make_post
    }
}



