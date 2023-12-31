src/core/benches/fmt.rs
=======================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    use std::fmt::{self, Write as FmtWrite};
use std::io::{self, Write as IoWrite};
use test::Bencher;

#[bench]
fn write_vec_value(bh: &mut Bencher) {
    bh.iter(|| {
        let mut mem = Vec::new();
        for _ in 0..1000 {
            mem.write_all("abc".as_bytes()).unwrap();
        }
    });
}

#[bench]
fn write_vec_ref(bh: &mut Bencher) {
    bh.iter(|| {
        let mut mem = Vec::new();
        let wr = &mut mem as &mut dyn io::Write;
        for _ in 0..1000 {
            wr.write_all("abc".as_bytes()).unwrap();
        }
    });
}

#[bench]
fn write_vec_macro1(bh: &mut Bencher) {
    bh.iter(|| {
        let mut mem = Vec::new();
        let wr = &mut mem as &mut dyn io::Write;
        for _ in 0..1000 {
            write!(wr, "abc").unwrap();
        }
    });
}

#[bench]
fn write_vec_macro2(bh: &mut Bencher) {
    bh.iter(|| {
        let mut mem = Vec::new();
        let wr = &mut mem as &mut dyn io::Write;
        for _ in 0..1000 {
            write!(wr, "{}", "abc").unwrap();
        }
    });
}

#[bench]
fn write_vec_macro_debug(bh: &mut Bencher) {
    bh.iter(|| {
        let mut mem = Vec::new();
        let wr = &mut mem as &mut dyn io::Write;
        for _ in 0..1000 {
            write!(wr, "{:?}", "☃").unwrap();
        }
    });
}

#[bench]
fn write_str_value(bh: &mut Bencher) {
    bh.iter(|| {
        let mut mem = String::new();
        for _ in 0..1000 {
            mem.write_str("abc").unwrap();
        }
    });
}

#[bench]
fn write_str_ref(bh: &mut Bencher) {
    bh.iter(|| {
        let mut mem = String::new();
        let wr = &mut mem as &mut dyn fmt::Write;
        for _ in 0..1000 {
            wr.write_str("abc").unwrap();
        }
    });
}

#[bench]
fn write_str_macro1(bh: &mut Bencher) {
    bh.iter(|| {
        let mut mem = String::new();
        for _ in 0..1000 {
            write!(mem, "abc").unwrap();
        }
    });
}

#[bench]
fn write_str_macro2(bh: &mut Bencher) {
    bh.iter(|| {
        let mut mem = String::new();
        let wr = &mut mem as &mut dyn fmt::Write;
        for _ in 0..1000 {
            write!(wr, "{}", "abc").unwrap();
        }
    });
}

#[bench]
fn write_str_macro_debug(bh: &mut Bencher) {
    bh.iter(|| {
        let mut mem = String::new();
        let wr = &mut mem as &mut dyn fmt::Write;
        for _ in 0..1000 {
            write!(wr, "{:?}", "☃").unwrap();
        }
    });
}

#[bench]
fn write_u128_max(bh: &mut Bencher) {
    bh.iter(|| {
        std::hint::black_box(format!("{}", u128::MAX));
    });
}

#[bench]
fn write_u128_min(bh: &mut Bencher) {
    bh.iter(|| {
        let s = format!("{}", 0u128);
        std::hint::black_box(s);
    });
}

#[bench]
fn write_u64_max(bh: &mut Bencher) {
    bh.iter(|| {
        std::hint::black_box(format!("{}", u64::MAX));
    });
}

#[bench]
fn write_u64_min(bh: &mut Bencher) {
    bh.iter(|| {
        std::hint::black_box(format!("{}", 0u64));
    });
}


