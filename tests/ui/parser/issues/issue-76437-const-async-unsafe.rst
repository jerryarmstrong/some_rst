tests/ui/parser/issues/issue-76437-const-async-unsafe.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

mod t {
    const async unsafe pub fn t() {}
    //~^ ERROR expected one of `extern` or `fn`, found keyword `pub`
    //~| HELP visibility `pub` must come before `const async unsafe`
}


