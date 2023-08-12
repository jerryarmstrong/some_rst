tests/rustdoc-ui/diagnostic-width.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --diagnostic-width=10
#![deny(rustdoc::bare_urls)]

/// This is a long line that contains a http://link.com
pub struct Foo; //~^ ERROR


