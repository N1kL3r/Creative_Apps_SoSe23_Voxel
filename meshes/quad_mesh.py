from settings import *
from meshes.base_mesh import BaseMesh

# define class QuadMesh which is inherited from BaseMesh
# create pointers to the context
class QuadMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.ctx = self.app.ctx
        self.program = self.app.shader_program.water
        # define data format (3 floats per vertex coordinates, 3 floats per color)
        self.vbo_format = '2u1 3u1'
        self.attrs = ('in_tex_coord', 'in_position')
        self.vao = self.get_vao()

    # define vertex data for quad
    def get_vertex_data(self):
        # Create two triangles with counter-clockwise vertex traversal

        vertices = np.array([
            (0, 0, 0), (1, 0, 1), (1, 0, 0),
            (0, 0, 0), (0, 0, 1), (1, 0, 1)
        ], dtype='uint8')

        tex_coords = np.array([
            (0, 0), (1, 1), (1, 0),
            (0, 0), (0, 1), (1, 1)
        ], dtype='uint8')

        # accumulate lists to one NumPy array in the Format float32

        vertex_data = np.hstack([tex_coords, vertices])
        return vertex_data
