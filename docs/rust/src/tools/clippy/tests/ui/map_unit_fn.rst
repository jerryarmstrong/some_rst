src/tools/clippy/tests/ui/map_unit_fn.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused)]
struct Mappable;

impl Mappable {
    pub fn map(&self) {}
}

fn main() {
    let m = Mappable {};
    m.map();
}


