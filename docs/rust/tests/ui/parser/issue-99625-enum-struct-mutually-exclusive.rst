tests/ui/parser/issue-99625-enum-struct-mutually-exclusive.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

pub enum struct Range {
    //~^ ERROR `enum` and `struct` are mutually exclusive
    Valid {
        begin: u32,
        len: u32,
    },
    Out,
}

fn main() {
}


