tests/ui/parser/issue-87694-misplaced-pub.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const pub fn test() {}
//~^ ERROR expected one of `async`, `extern`, `fn`, or `unsafe`, found keyword `pub`
//~| NOTE expected one of `async`, `extern`, `fn`, or `unsafe`
//~| HELP visibility `pub` must come before `const`
//~| SUGGESTION pub const


