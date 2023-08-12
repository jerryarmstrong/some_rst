tests/ui/deprecation/deprecated-macro_escape-inner.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

mod foo {
    #![macro_escape] //~ WARN `#[macro_escape]` is a deprecated synonym for `#[macro_use]`
}

fn main() {
}


