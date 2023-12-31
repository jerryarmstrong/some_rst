src/tools/clippy/tests/ui/diverging_sub_expression.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::diverging_sub_expression)]
#![allow(clippy::match_same_arms, clippy::overly_complex_bool_expr)]
#[allow(clippy::empty_loop)]
fn diverge() -> ! {
    loop {}
}

struct A;

impl A {
    fn foo(&self) -> ! {
        diverge()
    }
}

#[allow(unused_variables, clippy::unnecessary_operation, clippy::short_circuit_statement)]
fn main() {
    let b = true;
    b || diverge();
    b || A.foo();
}

#[allow(dead_code, unused_variables)]
fn foobar() {
    loop {
        let x = match 5 {
            4 => return,
            5 => continue,
            6 => true || return,
            7 => true || continue,
            8 => break,
            9 => diverge(),
            3 => true || diverge(),
            10 => match 42 {
                99 => return,
                _ => true || panic!("boo"),
            },
            _ => true || break,
        };
    }
}


