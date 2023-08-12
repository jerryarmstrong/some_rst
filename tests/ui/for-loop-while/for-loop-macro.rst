tests/ui/for-loop-while/for-loop-macro.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
macro_rules! var {
    ( $name:ident ) => ( $name );
}

pub fn main() {
    let x = [ 3, 3, 3 ];
    for var!(i) in &x {
        assert_eq!(*i, 3);
    }
}


