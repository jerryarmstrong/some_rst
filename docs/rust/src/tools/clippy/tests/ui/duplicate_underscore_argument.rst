src/tools/clippy/tests/ui/duplicate_underscore_argument.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::duplicate_underscore_argument)]
#[allow(dead_code, unused)]

fn join_the_dark_side(darth: i32, _darth: i32) {}
fn join_the_light_side(knight: i32, _master: i32) {} // the Force is strong with this one

fn main() {
    join_the_dark_side(0, 0);
    join_the_light_side(0, 0);
}


