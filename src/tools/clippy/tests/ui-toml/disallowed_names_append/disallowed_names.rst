src/tools/clippy/tests/ui-toml/disallowed_names_append/disallowed_names.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[warn(clippy::disallowed_names)]

fn main() {
    // `foo` is part of the default configuration
    let foo = "bar";
    // `ducks` was unrightfully disallowed
    let ducks = ["quack", "quack"];
    // `fox` is okay
    let fox = ["what", "does", "the", "fox", "say", "?"];
}


