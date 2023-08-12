tests/ui/extern/auxiliary/extern_calling_convention.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure Rust generates the correct calling convention for extern
// functions.

#[inline(never)]
#[cfg(target_arch = "x86_64")]
pub extern "win64" fn foo(a: isize, b: isize, c: isize, d: isize) {
    assert_eq!(a, 1);
    assert_eq!(b, 2);
    assert_eq!(c, 3);
    assert_eq!(d, 4);

    println!("a: {}, b: {}, c: {}, d: {}",
             a, b, c, d)
}

#[inline(never)]
#[cfg(not(target_arch = "x86_64"))]
pub extern "C" fn foo(a: isize, b: isize, c: isize, d: isize) {
    assert_eq!(a, 1);
    assert_eq!(b, 2);
    assert_eq!(c, 3);
    assert_eq!(d, 4);

    println!("a: {}, b: {}, c: {}, d: {}",
             a, b, c, d)
}


