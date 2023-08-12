tests/ui/macros/issue-98466-allow.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(named_arguments_used_positionally)]

fn main() {
    let mut _x: usize;
    _x = 1;
    println!("_x is {}", _x = 5);
    println!("_x is {}", y = _x);
    println!("first positional arg {}, second positional arg {}, _x is {}", 1, 2, y = _x);

    let mut _x: usize;
    _x = 1;
    let _f = format!("_x is {}", _x = 5);
    let _f = format!("_x is {}", y = _x);
    let _f = format!("first positional arg {}, second positional arg {}, _x is {}", 1, 2, y = _x);
}


