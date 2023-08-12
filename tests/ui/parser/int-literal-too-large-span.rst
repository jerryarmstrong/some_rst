tests/ui/parser/int-literal-too-large-span.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // issue #17123

fn main() {
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    //~^ ERROR integer literal is too large
        ; // the span shouldn't point to this.
}


