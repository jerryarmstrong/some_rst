tests/ui/resolve/blind-item-mixed-use-item.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

mod m {
    pub fn f<T>(_: T, _: ()) { }
    pub fn g<T>(_: T, _: ()) { }
}

const BAR: () = ();
struct Data;
use m::f;

fn main() {
    const BAR2: () = ();
    struct Data2;
    use m::g;

    f(Data, BAR);
    g(Data2, BAR2);
}


