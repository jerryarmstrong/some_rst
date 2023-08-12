tests/ui/log-err-phi.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    if false {
        println!("{}", "foobar");
    }
}


