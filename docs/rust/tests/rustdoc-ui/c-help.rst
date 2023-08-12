tests/rustdoc-ui/c-help.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Chelp
// check-stdout
// regex-error-pattern: -C\s+incremental

pub struct Foo;


