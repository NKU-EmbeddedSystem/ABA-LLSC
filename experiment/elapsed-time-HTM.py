def readfile(filename):
    f = open(filename)
    lines = f.readlines()
    result = 0.0
    count = 0
    for line in lines:
        index = line.find('real')
        if index != -1:
            count += 1
            m = float(line[5 : line.find('m')])
            s = float(line[line.find('m') + 1 : -2])
            result += m * 60 + s
    
    result /= count
    return result

log = open('elapsed-time-HTM.csv', 'w')
base = 'logs/'
solutions = ['HST-HTM'] # Pico-HTM don't scale up to 8 threads
for solution in solutions:
    thread = 1
    log.write(solution + ',')
    while thread <= 32:
        log.write(str(thread) + ',')
        thread = thread * 2
    log.write('\n')
    names = ['blackscholes', 'bodytrack', 'facesim', 'fluidanimate', 'freqmine', 'swaptions', 'x264']
    for name in names:
        log.write(name + ',')
        thread = 1
        while thread <= 32:
            filename = base + solution + '/' + name + str(thread) + '.txt'
            t = readfile(filename)
            log.write(str(t) + ',')
            thread = thread * 2
        log.write('\n')

log.close()
