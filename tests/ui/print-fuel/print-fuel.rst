tests/ui/print-fuel/print-fuel.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name="foo"]
#![allow(dead_code)]

// (#55495: The --error-format is to sidestep an issue in our test harness)
// compile-flags: -C opt-level=0 --error-format human -Z print-fuel=foo
// check-pass

struct S1(u8, u16, u8);
struct S2(u8, u16, u8);
struct S3(u8, u16, u8);

fn main() {
}


