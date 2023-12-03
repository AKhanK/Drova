from django.core.exceptions import ValidationError

def file_size(value):
    filesize=value.size
    filesize>419430400
    



    # raise ValidationError("maximum size is  mb")