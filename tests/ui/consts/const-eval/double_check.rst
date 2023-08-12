tests/ui/consts/const-eval/double_check.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

enum Foo {
    A = 5,
    B = 42,
}
enum Bar {
    C = 42,
    D = 99,
}
#[repr(C)]
union Union {
    foo: &'static Foo,
    bar: &'static Bar,
    u8: &'static u8,
}
static BAR: u8 = 42;
static FOO: (&Foo, &Bar) = unsafe {(
    Union { u8: &BAR }.foo,
    Union { u8: &BAR }.bar,
)};

static FOO2: (&Foo, &Bar) = unsafe {(std::mem::transmute(&BAR), std::mem::transmute(&BAR))};

fn main() {}


