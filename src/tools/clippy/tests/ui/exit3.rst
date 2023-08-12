src/tools/clippy/tests/ui/exit3.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[warn(clippy::exit)]

fn main() {
    if true {
        std::process::exit(2);
    };
    std::process::exit(1);
}


