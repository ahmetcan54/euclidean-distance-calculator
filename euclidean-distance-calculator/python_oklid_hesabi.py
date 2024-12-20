
points = [(5,2),(6,5),(9,4),(6,2)]
distances = [] # hesaplanan mesafeler tutulacagi liste

# oklid hesabı 
def euclideanDistance(point1,point2): #
  xFark = abs(point1[0]-point2[0])
  yFark = abs(point1[1]-point2[1])
  oklid = ((xFark**2)+(yFark**2))**0.5
  return oklid

#hesaplanan degerlerin aktarilmasi
for point1 in points:
  for point2 in points:
    if point1 == point2:
      continue
    else :
      distances.append(euclideanDistance(point1,point2))

# en kucuk olanı cekme
min_distance = min(distances)

print(f"En küçük mesafe {min_distance}.")