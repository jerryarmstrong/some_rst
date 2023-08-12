tests/ui/traits/alias/style_lint.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(trait_alias)]

trait Foo = std::fmt::Display + std::fmt::Debug;
trait bar = std::fmt::Display + std::fmt::Debug; //~WARN trait alias `bar` should have an upper camel case name

fn main() {}


