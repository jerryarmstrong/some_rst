src/tools/rustfmt/tests/target/fn_once.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Add(usize);

impl FnOnce<(usize,)> for Add {
    type Output = Add;
    extern "rust-call" fn call_once(self, to: (usize,)) -> Add {
        Add(self.0 + to.0)
    }
}


