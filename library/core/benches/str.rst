library/core/benches/str.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::str;
use test::{black_box, Bencher};

mod char_count;
mod corpora;

#[bench]
fn str_validate_emoji(b: &mut Bencher) {
    b.iter(|| str::from_utf8(black_box(corpora::emoji::LARGE.as_bytes())));
}


