library/core/benches/ops.rs
===========================

Last edited: 2023-03-30 20:35:59

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


