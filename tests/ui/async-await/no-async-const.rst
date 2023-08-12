tests/ui/async-await/no-async-const.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// compile-flags: --crate-type lib

pub async const fn x() {}
//~^ ERROR expected one of `extern`, `fn`, or `unsafe`, found keyword `const`


