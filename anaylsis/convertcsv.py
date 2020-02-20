import csv

def writeCsv (i):
    filename = 'VID_TEST_CASE_' + str(i) + '_ANGLES'
    openfile = '../output/output_angle_calc/' + filename + '.txt'
    with open(filename +'.csv', 'w', newline='') as file:
        infile = open(openfile, 'r')
        writer = csv.writer(file)
        headers = ["Frame"]
        for j in range(26):
            headers.append("Angle " + str(j))
        writer.writerow(headers)
        count = 0
        for line in infile:
            addlist = [count]
            m = line[1:-2]
            oldl = (m.split(', '))
            newl = []
            for j in oldl:
                if len(j) >= 1:
                    newl.append(float(j))
            if len(newl) == 26:
                addlist+= newl
                writer.writerow(addlist)
                count += 1

writeCsv(9)