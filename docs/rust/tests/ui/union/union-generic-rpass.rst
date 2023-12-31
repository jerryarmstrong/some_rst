tests/ui/union/union-generic-rpass.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// revisions: mirunsafeck thirunsafeck
// [thirunsafeck]compile-flags: -Z thir-unsafeck

#![allow(dead_code)]

use std::mem::ManuallyDrop;

union MaybeItem<T: Iterator> {
    elem: ManuallyDrop<T::Item>,
    none: (),
}

union U<A, B> where A: Copy, B: Copy {
    a: A,
    b: B,
}

unsafe fn union_transmute<A, B>(a: A) -> B where A: Copy, B: Copy {
    U { a }.b
}

fn main() {
    unsafe {
        let b = union_transmute::<(u8, u8), u16>((1, 1));
        assert_eq!(b, (1 << 8) + 1);

        let v: Vec<u8> = vec![1, 2, 3];
        let mut i = v.iter();
        i.next();
        let mi = MaybeItem::<std::slice::Iter<_>> { elem: ManuallyDrop::new(i.next().unwrap()) };
        assert_eq!(**mi.elem, 2);
    }
}


