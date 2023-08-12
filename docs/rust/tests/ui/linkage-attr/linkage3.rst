tests/ui/linkage-attr/linkage3.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // FIXME https://github.com/rust-lang/rust/issues/59774

// check-fail
// normalize-stderr-test "thread.*panicked.*Metadata module not compiled.*\n" -> ""
// normalize-stderr-test "note:.*RUST_BACKTRACE=1.*\n" -> ""

#![feature(linkage)]

extern "C" {
    #[linkage = "foo"]
    static foo: *const i32;
//~^ ERROR: invalid linkage specified
}

fn main() {
    println!("{:?}", unsafe { foo });
}


