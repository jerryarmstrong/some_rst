src/tools/rustfmt/tests/source/configs/fn_args_layout/tall.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-fn_args_layout: Tall
// Function arguments density

trait Lorem {
    fn lorem(ipsum: Ipsum, dolor: Dolor, sit: Sit, amet: Amet);

    fn lorem(ipsum: Ipsum, dolor: Dolor, sit: Sit, amet: Amet) {
        // body
    }

    fn lorem(ipsum: Ipsum, dolor: Dolor, sit: Sit, amet: Amet, consectetur: onsectetur, adipiscing: Adipiscing, elit: Elit);

    fn lorem(ipsum: Ipsum, dolor: Dolor, sit: Sit, amet: Amet, consectetur: onsectetur, adipiscing: Adipiscing, elit: Elit) {
        // body
    }
}


