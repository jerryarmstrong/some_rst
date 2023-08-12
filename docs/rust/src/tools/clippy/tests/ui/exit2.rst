src/tools/clippy/tests/ui/exit2.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[warn(clippy::exit)]

fn also_not_main() {
    std::process::exit(3);
}

fn main() {
    if true {
        std::process::exit(2);
    };
    also_not_main();
    std::process::exit(1);
}


