#! /usr/bin/python

# The data structure for the dance floor


__author__="sdrakeley"
__date__ ="$Feb 20, 2014 8:33:20 PM$"

import pygame


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
            
        
        
class Tile:
    
    def __init__(self, pitch, time):
        self.time = time
        self.pitch = pitch
        self.is_active = False
        
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
    windowSurf.fill(pygame.Color(255,255,255))
    pygame.draw.polygon(windowSurf, pygame.Color(0,255,0), ((146,0), (291,106), (236,277), (56,277), (0,106)))
    
    
    
    import sys
    print sys.version 
