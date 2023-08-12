tests/ui/conditional-compilation/test-cfg.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --cfg foo

#[cfg(all(foo, bar))] // foo AND bar
fn foo() {}

fn main() {
    foo(); //~ ERROR cannot find function `foo` in this scope
}


