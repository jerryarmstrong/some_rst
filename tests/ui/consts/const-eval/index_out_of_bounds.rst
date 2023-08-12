tests/ui/consts/const-eval/index_out_of_bounds.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    static FOO: i32 = [][0];
//~^ ERROR E0080

fn main() {}


