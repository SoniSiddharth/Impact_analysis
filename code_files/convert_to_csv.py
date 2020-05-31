import csv

def To_csv(output, search_string, results_returned,threshold):
	name = "Similar_to_" + str(search_string) + ".csv"
	with open(name,'w',newline='') as ak:
		AJS=csv.writer(ak)
		AJS.writerow(['Your keyword: '])
		AJS.writerow([search_string])
		AJS.writerow('\n')
		AJS.writerow('\n')
		AJS.writerow(['Number of results:'])
		AJS.writerow([str(results_returned)])
		AJS.writerow('\n')
		AJS.writerow('\n')
		AJS.writerow(['Your current threshold:'])
		AJS.writerow([str(threshold)])
		AJS.writerow('\n')
		AJS.writerow('\n')
		AJS.writerow(['Here are your similar Test IDs:'])
		AJS.writerow('\n')

		for i in range (len(output)):
			AJS.writerow(['Test ID'+' '+str(i+1),output[i]])
			AJS.writerow('\n')
