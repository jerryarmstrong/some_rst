src/core/benches/ops.rs
=======================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    use core::ops::*;
use test::Bencher;

// Overhead of dtors

struct HasDtor {
    _x: isize,
}

impl Drop for HasDtor {
    fn drop(&mut self) {}
}

#[bench]
fn alloc_obj_with_dtor(b: &mut Bencher) {
    b.iter(|| {
        HasDtor { _x: 10 };
    })
}


