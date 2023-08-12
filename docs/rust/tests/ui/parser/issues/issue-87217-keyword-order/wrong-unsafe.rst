tests/ui/parser/issues/issue-87217-keyword-order/wrong-unsafe.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

// There is an order to respect for keywords before a function:
// `<visibility>, const, async, unsafe, extern, "<ABI>"`
//
// This test ensures the compiler is helpful about them being misplaced.
// Visibilities are tested elsewhere.

extern unsafe fn test() {}
//~^ ERROR expected `fn`, found keyword `unsafe`
//~| NOTE expected `fn`
//~| HELP `unsafe` must come before `extern`
//~| SUGGESTION unsafe extern
//~| NOTE keyword order for functions declaration is `pub`, `default`, `const`, `async`, `unsafe`, `extern`


