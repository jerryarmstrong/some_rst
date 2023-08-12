tests/ui/expr/if-bot.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let i: isize = if false { panic!() } else { 5 };
    println!("{}", i);
}


