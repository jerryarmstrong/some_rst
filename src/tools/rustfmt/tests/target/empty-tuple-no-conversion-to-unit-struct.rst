src/tools/rustfmt/tests/target/empty-tuple-no-conversion-to-unit-struct.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum TestEnum {
    Arm1(),
    Arm2,
}

fn foo() {
    let test = TestEnum::Arm1;
    match test {
        TestEnum::Arm1() => {}
        TestEnum::Arm2 => {}
    }
}


