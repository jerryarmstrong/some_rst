tests/ui/mir/mir-inlining/ice-issue-68347.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags:-Zmir-opt-level=3
pub fn main() {
    let _x: fn() = handle_debug_column;
}

fn handle_debug_column() {
    let sampler = sample_columns();

    let foo = || {
        sampler.get(17);
    };
    foo();
}

fn sample_columns() -> impl Sampler {
    ColumnGen {}
}

struct ColumnGen {}

trait Sampler {
    fn get(&self, index: i32);
}

impl Sampler for ColumnGen {
    fn get(&self, _index: i32) {}
}


