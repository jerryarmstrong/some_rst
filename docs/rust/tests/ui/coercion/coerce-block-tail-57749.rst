tests/ui/coercion/coerce-block-tail-57749.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail
use std::ops::Deref;

fn main() {
    fn save(who: &str) {
        println!("I'll save you, {}!", who);
    }

    struct Madoka;

    impl Deref for Madoka {
        type Target = str;
        fn deref(&self) -> &Self::Target {
            "Madoka"
        }
    }

    save(&{ Madoka });

    fn reset(how: &u32) {
        println!("Reset {} times", how);
    }

    struct Homura;

    impl Deref for Homura {
        type Target = u32;
        fn deref(&self) -> &Self::Target {
            &42
        }
    }

    reset(&{ Homura });
    //~^ ERROR mismatched types
}


