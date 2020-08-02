<p align="center">
  <img src="https://imgur.com/D5egC9o.png" width="600">
</p>

<p align="center">
  <sub>Image of dadjokes++ geting used on terminal startup.</sub>
</p>

<br>

<p align="center">
  <a href="https://github.com/ahmedkhalf/dadjokes-plus-plus/network/members">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/ahmedkhalf/dadjokes-plus-plus">
  </a>
  <a href="https://github.com/ahmedkhalf/dadjokes-plus-plus/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/ahmedkhalf/dadjokes-plus-plus">
  </a>
  <a href="https://github.com/ahmedkhalf/dadjokes-plus-plus/watchers">
    <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/ahmedkhalf/dadjokes-plus-plus">
  </a>
</p>

<p align="center">
  <a href="https://pepy.tech/project/dadjokes-plus-plus">
    <img src="https://pepy.tech/badge/dadjokes-plus-plus" alt="Downloads">
  </a>
  <a href="https://pepy.tech/project/dadjokes-plus-plus/month">
    <img src="https://pepy.tech/badge/dadjokes-plus-plus/month" alt="Downloads/Month">
  </a>
  <a href="https://pepy.tech/project/dadjokes-plus-plus/week">
    <img src="https://pepy.tech/badge/dadjokes-plus-plus/week" alt="Downloads/Week">
  </a>
</p>

<br>

# Dadjokes++
Dad jokes on steroid.

Fetch jokes from icanhazdadjoke. Unlike other alternatives, dadjokes++ can download all jokes to your computer for faster and offline retrieval.

## Installation

Make sure you have python 3 and pip installed, then execute this in your terminal:

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
