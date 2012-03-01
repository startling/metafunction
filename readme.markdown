# metafunction

_metafunction_ is a higher-order function library for Python. Here's what we've got so far:

* function composition with `compose`
* `curry` and `uncurry`, for extracting arguments from tuples or lists or putting them into one
* `scanr`, `scanr1`, `scanl`, and `scanl1`, which are hard to explain unless you know Haskell...
* `foldr`, `foldr1`, `foldl`, and `foldl`, which are similar to Python 2.x's `reduce` but offer you more control.

If you're unsure about how something works, you can either look in the source (there are pretty extensive comments and docstrings), read the tests, or contact me.

Thanks for being interested!

## Installation

You can install straight from git using pip:

`pip install git+git://github.com/startling/metafunction.git`

or you can `git clone git://github.com/startling/metafunction.git` and `pip -e install metafunction` if you want to hack on it.

## License

Metafunction is released under the MIT License:

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
    of the Software, and to permit persons to whom the Software is furnished to do
    so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
