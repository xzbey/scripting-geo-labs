from layer_worker import *

layers = []

add_layer(layers, create_layer("Границы районов", "Polygon", "EPSG:4326", 12))
add_layer(layers, create_layer("Дороги", "LineString", "EPSG:3857", 48))
add_layer(layers, create_layer("Остановки", "Point", "EPSG:4326", 35))
add_layer(layers, create_layer("Зоны парков", "Polygon", "EPSG:32637", 7))
add_layer(layers, create_layer("Реки", "LineString", "EPSG:32637", 16))

print("Все слои:")
print_all_layers(layers)

print("\nСлой с именем 'Дороги':")
road_layer = find_layer_by_name(layers, "Дороги")
if road_layer is not None:
	print_layer(road_layer)
else:
	print("Слой не найден")

print("\nСлои с геометрией Polygon:")
filtered_layers = filter_by_geometry(layers, "Polygon")
if filtered_layers:
    print_all_layers(filtered_layers)
else:
	print("Слоев с такой геометрией нет")

print(f"\nСуммарное количество объектов: {count_total_features(layers)}")
