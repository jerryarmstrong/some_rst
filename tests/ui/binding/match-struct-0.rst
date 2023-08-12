tests/ui/binding/match-struct-0.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct Foo{
    f : isize,
}

pub fn main() {
    let f = Foo{f: 1};
    match f {
        Foo{f: 0} => panic!(),
        Foo{..} => (),
    }
    match f {
        Foo{f: 0} => panic!(),
        Foo{f: _f} => (),
    }
    match f {
        Foo{f: 0} => panic!(),
        _ => (),
    }
}


