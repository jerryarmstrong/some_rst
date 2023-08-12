tests/ui/issues/issue-68696-catch-during-unwind.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Checks that catch_unwind can be used if unwinding is already in progress.
// Used to fail when standard library had been compiled with debug assertions,
// due to incorrect assumption that a current thread is not panicking when
// entering the catch_unwind.
//
// run-pass

use std::panic::catch_unwind;

#[derive(Default)]
struct Guard;

impl Drop for Guard {
    fn drop(&mut self) {
        let _ = catch_unwind(|| {});
    }
}

fn main() {
    #[cfg(panic = "unwind")]
    let _ = catch_unwind(|| {
        let _guard = Guard::default();
        panic!();
    });
}


