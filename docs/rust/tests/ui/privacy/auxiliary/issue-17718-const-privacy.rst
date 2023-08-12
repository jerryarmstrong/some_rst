tests/ui/privacy/auxiliary/issue-17718-const-privacy.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub use foo::FOO2;

pub const FOO: usize = 3;
const BAR: usize = 3;

mod foo {
    pub const FOO2: usize = 3;
}


