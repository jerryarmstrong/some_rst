src/tools/clippy/tests/ui/struct_excessive_bools.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::struct_excessive_bools)]

macro_rules! foo {
    () => {
        struct MacroFoo {
            a: bool,
            b: bool,
            c: bool,
            d: bool,
        }
    };
}

foo!();

struct Foo {
    a: bool,
    b: bool,
    c: bool,
}

struct BadFoo {
    a: bool,
    b: bool,
    c: bool,
    d: bool,
}

#[repr(C)]
struct Bar {
    a: bool,
    b: bool,
    c: bool,
    d: bool,
}

fn main() {
    struct FooFoo {
        a: bool,
        b: bool,
        c: bool,
        d: bool,
    }
}


