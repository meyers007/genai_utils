#!/usr/bin/env python 

def _extractImagesFromPDF(file=None, **kwargs):
    assert file.endswith("pdf"), "Called with non PDF File!!"

    ret = {}
    with pdfplumber.open(file) as doc:
        for pageNumber, page in enumerate(doc.pages):
            images = page.images
            for image_index, img in enumerate(images):
                bbox = (img['x0'], img['top'], img['x1'], img['bottom'])
                image = page.within_bbox(bbox).to_image()
                pil_image = image.original
                imageRGB = pil_image.convert("RGB")
                b = BytesIO()
                imageRGB.save(b, format='PNG')
                b.seek(0)
                br= b.read()
                b64Image = base64.b64encode(br).decode("utf-8")
                url = "data:image/jpg;base64, " + b64Image
                #img = f"<img src='{url}' >"
                #display (HTML(img))
                ret[url] = 1
    ret = [r for r in ret.keys()]
    return ret
