src/tools/rust-analyzer/crates/ide-completion/src/tests/proc_macros.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Completion tests for expressions.
use expect_test::{expect, Expect};

use crate::tests::completion_list;

fn check(ra_fixture: &str, expect: Expect) {
    let actual = completion_list(ra_fixture);
    expect.assert_eq(&actual)
}

#[test]
fn complete_dot_in_attr() {
    check(
        r#"
//- proc_macros: identity
pub struct Foo;
impl Foo {
    fn foo(&self) {}
}

#[proc_macros::identity]
fn main() {
    Foo.$0
}
"#,
        expect![[r#"
            me foo() fn(&self)
            sn box   Box::new(expr)
            sn call  function(expr)
            sn dbg   dbg!(expr)
            sn dbgr  dbg!(&expr)
            sn let   let
            sn letm  let mut
            sn match match expr {}
            sn ref   &expr
            sn refm  &mut expr
        "#]],
    )
}

#[test]
fn complete_dot_in_attr2() {
    check(
        r#"
//- proc_macros: identity
pub struct Foo;
impl Foo {
    fn foo(&self) {}
}

#[proc_macros::identity]
fn main() {
    Foo.f$0
}
"#,
        expect![[r#"
            me foo() fn(&self)
            sn box   Box::new(expr)
            sn call  function(expr)
            sn dbg   dbg!(expr)
            sn dbgr  dbg!(&expr)
            sn let   let
            sn letm  let mut
            sn match match expr {}
            sn ref   &expr
            sn refm  &mut expr
        "#]],
    )
}

#[test]
fn complete_dot_in_attr_input() {
    check(
        r#"
//- proc_macros: input_replace
pub struct Foo;
impl Foo {
    fn foo(&self) {}
}

#[proc_macros::input_replace(
    fn suprise() {
        Foo.$0
    }
)]
fn main() {}
"#,
        expect![[r#"
            me foo() fn(&self)
            sn box   Box::new(expr)
            sn call  function(expr)
            sn dbg   dbg!(expr)
            sn dbgr  dbg!(&expr)
            sn let   let
            sn letm  let mut
            sn match match expr {}
            sn ref   &expr
            sn refm  &mut expr
        "#]],
    )
}

#[test]
fn complete_dot_in_attr_input2() {
    check(
        r#"
//- proc_macros: input_replace
pub struct Foo;
impl Foo {
    fn foo(&self) {}
}

#[proc_macros::input_replace(
    fn suprise() {
        Foo.f$0
    }
)]
fn main() {}
"#,
        expect![[r#"
            me foo() fn(&self)
            sn box   Box::new(expr)
            sn call  function(expr)
            sn dbg   dbg!(expr)
            sn dbgr  dbg!(&expr)
            sn let   let
            sn letm  let mut
            sn match match expr {}
            sn ref   &expr
            sn refm  &mut expr
        "#]],
    )
}


