from dataclasses import dataclass

@dataclass
class Layer:
    name: str
    geometry: str
    crs: str
    features: int


def create_layer(name: str, geometry: str, crs: str, features: int) -> Layer:
    return Layer(name, geometry, crs, features)

def add_layer(layers: list, layer: Layer) -> None:
    layers.append(layer)

def find_layer_by_name(layers: list, name: str) -> Layer | None:
    for layer in layers:
        if layer.name == name:
            return layer
    return None

def filter_by_geometry(layers: list, geometry: str) -> list:
    m_layers = []
    for layer in layers:
        if layer.geometry == geometry:
            m_layers.append(layer)
    return m_layers

def count_total_features(layers: list) -> int:
    return sum(layer.features for layer in layers)

def print_layer(layer: Layer) -> None:
    print(f"Имя слоя: {layer.name}\n"
          f"Тип геометрии: {layer.geometry}\n"
          f"Система координат: {layer.crs}\n"
          f"Количество объектов: {layer.features}")

def print_all_layers(layers: list) -> None:
    for layer in layers:
        print_layer(layer)
