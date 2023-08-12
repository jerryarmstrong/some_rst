src/tools/clippy/tests/ui/crate_level_checks/entrypoint_recursion.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-macos

#![feature(rustc_attrs)]

#[warn(clippy::main_recursion)]
#[allow(unconditional_recursion)]
#[rustc_main]
fn a() {
    println!("Hello, World!");
    a();
}


