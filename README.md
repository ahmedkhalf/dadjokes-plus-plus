<p align="center">
  <img src="https://imgur.com/D5egC9o.png" width="600">
</p>

<p align="center">
  <sub>Image of dadjokes++ geting used in the terminal.</sub>
</p>

<br>

# Dadjokes++
Dad jokes on steroid.

## Installation

Make sure you have python and pip installed, then execute this in your terminal:

```bash
pip install dadjokes-plus-plus
```

## Usage


### From terminal

#### Fetch a random joke online
```bash
$ dadjokes
I used to be a banker, but I lost interest.
```

#### Download all jokes to jokes.txt
```bash
$ dadjokes -d "jokes.txt"
```

#### Load a random joke from jokes.txt
```bash
$ dadjokes -l "jokes.txt"
A steak pun is a rare medium well done.
```

*Note:* if you don't provide -d or -l a path it will automatically be "jokes.txt".

### From python

#### Fetch a random joke online
```python
import dadjokes
print(dadjoke.joke())
```

#### Download all jokes to jokes.txt
```python
import dadjokes
print(dadjoke.save_jokes("jokes.txt"))
```

#### Load a random joke from jokes.txt
```python
import dadjokes
print(dadjoke.joke("jokes.txt"))
```
