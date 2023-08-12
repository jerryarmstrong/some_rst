tests/ui/macros/issue-78892-substitution-in-statement-attr.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// regression test for #78892

macro_rules! mac {
    ($lint_name:ident) => {{
        #[allow($lint_name)]
        let _ = ();
    }};
}

fn main() {
    mac!(dead_code)
}


