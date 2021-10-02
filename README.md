# Visual-Brainfuck-Interpreter-VBI
one of the slowest interpreters for brainfuck! complete with visualization! made with python

## About BrainFuck:
An esoteric programing language that was built by urban miller in the 1990s. one of the first and most interesting.
it was made with the purpose of having the smallest compiler(interpreter) possible, one of the interpreters is even about 100 bytes!

more at(I highly recommend reading these):
* [esolangs.org](https://esolangs.org/wiki/Brainfuck)
* [wikipedia](https://en.wikipedia.org/wiki/Brainfuck)

## The Basics
if you don't know how the language works, I hugely recommend you read this part or watch a youtube video about it.
* [trutles youtube chanell](https://www.youtube.com/watch?v=dxJpGVaCAyU)
* [How Brainfuck Works](https://www.youtube.com/watch?v=-3C200nCwpk)

the program uses only 8 commands, it has an array of cells with values on each of the cell
you can increase or decrease the value in each cell
you have a pointer pointing to a cell at every moment. if you want to do something with a cell, you have to put the pointer to it
you can move the pointer with the "<" and ">" command 
you can increase or decrease the value of the cell you are pointing on by one, with the "+" and "-" commands
you can get input with "," and print the ASCII value of the current cell with "."
by using brackets, you create a loop
if the value in the current cell is not 0, then it does the instructions in the brackets
if at the end of a bracket, the value on the current cell was not 0, it will do the instructions again
and that was the whole language.
but I highly recommend watching a video on it

## Goal
this interpreter was built because I couldn't find a visual interpreter that was not only on the web and I could use it offline. so I made my own!

note that there are good interpreters out there, I just couldn't find them at the moment and the project seemed fun enough to work on.


## Visualization, The Most Important
this interpreter is not trash after all
most of my time making it was to create and debug the visualization part.
you can activate it with one of the arguments. go to: [Flags](#flags)

it works pretty well if I do say so myself
it loads [<the amount you want>] cells to the right and left of it, with their value on them.
in the next line, it prints where the pointer is with a "^" sign
after that, it shows you the range of the things showing, for example, it shows which cell coordinate is the most right and the most left cell(I REALLY don't know how to explain it)
its something like this:

(4 each side)
  
``` 
[0] [0] [23] [5] [8] [48] [65] [0] [10]   # (the value cell line)

                  ^                       # (the pointer line)

3                                   11    # (the ranges line)
```

 if it couldn't print the far most right(or the far most left) cell(because it is going to hit the end and the start of the cell list), then it will handle that as well

  
(4 each side)

```
[0] [0] [23] [5] [8] [48] [65] [0] [10]   # (the value cell line)

     ^                                    # (the pointer line)
 
 1                                  9     # (the ranges line)
```
  
it does this so the amount of cells printed remains the same

## Examples
most of the examples provided are from Daniel B Cristofani
  * [his website](http://www.hevanet.com/cristofd/)
  * [his brainfuck page](http://brainfuck.org/)
  * [his git hub](https://github.com/danielcristofani)
  
## How To Use
I don't know how to install my code on someone's computer in a way that they can use the command line to use it, but it's not that bad after all.
after downloading(or cloning) the "main.py" file into your computer, and having python installed and your brainfuck code ready, you can type this command in your command line.

```
python main.py [file path or code(check Flags)] <args>
```

I have some examples ready for you if you don't have a brainfuck code.
after cloning into the project:
```
python main.py "examples/fib.b"
# prints the FibonaccI sequence
```
or you can say:
 ```
 python main.py ">>++++ ++[>++++ ++++ +++<-]>-." -i
 # prints "A"
  ```

## Speed

  I have tried to make this as fast as i can. i am not the best of programmers, but im pretty proud with its speed.
  the first version is one of the slowest things you can find on the internet. but the last version(v3.0 at the time) is pretty fast.
  its up to 306 times faster than the first version. and in some special tests, its the fastest thing i could find by far.
  
  if you use a real test(hanoi.b) i get the second spot with about 11 minutes to compile.
  
```
python main.py examples/hanoi.b
# takes around 11 minutes
```

## Flags
this interpreter doesn't have that many arguments 


* '-d' {value}           "dalay after each command"
* '-p'                   "output only the parsed version of the code"
* '-v' {amount}/nothing  "activates the visuals. you can enter a number after it so it shows n cells each side if you don't, the defullt is 5)"   
* '-a' {amount}          "how long do you want the cell aray to be?(how many cells)"
* '-i'                   "insted of interpreting the code in the filepath, interpret the code that is writen there(please check [How To Use](#how-to-use) for an example)"
  
## Special Features
I've added some extra features to this interpreter to help de-bugging programs. it's my code after all
note that these commands are made for you to use IN the code

### THESE FEAURES ARE ONLY AVALABLE IN THE FIRST VERSION
  
```
q    # you can just add this to anywhere in your code, and the program will stop running when it hits that point. this REALLY helps de-bugging HUGELY
"#"  # you can comment your code with this. everything after it will be ignored
```
  
# Future
it still has some problems, but I try to fix them all. exept that, here are some improvements I want to make:
  
  ### More Flags
  I don't have any plans now, but you can suggest!
