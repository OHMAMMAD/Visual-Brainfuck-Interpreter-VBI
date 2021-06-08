# Visual-Brainfuck-Interpreter-VBI
one of the slowest interpreters for brainfuck! complete with visualization!

## About BrainFuck:
An esoteric programing language that was built by urban miller at the 1990s. one of the first and most intrestings.
it was made with the purpose of having the smallest compiler(interpreter) possible, one of the interpreters is even about 100 bytes!

more at(i highly recommend reading these):
* [esolangs.org](https://esolangs.org/wiki/Brainfuck)
* [wikipedia](https://en.wikipedia.org/wiki/Brainfuck)

## The Basics
the basics of the lang


## Goal
this interpreter was built because i couldent find a visual interpreter that was not only on the web and i could use it offline. so i made my own!
note that there are good interpreter out there, i just couldn't find them at the moment and the project seemed fun enough to work on.


## Visualization, The Most Important
this interpreter is not trash after all
most of my time making it was to create and de-bug the visualization part.
you can activate it with one of the arguments. go to: [Flags](#flags)

it works preety well if i do say so myself
it loads [<the amount you want>] cells to the right and left of it, with their value on them.
in the next line, it prints where the pointer is with a "^" sign
after that, it shows you the range of the things showing, for example, it shows what which cell-coordinate is the most right and the most left cell(i REALLY dont know how to explain it)
its something like this:

(4 each side)
  
``` 
[0] [0] [23] [5] [8] [48] [65] [0] [10]  (the value cell line)

                  ^                      (the pointer line)

3                                   11   (the ranges line)
```

 if it couldn't print the far most right(or the far most left) cell(because its going to hit the end and the start of the cell list), then it will handle that as well

  
(4 each side)

```
[0] [0] [23] [5] [8] [48] [65] [0] [10]  (the value cell line)

     ^                                   (the pointer line)
 
 1                                  9    (the ranges line)
```
  
i does this so the amount of cells printed, remains the same
  
  
## how to use:
i dont know how to install my code on someones computer in a way that they can use the command line to use it, but its not that bad after all.
after downloading(or cloning) the "main.py" file into your computer, and having python installed and your brainfuck code ready, you can type this command in your command line.

```
python main.py [file path] <args>
```

i have some examples ready for you if you dont have a brainfuck code.
after cloning into the project:
```
python main.py "examples/fib.b"
# prints the Fibonacci sequence
```


## not so great....
this brainfuck interpreter is one of the slowest, mainly because of two reseaons:

1) this is on python(lets just blame python insted of my bad coding skills)

2) im not the gratest of coders/programers

one of the things asusiated with an interpreters speed, is to test a program with it.
this great peace  of code can run towers of hanoi in...ummm..... im not sure how long. i wanted to test it one time, but it taked more than 1h 10m so i just gave up

```
python main.py examples/hanoi.b
# takes more than 1h 10m
```

## Flags
this interpreter doesn't have that many arguments 

```
-s    # to show the visualization
# others are broken right now
```
  
## Special Features
i've added some extra features to this interpreter to help de-buging programs. its my code after all
note that these commands are made for you to use IN the code

```
q    # you can just add this to anywhere in your code, and the program will stop running when it hits that point. this REALLY helps de-bugging HUGELY
"#"  # you can comment your code with this. NOTE: you can only add it to the start of a line
```
  
  # THE PAGE IS NOT DONE
