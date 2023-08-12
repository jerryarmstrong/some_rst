tests/ui/borrowck/borrowck-lend-flow-match.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn separate_arms() {
    // Here both arms perform assignments, but only one is illegal.

    let mut x = None;
    match x {
        None => {
            // It is ok to reassign x here, because there is in
            // fact no outstanding loan of x!
            x = Some(0);
        }
        Some(ref r) => {
            x = Some(1); //~ ERROR cannot assign to `x` because it is borrowed
            drop(r);
        }
    }
}

fn main() {}


