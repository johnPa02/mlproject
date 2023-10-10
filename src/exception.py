import sys

def error_message_detail(error, error_detail:sys):
    _, _, tb = sys.exc_info()
    file_name = tb.tb_frame.f_code.co_filename
    line_no = tb.tb_lineno
    error_message = f"{error} at {file_name} line {line_no}: {error_detail}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys = None):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
    def __str__(self):
        return self.error_message
        