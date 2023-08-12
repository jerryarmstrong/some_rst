tests/ui/drop/drop-on-empty-block-exit.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616
#![allow(non_camel_case_types)]

enum t { foo(Box<isize>), }

pub fn main() {
    let tt = t::foo(Box::new(10));
    match tt { t::foo(_z) => { } }
}


