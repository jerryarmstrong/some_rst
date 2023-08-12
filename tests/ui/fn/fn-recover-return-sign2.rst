tests/ui/fn/fn-recover-return-sign2.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Separate test file because `Fn() => bool` isn't getting fixed and rustfix complained that
// even though a fix was applied the code was still incorrect

fn foo() => impl Fn() => bool {
    //~^ ERROR return types are denoted using `->`
    //~| ERROR expected one of `+`, `->`, `::`, `where`, or `{`, found `=>`
    unimplemented!()
}


