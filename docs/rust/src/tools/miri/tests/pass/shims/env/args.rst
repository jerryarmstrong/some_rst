src/tools/miri/tests/pass/shims/env/args.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    for arg in std::env::args() {
        println!("{}", arg);
    }
}


