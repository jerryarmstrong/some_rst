tests/ui/auto-traits/auto-trait-validation.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(auto_traits)]

// run-rustfix

auto trait Generic<T> {}
//~^ auto traits cannot have generic parameters [E0567]
auto trait Bound : Copy {}
//~^ auto traits cannot have super traits or lifetime bounds [E0568]
auto trait LifetimeBound : 'static {}
//~^ auto traits cannot have super traits or lifetime bounds [E0568]
auto trait MyTrait { fn foo() {} }
//~^ auto traits cannot have associated items [E0380]
fn main() {}


