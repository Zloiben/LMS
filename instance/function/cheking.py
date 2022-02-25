from config import ALLOWED_EXTENSIONS, REGEX
import re


def allowed_file(filename: str) -> bool:
    """
    Для проверки формата файла в разрешенных.\n
    :param filename: Полное название файла Пример: test.txt
    :return: Если верно возращает True в противном случае False
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def check_email(email: str) -> bool:
    """
     Для проверки введенной почты.\n
    :param email: Почта.
    :return: Возращает True если верно в противном случае False.
    """
    if re.fullmatch(REGEX, email):
        return True
    else:
        return False
