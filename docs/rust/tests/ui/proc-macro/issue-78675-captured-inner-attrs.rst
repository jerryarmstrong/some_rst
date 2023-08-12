tests/ui/proc-macro/issue-78675-captured-inner-attrs.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2018
// compile-flags: -Z span-debug
// aux-build:test-macros.rs

#![no_std] // Don't load unnecessary hygiene information from std
extern crate std;

#[macro_use] extern crate test_macros;

macro_rules! foo {(
    #[fake_attr]
    $item:item
) => (
    $item
)}

macro_rules! outer {($item:item) => (
    print_bang! { // Identity proc-macro
        foo! {
            #[fake_attr]
            $item
        }
    }
)}
outer! {
    mod bar {
        //! Foo
    }
}

fn main() {}


