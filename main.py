# import the settings from the settings.py file
from settings import *
import moderngl as mgl
import pygame as pg
# The sys module is a set of functions which provide crucial information about how your Python script is interacting with the host system
import sys
# import shader class program
from shader_program import ShaderProgram
from scene import Scene
from player import Player
from textures import Textures

# create a class for the Voxel Engine
class VoxelEngine:
    # initialize the python sub modules and set OpenGL attributes
    def __init__(self):
        pg.init()
        # Version of OpenGL = ModernGL
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, MAJOR_VER)

        # This prohibits the use of deprecated functions
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, MINOR_VER)

        # disabling deprecated functions - set type of GL context
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        # Value is set to 24 Bits for the Depth Buffer
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, DEPTH_SIZE)

        pg.display.gl_set_attribute(pg.GL_MULTISAMPLESAMPLES, NUM_SAMPLES)


        # Set the window resolution
        pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)

        # create OpenGL context and call context method of ModernGL module
        self.ctx = mgl.create_context()


        # activate fragment depth testing
        # OpenGL tests the depth value of a fragment against the content of the depth buffer
        # Culling of invisible Faces (only render the faces that are facing the viewer)
        # Color-Blending (implement transparency within objects)
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)

        # collection of unused OpenGL objects so that they are not manually deleted
        self.ctx.gc_mode = 'auto'

        # keep track of time
        self.clock = pg.time.Clock()

        # check if application is running
        self.delta_time = 0
        self.time = 0

        # lock mouse inside window borders
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.is_running = True
        self.on_init()

    # create instance of shader program
    def on_init(self):
        self.textures = Textures(self)
        self.player = Player(self)
        self.shader_program = ShaderProgram(self)
        self.scene = Scene(self)


    # method for updating the state of objects
    def update(self):

        self.player.update()
        # update shader
        self.shader_program.update()
        self.scene.update()

        # Update time delta value
        self.delta_time = self.clock.tick()

        # Update time
        self.time = pg.time.get_ticks() * 0.001

        # Display information about running performance (frame rate value)
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')

    # method for rendering state ob objects
    def render(self):
        # Clear Frame- and Depth-Buffers
        self.ctx.clear(color=BG_COLOR)
        self.scene.render()

        # display new frame with flip method
        pg.display.flip()

    # method for handling events and calling main appliation loop
    def handle_events(self):

        # watch events for closing window or pressing Escape key and potentially set running flag to FALSE
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False
            self.player.handle_event(event=event)


    # method for running app
    def run(self):

        # Implementation of main loop and call methods or quit application otherwise
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()

# write the constructor
if __name__ == '__main__':
    app = VoxelEngine()
    app.run()
