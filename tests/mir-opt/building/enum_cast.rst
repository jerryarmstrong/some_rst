tests/mir-opt/building/enum_cast.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // EMIT_MIR enum_cast.foo.built.after.mir
// EMIT_MIR enum_cast.bar.built.after.mir
// EMIT_MIR enum_cast.boo.built.after.mir

enum Foo {
    A
}

enum Bar {
    A, B
}

#[repr(u8)]
enum Boo {
    A, B
}

fn foo(foo: Foo) -> usize {
    foo as usize
}

fn bar(bar: Bar) -> usize {
    bar as usize
}

fn boo(boo: Boo) -> usize {
    boo as usize
}

// EMIT_MIR enum_cast.droppy.built.after.mir
enum Droppy {
    A, B, C
}

impl Drop for Droppy {
    fn drop(&mut self) {}
}

fn droppy() {
    {
        let x = Droppy::C;
        // remove this entire test once `cenum_impl_drop_cast` becomes a hard error
        #[allow(cenum_impl_drop_cast)]
        let y = x as usize;
    }
    let z = Droppy::B;
}

fn main() {
}


