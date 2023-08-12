tests/ui/macros/recovery-forbidden.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

macro_rules! dont_recover_here {
    ($e:expr) => {
        compile_error!("Must not recover to single !1 expr");
    };

    (not $a:literal) => {};
}

dont_recover_here! { not 1 }

fn main() {}


