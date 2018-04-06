from graph import Node, Graph
from utils import *
import pygame
import numpy as np

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 255)
magenta = (255, 0, 255)
pygame.font.init()
basicfont = pygame.font.SysFont(pygame.font.get_default_font(), 20)

class GridWorld():
    def __init__(self, x_dim, y_dim, gap, radius):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.gap = gap
        self.radius = radius
        # First make an element for each row (height of grid)
        self.cells = [0] * y_dim
        # Go through each element and replace with row (width of grid)
        for i in range(y_dim):
            self.cells[i] = [0] * x_dim

        self.graph = Graph()

        self.generateGraphFromGrid()

        self.redraw_rects = []

    def __getitem__(self, pos):
        return self.graph.nodes[pos]

    def __setitem__(self, pos, node):
        self.graph.nodes[pos] = node

    def __str__(self):
        msg = 'Graph:'
        for i in self.graph:
            msg += '\n  node: ' + i + ' g: ' + \
                str(self.graph[i].g) + ' rhs: ' + str(self.graph[i].rhs) + \
                ' neighbors: ' + str(self.graph[i].children)
        return msg

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return self.graph.nodes.__iter__()

    def draw(self, surface):
        WINDOW_SIZE = (self.x_dim * self.gap + 4 * self.radius, self.y_dim * self.gap + 4 * self.radius)
        lines = []
        for pos in self:
            node = self[pos]
            if pos == self.graph.goal:
                COLOR = (153, 51, 255)
            elif node.dead:
                COLOR = (80, 80, 80)
            else:
                COLOR = (102, 204, 255)
            node = self.graph.nodes[pos]
            CENTER = (pos[0]*self.gap+2*self.radius, pos[1]*self.gap+2*self.radius)

            self.redraw_rects += [pygame.draw.circle(surface, COLOR, CENTER, self.radius)]
            self.redraw_rects += [pygame.draw.circle(surface, black, CENTER, self.radius, 1)]

            text = basicfont.render("g: " + str(node.g), True, (0, 0, 200))
            textrect = text.get_rect()
            textrect.center = CENTER
            self.redraw_rects += [surface.blit(text, textrect)]

            for child in node.children:
                if [child, pos] not in lines:
                    CCENTER = (child[0]*self.gap+2*self.radius, child[1]*self.gap+2*self.radius)
                    distance = np.linalg.norm([CCENTER[0] - CENTER[0], CCENTER[1] - CENTER[1]])
                    lines.append([child, pos])
                    lines.append([pos, child])
                    d = np.array([child[0] - pos[0], child[1] - pos[1]])
                    if d[0] == 0 or d[1] == 0:
                        linecolor = (30, 30, 30)
                    elif d[0]/d[1] < 0:
                        linecolor = (0, 0, 100)
                    else:
                        linecolor = (100, 0, 0)
                    v = normalize(d)

                    point1 = CENTER + (self.radius * v)
                    point1 = (int(point1[0]), int(point1[1]))

                    point2 = CENTER + ((distance - self.radius) * v)
                    point2 = (int(point2[0]), int(point2[1]))
                    self.redraw_rects += [pygame.draw.line(surface, linecolor, point1, point2, 5)]

            for parent in node.parents:
                if [parent, pos] not in lines:
                    PCENTER = (parent[0]*self.gap+2*self.radius, parent[1]*self.gap+2*self.radius)
                    distance = np.linalg.norm([CENTER[0] - PCENTER[0], CENTER[1] - PCENTER[1]])
                    lines.append([parent, pos])
                    lines.append([pos, parent])
                    d = np.array([pos[0] - parent[0], pos[1] - parent[1]])
                    if d[0] == 0 or d[1] == 0:
                        linecolor = (30, 30, 30)
                    elif d[0]/d[1] < 0:
                        linecolor = (0, 0, 100)
                    else:
                        linecolor = (100, 0, 0)

                    v = normalize(d)
                    point1 = PCENTER + (self.radius * v)
                    point1 = (int(point1[0]), int(point1[1]))

                    point2 = PCENTER + ((distance - self.radius) * v)
                    point2 = (int(point2[0]), int(point2[1]))
                    self.redraw_rects += [pygame.draw.line(surface, linecolor, point1, point2, 5)]

        rr = self.redraw_rects
        self.redraw_rects = []
        return rr

    def printGrid(self):
        print('** GridWorld **')
        for row in self.cells:
            print(row)

    def printGValues(self):
        for j in range(self.y_dim):
            str_msg = ""
            for i in range(self.x_dim):
                node_id = 'x' + str(i) + 'y' + str(j)
                node = self.graph[node_id]
                if node.g == float('inf'):
                    str_msg += ' - '
                else:
                    str_msg += ' ' + str(node.g) + ' '
            print(str_msg)

    def generateGraphFromGrid(self):
        edge = 1
        for i in range(len(self.cells)):
            row = self.cells[i]
            for j in range(len(row)):
                node = Node((i, j))
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if x == 0 and y == 0:
                            continue
                        if i + x >= 0 and j + y >=0 and i + x < self.x_dim and j + y < self.y_dim:
                            node.addNeighbor((i + x, j + y))
                self.graph[(i, j)] = node

                # # print('graph node ' + str(i) + ',' + str(j))
                # node = Node((i, j))
                # if i > 0:  # not top row
                #     node.addNeighbor((i-1, j))
                # if i + 1 < self.y_dim:  # not bottom row
                #     node.addNeighbor((i+1, j))
                # if j > 0:  # not left col
                #     node.addNeighbor((i, j-1))
                # if j + 1 < self.x_dim:  # not right col
                #     node.addNeighbor((i, j+1))
                # self.graph[(i, j)] = node
