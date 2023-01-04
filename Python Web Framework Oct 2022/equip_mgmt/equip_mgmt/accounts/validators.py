from django.core.exceptions import ValidationError

from equip_mgmt.core.utils import megabytes_to_bytes


def validate_file_less_than_1mb(fileobj):
    filesize = fileobj.file.size
    megabyte_limit = 1.0
    if filesize > megabytes_to_bytes(megabyte_limit):
        raise ValidationError(f'Max file size is {megabyte_limit}MB')
