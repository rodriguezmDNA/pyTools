USAGE = """
Python demo for `xargs`-based command-line parallelization.
Run this script as:
    $ python [thisscript.py] [number]
for serial, single-argument execution. Then try:
    $ seq -1 0.25 1 | xargs -I% -P2 -n1 python argsDemo.py % 100
This runs `p.py` with numbers -1 to 1 in steps of 0.25, 2 processes at a time.
Change `-P2` to `-P8` for eight processes, etc. As explained below, only change
`-P` flag, ***not*** the `-n` flag unless you know what you're doing.
On macOS, you may need to `brew install findutils --with-default-names` to get
`xargs`.
On my computer, this prints:
    $ seq -1 0.25 1 | xargs -I% -P2 -n1 python p.py % 100
    ['p.py', '-1.00', '100']
    99.0
    done
    ['p.py', '-0.75', '100']
    99.25
    done
    ['p.py', '-0.25', '100']
    99.75
    done
    ['p.py', '-0.50', '100']
    99.5
    done
    ['p.py', '0.25', '100']
    100.25
    done
    ['p.py', '0.00', '100']
    100.0
    done
    ['p.py', '0.50', '100']
    100.5
    done
    ['p.py', '0.75', '100']
    100.75
    done
    ['p.py', '1.00', '100']
    101.0
    done
Notice how some of the lines are out-of-order, which implies that multiple
processes were being run at the same time.
N.B.: the `-n1` parameter tells `xargs` to give one line of its input to each
process it spawns. This is required because our Python script doesn't know how
to handle `python [thisscript.py] [number1] [number2]` which would be the case
if `-n2` was used. (That is left as an exercise to the reader.)
N.B. 2: the `-I%` parameter tells `xargs` where to put each line of input in the
command. It's not strictly necessary here since by default it'll append the
input to the end of the command.
N.B. 3: the `seq` command generates the list of numbers, which is convenient,
but you can use any command to generate a list of inputs to sweep over,
including putting them in a file (one number per line) and then replacing the
`seq` call with `cat [myparameters.txt]`.
"""


def doWork(x, N=1):
    print(x + N)
    print('done')


def usage():
    print(USAGE)


if __name__ == '__main__':
    import sys
    print(sys.argv)
    if len(sys.argv) < 2:
        usage()
    elif len(sys.argv) < 3:
        doWork(float(sys.argv[1]))
    elif len(sys.argv) < 4:
        doWork(float(sys.argv[1]), float(sys.argv[2]))