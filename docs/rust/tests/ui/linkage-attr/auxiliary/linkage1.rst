tests/ui/linkage-attr/auxiliary/linkage1.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[no_mangle]
pub static foo: isize = 3;

pub fn bar() {}


