import json
import logging

from enum import IntEnum

logger = logging.getLogger(__name__)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def json_response(code, message, params={}, encoding='utf-8'):
    res = dict(code=int(code), message=message)
    for key in params:
        res[key] = params[key]
    return res


class ApiErrorCode(IntEnum):
    ok = 0,
    generic_error = 1,
    request_too_many_sms = 101,
    wrong_sms_code = 102,
    wrong_invite_code = 103,
    multiple_register = 104,

    failed_to_gen_video = 201,
    failed_to_gen_tts = 202,
    manifest_not_exists = 203,

    article_start_not_found = 301,
    article_end_not_found = 302,
    article_content_not_found = 303,
    article_paragraph_not_found = 304,
    article_no_debug_info = 305,

    not_supported = 401,

    lfasr_not_generated = 501
    autosub_upload_failed = 502
    autosub_upload_file_exceed_limit = 503
    tts_generation_failed = 504

    stream_url_gone = 601,
    stream_url_forbidden = 602
    proxy_connect_error = 603
    sensitive_word_found = 604

    bgm_count_exceed_limit = 701,

    auth_failed = 801,

    export_times_exceed = 901
    export_exists = 902

    # open api:
    open_api_user_not_exist = 100001
    open_api_token_expired = 100002
    open_api_sign_error = 100003
