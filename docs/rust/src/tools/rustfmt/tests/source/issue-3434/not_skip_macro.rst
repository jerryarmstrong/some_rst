src/tools/rustfmt/tests/source/issue-3434/not_skip_macro.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[this::is::not::skip::macros(ouch)]

fn main() {
    let macro_result1 = ouch! { <div>
this should be mangled</div>
    }
    .to_string();
}


