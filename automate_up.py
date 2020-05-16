import watchdog.events 
import watchdog.observers 
import time 
import pickle
from datetime import datetime, timedelta


class Handler(watchdog.events.PatternMatchingEventHandler): 
	def __init__(self): 
		# Set the patterns for PatternMatchingEventHandler
		watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.pdf','*.docx','*.txt'], ignore_directories=True, case_sensitive=False) # Add the extensions as per your need
		self.last_modified = datetime.now() 
	def on_created(self, event): 
		print("Watchdog received created event - % s." % event.src_path) 
		# print("Hello")
		# Event is created, you can process it now 

	def on_modified(self, event): 
		if datetime.now() - self.last_modified < timedelta(seconds=1):
			return 
		else:
			self.last_modified = datetime.now()
		print("Watchdog received modified event - % s." % event.src_path) 
		paths.append(event.src_path)
		# update_emb(event.src_path)
		# Event is modified, you can process it now

	def on_deleted(self, event): 
		print("Watchdog received deleted event - % s." % event.src_path) 
		# print("Hello")
		# Event is modified, you can process it now 


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