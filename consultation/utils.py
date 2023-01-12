# const getHour = Number(hour?.split(":")[0])
#   if (getHour < 8 || getHour >= 18) {
#     throw new AppError("You can only schedule between 08:00 and 18:00")
#   }

#   const checkDate = new Date(date)
#   const weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#   const checkDay = weekday[checkDate.getDay()]
#   if (checkDay === "Sunday" || checkDay === "Saturday") {
#     throw new AppError(`You cannot schedule a visit at ${checkDay}`)
#   }

#   const checkSchedule = await scheduleRepository.findOneBy({ date: date, hour: hour })
#   if (checkSchedule) {
#     throw new AppError("Schedule already exists")
#   }

import datetime


def checkConsultationDate(data):
    hour = int(data["hour"][:2:])
    if hour < 8 or hour >= 18:
        return False

    year = int(data["date"].split("-")[0])
    month = int(data["date"].split("-")[1])
    day = int(data["date"].split("-")[2])
    weekday = datetime.datetime(year, month, day).weekday()

    if weekday >= 5:
        return False

    return True
