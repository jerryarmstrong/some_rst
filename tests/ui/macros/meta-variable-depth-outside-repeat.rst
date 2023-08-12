tests/ui/macros/meta-variable-depth-outside-repeat.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(macro_metavar_expr)]

macro_rules! metavar {
    ( $i:expr ) => {
        ${length(0)}
        //~^ ERROR meta-variable expression `length` with depth parameter must be called inside of a macro repetition
    };
}

const _: i32 = metavar!(0);

fn main() {}


