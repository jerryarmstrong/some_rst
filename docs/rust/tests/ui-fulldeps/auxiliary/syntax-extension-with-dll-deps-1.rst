tests/ui-fulldeps/auxiliary/syntax-extension-with-dll-deps-1.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host

#![crate_type = "dylib"]

pub fn the_answer() -> isize {
    2
}


