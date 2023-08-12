src/core/benches/any.rs
=======================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    use core::any::*;
use test::{black_box, Bencher};

#[bench]
fn bench_downcast_ref(b: &mut Bencher) {
    b.iter(|| {
        let mut x = 0;
        let mut y = &mut x as &mut dyn Any;
        black_box(&mut y);
        black_box(y.downcast_ref::<isize>() == Some(&0));
    });
}


