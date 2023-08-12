tests/ui/parser/issues/issue-76437-const.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

mod t {
    const pub fn t() {}
    //~^ ERROR expected one of `async`, `extern`, `fn`, or `unsafe`, found keyword `pub`
    //~| HELP visibility `pub` must come before `const`
}


