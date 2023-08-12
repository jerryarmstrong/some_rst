tests/ui/traits/bound/on-structs-and-enums-rpass.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(unused_variables)]
// pretty-expanded FIXME #23616

trait U {}
trait T<X: U> { fn get(self) -> X; }

trait S2<Y: U> {
    fn m(x: Box<dyn T<Y>+'static>) {}
}

struct St<X: U> {
    f: Box<dyn T<X>+'static>,
}

impl<X: U> St<X> {
    fn blah() {}
}

fn main() {}


