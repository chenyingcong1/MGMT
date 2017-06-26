## jQuery Treemap
A (simple) jQuery plugin for generating treemaps.

Demonstrations and usage information: http://rexmac.com/jquery/treemap

## Installation
Include the CSS & JS:

    <link rel="stylesheet" type="text/css" href="css/jquery.treemap.css">
    <script src="js/dist/jquery.treemap.min.js"></script>

## Settings
The settings shown below are the defaults.

    {
        data: [],                      // Data array for treemap
        color: ['#f00', '#0f0'],       // Color extremes; low and high, respectively
        legend: false,                 // Legend is off by default
        legendLabels: ['Low', 'High'], // Labels used for legend
        legendPosition: 'bottom',      // Position of legend relative to treemap; may be 'top' or 'bottom'
        width: 500,                    // Width (in pixels)
        height: 300                    // Height (in pixels)
    }

### `data`
An array of JS objects containing labels and values for each node of the treemap.

Example:

    [
        {label: "Apple", value: 24},
        {label: "Papaya", value: 40},
        {label: "Mango", value: 13},
        {label: "Avocado", value: 2}
    ]

## Methods
Use the folloing syntax when calling methods:

<pre>$(<em>selector</em>).treemap('<em>method</em>', <em>[argument]</em>);</pre>

Where _selector_ is a valid jQuery selector, _method_ is the method name, and _argument_ is an argument to pass to the method (if any).

## `destroy`

Destroys the treemap for the given selector.

## Credits and Inspiration

This plugin was heavily inspired by and borrows a lot of code from [lrgalego](https://github.com/lrgalego)'s [jQuery Treemap plugin](https://github.com/lrgalego/jquery-treemap) and [Josh Nathanson](http://www.jnathanson.com/)'s [HeatColor plugin](http://www.jnathanson.com/blog/client/jquery/heatcolor/index.cfm).

## Licence (MIT)

Copyright (c) 2013 Rex McConnell (http://rexmac.com/)

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
