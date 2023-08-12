src/tools/rustfmt/tests/source/break-and-continue.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // break and continue formatting

#![feature(loop_break_value)]

fn main() {
    'a: loop {
        break 'a;
    }

    let mut done = false;
    'b: while !done {
        done = true;
        continue 'b;
    }

    let x = loop {
        break 5;
    };

    let x = 'c: loop {
        break 'c 5;
    };
}


