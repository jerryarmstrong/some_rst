tests/ui/moves/move-in-guard-1.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn main() {


    let x: Box<_> = Box::new(1);

    let v = (1, 2);

    match v {
        (1, _) if take(x) => (),
        (_, 2) if take(x) => (), //~ ERROR use of moved value: `x`
        _ => (),
    }
}

fn take<T>(_: T) -> bool { false }


