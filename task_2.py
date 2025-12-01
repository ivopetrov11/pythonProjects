# INPUT -> photo.jpg, Warsaw, 2013-09-05 14:08:15
# OUTPUT -> Warsaw02.jpg

def solution(S):
    lines = S

    photos_by_city = {}
    # <<photoname>>.<<extension>>, <<city_name>>, yyyy-mm-dd hh:mm:ss

    for idx, line in enumerate(lines):
        filename, city, timestamp = line.split(", ")
        name, ext = filename.split(".")

        photo = {
            "index": idx,
            "ext": ext,
            "city": city,
            "time": timestamp
        }

        photos_by_city.setdefault(city, []).append(photo)

    # Sort each city by timestamp
    for city in photos_by_city:
        photos_by_city[city].sort(key=lambda p: p["time"])

    result = [None] * len(lines)

    # Rename photos
    for city, photos in photos_by_city.items():
        total = len(photos)
        digits = len(str(total))

        for i, ph in enumerate(photos):
            new_name = f"{city}{str(i+1).zfill(digits)}.{ph['ext']}"
            result[ph["index"]] = new_name


    return "\n".join(result)

# ----------------------

lines_input_list = []
while True:
    line = input()
    if not line:
        break
    lines_input_list.append(line)
print(solution(lines_input_list))

# photo.jpg, Warsaw, 2013-09-05 14:08:15
# Jay.png, London, 2015-06-20 15:13:22
# myFriends.png, Warsaw, 2013-09-05 14:07:13
# Eiffel.jpg, Paris, 2015-07-23 08:03:02
# pisatower.jpg, Paris, 2015-07-22 23:59:59
# BOB.jpg, London, 2015-08-05 00:02:03
# notredame.png, Paris, 2015-09-01 12:00:00
# me.jpg, Warsaw, 2013-09-06 15:40:22
# a.png, Warsaw, 2016-02-13 13:33:50
# b.jpg, Warsaw, 2016-01-02 15:12:22
# c.jpg, Warsaw, 2016-01-02 14:34:30
# d.jpg, Warsaw, 2016-01-02 15:15:01
# e.png, Warsaw, 2016-01-02 09:49:09
# f.png, Warsaw, 2016-01-02 10:55:32
# g.jpg, Warsaw, 2016-02-29 22:13:11

# Warsaw02.jpg
# London1.png
# Warsaw01.png
# Paris2.jpg
# Paris1.jpg
# London2.jpg
# Paris3.png
# Warsaw03.jpg
# Warsaw09.png
# Warsaw07.jpg
# Warsaw06.jpg
# Warsaw08.jpg
# Warsaw04.png
# Warsaw05.png
# Warsaw10.jpg

