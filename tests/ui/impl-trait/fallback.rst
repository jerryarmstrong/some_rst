tests/ui/impl-trait/fallback.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn take_edge_counters(
    x: &mut Option<Vec<i32>>,
) -> Option<impl Iterator<Item = i32>> {
    x.take().map_or(None, |m| Some(m.into_iter()))
}

fn main() {}


