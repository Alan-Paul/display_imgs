###Show pic
a project to show pictures on remote server

### requirement
    Django==2.2.3

### usage
    Prepare your images' name in a log.txt file
    
        eg. the content of my log.txt is like this:        
        img1.jpg
        img2.jpg
        ...
        imgX.jpg
    
    Then modify the main_settings/settings.py like this:
    
        IMG_ROOT = "/path/to/img_root"
        IMG_LIST = "/path/to/log.txt"
        IMG_PER_PAGE = 20
    
    Run the app like this :
        python manage.py runserver 0.0.0.0:8000
        
### else
use pipreqs to export the requirements:

    pip install pipreqs 
    cd /path/to/Project_root
    pipreqs ./