tests/ui/rfc-2565-param-attrs/param-attrs-2018.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

trait Trait2015 { fn foo(#[allow(C)] i32); }
//~^ ERROR expected one of `:`, `@`, or `|`, found `)`

fn main() {}


