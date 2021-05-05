md = input("請輸入生日日期:")
md=md.split(' ')
month = int(str(md[0]))
date = int(str(md[1]))


def get_constellation(month, date):
    dates = (21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22)
    constellations = ("Sagittarius", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Capricorn", "Sagittarius")
    if date < dates[month-1]:
        return "星座為:"+constellations[month-1]
    else:
        return "星座為:"+constellations[month]

print (get_constellation(month,date))