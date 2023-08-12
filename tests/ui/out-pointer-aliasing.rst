tests/ui/out-pointer-aliasing.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#[derive(Copy, Clone)]
pub struct Foo {
    f1: isize,
    _f2: isize,
}

#[inline(never)]
pub fn foo(f: &mut Foo) -> Foo {
    let ret = *f;
    f.f1 = 0;
    ret
}

pub fn main() {
    let mut f = Foo {
        f1: 8,
        _f2: 9,
    };
    f = foo(&mut f);
    assert_eq!(f.f1, 8);
}


