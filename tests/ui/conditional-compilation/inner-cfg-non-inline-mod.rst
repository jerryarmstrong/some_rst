tests/ui/conditional-compilation/inner-cfg-non-inline-mod.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

mod module_with_cfg;

mod module_with_cfg {} // Ok, the module above is configured away by an inner attribute.

fn main() {}


