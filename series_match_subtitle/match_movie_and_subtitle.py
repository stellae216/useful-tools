# 匹配视频和字幕，根据匹配字幕信息，新建同名字幕到视频同目录(已存在字幕不会重复创建)
# 只需要修改参数line 5-12
import os

# 视频示例
movie_dir = "C:\Movies\来自深渊\来自深渊：烈日的黄金乡 第2季"
movie_example = "[Erai-raws] Made in Abyss - Retsujitsu no Ougonkyou - 01 [1080p][29701495].mkv"
movie_target = "01"
# 字幕示例
subtitle_dir = os.path.join(movie_dir, "zimu")
subtitle_example = "1661232529516-07.ass"
subtitle_target = "07"
subtitle_end = ".ass"


movie_suffix = movie_example.rsplit(".", 1)[-1]
subtitle_suffix = subtitle_example.rsplit(".", 1)[-1]
# 计算视频目标下标范围
movie_start_idx = movie_example.find(movie_target)
if movie_start_idx == -1:
    raise ValueError("初始视频数据不正确")
movie_end_idx = movie_start_idx + len(movie_target) - 1

# 计算字幕目标下标范围
subtitle_start_idx = subtitle_example.find(subtitle_target)
if subtitle_start_idx == -1:
    raise ValueError("初始字幕数据不正确")
subtitle_end_idx = subtitle_start_idx + len(subtitle_target) - 1


file_list = os.listdir(movie_dir)
subtitle_list = os.listdir(subtitle_dir)


def find_subtitle(serial_number: str, sub_titles: list) -> str:
    for sub_name in subtitle_list:
        if not sub_name.endswith(subtitle_end):
            continue
        sub_serial_number = sub_name[subtitle_start_idx: subtitle_end_idx + 1]
        if sub_serial_number != serial_number:
            continue
        return sub_name


def main():
    count = 0
    for filename in file_list:
        if filename == ".DS_Store":
            continue
        if filename.find(".") == -1:
            print(f"跳过文件【{filename}】")
            continue
        movie_file_head, m_suffix = filename.rsplit(".", 1)
        if m_suffix != movie_suffix:
            print(f"跳过文件【{filename}】")
            continue
        if f"{movie_file_head}.{subtitle_suffix}" in file_list:
            print(f"文件【{filename}】字幕已存在！")
            continue
        serial_number = filename[movie_start_idx: movie_end_idx + 1]
        print(f"解析视频【{filename}】序号成功！正在匹配字幕")
        # 匹配字幕
        subtitle_file = find_subtitle(serial_number, subtitle_list)
        if not subtitle_file:
            print("匹配字幕失败！")
            continue
        sub_file_path = os.path.join(subtitle_dir, subtitle_file)
        if not os.path.exists(sub_file_path):
            print("匹配字幕失败！")
            continue
        new_sub_file_path = os.path.join(movie_dir, f"{movie_file_head}.{subtitle_suffix}")
        with open(new_sub_file_path, "wb") as f_new:
            with open(sub_file_path, "rb") as f_old:
                f_new.write(f_old.read())
        count = count + 1
        print(f"匹配字幕成功！复制字幕文件到【{new_sub_file_path}】")

    print(f"成功匹配字幕的视频共【{count}】个!")


if __name__ == '__main__':
    main()
