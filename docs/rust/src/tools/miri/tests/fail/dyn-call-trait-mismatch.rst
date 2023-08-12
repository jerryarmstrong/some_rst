src/tools/miri/tests/fail/dyn-call-trait-mismatch.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait T1 {
    fn method1(self: Box<Self>);
}
trait T2 {
    fn method2(self: Box<Self>);
}

impl T1 for i32 {
    fn method1(self: Box<Self>) {}
}

fn main() {
    let r = Box::new(0) as Box<dyn T1>;
    let r2: Box<dyn T2> = unsafe { std::mem::transmute(r) };
    r2.method2(); //~ERROR: call on a pointer whose vtable does not match its type
}


