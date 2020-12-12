import pathlib

def readfile(filename):
    p = pathlib.Path(filename)
    if not p.is_file():
        return -1
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
    if count == 0:
        return -1
    result /= count
    return result

log = open('speedup.csv', 'w')
base = 'logs/'
solutions = ['Pico-CAS', 'Pico-ST', 'PST', 'HST', 'HST-weak', 'Pico-HTM', 'PST-remap'] #HST not complete
names = ['blackscholes', 'bodytrack', 'facesim', 'fluidanimate', 'freqmine', 'swaptions', 'x264']
for name in names:
    log.write(name + ',')
    thread = 1
    while thread <= 32:
        log.write(str(thread) + ',')
        thread = thread * 2
    log.write('\n')

    for solution in solutions:
        log.write(solution + ',')
        baseline = readfile(base + 'Pico-CAS/' + name + '1.txt') # normolize Pico-CAS single thread as 1
        thread = 1
        while thread <= 32:
            filename = base + solution + '/' + name + str(thread) + '.txt'
            t = readfile(filename)
            if t == -1:
                log.write('-1,')
            else:
                t = baseline / t
                log.write(str(t) + ',')
            thread = thread * 2
        
        log.write('\n')

log.close()