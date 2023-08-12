tests/ui/lint/lint-match-arms.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn deny_on_arm() {
    match 0 {
        #[deny(unused_variables)]
        //~^ NOTE the lint level is defined here
        y => (),
        //~^ ERROR unused variable
    }
}

#[deny(unused_variables)]
fn allow_on_arm() {
    match 0 {
        #[allow(unused_variables)]
        y => (), // OK
    }
}

fn main() {}


