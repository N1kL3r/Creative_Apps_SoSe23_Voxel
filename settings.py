# install libraries
# pip3 install pygame moderngl PyGLM numba
    # PyGame    = For development of multimedia applications like video games
    # Moderngl  = Python wrapper over Opengl 3.3+
    # PyGLM     = Mathematics library for graphics programming (written in C++)
    # Numba     = Optimizing compiler for Numerical Functions in Python

from numba import njit
import numpy as np
import glm
import math

# OpenGL settings
MAJOR_VER, MINOR_VER = 3, 3
DEPTH_SIZE = 24
NUM_SAMPLES = 1  # antialiasing

# resolution of the Window that will appear
WIN_RES = glm.vec2(1600, 900)

# world generation
SEED = 16

# ray casting
MAX_RAY_DIST = 6

# settings for the chunk
CHUNK_SIZE = 48                         # SIDE SIZE
H_CHUNK_SIZE = CHUNK_SIZE // 2          # HALF SIZE
CHUNK_AREA = CHUNK_SIZE * CHUNK_SIZE    # FACE AREA
CHUNK_VOL = CHUNK_AREA * CHUNK_SIZE     # VOLUME
CHUNK_SPHERE_RADIUS = H_CHUNK_SIZE * math.sqrt(3) #radius sphere


# WORLD
WORLD_W, WORLD_H = 20, 2
WORLD_D = WORLD_W
WORLD_AREA = WORLD_W * WORLD_D
WORLD_VOL = WORLD_AREA * WORLD_H


# world center
CENTER_XZ = WORLD_W * H_CHUNK_SIZE
CENTER_Y = WORLD_H * H_CHUNK_SIZE




# basic parameters for the camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50

# Vertical Field of View
V_FOV = glm.radians(FOV_DEG)

# Horizontal Field of View
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)

# basic parameters for the player
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89)

# player
PLAYER_SPEED = 0.005
PLAYER_ROT_SPEED = 0.003    # Rotation Speed
PLAYER_POS = glm.vec3(CENTER_XZ, CHUNK_SIZE, CENTER_XZ)           # Position
MOUSE_SENSITIVITY = 0.002


# define colors (make sure to insert this function into main.py into render method self.ctx.clear(color=...)
BG_COLOR = glm.vec3(0.58, 0.83, 0.99)

# textures
SAND = 1
GRASS = 2
DIRT = 3
STONE = 4
SNOW = 5
LEAVES = 6
WOOD = 7

# terrain levels
SNOW_LVL = 54
STONE_LVL = 49
DIRT_LVL = 40
GRASS_LVL = 8
SAND_LVL = 7

# tree settings
TREE_PROBABILITY = 0.02
TREE_WIDTH, TREE_HEIGHT = 4, 8
TREE_H_WIDTH, TREE_H_HEIGHT = TREE_WIDTH // 2, TREE_HEIGHT // 2

# water
WATER_LINE = 5.6
WATER_AREA = 5 * CHUNK_SIZE * WORLD_W

# cloud
CLOUD_SCALE = 25
CLOUD_HEIGHT = WORLD_H * CHUNK_SIZE * 2