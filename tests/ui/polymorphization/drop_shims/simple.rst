tests/ui/polymorphization/drop_shims/simple.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags:-Zpolymorphize=on

pub struct OnDrop<F: Fn()>(pub F);

impl<F: Fn()> Drop for OnDrop<F> {
    fn drop(&mut self) { }
}

fn foo<R, S: FnOnce()>(
    _: R,
    _: S,
) {
    let bar = || {
        let _ = OnDrop(|| ());
    };
    let _ = bar();
}

fn main() {
    foo(3u32, || {});
}


