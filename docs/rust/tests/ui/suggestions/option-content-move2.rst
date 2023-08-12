tests/ui/suggestions/option-content-move2.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct NotCopyable;

fn func<F: FnMut() -> H, H: FnMut()>(_: F) {}

fn parse() {
    let mut var = None;
    func(|| {
        // Shouldn't suggest `move ||.as_ref()` here
        move || {
        //~^ ERROR: cannot move out of `var`
            var = Some(NotCopyable);
        }
    });
}

fn main() {}


