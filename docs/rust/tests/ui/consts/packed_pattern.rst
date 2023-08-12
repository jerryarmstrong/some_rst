tests/ui/consts/packed_pattern.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#[derive(PartialEq, Eq, Copy, Clone)]
#[repr(packed)]
struct Foo {
    field: (i64, u32, u32, u32),
}

const FOO: Foo = Foo {
    field: (5, 6, 7, 8),
};

fn main() {
    match FOO {
        Foo { field: (5, 6, 7, 8) } => {},
        FOO => unreachable!(), //~ WARNING unreachable pattern
        _ => unreachable!(),
    }
}


