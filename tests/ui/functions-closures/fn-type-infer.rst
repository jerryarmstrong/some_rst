tests/ui/functions-closures/fn-type-infer.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

#![allow(unused_variables)]

pub fn main() {
    // We should be able to type infer inside of ||s.
    let _f = || {
        let i = 10;
    };
}


