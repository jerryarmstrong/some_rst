tests/ui/extern/auxiliary/reexport-should-still-link.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub use foo::bar;

mod foo {
    pub fn bar() {}
}


