import logging


def save_file_path(path: str, contents: bytes):
    """
    保存文件到指定路径
    :param path: 保存文件路径
    :param contents: 文件二进制流
    :return:
    """
    assert isinstance(contents, bytes)
    with open(path, "wb") as f:
        f.write(contents)
    logging.info("保存成功！文件保存位置: ", path)
