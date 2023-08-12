src/tools/rustfmt/tests/source/issue-3253/paths/excluded.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This module is not imported in the cfg_if macro in lib.rs so it is ignored
// while the foo and bar mods are formatted.
// Check the corresponding file in tests/target/issue-3253/paths/excluded.rs
trait CoolerTypes { fn dummy(&self) {
}
}


