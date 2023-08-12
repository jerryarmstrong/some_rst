tests/ui/rfc-2306/convert-id-const-with-gate.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test should pass since 'identity' is const fn.

// build-pass (FIXME(62277): could be check-pass?)

fn main() {
    const _FOO: u8 = ::std::convert::identity(42u8);
}


