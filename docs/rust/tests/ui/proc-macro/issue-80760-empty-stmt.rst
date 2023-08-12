tests/ui/proc-macro/issue-80760-empty-stmt.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:test-macros.rs
// compile-flags: -Z span-debug

#![no_std] // Don't load unnecessary hygiene information from std
extern crate std;

#[macro_use]
extern crate test_macros;

macro_rules! empty_stmt {
    ($s:stmt) => {
        print_bang!($s);

        // Currently, all attributes are ignored
        // on an empty statement
        #[print_attr]
        #[rustc_dummy(first)]
        #[rustc_dummy(second)]
        $s
    }
}

fn main() {
    empty_stmt!(;);
}


