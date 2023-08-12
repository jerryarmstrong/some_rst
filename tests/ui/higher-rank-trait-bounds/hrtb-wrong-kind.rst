tests/ui/higher-rank-trait-bounds/hrtb-wrong-kind.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn a() where for<T> T: Copy {}
//~^ ERROR only lifetime parameters can be used in this context

fn b() where for<const C: usize> [(); C]: Copy {}
//~^ ERROR only lifetime parameters can be used in this context

fn main() {}


