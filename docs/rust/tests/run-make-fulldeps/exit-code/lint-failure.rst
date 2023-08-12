tests/run-make-fulldeps/exit-code/lint-failure.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(broken_intra_doc_links)]

/// [intradoc::failure]
pub fn main() {
    println!("Hello, world!");
}


