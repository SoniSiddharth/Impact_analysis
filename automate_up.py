import watchdog.events 
import watchdog.observers 
import time 
import pickle
from datetime import datetime, timedelta

#Citation: The basic framework for the watchdog observer has been taken from this link: https://www.geeksforgeeks.org/create-a-watchdog-in-python-to-look-for-filesystem-changes/

class Handler(watchdog.events.PatternMatchingEventHandler): 
	def __init__(self): 
		watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.pdf','*.docx','*.txt'], ignore_directories=True, case_sensitive=False) # Add the extensions as per your need
		self.last_modified = datetime.now() 
		
	def on_created(self, event): 
		print("Event is created - % s." % event.src_path) 
		# print("Hello") 

	def on_modified(self, event): 
		if datetime.now() - self.last_modified < timedelta(seconds=1):
			return 
		else:
			self.last_modified = datetime.now()
		print("Event is modified - % s." % event.src_path) 
		paths.append(event.src_path)
		# update_emb(event.src_path)

	def on_deleted(self, event): 
		print("Event is deleted - % s." % event.src_path) 
		# print("Hello") 


if __name__ == "__main__": 
	src_path = r"C:\Users\Janvi Thakkar\Desktop\projects\Capegemini\separate_test_doc"
	event_handler = Handler() 
	observer = watchdog.observers.Observer() 
	observer.schedule(event_handler, path=src_path, recursive=True) 
	observer.start() 
	paths=[] 
	try: 
		while True: 
			time.sleep(10) 
	except KeyboardInterrupt: 
		observer.stop()
		with open('listfile.data','wb') as filehandle:
			pickle.dump(paths,filehandle)
	observer.join() 
