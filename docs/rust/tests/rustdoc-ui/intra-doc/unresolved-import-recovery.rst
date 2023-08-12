tests/rustdoc-ui/intra-doc/unresolved-import-recovery.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #95879.

use unresolved_crate::module::Name; //~ ERROR failed to resolve

/// [Name]
pub struct S;


