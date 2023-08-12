tests/ui/consts/const-vec-syntax.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

fn f(_: &[isize]) {}

pub fn main() {
    let v = [ 1, 2, 3 ];
    f(&v);
}


