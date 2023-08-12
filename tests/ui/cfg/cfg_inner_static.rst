tests/ui/cfg/cfg_inner_static.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:cfg_inner_static.rs

// pretty-expanded FIXME #23616

extern crate cfg_inner_static;

pub fn main() {
    cfg_inner_static::foo();
}


