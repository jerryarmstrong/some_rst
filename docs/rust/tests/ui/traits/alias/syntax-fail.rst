tests/ui/traits/alias/syntax-fail.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(trait_alias)]

trait Foo {}
auto trait A = Foo; //~ ERROR trait aliases cannot be `auto`
unsafe trait B = Foo; //~ ERROR trait aliases cannot be `unsafe`

trait C: Ord = Eq; //~ ERROR bounds are not allowed on trait aliases
trait D: = Eq; //~ ERROR bounds are not allowed on trait aliases

fn main() {}


