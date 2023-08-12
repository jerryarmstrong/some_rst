tests/ui/typeck/assign-non-lval-derefmut.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    let x = std::sync::Mutex::new(1usize);
    x.lock().unwrap() = 2;
    //~^ ERROR invalid left-hand side of assignment
    x.lock().unwrap() += 1;
    //~^ ERROR binary assignment operation `+=` cannot be applied to type `MutexGuard<'_, usize>`

    let mut y = x.lock().unwrap();
    y = 2;
    //~^ ERROR mismatched types
    y += 1;
    //~^ ERROR binary assignment operation `+=` cannot be applied to type `MutexGuard<'_, usize>`
}


