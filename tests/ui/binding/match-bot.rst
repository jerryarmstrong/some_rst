tests/ui/binding/match-bot.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let i: isize =
        match Some::<isize>(3) { None::<isize> => { panic!() } Some::<isize>(_) => { 5 } };
    println!("{}", i);
}


