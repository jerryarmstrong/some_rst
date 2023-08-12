src/tools/rust-analyzer/crates/hir-def/src/nameres/tests/primitives.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::*;

#[test]
fn primitive_reexport() {
    check(
        r#"
//- /lib.rs
mod foo;
use foo::int;

//- /foo.rs
pub use i32 as int;
"#,
        expect![[r#"
            crate
            foo: t
            int: t

            crate::foo
            int: t
        "#]],
    );
}


