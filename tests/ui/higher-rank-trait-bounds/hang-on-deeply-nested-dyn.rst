tests/ui/higher-rank-trait-bounds/hang-on-deeply-nested-dyn.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // normalize-stderr-test: "long-type-\d+" -> "long-type-hash"

fn id(
    f: &dyn Fn(u32),
) -> &dyn Fn(
    &dyn Fn(
        &dyn Fn(
            &dyn Fn(&dyn Fn(&dyn Fn(&dyn Fn(&dyn Fn(&dyn Fn(&dyn Fn(&dyn Fn(&dyn Fn(u32))))))))),
        ),
    ),
) {
    f
    //~^ ERROR mismatched types
}

fn main() {}


