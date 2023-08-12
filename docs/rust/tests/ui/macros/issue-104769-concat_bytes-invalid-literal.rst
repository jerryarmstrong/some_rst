tests/ui/macros/issue-104769-concat_bytes-invalid-literal.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(concat_bytes)]

fn main() {
    concat_bytes!(7Y);
    //~^ ERROR invalid suffix `Y` for number literal
    concat_bytes!(888888888888888888888888888888888888888);
    //~^ ERROR integer literal is too large
}


