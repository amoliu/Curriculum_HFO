#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 13:30:10 2017
Base class for Curriculum Learning approaches. A Curriculum composed of only the target task is built.
@author: Felipe Leno
"""
import abc

class Curriculum(object):
    """ This is the base class for all Curriculum Learning implementations.

    """
    __metaclass__ = abc.ABCMeta
    seed = None
    agent = None
   
    def __init__(self, seed=12345,agent=None):
        self.seed = seed
        self.agent = agent
        #If the set of agents is not null, a reference to the curriculum is created
        if agent != None:
            #for agentUnity in agent:
            #    agentUnity.set_curriculum(self)
            agent.set_curriculum(self)
        
    @abc.abstractmethod      
    def print_result(self):
        """Prints the CUrriculum"""
        pass

    @abc.abstractmethod
    def generate_curriculum(self,target_task, sourceFolder,workFolder):
        """ The Curriculum is generated by this function (stored internally) """
        pass
    @abc.abstractmethod
    def generate_curriculum_from_tasks(self,target_task, taskList):
        pass
     
        
    @abc.abstractmethod
    def empty_curriculum(self):
        """ Returns if the curriculum still has an untrained task """
        pass
    
    @abc.abstractmethod    
    def draw_task(self):
        """ Get the next task in the curriculum """
        pass
    @abc.abstractmethod 
    def previous_tasks(self,task):
        """Returns the children for a given task"""
        pass
    
 

