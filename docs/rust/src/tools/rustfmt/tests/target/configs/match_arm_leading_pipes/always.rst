src/tools/rustfmt/tests/target/configs/match_arm_leading_pipes/always.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-match_arm_leading_pipes: Always

fn foo() {
    match foo {
        | "foo" | "bar" => {}
        | "baz"
        | "something relatively long"
        | "something really really really realllllllllllllly long" => println!("x"),
        | "qux" => println!("y"),
        | _ => {}
    }
}

fn issue_3973() {
    match foo {
        | "foo" | "bar" => {}
        | _ => {}
    }
}

fn bar() {
    match baz {
        | "qux" => {}
        | "foo" | "bar" => {}
        | _ => {}
    }
}


