tests/ui/feature-gates/feature-gate-link_cfg.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[link(name = "foo", cfg(foo))]
//~^ ERROR: is unstable
extern "C" {}

fn main() {}


