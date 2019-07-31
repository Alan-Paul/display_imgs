from django.shortcuts import render
import os
from main_settings.settings import IMG_LIST, IMG_PER_PAGE

def display_img(request):
    img_path, page_range = generateImgPath()
    try:
        page = request.GET['p']
    except:
        page = 1
    page = int(page)
    min = (page - 1) * IMG_PER_PAGE
    max = page * IMG_PER_PAGE
    index_min = 0 if min < 0 else min
    index_max = len(img_path) if max > len(img_path) else max
    display_img = img_path[index_min: index_max]
    return render(request, 'display_img.html', {'all_img':display_img, 'pagerange':range(1, page_range), 'pageend':page_range, 'nowpage':page})

def generateImgPath():
    img_path_list = IMG_LIST
    img_path = []
    with open(img_path_list, 'r') as f:
        for line in f:
            line = line.rstrip()
            img_name = line.split()[0]
            img_path.append(img_name)
    img_per_page = IMG_PER_PAGE
    page_range = len(img_path) // img_per_page + 1
    return img_path,page_range