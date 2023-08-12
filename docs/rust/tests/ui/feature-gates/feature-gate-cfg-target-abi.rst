tests/ui/feature-gates/feature-gate-cfg-target-abi.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg(target_abi = "x")] //~ ERROR `cfg(target_abi)` is experimental
struct Foo(u64, u64);

#[cfg_attr(target_abi = "x", x)] //~ ERROR `cfg(target_abi)` is experimental
struct Bar(u64, u64);

#[cfg(not(any(all(target_abi = "x"))))] //~ ERROR `cfg(target_abi)` is experimental
fn foo() {}

fn main() {
    cfg!(target_abi = "x");
    //~^ ERROR `cfg(target_abi)` is experimental and subject to change
}


