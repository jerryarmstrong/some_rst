src/tools/rustfmt/tests/target/inner-module-path/lib.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[path = "."]
mod a {
    mod b;
}

mod c {
    mod d;
}


