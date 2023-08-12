tests/ui/methods/method-argument-inference-associated-type.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub struct ClientMap;
pub struct ClientMap2;

pub trait Service {
    type Request;
    fn call(&self, _req: Self::Request);
}

pub struct S<T>(#[allow(unused_tuple_struct_fields)] T);

impl Service for ClientMap {
    type Request = S<Box<dyn Fn(i32)>>;
    fn call(&self, _req: Self::Request) {}
}


impl Service for ClientMap2 {
    type Request = (Box<dyn Fn(i32)>,);
    fn call(&self, _req: Self::Request) {}
}


fn main() {
    ClientMap.call(S { 0: Box::new(|_msgid| ()) });
    ClientMap.call(S(Box::new(|_msgid| ())));
    ClientMap2.call((Box::new(|_msgid| ()),));
}


