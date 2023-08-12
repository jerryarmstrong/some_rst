tests/ui/parser/issue-87694-duplicated-pub.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub const pub fn test() {}
//~^ ERROR expected one of `async`, `extern`, `fn`, or `unsafe`, found keyword `pub`
//~| NOTE expected one of `async`, `extern`, `fn`, or `unsafe`
//~| HELP there is already a visibility modifier, remove one
//~| NOTE explicit visibility first seen here


