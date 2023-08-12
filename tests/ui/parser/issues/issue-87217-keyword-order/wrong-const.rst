tests/ui/parser/issues/issue-87217-keyword-order/wrong-const.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

// There is an order to respect for keywords before a function:
// `<visibility>, const, async, unsafe, extern, "<ABI>"`
//
// This test ensures the compiler is helpful about them being misplaced.
// Visibilities are tested elsewhere.

unsafe const fn test() {}
//~^ ERROR expected one of `extern` or `fn`, found keyword `const`
//~| NOTE expected one of `extern` or `fn`
//~| HELP `const` must come before `unsafe`
//~| SUGGESTION const unsafe
//~| NOTE keyword order for functions declaration is `pub`, `default`, `const`, `async`, `unsafe`, `extern`


