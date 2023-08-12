tests/rustdoc-ui/z-help.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Zhelp
// check-stdout
// regex-error-pattern: -Z\s+self-profile

pub struct Foo;


