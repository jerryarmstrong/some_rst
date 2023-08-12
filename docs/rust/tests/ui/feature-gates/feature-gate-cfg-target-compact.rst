tests/ui/feature-gates/feature-gate-cfg-target-compact.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg(target(os = "x"))] //~ ERROR compact `cfg(target(..))` is experimental
struct Foo(u64, u64);

#[cfg_attr(target(os = "x"), x)] //~ ERROR compact `cfg(target(..))` is experimental
struct Bar(u64, u64);

#[cfg(not(any(all(target(os = "x")))))] //~ ERROR compact `cfg(target(..))` is experimental
fn foo() {}

fn main() {
    cfg!(target(os = "x"));
    //~^ ERROR compact `cfg(target(..))` is experimental and subject to change
}


