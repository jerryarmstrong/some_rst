src/tools/clippy/tests/ui/toplevel_ref_arg_non_rustfix.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:macro_rules.rs

#![warn(clippy::toplevel_ref_arg)]
#![allow(unused)]

#[macro_use]
extern crate macro_rules;

fn the_answer(ref mut x: u8) {
    *x = 42;
}

macro_rules! gen_function {
    () => {
        fn fun_example(ref _x: usize) {}
    };
}

fn main() {
    let mut x = 0;
    the_answer(x);

    // lint in macro
    #[allow(unused)]
    {
        gen_function!();
    }

    // do not lint in external macro
    {
        ref_arg_function!();
    }
}


