tests/rustdoc/generic_const_exprs.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for <https://github.com/rust-lang/rust/issues/92859>.

#![allow(incomplete_features)]
#![feature(generic_const_exprs)]

#![crate_name = "foo"]

// @has 'foo/trait.Foo.html'

pub trait Foo: Sized {
    const WIDTH: usize;

    fn arrayify(self) -> [Self; Self::WIDTH];
}

impl<T: Sized> Foo for T {
    const WIDTH: usize = 1;

    // @has - '//*[@id="tymethod.arrayify"]/*[@class="code-header"]' \
    // 'fn arrayify(self) -> [Self; Self::WIDTH]'
    fn arrayify(self) -> [Self; Self::WIDTH] {
        [self]
    }
}


