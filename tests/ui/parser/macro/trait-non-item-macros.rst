tests/ui/parser/macro/trait-non-item-macros.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! bah {
    ($a:expr) => {
        $a
    }; //~^ ERROR macro expansion ignores token `2` and any following
}

trait Bar {
    bah!(2);
}

fn main() {
    let _recovery_witness: () = 0; //~ ERROR mismatched types
}


