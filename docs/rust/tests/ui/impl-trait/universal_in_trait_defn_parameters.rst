tests/ui/impl-trait/universal_in_trait_defn_parameters.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::fmt::Debug;

trait InTraitDefnParameters {
    fn in_parameters(_: impl Debug) -> String;
}

impl InTraitDefnParameters for () {
    fn in_parameters(v: impl Debug) -> String {
        format!("() + {:?}", v)
    }
}

fn main() {
    let s = <() as InTraitDefnParameters>::in_parameters(22);
    assert_eq!(s, "() + 22");
}


