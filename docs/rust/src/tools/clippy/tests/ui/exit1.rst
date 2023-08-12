src/tools/clippy/tests/ui/exit1.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[warn(clippy::exit)]

fn not_main() {
    if true {
        std::process::exit(4);
    }
}

fn main() {
    if true {
        std::process::exit(2);
    };
    not_main();
    std::process::exit(1);
}


