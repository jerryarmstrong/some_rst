tests/ui/consts/promoted_const_call4.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::sync::atomic::*;

static FLAG: AtomicBool = AtomicBool::new(false);

struct NoisyDrop(&'static str);
impl Drop for NoisyDrop {
    fn drop(&mut self) {
        FLAG.store(true, Ordering::SeqCst);
    }
}
fn main() {
    {
        let _val = &&(NoisyDrop("drop!"), 0).1;
    }
    assert!(FLAG.load(Ordering::SeqCst));
}


