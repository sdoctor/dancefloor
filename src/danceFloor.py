#! /usr/bin/python

# The data structure for the dance floor


__author__="sdrakeley"
__date__ ="$Feb 20, 2014 8:33:20 PM$"

import pygame
from pygame.locals import QUIT
import sys


class Floor:
   
    def __init__(self, num_pitches=5, num_seconds=4):
        """ 
            @param num_pitches : number of pitches in range of notes (num rows)
            @param num_seconds : number of seconds in loop (num columns)
            
            Creates an PxS matrix where P is num pitches and S is num seconds
        """
        self.num_rows = num_pitches
        self.rows = []
        for pitch in range(0, self.num_rows):
            self.rows.append(Row(num_seconds, pitch))
        
    def display(self, time):
        display_str = ""
        for row in self.rows:
            display_str += row.display(time)
            
        return display_str
    
    def display_pygame(self, time, windowSurf):
        for row in self.rows:
            row.display_pygame(time, windowSurf)
    
    def set_active(self, pitch, time):
        self.rows[pitch].set_active(time) 
            
        
        
class Row:
    """ Container for the tiles
        Each row corresponds to a pitch #TODO is this info redundnant?
    """
    def __init__(self, num_seconds, pitch):
        self.pitch = pitch
        self.num_tiles = num_seconds
        self.tiles = []
        for s in range(0, num_seconds):
            self.tiles.append(Tile(self.pitch, s))
            
    def set_active(self, time):
        self.tiles[time].set_active()
        
    def display(self, time):
        display_str = ""
        for tile in self.tiles:
            display_str += tile.display(time)            
        return display_str + "\n"
    
    def display_pygame(self, time, windowSurf):
        for tile in self.tiles:
            tile.display_pygame(windowSurf)
            
        
        
class Tile:
    
    def __init__(self, pitch, time):
        self.time = time
        self.pitch = pitch
        self.is_active = False
        self.active_color = pygame.Color(200, 200, 200)
        self.inactive_color = pygame.Color(100, 100, 100)
        
    def set_active(self):
        self.is_active = True
        
    def get_active_state(self):
        return self.is_active
        
    def get_pitch(self):
        return self.pitch
    
    def display(self, time):
        if self.time == time and self.is_active:
            return "[%d]" % self.pitch
        else:
            return "[ ]"
        
    def display_pygame(self, windowSurf):
        """ Display for pygame
        """
        cur_color = self.active_color if self.is_active else self.inactive_color
        pygame.draw.rect(windowSurf, cur_color, 
                        (self.time*55+10, self.pitch*55+10, 50, 50))


if __name__ == "__main__":
    floor = Floor(num_pitches=5, num_seconds=4)
    print "empty floor on second 0"
    print floor.display(0)
    print "setting pitch 3 active on second 2"
    floor.set_active(3, 2) #pitch, time (rise over run)
    floor.set_active(2, 2)
    floor.set_active(1, 2)
    floor.set_active(0, 2)
    print floor.display(2)
    
    windowSurf = pygame.display.set_mode((640, 480))
    while True:
        windowSurf.fill(pygame.Color(255,255,255))
        # To make an arbitrary polygon
        #pygame.draw.polygon(windowSurf, pygame.Color(0, 255, 0), ((146, 0), 
        #                                                          (291, 106), 
        #                                                          (236, 277), 
        #                                                          (56, 277), 
        #                                                          (0, 106)))
        #
        ##########################This display section works to build the grid!
        floor.display_pygame(0, windowSurf)
        #for i in range(0, 8):
        #    for j in range(0, 8):
        #        pygame.draw.rect(windowSurf, pygame.Color(100, 100, 100), 
        #                        (i*55+10, j*55+10, 50, 50))
            
        # For drawing individual pixels
        #pixArray = pygame.PixelArray(windowSurf)
        #for x in range(100, 200, 4):
        #    for y in range(100, 200, 4):
        #        pixArray[x][y] = pygame.Color(255, 0, 0)
                
        #del pixArray
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
         
        
        pygame.display.update()
    
        

    
