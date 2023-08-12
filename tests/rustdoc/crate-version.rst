tests/rustdoc/crate-version.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-version=1.3.37

// @has 'crate_version/index.html' '//*[@class="version"]' 'Version 1.3.37'


