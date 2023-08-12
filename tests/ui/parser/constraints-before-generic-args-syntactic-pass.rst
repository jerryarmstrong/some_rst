tests/ui/parser/constraints-before-generic-args-syntactic-pass.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#[cfg(FALSE)]
fn syntax() {
    foo::<T = u8, T: Ord, String>();
    //~^ WARN associated type bounds are unstable
    //~| WARN unstable syntax
    foo::<T = u8, 'a, T: Ord>();
    //~^ WARN associated type bounds are unstable
    //~| WARN unstable syntax
}

fn main() {}


