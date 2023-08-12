tests/ui/empty/no-link.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:empty-struct.rs

#[no_link]
extern crate empty_struct;

fn main() {
    empty_struct::XEmpty1 {};
}


