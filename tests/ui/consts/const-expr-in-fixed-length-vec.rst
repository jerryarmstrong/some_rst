tests/ui/consts/const-expr-in-fixed-length-vec.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Check that constant expressions can be used for declaring the
// type of a fixed length vector.

// pretty-expanded FIXME #23616

pub fn main() {

    const FOO: usize = 2;
    let _v: [isize; FOO*3];

}


