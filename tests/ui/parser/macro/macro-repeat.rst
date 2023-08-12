tests/ui/parser/macro/macro-repeat.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! mac {
    ( $($v:tt)* ) => {
        $v
        //~^ ERROR still repeating at this depth
        //~| ERROR still repeating at this depth
    };
}

fn main() {
    mac!(0);
    mac!(1);
}


