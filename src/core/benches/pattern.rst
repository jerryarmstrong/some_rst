src/core/benches/pattern.rs
===========================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    use test::black_box;
use test::Bencher;

#[bench]
fn starts_with_char(b: &mut Bencher) {
    let text = black_box("kdjsfhlakfhlsghlkvcnljknfqiunvcijqenwodind");
    b.iter(|| {
        for _ in 0..1024 {
            black_box(text.starts_with('k'));
        }
    })
}

#[bench]
fn starts_with_str(b: &mut Bencher) {
    let text = black_box("kdjsfhlakfhlsghlkvcnljknfqiunvcijqenwodind");
    b.iter(|| {
        for _ in 0..1024 {
            black_box(text.starts_with("k"));
        }
    })
}

#[bench]
fn ends_with_char(b: &mut Bencher) {
    let text = black_box("kdjsfhlakfhlsghlkvcnljknfqiunvcijqenwodind");
    b.iter(|| {
        for _ in 0..1024 {
            black_box(text.ends_with('k'));
        }
    })
}

#[bench]
fn ends_with_str(b: &mut Bencher) {
    let text = black_box("kdjsfhlakfhlsghlkvcnljknfqiunvcijqenwodind");
    b.iter(|| {
        for _ in 0..1024 {
            black_box(text.ends_with("k"));
        }
    })
}


