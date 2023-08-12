tests/ui/path.rs
================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

mod foo {
    pub fn bar(_offset: usize) { }
}

pub fn main() { foo::bar(0); }


