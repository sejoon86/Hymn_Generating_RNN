import midi
import numpy as np
import matplotlib.pyplot as plt
import re
import math

 

def convert_midi_to_csv(file_name): 
	print(file_name)
	pattern = midi.read_midifile(file_name)
	data_string = str(pattern)
	A = data_string.splitlines() 

	num_arr = []

	for N in range(len(A)):
		#print(A[N].find('NoteOnEvent'))
		if(A[N].find('resolution') != -1):
			#print(A[N])
			resolution = [int(i) for i in re.findall(r'\d+', A[N])][1]
			#print(resolution)
		
		if(A[N].find('NoteOnEvent') != -1 or A[N].find('NoteOffEvent') != -1):
			#print(A[N])
			#print([int(i) for i in re.findall(r'\d+', A[N])])
			num_arr.append([int(i) for i in re.findall(r'\d+', A[N])])
	np_arr = np.array(num_arr)

	channel = np_arr[:,1]
	unique_channels = set(channel) 




	flag_grid_init = False



	for unique_channel in unique_channels:
		ch0 = np.where(channel==unique_channel) # channel 0만 보기

		tick = np_arr[ch0,0][0]
		note = np_arr[ch0,2][0]
		vel = np_arr[ch0,3][0]
		
		#vel  note  tick
		start_tick_arr = []
		note_arr = []

		current_tick = 0
		tick_arr = []
		for N in range(len(vel)):

			current_tick += tick[N]
			tick_arr.append(current_tick)
			if(vel[N]!=0):
				start_tick_arr.append(current_tick)
				note_arr.append(note[N])

		start_tick_arr = np.array(start_tick_arr)
		note_arr = np.array(note_arr) 
		
		#vel  note  tick 
		start_tick_arr = []
		stop_tick_arr = []
		start_note_arr = []
		stop_note_arr = []

		tick_arr = []

		current_tick = 0

		for N in range(len(vel)):

			current_tick += tick[N]

			tick_arr.append(current_tick)

			if(vel[N]!=0):
				start_tick_arr.append(current_tick)
				start_note_arr.append(note[N])
			else:
				stop_tick_arr.append(current_tick)
				stop_note_arr.append(note[N])



		start_tick_arr = np.array(start_tick_arr)/resolution
		start_note_arr = np.array(start_note_arr)
		stop_tick_arr = np.array(stop_tick_arr)/resolution
		stop_note_arr = np.array(stop_note_arr)
		tick_arr = np.array(tick_arr)/resolution

		
		
		
		
		
		note_duration = {}
		for note_num in range(128):
			ndx = np.where(note == note_num)
			if len(ndx[0]) > 0:
				if len(ndx[0])%2 != 0:
					print("ERROR!!!!!!!!!!!!!!!!!")
				assert len(ndx[0])%2 == 0, "error! note numbers have an odd number"
				note_duration[note_num] = np.round(tick_arr[ndx] * 16)# 8등분 최소단위!
				#print('{}: {}'.format(note_num, note_duration[note_num]))

		if not flag_grid_init:
			max_tick = 0
			for key in note_duration.keys():
				if max_tick < max(note_duration[key]):
					max_tick = max(note_duration[key])
			print("max tick is {}".format(max_tick))
			grid_note = np.zeros((128,int(max_tick)))

			for key in note_duration.keys():
				ticks = note_duration[key]
				for idx in range(0, ticks.shape[0]-1, 2):
					grid_note[int(key), int(ticks[idx]):int(ticks[idx+1])] = 1
					grid_note[int(key), int(ticks[idx])] = 2 
			
			flag_grid_init = True
		

		for key in note_duration.keys():
			ticks = note_duration[key]
			for idx in range(0, ticks.shape[0]-1, 2):
				grid_note[int(key), int(ticks[idx]):int(ticks[idx+1])] = 1
				grid_note[int(key), int(ticks[idx])] = 2


	assert np.max(np.sum(grid_note>0, axis=0)) <= 41, "more than 41 notes at once" 
	grid_note.astype(int)
    
	plt.figure(figsize=(18,6))
	plt.subplot(211)
	plt.imshow(grid_note)
	plt.ylim([0,128])
	plt.title(file_name)
	plt.subplot(212)
	plt.plot(np.sum(grid_note>0, axis=0))
	plt.show()
	savefile_name = file_name[:-4]+".csv"
	np.savetxt(savefile_name, grid_note, delimiter=",")    
	print(savefile_name)
