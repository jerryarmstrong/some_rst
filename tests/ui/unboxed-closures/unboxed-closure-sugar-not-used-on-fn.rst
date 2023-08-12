tests/ui/unboxed-closures/unboxed-closure-sugar-not-used-on-fn.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the `Fn` traits require `()` form without a feature gate.

fn bar1(x: &dyn Fn<(), Output=()>) {
    //~^ ERROR of `Fn`-family traits' type parameters is subject to change
}

fn bar2<T>(x: &T) where T: Fn<()> {
    //~^ ERROR of `Fn`-family traits' type parameters is subject to change
}

fn main() { }


