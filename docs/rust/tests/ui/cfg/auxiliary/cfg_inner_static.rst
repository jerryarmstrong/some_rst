tests/ui/cfg/auxiliary/cfg_inner_static.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // this used to just ICE on compiling
pub fn foo() {
    if cfg!(foo) {
        static a: isize = 3;
        a
    } else { 3 };
}


