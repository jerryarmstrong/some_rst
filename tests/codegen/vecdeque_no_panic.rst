tests/codegen/vecdeque_no_panic.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test checks that `VecDeque::front[_mut]()` and `VecDeque::back[_mut]()` can't panic.

// compile-flags: -O
// ignore-debug: the debug assertions get in the way

#![crate_type = "lib"]

use std::collections::VecDeque;

// CHECK-LABEL: @dont_panic
#[no_mangle]
pub fn dont_panic(v: &mut VecDeque<usize>) {
    // CHECK-NOT: expect
    // CHECK-NOT: panic
    v.front();
    v.front_mut();
    v.back();
    v.back_mut();
}


