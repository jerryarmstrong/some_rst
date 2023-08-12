tests/ui/suggestions/suggest-mut-method-for-loop.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::collections::HashMap;
struct X(usize);
struct Y {
    v: u32
}

fn main() {
    let mut buzz = HashMap::new();
    buzz.insert("a", Y { v: 0 });

    for mut t in buzz.values() {
                  //~^ HELP
                  //~| SUGGESTION values_mut()
        t.v += 1;
        //~^ ERROR cannot assign
    }
}


