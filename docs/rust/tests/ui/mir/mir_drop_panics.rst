tests/ui/mir/mir_drop_panics.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// needs-unwind
// error-pattern:panic 1
// error-pattern:drop 2

struct Droppable(u32);
impl Drop for Droppable {
    fn drop(&mut self) {
        if self.0 == 1 {
            panic!("panic 1");
        } else {
            eprintln!("drop {}", self.0);
        }
    }
}

fn mir() {
    let x = Droppable(2);
    let y = Droppable(1);
}

fn main() {
    mir();
}


