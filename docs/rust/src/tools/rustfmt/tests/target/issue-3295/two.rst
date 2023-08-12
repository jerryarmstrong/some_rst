src/tools/rustfmt/tests/target/issue-3295/two.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-version: Two
pub enum TestEnum {
    a,
    b,
}

fn the_test(input: TestEnum) {
    match input {
        TestEnum::a => String::from("aaa"),
        TestEnum::b => String::from(
            "this is a very very very very very very very very very very very very very very very ong string",
        ),
    };
}


