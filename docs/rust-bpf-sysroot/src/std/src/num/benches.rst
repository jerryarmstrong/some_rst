src/std/src/num/benches.rs
==========================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    use test::Bencher;

#[bench]
fn bench_pow_function(b: &mut Bencher) {
    let v = (0..1024).collect::<Vec<u32>>();
    b.iter(|| {
        v.iter().fold(0u32, |old, new| old.pow(*new as u32));
    });
}


