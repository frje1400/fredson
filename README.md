# Fredson

## 1. Introduction

A JSON parsers in Python. Developed for educational purposes only in order to get a feel for how
a parser works. The parser passes an extensive test suite and should be fully compatible with Python's
built in JSON module (i.e. implementation defined behaviour should match 1:1). It's very slow however
due to being implemented in pure Python, and thus not suitable for production workloads.

## 2. What I learned

> The first 90 percent of the code accounts for the first 90 percent of the development time.
> The remaining 10 percent of the code accounts for the other 90 percent of the development time.
>
> Tom Cargill, Bell Labs

### 2.1 Using a Test Suite

My expectations going in to this project were that writing the overall tokenization and parsing logic
would be the majority of the work. This turned out to false. Instead, solving
various edge cases around unicode and error handling turned out to way more time-consuming.

I learned that having an extensive test suite is invaluable when implementing something like a JSON
parser that has both a standard (RFC 8259), and many previous implementations. When my parser was in
the state it passed the basic unit tests that I used during initial development, it was still in a very
rough state. That rough state just wasn't visible yet because I hadn't run the parser through a comprehensive
test suite. 

If I hadn't found the test suite (link) developed by Nicholas Seriot, developing a JSON parser
would have been very time consuming. I estimate that reading the specification and developing the tests
would have been more work than the actual implementation.

### 2.2 CPython Performance

I also learned a bit about CPython performance. The parser uses two phases: a tokenization step where the
input string is turned into tokens and then a separate parsing step. I found that the tokenization phase
was significantly slower than the actual parsing.

The key mistake I made in the first version of the tokenizer was to create a Python class that treated
the input string as a queue with a pop() method that advanced to the next character. The end result of this
was that I called the pop() method on this queue once for every character in the input stream. 

Profiling showed that these calls to pop() dominated the total time to parse. While performance was
linear, it was quite slow. Armed with this knowledge, I rewrote the tokenizer to work directly with a
Python string. This rewrite resulted in a 2x speedup, with the downside that the code now looked "lower level"
than with nicer queue abstractions.

However, one could argue that this 2x speedup was inconsequential since it's still roughly 100x slower
than the built-in JSON module. I learned that to get acceptable performance out of Python for this kind
of workload, I would need to use one of the many techniques for extending Python with native code, such
as C-extensions, Cython or Numba. 

Using PyPy instead of CPython lead to a 3x speedup on a 25 MB test file.

### 2.3 Reference Implementation

Having a reference implementation...












