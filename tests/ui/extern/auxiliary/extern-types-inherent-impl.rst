tests/ui/extern/auxiliary/extern-types-inherent-impl.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(extern_types)]

extern "C" {
    pub type CrossCrate;
}

impl CrossCrate {
    pub fn foo(&self) {}
}


