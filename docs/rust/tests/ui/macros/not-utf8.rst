tests/ui/macros/not-utf8.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: did not contain valid UTF-8

fn foo() {
    include!("not-utf8.bin")
}


