tests/ui/consts/const-big-enum.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

enum Foo {
    Bar(u32),
    Baz,
    Quux(u64, u16)
}

static X: Foo = Foo::Baz;

pub fn main() {
    match X {
        Foo::Baz => {}
        _ => panic!()
    }
    match Y {
        Foo::Bar(s) => assert_eq!(s, 2654435769),
        _ => panic!()
    }
    match Z {
        Foo::Quux(d,h) => {
            assert_eq!(d, 0x123456789abcdef0);
            assert_eq!(h, 0x1234);
        }
        _ => panic!()
    }
}

static Y: Foo = Foo::Bar(2654435769);
static Z: Foo = Foo::Quux(0x123456789abcdef0, 0x1234);


