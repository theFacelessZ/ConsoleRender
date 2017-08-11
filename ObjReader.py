from Vector3 import Vector3
from GameObject import MeshComponent


class ObjVertex:

    def __init__(self, x = 0.0, y = 0.0, z = 0.0, w = 1.0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w


class ObjUVW:

    def __init__(self, u = 0.0, v = 0.0, w = 0.0):
        self.u = u
        self.v = v
        self.w = w


class ObjData:

    def __init__(self):
        self.vertices = []
        self.texture_coords = []
        self.normals = []
        self.parameter_space = []
        self.faces = []

    def is_empty(self):
        return not (len(self.vertices) + \
               len(self.texture_coords) + \
               len(self.normals) + \
               len(self.parameter_space) + \
               len(self.faces))


class ObjReader:

    @staticmethod
    def load(file_path):
        parser = ObjReader(file_path)
        return parser.parse()

    @staticmethod
    def get_mapping():
        return {
            'v': {
                'class': Vector3,
                'field': 'vertices',
            },
            'vt': {
                'class': ObjUVW,
                'field': 'texture_coords',
            },
            'vn': {
                'class': ObjUVW,
                'field': 'normals',
            },
        }

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        result = {}

        current_geometry_name = 'default'
        current_geometry = ObjData()

        mapping = ObjReader.get_mapping()

        with open(self.file_path) as f:
            while True:

                line = f.readline()

                # EOF.
                if line == '':
                    if not len(result):
                        result[current_geometry_name] = current_geometry

                    break

                data = line.replace('\n', '').split(' ')
                # Ignore comments.
                if data[0] in ['#', 'mtllib', '']:
                    continue

                # New geometry flag.
                if data[0] in ['g']:
                    if not current_geometry.is_empty():
                        result[current_geometry_name] = current_geometry

                    current_geometry_name = data[1]
                    current_geometry = ObjData()

                    if current_geometry_name in result.keys():
                        current_geometry = result[current_geometry_name]

                    continue

                if data[0] not in mapping:
                    continue

                # Initialize a class defined in mapping.
                element_schema = mapping[data[0]]

                element = element_schema['class'](*data[1:])
                getattr(current_geometry, element_schema['field']).append(element)

        return result
