tests/ui/no-link-unknown-crate.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[no_link]
extern crate doesnt_exist; //~ ERROR can't find crate

fn main() {}


