tests/ui/consts/const-expr-in-vec-repeat.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Check that constant expressions can be used in vec repeat syntax.

// pretty-expanded FIXME #23616

pub fn main() {

    const FOO: usize = 2;
    let _v = [0; FOO*3*2/2];

}


