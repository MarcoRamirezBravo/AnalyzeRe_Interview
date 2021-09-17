import argparse

def compute(args):
        input = []
        output = []
       
        with open("input") as f:
            data = f.readlines()
            for line in data:
                try:
                    input.append(float(line))
                except:
                    print("Except")
                    return
    
        counter = 0.0
	
	for val in input:
		if val>args.x and counter<args.y:
			count = val-(args.x)
			if (counter+count) > args.y and (counter!= args.y):
				count -= (counter+count)-args.y
				counter+= count
			else:
				counter = counter + count
			output.append(count)
		else:
			output.append(float(0.0))

	output.append(counter)
        print('\n'.join(map(str,output)))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('x',type=float,default=0.0)
	parser.add_argument('y',type=float,default=0.0)
	args = parser.parse_args()
	compute(args)