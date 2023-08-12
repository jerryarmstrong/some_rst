src/tools/miri/test-cargo-miri/subcrate/src/lib.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg(doctest)]
compile_error!("rustdoc should not touch me");

#[cfg(test)]
compile_error!("Miri should not touch me");


