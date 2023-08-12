tests/ui/unsafe/issue-87414-query-cycle.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #87414.

// check-pass
// compile-flags: -Zthir-unsafeck

fn bad<T>() -> Box<dyn Iterator<Item = [(); { |x: u32| { x }; 4 }]>> { todo!() }

fn foo() -> [(); { |x: u32| { x }; 4 }] { todo!() }
fn bar() { let _: [(); { |x: u32| { x }; 4 }]; }

// This one should not cause any errors either:
unsafe fn unsf() {}
fn bad2<T>() -> Box<dyn Iterator<Item = [(); { unsafe { || { unsf() } }; 4 }]>> { todo!() }

fn main() {}


