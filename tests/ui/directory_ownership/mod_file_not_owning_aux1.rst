tests/ui/directory_ownership/mod_file_not_owning_aux1.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-test this is not a test

macro_rules! m {
    () => { mod mod_file_not_owning_aux2; }
}
m!();


