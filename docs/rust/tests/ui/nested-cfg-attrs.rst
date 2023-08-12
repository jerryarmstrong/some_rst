tests/ui/nested-cfg-attrs.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg_attr(all(), cfg_attr(all(), cfg(foo)))]
fn f() {}

fn main() { f() } //~ ERROR cannot find function `f` in this scope


