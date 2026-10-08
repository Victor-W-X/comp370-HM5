'''
outputs the number of each complaint type per borough for a given (creation) date range.
'''
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help = 'path to input csv file')
    parser.add_argument('-o', '--output', type=str, help = 'path to output file')
    parser.add_argument('-s', '--start_date', type=str, help = 'start date, format: year/month/day')
    parser.add_argument('-e', '--end_date', type=str, help = 'end date, format: year/month/day')    

    args = parser.parse_args()

    input = args.input
    output = args.output
    start_date = tuple(map(int,args.start_date.split("/")))
    
    end_date = tuple(map(int,args.end_date.split("/")))


    print('processing file', input)
    print('output', output)
    print('start_date', start_date)
    print('end_date', end_date)


    i = 0

    with open(args.input, 'r') as fi:
        col = next(fi)
        if output is not None:
            with open(args.output, 'w') as fo:
                fo.write(col)
                for line in fi:
                    line_args = line.strip().split(',')
                    if len(line_args[2].split()) == 0:
                        continue
                    s= line_args[1].split()[0].split("/")
                    e= line_args[2].split()[0].split("/")
                    s_d = int(s[2]), int(s[0]), int(s[1])
                    e_d = int(s[2]), int(s[0]), int(s[1])
            
                    if start_date <= s_d and e_d <= end_date:
                        if output is not None:
                            fo.write(line)
                        else:
                            print(line)
        else:
            print(col)
            for line in fi:
                    line_args = line.strip().split(',')
                    if len(line_args[2].split()) == 0:
                        continue
                    s= line_args[1].split()[0].split("/")
                    e= line_args[2].split()[0].split("/")
                    s_d = int(s[2]), int(s[0]), int(s[1])
                    e_d = int(s[2]), int(s[0]), int(s[1])
            
                    if start_date <= s_d and e_d <= end_date:
                        if output is not None:
                            fo.write(line)
                        else:
                            print(line)

       

    
if __name__ == '__main__':
    main()
