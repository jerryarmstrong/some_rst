src/tools/rustfmt/tests/mod-resolver/module-not-found/bad_path_attribute/lib.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // module resolution fails because the path does not exist.
#[path = "path/to/does_not_exist.rs"]
mod a;


