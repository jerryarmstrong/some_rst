tests/ui/moves/issue-46099-move-in-macro.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #46099
// Tests that we don't emit spurious
// 'value moved in previous iteration of loop' message

macro_rules! test {
    ($v:expr) => {{
        drop(&$v);
        $v
    }}
}

fn main() {
    let b = Box::new(true);
    test!({b}); //~ ERROR use of moved value
}


