tests/ui/associated-consts/associated-const-type-parameters.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

trait Foo {
    const X: i32;
    fn get_x() -> i32 {
       Self::X
    }
}

struct Abc;
impl Foo for Abc {
    const X: i32 = 11;
}

struct Def;
impl Foo for Def {
    const X: i32 = 97;
}

struct Proxy<T>(#[allow(unused_tuple_struct_fields)] T);

impl<T: Foo> Foo for Proxy<T> {
    const X: i32 = T::X;
}

fn sub<A: Foo, B: Foo>() -> i32 {
    A::X - B::X
}

trait Bar: Foo {
    const Y: i32 = Self::X;
}

fn main() {
    assert_eq!(11, Abc::X);
    assert_eq!(97, Def::X);
    assert_eq!(11, Abc::get_x());
    assert_eq!(97, Def::get_x());
    assert_eq!(-86, sub::<Abc, Def>());
    assert_eq!(86, sub::<Def, Abc>());
    assert_eq!(-86, sub::<Proxy<Abc>, Def>());
    assert_eq!(-86, sub::<Abc, Proxy<Def>>());
    assert_eq!(86, sub::<Proxy<Def>, Proxy<Abc>>());
}


