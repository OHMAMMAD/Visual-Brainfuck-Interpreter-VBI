# Visual-Brainfuck-Interpreter-VBI
an attempt to make an optimized interpreter for the brainfuck programming language. purely in python
made to help debugging brainfuck code 

## About BrainFuck:
An esoteric programing language built by urban miller in the 1990s.


brainfuck:
* [esolangs.org](https://esolangs.org/wiki/Brainfuck)
* [wikipedia](https://en.wikipedia.org/wiki/Brainfuck)


for more information and simpler explanation about brainfuck, i recommend:
* [How Brainfuck Works](https://www.youtube.com/watch?v=-3C200nCwpk)


## How Debuging Works:
this program was made with a visualization feature to help debugging code better

you can activate it with '-v' argument. go to [Flags](#flags) for explanation


### example:
```
``
python main.py [filepath] -v
``
```


(4 each side)
  
``` 
[0] [0] [23] [5] [8] [48] [65] [0] [10]   # (the value cell line)

                  ^                       # (the pointer line)

3                                   11    # (the ranges line)
```

it shows the pointer dynamicly, the pointer location changes in the screen based on the available cells in each direction



(4 each side)

```
[0] [0] [23] [5] [8] [48] [65] [0] [10]   # (the value cell line)

     ^                                    # (the pointer line)
 
 1                                  9     # (the ranges line)
```
  
it does this so the amount of cells printed remains the same

## Brainfuck Code Examples
most of the examples provided are from @danielcristofani
  * [his website](http://www.hevanet.com/cristofd/)
  * [his brainfuck page](http://brainfuck.org/)
  * [his github](https://github.com/danielcristofani)
  
## How To Use

after cloning the repository, run the main file and provide a valid brainfuck file path.

```
python main.py [file path] <args>
```

you can use the examples provided in the repo:
```
python main.py "examples/fib.b"
# prints the FibonaccI sequence
```

you can also use the file argument to write brainfuck code directly.
remmeber to use '-i' at the end of your command 

```
 python main.py ">>++++ ++[>++++ ++++ +++<-]>-." -i
 # prints "A"
  ```

## Speed

i tried to make this interpreter as fast as possible, optimizing the algotithm multiple times, getting inspiration from other top speed interpreters and finding faster ways to organize and use data.

the code can still use lots of inprovements, but so far, the v3.0 is oparating 300 times faster than the first version.


```
python main.py examples/hanoi.b
# takes around 11 minutes
```

## Flags
this interpreter doesn't have that many arguments 

```
* '-d' {value}           // dalay after each command
* '-p'                   // output parsed version only
* '-v' {amount}/nothing  // activate visualization for debugging, a number can be provided after argument to be used as the amount of cells rendered each side of the pointer, if not, default is 5

* '-a' {amount}          // changes the amount of memmory locations(cells) available
* '-i'                   // interpret the code directly from terminal
```

## Special Features
experimental features to help debug code

### note: these are only available in v1.0, and are not real brainfuck code.

```
q    // halt the program when reached
"#"  // used to comment code, anything after it will be ignored
```

