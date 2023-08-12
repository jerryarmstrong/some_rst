tests/ui/parser/issues/issue-87217-keyword-order/const-async-const.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

// Test that even when `const` is already present, the proposed fix is to remove the second `const`

const async const fn test() {}
//~^ ERROR expected one of `extern`, `fn`, or `unsafe`, found keyword `const`
//~| NOTE expected one of `extern`, `fn`, or `unsafe`
//~| HELP `const` already used earlier, remove this one
//~| NOTE `const` first seen here


