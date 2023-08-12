tests/ui/resolve/use_suggestion.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x1 = HashMap::new(); //~ ERROR failed to resolve
    let x2 = GooMap::new(); //~ ERROR failed to resolve

    let y1: HashMap; //~ ERROR cannot find type
    let y2: GooMap; //~ ERROR cannot find type
}


