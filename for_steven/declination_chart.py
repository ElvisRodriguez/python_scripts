MONTHS = 12


def parse_table():
    with open('declination_table.txt', 'r') as file:
        table = []
        for line in file.readlines():
            line = line.replace('\t', ' ')
            line = line.replace('\n', '')
            line = line.replace('°', '')
            values = [float(x) for x in line.split(' ') if x != '']
            table.append(values)
        chart = []
        for i in range(MONTHS):
            chart.extend([t[i] for t in table])
        return chart


def solar_declination(day, chart):
    return chart[day - 1]


chart = parse_table()
print(solar_declination(344, chart))
