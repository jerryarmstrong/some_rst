src/tools/clippy/tests/ui/crate_level_checks/std_main_recursion.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[warn(clippy::main_recursion)]
#[allow(unconditional_recursion)]
fn main() {
    println!("Hello, World!");
    main();
}


