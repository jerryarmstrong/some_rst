library/std/src/io/impls/tests.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::io::prelude::*;

#[bench]
fn bench_read_slice(b: &mut test::Bencher) {
    let buf = [5; 1024];
    let mut dst = [0; 128];

    b.iter(|| {
        let mut rd = &buf[..];
        for _ in 0..8 {
            let _ = rd.read(&mut dst);
            test::black_box(&dst);
        }
    })
}

#[bench]
fn bench_write_slice(b: &mut test::Bencher) {
    let mut buf = [0; 1024];
    let src = [5; 128];

    b.iter(|| {
        let mut wr = &mut buf[..];
        for _ in 0..8 {
            let _ = wr.write_all(&src);
            test::black_box(&wr);
        }
    })
}

#[bench]
fn bench_read_vec(b: &mut test::Bencher) {
    let buf = vec![5; 1024];
    let mut dst = [0; 128];

    b.iter(|| {
        let mut rd = &buf[..];
        for _ in 0..8 {
            let _ = rd.read(&mut dst);
            test::black_box(&dst);
        }
    })
}

#[bench]
fn bench_write_vec(b: &mut test::Bencher) {
    let mut buf = Vec::with_capacity(1024);
    let src = [5; 128];

    b.iter(|| {
        let mut wr = &mut buf[..];
        for _ in 0..8 {
            let _ = wr.write_all(&src);
            test::black_box(&wr);
        }
    })
}


