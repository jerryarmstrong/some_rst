tests/rustdoc-js/prototype.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // The alias needed to be there to reproduce the bug
// that used to be here.
#[doc(alias="other_alias")]
pub fn something_else() {}


