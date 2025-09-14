class PointsForPlace:
    def get_points_for_place(self, place):
        points = 0
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            points = 101 - place
        return points


class PointsForMeters:
    def get_points_for_meters(self, meters):
        points = 0
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            points = meters * 0.5
        return points


class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, meters, place):
        points_place = self.get_points_for_place(place)
        points_meters = self.get_points_for_meters(meters)
        total = points_place + points_meters
        return total


# Тесты
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))  # 91

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))  # 5.0

total_points = TotalPoints()
print(total_points.get_points_for_place(10))      # 91
print(total_points.get_points_for_meters(10))     # 5.0
print(total_points.get_total_points(10, 10))      # 96.0