import sys, time, os
import string


#This class represent a task in GTG.
class Task :
    def __init__(self, ze_id) :
        #the id of this task in the project
        #tid is a string ! (we have to choose a type and stick to it)
        self.tid = str(ze_id)
        self.content = ""
        self.sync_func = None
        self.title = "My task"
        #available status are : Active - Done - Dismiss
        self.status = "Active"
                
    def get_id(self) :
        return self.tid
        
    def get_title(self) :
        return self.title
    
    def set_title(self,title) :
        self.title = title
        
    def set_status(self,status) :
        self.status = status
        
    def get_status(self) :
        return self.status
        
    def get_text(self) :
        #defensive programmtion to avoid returning None
        if self.content :
            return str(self.content)
        else :
            return ""
        
    def set_text(self,texte) :
        self.content = str(texte)
        
    #This is a callback. The "sync" function has to be set
    def set_sync_func(self,sync) :
        self.sync_func = sync
        
    def sync(self) :
        self.sync_func(self.tid)
        
###########################################################################
        
#This class represent a project : a list of tasks sharing the same backend
class Project :
    def __init__(self, name) :
        self.name = name
        self.list = {}
        self.sync_func = None
        
    def list_tasks(self):
        result = self.list.keys()
        #we must ensure that we not return a None
        if not result :
            result = []
        return result
        
    def get_task(self,ze_id) :
        return self.list[str(ze_id)]
        
    def add_task(self,task) :
        tid = task.get_id()
        self.list[str(tid)] = task
        
    def new_task(self) :
        tid = self.__free_tid()
        task = Task(tid)
        self.list[str(tid)] = task
        return task
    
    def delete_task(self,tid) :
        del self.list[tid]
        self.sync()
    
    def __free_tid(self) :
        k = 0
        while self.list.has_key(str(k)) :
            k += 1
        return str(k)
        
    #This is a callback. The "sync" function has to be set
    def set_sync_func(self,sync) :
        self.sync_func = sync
        
    def sync(self) :
        self.sync_func()
        
        
    
